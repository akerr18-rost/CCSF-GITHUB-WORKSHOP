# 📈 Trading Strategy Workshop

Welcome! In this workshop you will edit a trading strategy, push it to GitHub, and watch it run in the cloud.

---

## 🚀 How it works

1. **Fork** this repo (top right corner on GitHub)
2. **Clone** your fork to your computer
```bash
git clone https://github.com/YOUR-USERNAME/trading-workshop
cd trading-workshop
```
3. **Open** `strategy.py` in any text editor
4. **Change** the two numbers to try a new strategy
5. **Push** your changes
```bash
git add strategy.py
git commit -m "my strategy"
git push
```
6. Go to your repo on GitHub → click the **Actions** tab → watch your strategy run!

---

## 📁 Files

| File | What it does | Do you edit it? |
|---|---|---|
| `strategy.py` | Your trading strategy | ✅ YES |
| `strategy_menu.py` | Premade strategies to try | Copy from here |
| `backtest.py` | Runs the simulation | ❌ No |
| `data/SNAP.csv` | Historical SNAP stock prices | ❌ No |

---

## 💡 Tips

- The only file you need to touch is `strategy.py`
- Look at `strategy_menu.py` for ideas
- Every push triggers a new backtest — try as many times as you want
- There is no wrong answer, experiment!

---

## 🛠 Run it locally (optional)

If you have Python installed you can also run it on your machine:
```bash
python backtest.py
```
