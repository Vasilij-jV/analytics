import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import logging

# Создание графика по ценам закрытия и скользящей средней цены закрытия
def create_and_save_plot(data, ticker, period, filename=None):
    # Улучшенное управление временными периодами. Форматирование строки "period" для отображения в названии файла
    if len(period) > 3:
        name_file_with_spaces = period.split(',')
        name_file_without_spaces = [elem.strip() for elem in name_file_with_spaces]
        date_format = '%Y-%m-%d'
        parse_date = [datetime.datetime.strptime(elem, date_format) for elem in name_file_without_spaces]
        formatted_date_as_list = [elem.strftime('%d.%m.%y') for elem in parse_date]
        period = '-'.join(formatted_date_as_list)
        logging.info(f'')
    # Построение данных
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Close Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            logging.info(f'Информация о дате отсутствует или не имеет распознаваемого формата.')
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Close Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"CHARTS/{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")
    logging.info(f'График сохранен как {filename}')


# Экспорт данных в CSV
def export_data_to_csv(data, filename):
    if isinstance(data, pd.DataFrame) and isinstance(filename, str):
        data.to_csv(filename, index=False)
        logging.info(f'Объект {type(data)} экспортирован в файл')


# Визуализация технических индикаторов
def plot_technical_indicators(data, ticker, indicator, filename=None):
    plt.figure(figsize=(14, 7))

    if indicator == 'RSI':
        plt.plot(data['RSI'], label='RSI')
        plt.title('RSI Chart for ' + ticker)
    elif indicator == 'MACD':
        plt.plot(data['MACD'], label='MACD', color='blue')
        plt.plot(data['Signal Line'], label='Signal Line', color='red')
        plt.title('MACD Chart for ' + ticker)

    plt.legend()

    if filename is None:
        filename = f"CHARTS/{ticker}_{indicator}_chart.png"

    plt.savefig(filename)
    print(f"{indicator} график сохранён, как {filename}")
    logging.info(f'{indicator} график сохранён, как {filename}')

