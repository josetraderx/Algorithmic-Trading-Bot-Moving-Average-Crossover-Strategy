import matplotlib.pyplot as plt

def plot_strategy(data):
    """
    Visualization of the Strategy
    Plots close price, SMAs, and buy/sell signals on a chart.

    Parameters:
        data (pd.DataFrame): Must include 'Close', 'SMA_9', 'SMA_21', and 'Signal'
    """

    plt.figure(figsize=(14, 7))

    # Plot price and SMas
    plt.plot(data.index, data['Close'], label='Close Price', color='blue')
    plt.plot(data.index, data['SMA_9'], label='SMA_9', color='green', linestyle='--')
    plt.plot(data.index, data['SMA_21'], label='SMA_21', color='red', linestyle='--')    # Buy/Sell signals
    buy_signals = data[data['Signal'] == 1]
    sell_signals = data[data['Signal'] == -1]
    
    plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='green', label='Buy Signal', alpha=1)
    plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='red', label='Sell Signal', alpha=1)

    plt.title('Moving Average Crossover Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show( )
