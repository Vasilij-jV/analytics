import unittest
from data_download import (calculate_rsi_from_yfinance, calculate_macd_from_yfinance, fetch_stock_data,
                           add_moving_average)
from data_plotting import plot_technical_indicators, create_and_save_plot
import pandas as pd
import os
import logging


class TestTechnicalIndicators(unittest.TestCase):

    def setUp(self):
        self.ticker = 'AAPL'
        self.period = '1mo'

    #  Добавление дополнительных технических индикаторов
    def test_rsi_calculation(self):
        data_rsi = calculate_rsi_from_yfinance(self.ticker, self.period)
        self.assertIsInstance(data_rsi, pd.DataFrame)
        self.assertTrue('RSI' in data_rsi.columns)

    def test_macd_calculation(self):
        data_macd = calculate_macd_from_yfinance(self.ticker, self.period)
        self.assertIsInstance(data_macd, pd.DataFrame)
        self.assertTrue('MACD' in data_macd.columns)
        self.assertTrue('Signal Line' in data_macd.columns)

    # Визуализация технических индикаторов
    def test_rsi_chart_saved(self):
        data_rsi = calculate_rsi_from_yfinance(self.ticker, self.period)
        plot_technical_indicators(data_rsi, self.ticker, 'RSI')
        self.assertTrue(os.path.exists(f"CHARTS/{self.ticker}_RSI_chart.png"))

    def test_macd_chart_saved(self):
        data_macd = calculate_macd_from_yfinance(self.ticker, self.period)
        plot_technical_indicators(data_macd, self.ticker, 'MACD')
        self.assertTrue(os.path.exists(f"CHARTS/{self.ticker}_MACD_chart.png"))

    # Создание графика по ценам закрытия и скользящей средней цены закрытия
    def test_create_and_save_plot(self):
        stock_data = fetch_stock_data(self.ticker, self.period)
        stock_data = add_moving_average(stock_data)
        create_and_save_plot(stock_data, self.ticker, self.period)
        self.assertTrue(os.path.exists(f"CHARTS/{self.ticker}_{self.period}_stock_price_chart.png"))


if __name__ == '__main__':
    unittest.main()
