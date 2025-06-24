# Algo Trading Bot

Este proyecto implementa un bot de trading algorítmico que utiliza la estrategia de cruce de medias móviles (Moving Average Crossover) para operar en el mercado de acciones.

## Estructura del Proyecto

```
algo_bot/
├── core/
│   ├── data_loader.py     # Carga de datos históricos
│   ├── strategy.py        # Implementación de la estrategia
│   ├── backtester.py      # Backtesting y evaluación
│   └── visualizer.py      # Visualización de resultados
├── main.py                # Punto de entrada principal
└── requirements.txt       # Dependencias del proyecto
```

## Características

- Estrategia de cruce de medias móviles (SMA 7 y 20 períodos)
- Backtesting con datos históricos de Yahoo Finance
- Métricas de rendimiento:
  - Retorno anualizado
  - Volatilidad anualizada
  - Ratio de Sharpe
  - Drawdown máximo
- Visualización de señales y retornos acumulados

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/josetraderx/algo_bot.git
cd algo_bot
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar el bot:

```bash
python main.py
```

Esto generará:
- Gráfico de la estrategia con señales de compra/venta
- Gráfico de retornos acumulados
- Métricas de rendimiento en la consola

## Tecnologías

- Python
- pandas: Manipulación de datos
- yfinance: Descarga de datos históricos
- matplotlib: Visualización de resultados
