from graphviz import Digraph

# Create DFA diagram
dot = Digraph(comment="DFA - PROBLEM 5 (regex)", format="png")
dot.attr(rankdir="LR", size="10,7")
dot.attr("node", shape="circle", style="filled", fillcolor="lightblue")

# States
dot.node("q0", "q0\n(inicial)")
dot.node("q1", "q1")
dot.node("q2", "q2")
dot.node("q3", "q3\n(Aceptación)", shape="doublecircle", fillcolor="lightgreen")
dot.node("q4", "q4")

# Initial arrow
dot.node("start", shape="point")
dot.edge("start", "q0")

# Transitions
dot.edge("q0", "q1", label="0")
dot.edge("q0", "q2", label="1")

dot.edge("q1", "q3", label="0")
dot.edge("q1", "q4", label="1")

dot.edge("q2", "q1", label="0")
dot.edge("q2", "q3", label="1")

dot.edge("q4", "q1", label="0")
dot.edge("q4", "q3", label="1")

dot.edge("q3", "q3", label="0,1")  # absorbing accept state

# Render PNG and SVG
output_name = "DFA_problema5_q"
dot.render(output_name, format="png", cleanup=True)
dot.render(output_name, format="svg", cleanup=True)

print(f"✅ Files generated: {output_name}.png and {output_name}.svg")
