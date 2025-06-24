import pandas as pd
import matplotlib.pyplot as plt 

def backtest_strategy(data):
    """
    3. Backtesting the Strategy
    Evaluates the performance of the Moving Average Crossover strategy by calculating:
    - Daily returns
    - Strategy returns based on signals
    - Cumulative return curve

    Parameters:
        data (pd.DataFrame): Must include 'Close' and 'Signal' columns

    Returns:
        pd.DataFrame: Data with added return columns
    """

    # Calculate daily returns
    data['Daily_Return'] = data['Close'].pct_change()
    
    # Calculate strategy returns based on signals (with shift to simulate next-day execution)
    data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']
    
    # Calculate cumulative returns
    data['Cumulative_Return'] = (1 + data['Strategy_Return']).cumprod()

    return data


def evaluate_performance(data, trading_days_per_year=252, risk_free_rate=0.01):
    """
    Calculates key performance metrics for the strategy:
    - Annualized Return
    - Annualized Volatility
    - Sharpe Ratio
    - Maximum Drawdown

    Parameters:
        data (pd.DataFrame): Must include 'Strategy_Return' and 'Cumulative_Return'
        trading_days_per_year (int): Typically 252 for daily trading
        risk_free_rate (float): Annual risk-free return (default 1%)

    Returns:
        dict: Dictionary with performance metrics
    """    # Annualized Return
    annualized_return = data['Strategy_Return'].mean() * trading_days_per_year

    # Annualized Volatility
    annualized_volatility = data['Strategy_Return'].std() * (trading_days_per_year ** 0.5)

    # Sharpe Ratio
    sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility

    # Maximum Drawdown
    cumulative_max = data['Cumulative_Return'].cummax()
    drawdown = (data['Cumulative_Return'] - cumulative_max) / cumulative_max
    max_drawdown = drawdown.min()

    # Mostrar en consola
    print(f"Annualized Return: {annualized_return:.2f}")
    print(f"Annualized Volatility: {annualized_volatility:.2f}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Maximum Drawdown: {max_drawdown:.2%}")

    return {
        'Annualized Return': annualized_return,
        'Annualized Volatility': annualized_volatility,
        'Sharpe Ratio': sharpe_ratio,
        'Maximum Drawdown': max_drawdown
    }


def plot_cumulative_return(data):
    """
    Plots the cumulative return of the strategy.

    Parameters:
        data (pd.DataFrame): Must include 'Cumulative_Return' column
    """

    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Cumulative_Return'], label='Strategy Cumulative Return', color='b')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.title('Strategy Cumulative Return')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()  