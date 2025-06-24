from core.data_loader import load_data
from core.strategy import apply_moving_average_crossover
from core.backtester import backtest_strategy, evaluate_performance, plot_cumulative_return
from core.visualizer import plot_strategy


# 1. Load Data
df = load_data()   

# 2. Apply Strategy (Generate Signals)
df = apply_moving_average_crossover(df)

# 3. Backtest Strategy
df = backtest_strategy(df) 
plot_cumulative_return(df)

# 4. Evaluate Performance
metrics = evaluate_performance(df)

# 5. Plot results
plot_strategy(df)

print(metrics)
