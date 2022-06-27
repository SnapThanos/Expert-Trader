# Expert-Trader
Programme that helps automate your trading.


# Strategy
We Have 3 Smoothed Moving Averages at period 20, 50, 200.
We use the 15 minute timeframes to take trades.
NB: At this point we are only looking at the Ger30 (DAX) symbol.


# How do we take trades
We wait for the 20 and 50 Moving Averages to cross the 200 Moving Average.
That will be our buy/sell signal.
We hold the trade until our smallest Moving Average (20) to go above our previous level on the same Moving Average.
That will be our take closing signal.