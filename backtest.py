# ============================================================
#  BACKTEST ENGINE
#  You don't need to edit this file!
#  It runs your strategy from strategy.py against historical
#  SNAP stock data and shows you how much money you made.
# ============================================================

import csv
import importlib
import sys
import os

# --- Load the student's strategy ---
import strategy

buy_threshold  = strategy.buy_when_price_drops_by
sell_threshold = strategy.sell_when_price_rises_by

# --- Load stock data ---
data_path = os.path.join(os.path.dirname(__file__), "data", "SNAP.csv")
prices = []
dates  = []

with open(data_path, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        dates.append(row["Date"])
        prices.append(float(row["Close"]))

# --- Run the backtest ---
STARTING_CASH = 1000.00
cash          = STARTING_CASH
shares        = 0
buy_price     = None
trades        = []

print("=" * 52)
print("  TRADING WORKSHOP BACKTEST")
print("  Stock: SNAP  |  Starting cash: $1,000.00")
print(f"  Buy threshold:  -{buy_threshold*100:.1f}%")
print(f"  Sell threshold: +{sell_threshold*100:.1f}%")
print("=" * 52)

for i in range(1, len(prices)):
    today     = prices[i]
    yesterday = prices[i - 1]
    change    = (today - yesterday) / yesterday

    if shares == 0 and change <= -buy_threshold:
        # BUY
        shares    = int(cash / today)
        buy_price = today
        cash     -= shares * today
        trades.append(("BUY", dates[i], today, shares))
        print(f"  📈 BUY  {dates[i]}  ${today:.2f}  x{shares} shares")

    elif shares > 0 and change >= sell_threshold:
        # SELL
        cash += shares * today
        profit = (today - buy_price) * shares
        trades.append(("SELL", dates[i], today, shares))
        print(f"  📉 SELL {dates[i]}  ${today:.2f}  x{shares} shares  "
              f"({'+'if profit>=0 else ''}{profit:.2f})")
        shares    = 0
        buy_price = None

# Liquidate any remaining shares at last price
if shares > 0:
    cash += shares * prices[-1]

# --- Results ---
final_value  = cash
total_return = final_value - STARTING_CASH
pct_return   = (total_return / STARTING_CASH) * 100
num_trades   = len([t for t in trades if t[0] == "BUY"])

print("=" * 52)
print(f"  Total trades:   {num_trades}")
print(f"  Final value:    ${final_value:.2f}")

if total_return >= 0:
    print(f"  Total return:   +${total_return:.2f} (+{pct_return:.1f}%) ✅")
    print()
    print("  🎉 Your strategy made money!")
else:
    print(f"  Total return:   -${abs(total_return):.2f} ({pct_return:.1f}%) ❌")
    print()
    print("  💸 Your strategy lost money. Try different numbers!")

print("=" * 52)
