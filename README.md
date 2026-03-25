# 🐍 Python Placement Practice

> A collection of Python programs written during placement preparation — covering arrays, strings, searching algorithms, and DSA problem solving.

![Language](https://img.shields.io/badge/Language-Python%203-3776ab?style=flat-square&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-DSA%20%7C%20Arrays%20%7C%20Strings-b85c38?style=flat-square)
![Status](https://img.shields.io/badge/Status-Ongoing-f5c842?style=flat-square)

---

## 📁 Files Overview

| File | Topic | What It Does |
|---|---|---|
| `besttime_buyandsell_stock` | DSA — Sliding Window | Finds max profit from stock prices using two-pointer technique |
| `Binary_search.py` | Searching | Binary search implementation on a sorted array |
| `array.py` | Arrays | Move all zeros to the end while maintaining order of non-zero elements |
| `arr.py` | Arrays | Count consecutive pairs where `a[i] + 1 == a[i+1]` |
| `ar.py` | 2D Arrays | Demonstrates 2D array mutation |
| `array_addition.py` | Arrays | Element-wise addition of two arrays |
| `array_include_add.py` | Arrays | Read elements into array and add elements at index 0 and 2 |
| `array_traversel.py` | Arrays | Array traversal basics with sorting |
| `3.py` | Strings | String encoding, `upper()`, `capitalize()`, slicing |
| `b_regex.py` | Regex | Regex pattern matching on file input |
| `1.py` | Basics | Variable assignment and arithmetic |

---

## 🧠 Key Concepts Covered

- **Arrays** — traversal, mutation, two-pointer, zero movement, element-wise operations
- **2D Arrays** — indexing and value updates
- **Strings** — slicing, encoding, formatting, case methods
- **Searching** — Binary Search
- **DSA Problems** — Best Time to Buy and Sell Stock (LeetCode #121)
- **Regex** — file-based pattern matching
- **Python Basics** — variables, loops, input handling, list comprehension

---

## 🏆 DSA Problem Solved

### Best Time to Buy & Sell Stock
```
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5
```
**Approach:** Sliding window with two pointers `l` (buy) and `r` (sell).  
Track minimum price seen so far and update max profit on every step.  
**Time:** O(n) · **Space:** O(1)

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
cd REPO-NAME

# Run any file
python3 Binary_search.py
python3 array.py
python besttime_buyandsell_stock
```

> Some files require terminal input — enter values when prompted.

---

## 📌 Example Run — Binary Search

```bash
$ python3 Binary_search.py
1 3 5 7 9 11
7
7
```

---

## 📌 Example Run — Array Zero Move

```bash
$ python3 array.py
# Input array: [1, 0, 4, 0, 0, 5, 0, 6, 0, 0, 2]
# Output:       1 4 5 6 2 0 0 0 0 0 0
```

---

## 🗺 What's Coming Next

- [ ] Sorting algorithms (Bubble, Merge, Quick)
- [ ] Linked List problems
- [ ] Stack and Queue
- [ ] More LeetCode DSA problems
- [ ] String pattern matching

---

## 👤 Author

**Ram Prasad S M**  
3rd Year B.E. Computer Science  
📧 ramprasad.s.m28@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ramprasad-s-m-5849662a3) · [Portfolio](https://ramprasad28-hue.github.io/portfolio)

---

<p align="center">Solving one problem at a time 💪</p>
