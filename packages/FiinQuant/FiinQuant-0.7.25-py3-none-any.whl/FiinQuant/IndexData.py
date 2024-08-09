import pandas as pd      
class IndexData:
    def __init__(self,data):
        data_converted = self._convert_data_types(data)
        self.__private_attribute = data_converted
        self.TotalMatchVolume = data_converted['TotalMatchVolume'][0]
        self.MarketStatus = data_converted['MarketStatus'][0]
        self.TradingDate = data_converted['TradingDate'][0]
        self.ComGroupCode = data_converted['ComGroupCode'][0]
        self.ReferenceIndex = data_converted['ReferenceIndex'][0]
        self.OpenIndex = data_converted['OpenIndex'][0]
        self.CloseIndex = data_converted['CloseIndex'][0]
        self.HighestIndex = data_converted['HighestIndex'][0]
        self.LowestIndex = data_converted['LowestIndex'][0]
        self.IndexValue = data_converted['IndexValue'][0]
        self.IndexChange = data_converted['IndexChange'][0]
        self.PercentIndexChange = data_converted['PercentIndexChange'][0]
        self.MatchVolume = data_converted['MatchVolume'][0]
        self.MatchValue = data_converted['MatchValue'][0]
        self.TotalMatchValue = data_converted['TotalMatchValue'][0]
        self.TotalDealVolume = data_converted['TotalDealVolume'][0]
        self.TotalDealValue = data_converted['TotalDealValue'][0]
        self.TotalStockUpPrice = data_converted['TotalStockUpPrice'][0]
        self.TotalStockDownPrice = data_converted['TotalStockDownPrice'][0]
        self.TotalStockNoChangePrice = data_converted['TotalStockNoChangePrice'][0]
        self.TotalStockOverCeiling = data_converted['TotalStockOverCeiling'][0]
        self.TotalStockUnderFloor = data_converted['TotalStockUnderFloor'][0]
        self.ForeignBuyVolumeTotal = data_converted['ForeignBuyVolumeTotal'][0]
        self.ForeignBuyValueTotal = data_converted['ForeignBuyValueTotal'][0]
        self.ForeignSellVolumeTotal = data_converted['ForeignSellVolumeTotal'][0]
        self.ForeignSellValueTotal = data_converted['ForeignSellValueTotal'][0]
        self.VolumeBu = data_converted['VolumeBu'][0]
        self.VolumeSd = data_converted['VolumeSd'][0]

    def _convert_data_types(self, data):
        data_converted = {
            'TotalMatchVolume': [int(data['TotalMatchVolume'].values[0])],
            'MarketStatus': [data['MarketStatus'].values[0]],
            'TradingDate': [data['TradingDate'].values[0]],
            'ComGroupCode': [data['ComGroupCode'].values[0]],
            'ReferenceIndex': [float(data['ReferenceIndex'].values[0])],
            'OpenIndex': [float(data['OpenIndex'].values[0])],
            'CloseIndex': [float(data['CloseIndex'].values[0])],
            'HighestIndex': [float(data['HighestIndex'].values[0])],
            'LowestIndex': [float(data['LowestIndex'].values[0])],
            'IndexValue': [float(data['IndexValue'].values[0])],
            'IndexChange': [float(data['IndexChange'].values[0])],
            'PercentIndexChange': [float(data['PercentIndexChange'].values[0])],
            'MatchVolume': [int(data['MatchVolume'].values[0])],
            'MatchValue': [float(data['MatchValue'].values[0])],
            'TotalMatchValue': [float(data['TotalMatchValue'].values[0])],
            'TotalDealVolume': [int(data['TotalDealVolume'].values[0])],
            'TotalDealValue': [float(data['TotalDealValue'].values[0])],
            'TotalStockUpPrice': [int(data['TotalStockUpPrice'].values[0])],
            'TotalStockDownPrice': [int(data['TotalStockDownPrice'].values[0])],
            'TotalStockNoChangePrice': [int(data['TotalStockNoChangePrice'].values[0])],
            'TotalStockOverCeiling': [int(data['TotalStockOverCeiling'].values[0])],
            'TotalStockUnderFloor': [int(data['TotalStockUnderFloor'].values[0])],
            'ForeignBuyVolumeTotal': [int(data['ForeignBuyVolumeTotal'].values[0])],
            'ForeignBuyValueTotal': [float(data['ForeignBuyValueTotal'].values[0])],
            'ForeignSellVolumeTotal': [int(data['ForeignSellVolumeTotal'].values[0])],
            'ForeignSellValueTotal': [float(data['ForeignSellValueTotal'].values[0])],
            'VolumeBu': [int(data['VolumeBu'].values[0])],
            'VolumeSd': [int(data['VolumeSd'].values[0])]
        }
        return pd.DataFrame(data_converted)
    def get_data(self):
        return self.__private_attribute
    

    