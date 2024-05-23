import data_download as dd
import data_plotting as dplt
from pprint import pprint
import logging


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet "
        "Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, "
        "с начала года, макс.")


    enter_ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    enter_period = input("Введите период для данных (например: '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y',"
                         " '10y', 'ytd',"
                         " 'max', 'yyyy-mm-dd, yyyy-mm-dd'): ")


    # Получение данных для формирования объекта с данными о запасах
    ticker = enter_ticker
    period = enter_period

    # Получение исторических данных об акциях для указанного тикера и временного периода
    stock_data = dd.fetch_stock_data(ticker, period)

    # Добавляет колонку со скользящим средним к данным и переопределяет объект "stock_data"
    stock_data = dd.add_moving_average(stock_data)


    # Вывод средней цены из колонки "Close" за период
    dd.calculate_and_display_average_price(stock_data)


    # Уведомление о сильных колебаниях
    threshold = 5
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Перенаправление вывода логирования в файл. Функции по получению объекта по акциям и использованию колонки
    # объекта - "Close"
    # logging.basicConfig(level=logging.INFO,
    #                     handlers=[logging.FileHandler('LOGGING/close_logging.log', 'w',
    #                                                   'utf-8')]
    #                     )


    # Экспортирует объект DanaFrame в файл
    filename = 'save_dataframe.csv'
    dplt.export_data_to_csv(stock_data, filename)


    #  Добавление дополнительных технических индикаторов
    data_rsi = dd.calculate_rsi_from_yfinance(ticker, period)
    data_macd = dd.calculate_macd_from_yfinance(ticker, period)

    # Визуализация технических индикаторов
    dplt.plot_technical_indicators(data_rsi, ticker, 'RSI')
    dplt.plot_technical_indicators(data_macd, ticker, 'MACD')


    # Построение данных
    dplt.create_and_save_plot(stock_data, ticker, period, style='dark_background')


if __name__ == "__main__":
    main()
