# Terminal Connect Four (Python)

A fully functional, two-player terminal implementation of **Connect Four** built in Python. Designed to demonstrate core computer science mechanics, including matrix traversal, pass-by-reference state updates, and modular arithmetic.

---

## 🎮 Game Preview

```text
========================================
      WELCOME TO CONNECT FOUR!          
========================================

  0 1 2 3 4 5 6
 | . . . . . . . |
 | . . . . . . . |
 | . . . . . . . |
 | . . . . . . . |
 | . . . O . . . |
 | . . . X . . . |
  0 1 2 3 4 5 6

Player 'X', choose a column (0-6):
```

---

## 🚀 Features & Game Rules

* **Grid Size:** Standard $6 \times 7$ Connect Four board.
* **Turn Mechanics:** Alternating turns between Player `'X'` and Player `'O'`.
* **Gravity Drop:** Pieces drop automatically to the lowest available row in the selected column.
* **Input Protection:** Comprehensive input validation against non-integer entries, out-of-bounds indices, and full columns.
* **Win Detection:** Automatically scans 4 directional vectors (Horizontal, Vertical, Diagonal Down-Right, Diagonal Up-Right).

---



## 📋 Running the Project

### Prerequisites
* Python 3.x installed.

### Execution Steps
1. Clone the repository:
   ```bash
   git clone [https://github.com/safayetul-afk/terminal-connect-four-python.git](https://github.com/safayetul-afk/terminal-connect-four-python.git)
   ```
2. Navigate to the project root:
   ```bash
   cd terminal-connect-four-python
   ```
3. Run the game:
   ```bash
   python src/main.py
   ```