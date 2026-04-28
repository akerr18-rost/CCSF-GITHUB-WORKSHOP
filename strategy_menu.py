# ============================================================
#  STRATEGY MENU
#  Copy any strategy below and paste it into strategy.py
#  to try it out!
# ============================================================


# ------------------------------------------------------------
# STRATEGY 1: Buy the Dip (default)
# Buy when price drops, sell when it recovers
# ------------------------------------------------------------
buy_when_price_drops_by = 0.02   # buy when price drops 2%
sell_when_price_rises_by = 0.03  # sell when price rises 3%


# ------------------------------------------------------------
# STRATEGY 2: Aggressive Dip Buyer
# Wait for a bigger drop before buying
# ------------------------------------------------------------
# buy_when_price_drops_by = 0.05   # wait for a 5% drop
# sell_when_price_rises_by = 0.02  # take profits quickly


# ------------------------------------------------------------
# STRATEGY 3: Slow and Steady
# Small moves, quick exits
# ------------------------------------------------------------
# buy_when_price_drops_by = 0.01   # buy on any small dip
# sell_when_price_rises_by = 0.01  # sell on any small rise


# ------------------------------------------------------------
# STRATEGY 4: High Risk High Reward
# Wait for big swings
# ------------------------------------------------------------
# buy_when_price_drops_by = 0.08   # only buy on big crashes
# sell_when_price_rises_by = 0.10  # hold out for big gains


# ------------------------------------------------------------
# STRATEGY 5: Scalper
# Very tight margins, lots of trades
# ------------------------------------------------------------
# buy_when_price_drops_by = 0.005  # buy on tiny dips
# sell_when_price_rises_by = 0.005 # sell on tiny rises


# ============================================================
#  HOW TO USE:
#  1. Pick a strategy above
#  2. Copy those two lines
#  3. Paste them into strategy.py replacing the existing lines
#  4. Save, commit, and push!
# ============================================================
