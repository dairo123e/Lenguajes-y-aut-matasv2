#  Automata Theory Project

This repository contains the design and implementation of multiple **Deterministic Finite Automata (DFA)** and **Pushdown Automata (PDA)** using **Python** and the `graphviz` library.  
The project is part of the **Automata Theory course**, and its purpose is to model different formal languages and generate their graphical representation automatically.

---

##  Introduction
Automata are mathematical models used to represent and analyze formal languages.  
- **DFA (Deterministic Finite Automata):** Recognize **regular languages**.  
- **PDA (Pushdown Automata):** Recognize **context-free languages**, using a stack to store information.  

In this project, each problem provided in class is implemented as a Python script that generates the automaton diagram in **PNG** and **SVG** formats. This allows for easy visualization and verification of the designed automata.

---

##  Objectives
1. Implement DFAs and PDAs in Python using the `graphviz` library.  
2. Generate visual representations that are clear, colorful, and easy to analyze.  
3. Apply automata theory to different language recognition problems.  
4. Create a well-documented repository for academic collaboration and version control with **GitHub**.

---

##  Methodology
- Each problem was analyzed based on its **formal definition**.  
- States, transitions, and acceptance conditions were defined.  
- A **Python script** was created for each automaton.  
- The `graphviz` library was used to produce the automata diagrams.  
- Each diagram was exported to **PNG** and **SVG** for better visualization and portability.  

---

##  Repository Structure

###  DFA Implementations
1. **`AFD_problema1.py`**  
   DFA with colored transitions for clear visualization.  

2. **`AFD_problema2.py`**  
   DFA that accepts words with an **even number of `a`** and without the substring **`bc`**.  

3. **`AFD_problema3.py`**  
   DFA depending on the **parity of 0s and 1s**:  
   - No `1s` → string must contain an even number of `0s`.  
   - Even number of `1s` (greater than 0) → string must end with an odd number of `0s`.  

4. **`dfa_q0_colores.py`**  
   DFA where **q0** is both the **initial and accepting state**, including a **trap state**.  

5. **`DFA_problema5_q.py`**  
   DFA derived from a **regular expression**, including an **absorbing accepting state**.  

---

###  PDA Implementations
6. **`PDA_problema6_a2i.py`**  
   PDA for the language:  
   **L = { a^i b c a^(2i) | i > 0 }**  
   - Phase 1: Pushes `X` symbols for each `a`.  
   - Phase 2: Reads `b` then `c`.  
   - Phase 3: For each final `a`, pops one `X`.  
   - Accepts when the stack returns to its base symbol.  

7. **`PDA_problema7_na_ge_nb.py`**  
   PDA for the language:  
   **L = { w | n_a(w) ≥ n_b(w) }**  
   - Guarantees that the number of `a` is always greater or equal to `b`.  
   - If more `b` are read than available `a`, the automaton goes to a **trap state**.  

---

## ⚙️ Requirements
Before running the scripts, ensure you have installed:  
- **Python 3.x**  
- **Graphviz** (download from [Graphviz.org](https://graphviz.org/))  
- Python package `graphviz`:  
  ```bash
  pip install graphviz
