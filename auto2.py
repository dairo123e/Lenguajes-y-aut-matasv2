from graphviz import Digraph

# Create a directed graph
dot = Digraph(comment="DFA - Language with even number of a's and without substring 'bc'")
dot.attr(rankdir="LR", size="10,7")

# Define nodes
dot.attr("node", shape="circle", style="filled", fillcolor="lightblue")

# States (q0 and q2 are accepting states -> doublecircle)
dot.node("q0", "q0 (par,≠b)", shape="doublecircle")
dot.node("q1", "q1 (impar,≠b)")
dot.node("q2", "q2 (par,=b)", shape="doublecircle")
dot.node("q3", "q3 (impar,=b)")
dot.node("qT", "qT (trampa)", fillcolor="lightcoral")

# Initial state
dot.node("inicio", shape="point")
dot.edge("inicio", "q0")

# Transitions from q0
dot.edge("q0", "q1", label="a")
dot.edge("q0", "q2", label="b")
dot.edge("q0", "q0", label="c")

# Transitions from q1
dot.edge("q1", "q0", label="a")
dot.edge("q1", "q3", label="b")
dot.edge("q1", "q1", label="c")

# Transitions from q2
dot.edge("q2", "q1", label="a")
dot.edge("q2", "q2", label="b")
dot.edge("q2", "qT", label="c")

# Transitions from q3
dot.edge("q3", "q0", label="a")
dot.edge("q3", "q3", label="b")
dot.edge("q3", "qT", label="c")

# Transitions from qT (trap state)
dot.edge("qT", "qT", label="a,b,c")

# Export to file
dot.render("AFD_problema2", format="png", cleanup=True)

print("✅ Automaton generated as 'AFD_problema2.png'")
