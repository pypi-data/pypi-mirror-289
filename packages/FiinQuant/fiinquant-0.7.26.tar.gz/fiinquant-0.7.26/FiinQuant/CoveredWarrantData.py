import pandas as pd
class CoveredWarrantData:
    def __init__(self, data):
        data_converted = self._convert_data_types(data)
        
        self.__private_attribute = data_converted
       
        self.TotalMatchVolume = data_converted['TotalMatchVolume'][0]
        self.MarketStatus = data_converted['MarketStatus'][0]
        self.TradingDate = data_converted['TradingDate'][0]
        self.MatchType = data_converted['MatchType'][0]
        self.ComGroupCode = data_converted['ComGroupCode'][0]
        self.OrganCode = data_converted['OrganCode'][0]
        self.Ticker = data_converted['Ticker'][0]
        self.ReferencePrice = data_converted['ReferencePrice'][0]
        self.OpenPrice = data_converted['OpenPrice'][0]
        self.ClosePrice = data_converted['ClosePrice'][0]
        self.CeilingPrice = data_converted['CeilingPrice'][0]
        self.FloorPrice = data_converted['FloorPrice'][0]
        self.HighestPrice = data_converted['HighestPrice'][0]
        self.LowestPrice = data_converted['LowestPrice'][0]
        self.MatchPrice = data_converted['MatchPrice'][0]
        self.PriceChange = data_converted['PriceChange'][0]
        self.PercentPriceChange = data_converted['PercentPriceChange'][0]
        self.MatchVolume = data_converted['MatchVolume'][0]
        self.MatchValue = data_converted['MatchValue'][0]
        self.TotalMatchValue = data_converted['TotalMatchValue'][0]
        self.TotalBuyTradeVolume = data_converted['TotalBuyTradeVolume'][0]
        self.TotalSellTradeVolume = data_converted['TotalSellTradeVolume'][0]
        self.DealPrice = data_converted['DealPrice'][0]
        self.TotalDealVolume = data_converted['TotalDealVolume'][0]
        self.TotalDealValue = data_converted['TotalDealValue'][0]
        self.ForeignBuyVolumeTotal = data_converted['ForeignBuyVolumeTotal'][0]
        self.ForeignBuyValueTotal = data_converted['ForeignBuyValueTotal'][0]
        self.ForeignSellVolumeTotal = data_converted['ForeignSellVolumeTotal'][0]
        self.ForeignSellValueTotal = data_converted['ForeignSellValueTotal'][0]
        self.ForeignTotalRoom = data_converted['ForeignTotalRoom'][0]
        self.ForeignCurrentRoom = data_converted['ForeignCurrentRoom'][0]

    def _convert_data_types(self, data):
        data_converted = {
            'TotalMatchVolume': [int(data['TotalMatchVolume'].values[0])],
            'MarketStatus': [data['MarketStatus'].values[0]],
            'TradingDate': [data['TradingDate'].values[0]],
            'MatchType': [data['MatchType'].values[0]],
            'ComGroupCode': [data['ComGroupCode'].values[0]],
            'OrganCode': [data['OrganCode'].values[0]],
            'Ticker': [data['Ticker'].values[0]],
            'ReferencePrice': [float(data['ReferencePrice'].values[0])],
            'OpenPrice': [float(data['OpenPrice'].values[0])],
            'ClosePrice': [float(data['ClosePrice'].values[0])],
            'CeilingPrice': [float(data['CeilingPrice'].values[0])],
            'FloorPrice': [float(data['FloorPrice'].values[0])],
            'HighestPrice': [float(data['HighestPrice'].values[0])],
            'LowestPrice': [float(data['LowestPrice'].values[0])],
            'MatchPrice': [float(data['MatchPrice'].values[0])],
            'PriceChange': [float(data['PriceChange'].values[0])],
            'PercentPriceChange': [float(data['PercentPriceChange'].values[0])],
            'MatchVolume': [int(data['MatchVolume'].values[0])],
            'MatchValue': [float(data['MatchValue'].values[0])],
            'TotalMatchValue': [float(data['TotalMatchValue'].values[0])],
            'TotalBuyTradeVolume': [int(data['TotalBuyTradeVolume'].values[0])],
            'TotalSellTradeVolume': [int(data['TotalSellTradeVolume'].values[0])],
            'DealPrice': [float(data['DealPrice'].values[0])],
            'TotalDealVolume': [int(data['TotalDealVolume'].values[0])],
            'TotalDealValue': [float(data['TotalDealValue'].values[0])],
            'ForeignBuyVolumeTotal': [int(data['ForeignBuyVolumeTotal'].values[0])],
            'ForeignBuyValueTotal': [float(data['ForeignBuyValueTotal'].values[0])],
            'ForeignSellVolumeTotal': [int(data['ForeignSellVolumeTotal'].values[0])],
            'ForeignSellValueTotal': [float(data['ForeignSellValueTotal'].values[0])],
            'ForeignTotalRoom': [int(data['ForeignTotalRoom'].values[0])],
            'ForeignCurrentRoom': [int(data['ForeignCurrentRoom'].values[0])]
        }
        
        # Chuyển đổi dữ liệu thành DataFrame
        return pd.DataFrame(data_converted)
    
    def get_data(self):
        return self.__private_attribute




    


