import pandas as pd

def apply_moving_average_crossover(data, short_window=9, long_window=21):
        """
        2. Strategy Development
        This function applies a Moving Average Crossover strategy.

        - Buy: When the short-term SMA crosses above the long-term SMA.
        - Sell: When the short-term SMA crosses below the long-term SMA.

        Parameters:
            data (pd.DataFrame): Market data with 'Close' column
            short_window (int): Period for short-term SMA (default 9)
            long_window (int): Period for long-term SMA (default 21)

        Returns:
            pd.DataFrame: DataFrame with SMA columns and signal column
        """
        
        # Calculate short-term and long-term moving averages
        data['SMA_9'] = data['Close'].rolling(window=short_window).mean() # 9-day SMA
        data['SMA_21'] = data['Close'].rolling(window=long_window).mean() # 21-day SMA

        # Define trading signals
        data['Signal'] = 0 # Initialize signal column

        # Generate buy/signals based on crossover conditions
        data.loc[data['SMA_9'] > data['SMA_21'], 'Signal'] = 1  # Buy signal
        data.loc[data['SMA_9'] < data['SMA_21'], 'Signal'] = -1 # Sell signal

        # Shift signals to simulate next-day execution
        data['signal'] = data['Signal'].shift(1)  

        # Calculate the difference to identify changes in signal
        # This will help in identifying buy/sell points
        data['signal'] = data['Signal'].diff().fillna(0)

    
        return data
