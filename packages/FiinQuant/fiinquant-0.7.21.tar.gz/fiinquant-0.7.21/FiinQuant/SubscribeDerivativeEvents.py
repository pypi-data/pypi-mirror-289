import time
import threading
import pandas as pd
from signalrcore.hub_connection_builder import HubConnectionBuilder
from .DerivativeData import DerivativeData
import logging
REALTIME_API = "https://fiinquant-realtime-staging.fiintrade.vn/RealtimeHub?access_token="

class CustomHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.log_messages = []

    def emit(self, record):
        log_entry = self.format(record)
        self.log_messages.append(log_entry)

    def get_logs(self):
        return self.log_messages


class SubscribeDerivativeEvents:
    def __init__(self, access_token: str, tickers: list, callback: callable):
        self.url = REALTIME_API
        self.hub_connection = self._build_connection()
        self.connected = False 
        self.callback = callback
        self.access_token = access_token
        self.df = {ticker: pd.DataFrame(columns=[
            'TotalMatchVolume','MarketStatus','TradingDate','MatchType','ComGroupCode',
            'DerivativeCode','ReferencePrice','OpenPrice','ClosePrice','CeilingPrice',
            'FloorPrice','HighestPrice','LowestPrice','MatchPrice','PriceChange','PercentPriceChange','MatchVolume'
            ,'MatchValue','TotalMatchValue','TotalBuyTradeVolume','TotalSellTradeVolume','DealPrice','TotalDealVolume',
            'TotalDealValue','ForeignBuyVolumeTotal','ForeignBuyValueTotal','ForeignSellVolumeTotal','ForeignSellValueTotal',
            'ForeignTotalRoom','ForeignCurrentRoom','OpenInterest']) for ticker in tickers}

        self.tickers = tickers
        self._stop_event = threading.Event()
        self._stop = False
        # Create and configure custom handler
        self._stop_event = threading.Event()
        self.custom_handler = CustomHandler()
        self.custom_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.custom_handler.setFormatter(formatter)

        # Add custom handler to logger
        logger = logging.getLogger()
        logger.addHandler(self.custom_handler)
        logger.setLevel(logging.DEBUG)

    def _data_handler(self, message):
        if message is not None:
            for msg in message:
                ticker_data = msg['data'][0].split('|')
                ticker = ticker_data[5] 
                if ticker in self.df:
                    df = self.df[ticker]
                    df.loc[len(df)] = ticker_data
                    self.return_data = DerivativeData(df[-1:])
                    if self.callback:
                        self.callback(self.return_data)
                else:
                    print(f"Ticker {ticker} not in the list.")
        else:
            print("No data received.")
            

    def _build_connection(self):
        return HubConnectionBuilder()\
            .with_url(self.url, options={
                "access_token_factory": lambda: self.access_token
            })\
            .with_automatic_reconnect({
                "type": "raw",
                "keep_alive_interval": 1,
                "reconnect_interval": [1, 3, 5, 7, 11]
            }).build()

    def _receive_message(self, message):
        self._data_handler(message)

    def _handle_error(self, error):
        print(f"Error: {error}")

    def _on_connect(self):
        self.connected = True
        print("Connection established")
        self._join_groups()

    def _on_disconnect(self):
        self.connected = False
        print("Disconnected from the hub")

    def _join_groups(self):
        if self.connected:
            for ticker in self.tickers:
                self.hub_connection.send("JoinGroup", [f"Realtime.Derivative.{ticker}"])
                print(f"Joined group: Realtime.Derivative.{ticker}")
        else:
            raise ValueError("Cannot join groups, not connected")
    def _get_log_messages(self):
        return self.custom_handler.get_logs()
    def _run(self):
        if self.hub_connection.transport is not None:
            self.hub_connection.stop()

        self.hub_connection.on("ReceiveMessage", self._receive_message)
        self.hub_connection.on_close(self._handle_error)
        self.hub_connection.on_open(self._on_connect)
        self.hub_connection.on_close(self._on_disconnect)
        self.hub_connection.start()
        logging.basicConfig(level=logging.DEBUG)
        while not self._stop_event.is_set():
            time.sleep(0.0001)
            message = self._get_log_messages()
            for msg in message:
                if "An unexpected error occurred invoking 'JoinGroup' on the server." in msg:
                    print(msg)
                    self._stop = True
                    self._stop_event.set()
                    self.hub_connection.stop()
                    break
        
    def start(self):
        self.thread = threading.Thread(target=self._run)
        self.thread.start()
        
    def stop(self):
        self._stop_event.set()
        if self.connected:
            print("Disconnecting...")
            self.hub_connection.stop()
        self.thread.join()
        
