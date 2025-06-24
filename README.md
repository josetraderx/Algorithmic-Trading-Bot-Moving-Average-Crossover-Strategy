#AlgorithmicTradingBot

This project implements an algorithmic trading bot that uses the Moving Average Crossover strategy to trade the stock market.

## Project Structure

```
algo_bot/
├── core/
│ ├── data_loader.py # Loading historical data
│ ├── strategy.py # Strategy implementation
│ ├── backtester.py # Backtesting and evaluation
│ └── visualizer.py # Results visualization
├── main.py # Main entry point
└── requirements.txt # Project dependencies
```

## Features

- Moving average crossover strategy (7- and 20-period SMA)
- Backtesting with historical data from Yahoo Finance
- Performance metrics:
- Annualized return
- Annualized volatility
- Sharpe ratio
- Maximum drawdown
- Visualization Signals and Cumulative Returns

## Installation

1. Clone the repository:
```bash
git clone https://github.com/josetraderx/algo_bot.git
cd algo_bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

To run the bot:

```bash
python main.py
```

This will generate:
- Strategy chart with buy/sell signals
- Cumulative return chart
- Performance metrics in the console

## Technologies

- Python
- Pandas: Data manipulation
- yfinance: Downloading historical data
- matplotlib: Visualizing results
