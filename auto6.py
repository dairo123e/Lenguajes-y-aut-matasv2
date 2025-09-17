from graphviz import Digraph

dot = Digraph(comment="PDA - L = { a^i b c a^{2i} | i>0 }")
dot.attr(rankdir="LR", size="10,7")
dot.attr("node", shape="circle", style="filled", fillcolor="lightblue")

# States
dot.node("q0", "q0\n(apilar fase inicial)")
dot.node("q1", "q1\n(despues de b)")
dot.node("q2", "q2\n(consume final a's)")
dot.node("qacc", "q_acc\n(aceptación)", shape="doublecircle", fillcolor="lightgreen")

# Start
dot.node("start", shape="point")
dot.edge("start", "q0")

# Transitions (label: input, pop -> push)
# q0: read 'a' and push 2 X (case when top is Z0)
dot.edge("q0", "q0", label="a, Z0 -> XXZ0")
# q0: read 'a' with top X -> add 2 X (represented as X -> XXX)
dot.edge("q0", "q0", label="a, X -> XXX")
# q0: read 'b' requires X on top (ensures i>0), stack remains effectively the same
dot.edge("q0", "q1", label="b, X -> X")
# q1: read 'c' (stack does not change)
dot.edge("q1", "q2", label="c, X -> X")
# q2: for each final 'a', pop one X
dot.edge("q2", "q2", label="a, X -> ε")
# q2: if end of string and top is Z0, accept (ε-transition)
dot.edge("q2", "qacc", label="ε, Z0 -> Z0")

# Render
output_name = "PDA_problema6_a2i"
dot.render(output_name, format="png", cleanup=True)
dot.render(output_name, format="svg", cleanup=True)

print(f"✅ Files generated: {output_name}.png and {output_name}.svg")
