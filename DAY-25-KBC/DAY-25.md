````markdown
# 🎮 KBC - Kaun Banega Crorepati (Python CLI Game)

> *Test your knowledge and win big!*  
> A command-line trivia game inspired by the iconic Indian quiz show **Kaun Banega Crorepati (KBC)**.  
> Powered by real-time questions from the [Open Trivia DB](https://opentdb.com/) API, featuring lifelines and a thrilling prize ladder! 🏆

---

## 🔗 Code Link

Check out the full source code on GitHub:  
[https://github.com/vinayakmishra4/PYTHON-FROM-BASIC-TO-ADVANCE/blob/main/DAY-25-KBC/kbc.py](https://github.com/vinayakmishra4/PYTHON-FROM-BASIC-TO-ADVANCE/blob/main/DAY-25-KBC/kbc.py)

---

## ✨ Features

- 🎲 **15 multiple-choice questions** fetched live from an online trivia API
- 💰 **Progressive prize ladder** from ₹1,000 up to ₹1 Crore
- 🧪 **Two lifelines** to help you out:
  - **50-50**: Eliminate two wrong answers
  - **Skip**: Skip a tricky question (no prize for that one)
- 🔀 Randomized answer options to keep you on your toes
- ❌ Game ends on wrong answers or invalid inputs
- 🏆 See your total winnings at the end!

---

## 🚀 Getting Started

### 🧰 Prerequisites

- Python 3.x installed on your machine
- An active internet connection (to fetch fresh trivia questions)

### 📦 Installation

You only need the `requests` library (usually pre-installed):

```bash
pip install requests
````

---

## 🎮 How to Play

1. **Run the game:**

   ```bash
   python kbc_game.py
   ```

2. **Answer questions** by typing one of **A**, **B**, **C**, or **D**.

3. **Use lifelines wisely** by typing when prompted:

   * `lifeline 1` — activate **50-50** (eliminates two wrong answers)
   * `lifeline 2` — activate **Skip** (skip the question, no prize)
   * `none` — no lifeline, just answer

4. **Game ends if:**

   * You answer incorrectly
   * You enter an invalid response
   * You answer all 15 questions correctly 🎉

---

## 💸 Prize Ladder

| Question | Prize Amount |
| :------: | :----------: |
|     1    |    ₹1,000    |
|     2    |    ₹2,000    |
|     3    |    ₹3,000    |
|     4    |    ₹5,000    |
|     5    |    ₹10,000   |
|     6    |    ₹20,000   |
|     7    |    ₹40,000   |
|     8    |    ₹80,000   |
|     9    |   ₹1,60,000  |
|    10    |   ₹3,20,000  |
|    11    |   ₹6,40,000  |
|    12    |  ₹12,50,000  |
|    13    |  ₹25,00,000  |
|    14    |  ₹50,00,000  |
|    15    | ₹1,00,00,000 |

---

## 📸 Sample Gameplay

```
🎮 Welcome to KBC 🎮

Question 1 for ₹1,000:
What is the capital of France?

Use a lifeline? (type 'lifeline 1', 'lifeline 2', or 'none'): none

  A. Paris
  B. Rome
  C. Berlin
  D. Madrid

Your answer (A/B/C/D): A
✅ Correct! You've won ₹1,000
```

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are highly welcome!
Feel free to fork the repo and submit a pull request to:

* Add new lifelines or features
* Improve the user interface (colors, timers, sounds)
* Add unit tests for robustness
* Implement milestone safety nets

---

## 🙏 Acknowledgements

* Thanks to [Open Trivia DB](https://opentdb.com/) for their awesome API
* Inspired by the legendary quiz show **Kaun Banega Crorepati (KBC)**