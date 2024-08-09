import numpy as np
import pandas as pd

class FiinIndicator:
    class trend:
        class EMA:
            def __init__(self, column: pd.Series, window: int):
                self.column = column
                self.window = window
                self.ema_line = self._calculate_ema()
                
            def _calculate_ema(self):
                ema = self.column.ewm(span=self.window, min_periods=self.window, adjust=False).mean()
                return ema

            def ema(self):
                return self.ema_line
            
        class SMA:
            def __init__(self, column: pd.Series, window: int):
                self.column = column
                self.window = window
                self.sma_line = self._calculate_sma()
                
            def _calculate_sma(self):
                sma = self.column.rolling(window=self.window, min_periods=self.window).mean()
                return sma

            def sma(self):
                return self.sma_line

        class WMA:
            def __init__(self, close: pd.Series, window: int = 9):
                self.close = close
                self.window = window
                self.wma_line = self._calculate_wma()
            
            def _calculate_wma(self):
                weights = np.arange(1, self.window + 1)
                wma = self.close.rolling(window=self.window).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)
                return wma

            def wma(self):
                return self.wma_line

        class MACD:
            def __init__(self, column: pd.Series, window_slow: int = 26, window_fast: int = 12, window_sign: int = 9):
                self.column = column
                self.window_slow = window_slow
                self.window_fast = window_fast
                self.window_sign = window_sign
                self.ema_slow = self._calculate_ema_slow()
                self.ema_fast = self._calculate_ema_fast()
                self.macd_line = self._calculate_macd()
                self.macd_signal_line = self._calculate_macd_signal()
                self.macd_diff_line = self._calculate_macd_diff()

            def _calculate_ema_slow(self):
                ema_slow = FiinIndicator.trend.EMA(self.column, self.window_slow).ema()
                return ema_slow

            def _calculate_ema_fast(self):
                ema_fast = FiinIndicator.trend.EMA(self.column, self.window_fast).ema()
                return ema_fast
                
            def _calculate_macd(self):
                macd = self.ema_fast - self.ema_slow
                return macd
            
            def _calculate_macd_signal(self):
                macd_signal = FiinIndicator.trend.EMA(self.macd_line, self.window_sign).ema()
                return macd_signal
            
            def _calculate_macd_diff(self):
                macd_diff_line = self.macd_line - self.macd_signal_line
                return macd_diff_line

            def macd(self):
                return self.macd_line
            
            def macd_signal(self):
                return self.macd_signal_line
            
            def macd_diff(self):
                return self.macd_diff_line

        class ADX:
            def __init__(self, high: pd.Series, low: pd.Series, close: pd.Series, window: int = 14):
                self.high = high
                self.low = low
                self.close = close
                self.window = window
                self.tr, self.dm_plus, self.dm_minus = self._calculate_dm()
                self.tr_smooth = self._calculate_tr_smooth()
                self.plus_di = self._calculate_pos()
                self.minus_di = self._calculate_nev()
                self.adx_line = self._calculate_adx()
                
            def _calculate_dm(self):
                tr1 = self.high - self.low
                tr2 = abs(self.high - self.close.shift(1))
                tr3 = abs(self.low - self.close.shift(1))
                tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
                tr[0] = None

                dm_plus = self.high - self.high.shift(1)
                dm_minus = self.low.shift(1) - self.low
                dm_plus[dm_plus <= 0] = 0
                dm_minus[dm_minus <= 0] = 0
                return tr, dm_plus, dm_minus
            
            def _calculate_tr_smooth(self):
                tr_smooth = self.tr.rolling(window=self.window, min_periods=self.window).sum()
                tr_smooth[self.window - 1] = None
                return tr_smooth
            
            def _calculate_pos(self):
                dm_plus_smooth = self.dm_plus.rolling(window=self.window, min_periods=self.window).sum()
                plus_di = 100 * dm_plus_smooth / self.tr_smooth
                return plus_di
            
            def _calculate_nev(self):
                dm_minus_smooth = self.dm_minus.rolling(window=self.window, min_periods=self.window).sum() 
                minus_di = 100 * dm_minus_smooth / self.tr_smooth    
                return minus_di
            
            def _calculate_adx(self):
                dx = 100 * abs(self.plus_di - self.minus_di) / (self.plus_di + self.minus_di)      
                adx = FiinIndicator.trend.SMA(dx, self.window).sma()       
                return adx
            
            def adx(self):
                return self.adx_line
            
            def adx_pos(self):
                return self.plus_di
            
            def adx_neg(self):
                return self.minus_di

    class momentum:
        class RSI:
            def __init__(self, column: pd.Series, window: int = 14):
                self.column = column
                self.window = window
                self.rsi_line = self._calculate_rsi()
                
            def _calculate_rsi(self):
                self.column = self.column.astype(int)
                delta = self.column.diff()
                gain = delta.where(delta > 0, 0) 
                loss = -delta.where(delta < 0, 0) 
                avg_gain = gain.ewm(com=self.window - 1, min_periods=self.window, adjust=False).mean() 
                avg_loss = loss.ewm(com=self.window - 1, min_periods=self.window, adjust=False).mean() 
                rs = avg_gain / avg_loss.abs() 
                rsi = 100 - (100 / (1 + rs)) 
                rsi[(avg_loss == 0) | (avg_loss == -avg_gain)] = 100  
                return rsi
                
            def rsi(self):
                return self.rsi_line
            
        class Stochastic:
            def __init__(self, high: pd.Series, low: pd.Series, close: pd.Series, window: int = 14, smooth_window: int = 3):
                self.high = high
                self.low = low
                self.close = close
                self.window = window
                self.smooth_window = smooth_window
                self.stoch_line = self._calculate_stoch()
                self.stoch_signal_line = self._calculate_stoch_signal()
                
            def _calculate_stoch(self):
                lowest_low = self.low.rolling(window=self.window).min()
                highest_high = self.high.rolling(window=self.window).max()
                stoch_k = 100 * (self.close - lowest_low) / (highest_high - lowest_low)
                return stoch_k
            
            def _calculate_stoch_signal(self):
                stoch_k = self.stoch_line
                stoch_d = FiinIndicator.trend.SMA(stoch_k, self.smooth_window).sma()
                return stoch_d
                
            def stoch(self):
                return self.stoch_line
            
            def stoch_signal(self):
                return self.stoch_signal_line

    class volatility:
        class BollingerBands:
            def __init__(self, column: pd.Series, window: int = 20, window_dev: int = 2):
                self.column = column
                self.window = window
                self.window_dev = window_dev
                self.mavg = self._calculate_bollinger_mavg()
                self.std = self._calculate_bollinger_std()
                self.hband = self._calculate_bollinger_hband()
                self.lband = self._calculate_bollinger_lband()
                
            def _calculate_bollinger_mavg(self):
                bollinger_mavg = FiinIndicator.trend.SMA(self.column, self.window).sma()
                return bollinger_mavg
            
            def _calculate_bollinger_std(self):
                try:
                    rolling_windows = np.lib.stride_tricks.sliding_window_view(self.column, self.window)
                    stds = np.std(rolling_windows, axis=1)
                    stds = np.concatenate([np.full(self.window - 1, np.nan), stds])
                    std = pd.Series(stds, index=self.column.index)
                    return std
                except:
                    std = pd.Series([np.nan] * self.column.shape[0])
                    return std

            def _calculate_bollinger_hband(self):
                bollinger_hband = self.mavg + (self.window_dev * self.std)
                return bollinger_hband 
            
            def _calculate_bollinger_lband(self):
                bollinger_lband = self.mavg - (self.window_dev * self.std)
                return bollinger_lband 
            
            def bollinger_hband(self):
                return self.hband
            
            def bollinger_lband(self):
                return self.lband

        class Supertrend:
            def __init__(self, high: pd.Series, low: pd.Series, close: pd.Series, window: int = 14, multiplier: float = 3.0):
                self.high = high
                self.low = low
                self.close = close
                self.window = window
                self.multiplier = multiplier
                self.upper_band, self.lower_band = self._calculate_bands()
                self.supertrend_line = self._calculate_supertrend()

            def _calculate_bands(self):
                atr = FiinIndicator.volatility.ATR(self.high, self.low, self.close, self.window)
                hl2 = (self.high + self.low) / 2
                upper_band = hl2 + (atr * self.multiplier)
                lower_band = hl2 - (atr * self.multiplier)
                return upper_band, lower_band

            def _calculate_supertrend(self):
                supertrend = pd.Series(index=self.close.index)
                in_uptrend = True

                for i in range(self.window, len(self.close)):
                    if self.close[i] <= self.upper_band[i]:
                        in_uptrend = False
                    else:
                        in_uptrend = True

                    if in_uptrend:
                        supertrend[i] = self.lower_band[i]
                    else:
                        supertrend[i] = self.upper_band[i]

                return supertrend

            def supertrend(self):
                return self.supertrend_line

            def supertrend_hband(self):
                return self.upper_band

            def supertrend_lband(self):
                return self.lower_band

        class ATR:
            def __init__(self, high: pd.Series, low: pd.Series, close: pd.Series, window: int = 14):
                self.high = high
                self.low = low
                self.close = close
                self.window = window
                self.tr = self._calculate_tr()
                self.atr_line = self._calculate_atr()

            def _calculate_tr(self):
                tr1 = self.high - self.low
                tr2 = abs(self.high - self.close.shift(1))
                tr3 = abs(self.low - self.close.shift(1))
                tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
                return tr

            def _calculate_atr(self):
                atr = FiinIndicator.trend.SMA(column=self.tr, window=self.window).sma()
                for i in range(self.window, len(self.tr)):
                    atr.iloc[i] = (atr.iloc[i-1] * (self.window - 1) + self.tr.iloc[i]) / self.window
                return atr

            def atr(self):
                return self.atr

    class volume:
        class MFI:
            def __init__(self, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, window: int = 14):
                self.high = high
                self.low = low
                self.close = close
                self.volume = volume
                self.window = window
                self.typical_price = self._calculate_typical_price()
                self.money_flow = self._calculate_money_flow()
                self.positive_money_flow = self._calculate_positive_money_flow()
                self.negative_money_flow = self._calculate_negative_money_flow()
                self.mfi_line = self._calculate_mfi()
            
            def _calculate_typical_price(self):
                return (self.high + self.low + self.close) / 3

            def _calculate_money_flow(self):
                return self.typical_price * self.volume

            def _calculate_positive_money_flow(self):
                prev_typical_price = self.typical_price.shift(1)
                return self.money_flow.where(self.typical_price > prev_typical_price, 0)

            def _calculate_negative_money_flow(self):
                prev_typical_price = self.typical_price.shift(1)
                return self.money_flow.where(self.typical_price < prev_typical_price, 0)

            def _calculate_mfi(self):
                pos_flow_sum = self.positive_money_flow.rolling(window=self.window, min_periods=self.window).sum()
                neg_flow_sum = self.negative_money_flow.rolling(window=self.window, min_periods=self.window).sum()
                money_flow_ratio = pos_flow_sum / neg_flow_sum.replace(0, pd.NA)
                return 100 - (100 / (1 + money_flow_ratio))
            
            def mfi(self):
                return self.mfi_line

        class OBV:
            def __init__(self, column: pd.Series, volume: pd.Series):
                self.column = column
                self.volume = volume
                self.obv_line = self._calculate_obv()
            
            def _calculate_obv(self):
                obv = pd.Series(index=self.column.index)
                obv.iloc[0] = self.volume.iloc[0]

                for i in range(1, len(self.column)):
                    if self.column.iloc[i] > self.column.iloc[i - 1]:
                        obv.iloc[i] = obv.iloc[i - 1] + self.volume.iloc[i]
                    elif self.column.iloc[i] < self.column.iloc[i - 1]:
                        obv.iloc[i] = obv.iloc[i - 1] - self.volume.iloc[i]
                    else:
                        obv.iloc[i] = obv.iloc[i - 1]
                return obv

            def obv(self):
                return self.obv_line

        class VWAP:
            def __init__(self, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, window: int = 14):
                self.high = high
                self.low = low
                self.close = close
                self.volume = volume
                self.window = window
                self.typical_price = self._calculate_typical_price()
                self.vwap_line = self._calculate_vwap()

            def _calculate_typical_price(self):
                typical_price = (self.high + self.low + self.close) / 3
                return typical_price

            def _calculate_vwap(self):
                volume_weighted_price = self.typical_price * self.volume
                cumulative_volume_weighted_price = volume_weighted_price.rolling(window=self.window, min_periods=self.window).sum()
                cumulative_volume = self.volume.rolling(window=self.window, min_periods=self.window).sum()
                vwap = cumulative_volume_weighted_price / cumulative_volume.replace(0, pd.NA)
                return vwap

            def vwap(self):
                return self.vwap_line

