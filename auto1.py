import graphviz

# Create the automaton
dfa = graphviz.Digraph("DFA", format="png")
dfa.attr(rankdir="LR")

# States with colors
dfa.node("q0", label="q0\n(inicial)", shape="circle", style="filled", fillcolor="lightblue")
dfa.node("q1", shape="circle", style="filled", fillcolor="white")
dfa.node("q2", shape="circle", style="filled", fillcolor="white")
dfa.node("q3", label="q3\n(aceptación)", shape="doublecircle", style="filled", fillcolor="lightgreen")

# Initial arrow
dfa.node("", shape="none", width="0")
dfa.edge("", "q0")

# Transitions with colors
dfa.edge("q0", "q1", label="0", color="blue")
dfa.edge("q0", "q2", label="1", color="red")
dfa.edge("q1", "q0", label="0", color="blue")
dfa.edge("q1", "q3", label="1", color="red")
dfa.edge("q2", "q3", label="0", color="blue")
dfa.edge("q2", "q2", label="1", color="red")  # loop
dfa.edge("q3", "q1", label="0", color="blue")
dfa.edge("q3", "q2", label="1", color="red")

# Save in the same folder as PNG and SVG
dfa.render("AFD_Problema1", format="png", cleanup=True)
dfa.render("AFD_Problema1", format="svg", cleanup=True)

print("Automaton generated: AFD_Problema1.png and AFD_Problema1.svg")
