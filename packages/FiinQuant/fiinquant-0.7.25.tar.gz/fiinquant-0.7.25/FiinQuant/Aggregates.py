from datetime import datetime
import pandas as pd
import requests

HISTORICAL_API = "https://fiinquant-staging.fiintrade.vn/TradingView/GetStockChartData"

class BarData:
    def __init__(self, data):
        self.__private_attribute = data
        self.Open = data['Open']
        self.Low = data['Low']
        self.High = data['High']
        self.Close = data['Close']
        self.Volume = data['Volume']
        self.Timestamp = data['Timestamp']

    def to_dataFrame(self):
        return self.__private_attribute

class Bar:
    def __init__(self, 
                 access_token: str, 
                 ticker: str,  
                 by: str,  
                 from_date: str | datetime,  
                 to_date: str | datetime,  
                 multiplier: int = 1,  
                 limit: int = 1000):
        
        self.access_token = access_token
        self.ticker = ticker
        self.by = by.upper()
        self.from_date = self._format_date(from_date)     
        self.to_date = self._format_date(to_date)
        self.multiplier = multiplier
        self.limit = limit
        self.url = HISTORICAL_API
        self.TIME_FORMATS = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%Y-%m']
        self.VALID_FREQUENCIES = {'MINUTES': 'EachMinute', 'HOURS': 'EachOneHour', 'DAYS': 'Daily'}

    def _format_date(self, date):
        if isinstance(date, datetime):
            return date.strftime('%Y-%m-%d %H:%M:%S')
        return date
    
    def _is_valid_date(self, date, fmt):
        try:
            datetime.strptime(date, fmt)
            return True
        except ValueError:
            return False

    def _validate(self):
        if self.by not in self.VALID_FREQUENCIES:
            raise ValueError('Invalid value for "by". Must be one of MINUTES, HOURS, DAYS')
        
        if not any(self._is_valid_date(self.from_date, fmt) for fmt in self.TIME_FORMATS):
            raise ValueError(f"Invalid 'from_date': {self.from_date}")

        if not any(self._is_valid_date(self.to_date, fmt) for fmt in self.TIME_FORMATS):
            raise ValueError(f"Invalid 'to_date': {self.to_date}")
        
        
        
        if not(isinstance(self.multiplier, int) and self.multiplier > 0):
            raise ValueError('Multiplier must be a positive integer greater than 0')
        
        if not(isinstance(self.limit, int) and self.limit > 0):
            raise ValueError('Limit must be a positive integer greater than 0')

    def _fetch_data(self, data_type: str):

        if data_type != 'Index':
            self.ticker = self.ticker.upper()

        param = {
            'Code' : self.ticker, 
            'Type' : data_type,
            'Frequency' : self.VALID_FREQUENCIES[self.by],
            'From' : self.from_date,
            'To' : self.to_date,
            'PageSize' : self.limit
        }

        header = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(url=self.url, params=param, headers=header)
        res = response.json()

        if res['status'] != 'Success':
            raise ValueError(res['errors'][0]) 

        df = pd.DataFrame(res['items'])
        return df

    def _preprocess_data(self):
        self.df = self.df.rename(columns={
            "tradingDate": "Timestamp", 
            "openPrice": "Open", 
            "lowestPrice": "Low", 
            "highestPrice": "High", 
            "closePrice": "Close", 
            "totalMatchVolume": "Volume", 
        })

        if self.by == "MINUTES":  
            self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'], format='ISO8601')    
            self.df['MinuteOrder'] = self.df['Timestamp'].dt.hour * 60 + self.df['Timestamp'].dt.minute
            self.df['Group'] = (self.df['MinuteOrder'] - 555) // self.multiplier  # 555 = 9h15

            self.df['TimeStandard'] = self.df['Group'] * self.multiplier + 555 
            hoursStandard = (self.df['TimeStandard'] // 60).astype(int).astype(str).str.zfill(2)
            minutesStandard = (self.df['TimeStandard'] % 60).astype(int).astype(str).str.zfill(2)
            self.df['Date'] = self.df['Timestamp'].dt.date.astype(str)
            self.df['Timestamp'] = self.df['Date'] + ' ' + hoursStandard + ':' + minutesStandard + ':00'
            colGroup = 'Timestamp'
        
        if self.by == 'HOURS':
            self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'], format='ISO8601').dt.floor('h')
            self.df['HourOrder'] = self.df['Timestamp'].dt.hour
            self.df['Group'] = (self.df['HourOrder'] - 9) // self.multiplier

            self.df['TimeStandard'] = self.df['Group'] * self.multiplier + 9
            hoursStandard = (self.df['TimeStandard']).astype(int).astype(str).str.zfill(2)
            self.df['Date'] = self.df['Timestamp'].dt.date.astype(str)
            self.df['Timestamp'] = self.df['Date'] + ' ' + hoursStandard + ':00:00'
            colGroup = 'Timestamp'

        if self.by == 'DAYS':
            self.df['Timestamp'] = self.df['Timestamp'].str.split('T').str[0]
            self.df['Group'] = self.df.index // self.multiplier
            colGroup = 'Group'            

        self.df = self.df.groupby([colGroup]).agg({
            'Timestamp': 'first',
            'Open': 'first',     
            'High': 'max',       
            'Low': 'min',        
            'Close': 'last',     
            'Volume': 'sum'
        }).reset_index(drop=True)
        return self.df

    def get(self, data_type: str):
        self._validate()
        self.df = self._fetch_data(data_type)
        self.df = self._preprocess_data()
        return BarData(self.df)

class TickerBars(Bar):
    def get(self):
        return super().get('Stock')
    
class IndexBars(Bar):
    def get(self):
        return super().get('Index')

class CoveredWarrantBars(Bar):
    def get(self):
        return super().get('CW')
    
class DerivativeBars(Bar):
    def get(self):
        return super().get('Derivative')



