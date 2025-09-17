from graphviz import Digraph

dot = Digraph(comment="DFA - PROBLEM 3")
dot.attr(rankdir="LR", size="10,7")

# Node style
dot.attr("node", shape="circle", style="filled", fillcolor="lightblue")

# States (q0, q2, q5 are accepting)
dot.node("q0", "q0\n(no1, zeros Par)", shape="doublecircle")   # initial and accepting
dot.node("q1", "q1\n(no1, zeros Impar)")
dot.node("q2", "q2\n(unos Impar, zeros Par)", shape="doublecircle")
dot.node("q3", "q3\n(unos Impar, zeros Impar)")
dot.node("q4", "q4\n(unos>0, zeros Par)")
dot.node("q5", "q5\n(unos>0, zeros Impar)", shape="doublecircle")

# Initial node (point)
dot.node("start", shape="point")
dot.edge("start", "q0")

# Transitions
dot.edge("q0", "q1", label="0")
dot.edge("q0", "q2", label="1")

dot.edge("q1", "q0", label="0")
dot.edge("q1", "q2", label="1")

dot.edge("q2", "q3", label="0")
dot.edge("q2", "q4", label="1")

dot.edge("q3", "q2", label="0")
dot.edge("q3", "q4", label="1")

dot.edge("q4", "q5", label="0")
dot.edge("q4", "q2", label="1")

dot.edge("q5", "q4", label="0")
dot.edge("q5", "q2", label="1")

# Render in PNG and SVG
output_filename = "AFD_problema3"
dot.render(output_filename, format="png", cleanup=True)
dot.render(output_filename, format="svg", cleanup=True)

print(f"✅ Automaton generated in '{output_filename}.png' and '{output_filename}.svg'")
