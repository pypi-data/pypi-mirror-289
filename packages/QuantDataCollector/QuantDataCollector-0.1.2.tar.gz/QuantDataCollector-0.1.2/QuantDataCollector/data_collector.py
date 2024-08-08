from QuantDataCollector.factory_method import DataCollectorFactory
from QuantDataCollector.data_collector_config import default_config

class DataCollector:
    __object_type = "BaostockDataCollector"

    def __init__(self, config_dict = default_config):
        self.__df = DataCollectorFactory(self.__object_type, config_dict)

    def get_stock_type(self, stock_code):
        return self.__df.get_stock_type(stock_code)

    def get_all_stock_code(self, day = None):
        return self.__df.get_all_stock_code(day)

    def get_all_share_code(self, day = None):
        return self.__df.get_all_share_code(day)

    def get_stock_basic_data(self, stock_code):
        return self.__df.get_stock_basic_data(stock_code)

    def get_stock_data_period(self, stock_code_list, start=None, end=None, frequency='d'):
        return self.__df.get_stock_data_period(stock_code_list, start, end, frequency)

    def get_stock_data(self, stock_code_list, day=None, frequency='d'):
        return self.__df.get_stock_data(stock_code_list, day, frequency)

    def is_trade_day(self, day):
        return self.__df.is_trade_day(day)

    def get_recent_trade_day(self,day=None):
        return self.__df.get_recent_trade_day(day)

    def get_data_collector_info(self):
        return self.__df.get_data_collector_info()

if __name__ == '__main__':
    data_collector = DataCollector()
    #print(data_collector.get_stock_data_period("sz.399990", "2022-1-1","2022-1-24"))
    #print(data_collector.get_stock_type("sh.600000"))
    # _, share_codes = data_collector.get_all_share_code("2022-1-19")
    # _, stock_codes = data_collector.get_all_stock_code("2022-1-19")
    _, data = data_collector.get_stock_data(["sz.399990", "sh.600000"], "2024-8-6", frequency='5')
    print(data)
    # _, data2 = data_collector.get_stock_data_period(["sz.399990"], "2024-6-29", "2024-7-30", frequency='w')
    #print(data_collector.get_history_k_data("sh.599999", "2022-1-10"))
    #print(data_collector.get_stock_close_price("sh.600000", "2022-1-10"))
    #print(data_collector.is_trade_day("2022-1-20"))
    #print(data_collector.get_recent_trade_day())
    #data_collector.update_all_stock_data("1991-12-3")
