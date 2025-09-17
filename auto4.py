import graphviz

# Create the diagram
dfa = graphviz.Digraph("DFA", format="png")
dfa.attr(rankdir="LR")

# States with colors
dfa.node("q0", shape="doublecircle", style="filled", fillcolor="lightgreen")  # initial + accepting
dfa.node("q1", shape="circle", style="filled", fillcolor="lightblue")
dfa.node("q2", shape="circle", style="filled", fillcolor="lightblue")
dfa.node("qd", shape="circle", style="filled", fillcolor="lightcoral")  # trap state

# Initial state (empty arrow pointing to q0)
dfa.node("", shape="none", width="0")
dfa.edge("", "q0")

# Transitions
transitions = [
    ("q0", "q1", "0"),
    ("q0", "q2", "1"),
    ("q1", "qd", "0"),
    ("q1", "q0", "1"),
    ("q2", "q0", "0"),
    ("q2", "qd", "1"),
    ("qd", "qd", "0,1"),
]

for src, dst, label in transitions:
    dfa.edge(src, dst, label)

# Save in the same folder
dfa.render("dfa_q0_colores", format="png", cleanup=True)
dfa.render("dfa_q0_colores", format="svg", cleanup=True)

print("Files generated: dfa_q0_colores.png and dfa_q0_colores.svg in the same folder.")
