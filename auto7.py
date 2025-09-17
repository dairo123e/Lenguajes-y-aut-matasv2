from graphviz import Digraph

dot = Digraph(comment="PDA - L = { w | n_a(w) >= n_b(w) }")
dot.attr(rankdir="LR", size="8,5")
dot.attr("node", shape="circle", style="filled", fillcolor="lightblue")

# States
dot.node("q0", "q0\n(inicial, Aceptación)")
dot.node("qT", "qT\n(trampa)", fillcolor="lightcoral")

# Start node
dot.node("start", shape="point")
dot.edge("start", "q0")

# Transitions q0: 'a' (push X)
dot.edge("q0", "q0", label="a, Z0 -> X Z0")
dot.edge("q0", "q0", label="a, X -> X X")

# Transition q0: 'b' (pop X) or go to trap if no X
dot.edge("q0", "q0", label="b, X -> ε")
dot.edge("q0", "qT", label="b, Z0 -> Z0  (go to trap)")

# Trap transitions (stay in trap for any symbol)
dot.edge("qT", "qT", label="a, X/Z0 -> (stay)")
dot.edge("qT", "qT", label="b, X/Z0 -> (stay)")

# Render to PNG and SVG
output_name = "PDA_problema7_na_ge_nb"
dot.render(output_name, format="png", cleanup=True)
dot.render(output_name, format="svg", cleanup=True)

print(f"✅ Files generated: {output_name}.png and {output_name}.svg")
