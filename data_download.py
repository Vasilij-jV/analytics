import yfinance as yf
from pprint import pprint
import logging


logging.basicConfig(level=logging.INFO,
                        handlers=[logging.FileHandler('LOGGING/logging_download_plotting.log', 'w',
                                                      'utf-8')]
                        )
# Получение исторических данных об акциях для указанного тикера и временного периода
def fetch_stock_data(ticker, period):
    stock = yf.Ticker(ticker)
    logging.info(f'Объект "Ticker" {stock}')
    if len(period) > 3:
        list_with_space = period.split(',')
        start, end = [elem.strip() for elem in list_with_space]
        data = stock.history(start=start, end=end)
        logging.info(f'Временной период с заданным интервалом {type(data)}')
        return data
    else:
        data = stock.history(period=period)
        logging.info(f'Временной период с предопределённым интервалом {type(data)}')
        return data




# Добавление в DataFrame колонки со скользящим средним, рассчитанным на основе цен закрытия
def add_moving_average(data, window_size=15):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    logging.info(f'В DataFrame добавлено свойство "Moving_Average" {type(data)}')
    return data


#  Вывод средней цены из колонки "Close" за период
def calculate_and_display_average_price(stock_data):
    average_close = stock_data['Close'].mean()
    logging.info(f'Выводится среднее значение колонки "Close": {average_close}')
    print(f'Среднее значение колонки "Close": {average_close}\n')


# Уведомление о сильных колебаниях
def notify_if_strong_fluctuations(data, threshold):
    # Создаю список значений закрытия цен за период
    list_prices_close = data['Close'].tolist()
    # Определяю начальную цену закрытия за период
    initial_float = list_prices_close[0]
    # Определяю минимальную и максимальную цены закрытия за период
    max_float, min_float = max(list_prices_close), min(list_prices_close)
    # Вычисляю изменение цены за период между начальным и минимальным значениями в процентах
    price_change_between_initial_and_minimum = ((min_float - initial_float) / initial_float) * 100
    # Вычисляю изменение цены за период между начальным и максимальным значениями в процентах
    price_change_between_initial_and_maximum = ((max_float - initial_float) / initial_float) * 100
    # Вычисляю разницу в процентах между изменениями цены до минимального значения и до максимального значения
    difference_between_min_max = price_change_between_initial_and_maximum - price_change_between_initial_and_minimum
    if difference_between_min_max > threshold:
        logging.info(f'Значение колебаний: {difference_between_min_max}')
        print(f'Порог колебания цены - ({difference_between_min_max}) превышает допустимое значение - ({threshold})\n')
    return difference_between_min_max


# Добавление дополнительных технических индикаторов
# Рсчёт технического индикатора RSI
def calculate_rsi_from_yfinance(ticker, period, window=14):
    # Улучшенное управление временными периодами
    data = None
    if len(period) > 3:
        list_with_space = period.split(',')
        start, end = [elem.strip() for elem in list_with_space]
        data = yf.Ticker(ticker).history(start=start, end=end)
        logging.info(f'Временной период с заданным интервалом (RSI) {type(data)}')
    else:
        data = yf.Ticker(ticker).history(period=period)
        logging.info(f'Временной период с предопределённым интервалом (RSI) {type(data)}')
    # Расчёт RSI
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    data['RSI'] = rsi
    logging.info(f'Колонка "RSI": {type(data)}')
    return data


# Рсчёт технического индикатора MACD
def calculate_macd_from_yfinance(ticker, period, short_window=12, long_window=26, signal_window=9):
    # Улучшенное управление временными периодами
    data = None
    if len(period) > 3:
        list_with_space = period.split(',')
        start, end = [elem.strip() for elem in list_with_space]
        data = yf.Ticker(ticker).history(start=start, end=end)
        logging.info(f'Временной период с заданным интервалом (MACD) {type(data)}')
    else:
        data = yf.Ticker(ticker).history(period=period)
        logging.info(f'Временной период с предопределённым интервалом (MACD) {type(data)}')
    # Расчёт MACD
    short_ema = data['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, adjust=False).mean()

    macd = short_ema - long_ema
    signal_line = macd.ewm(span=signal_window, adjust=False).mean()

    data['MACD'] = macd
    data['Signal Line'] = signal_line
    logging.info(f'Колонка "MACD" и "Signal Line": {type(data)} {type(data)}')
    return data
