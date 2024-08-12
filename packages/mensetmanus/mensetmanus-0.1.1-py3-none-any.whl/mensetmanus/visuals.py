import mermaid.graph

DESIGN_CYCLE = [
    {
        "id": "A",
        "name": "Define and research the problem",
        "strands": [
            {"id": "1", "name": "Explain and justify the need"},
            {"id": "2", "name": "Identify and prioritize the research"},
            {"id": "3", "name": "Analyze existing products"},
            {"id": "4", "name": "Develop a design brief"},
        ],
    },
    {
        "id": "B",
        "name": "Develop ideas",
        "strands": [
            {"id": "1", "name": "Develop design specifications"},
            {"id": "2", "name": "Develop design ideas"},
            {"id": "3", "name": "Present and justify the chosen design"},
            {"id": "4", "name": "Develop planning drawings, sketches, or diagrams"},
        ],
    },
    {
        "id": "C",
        "name": "Plan and create the solution",
        "strands": [
            {"id": "1", "name": "Construct a logical plan"},
            {"id": "2", "name": "Demonstrate technical skills"},
            {"id": "3", "name": "Follow the plan to create a solution"},
            {"id": "4", "name": "Justify changes made to the design"},
        ],
    },
    {
        "id": "D",
        "name": "Test and evaluate the solution",
        "strands": [
            {"id": "1", "name": "Develop testing methods"},
            {"id": "2", "name": "Evaluate the success of the solution"},
            {"id": "3", "name": "Explain how to improve the solution"},
            {"id": "4", "name": "Explain the impact of the solution"},
        ],
    },
]

def get_design_cycle_diagram():
    text = "flowchart TB\n"
    prev_node = None
    prev_crit = None
    for criteria in DESIGN_CYCLE:
        text += f"\tsubgraph {criteria['id']}[{criteria['id']}: {criteria['name']}]\n"
        prev_node = None
        for strand in criteria["strands"]:
            node_id = f"{criteria['id']}-{strand['id']}"
            node_txt = f"{strand['id']}: {strand['name']}"
            if prev_node is None:
                text += f"\t{node_id}[{node_txt}]\n"
            else:
                text += f"\t{prev_node}-->{node_id}[{node_txt}]\n"
            prev = node_id
        text += f"\tend\n"
        if prev_crit is not None:
            text += f"\t{prev_crit} --> {criteria['id']}\n"
        prev_crit = criteria["id"]
    text += f"\t{DESIGN_CYCLE[-1]['id']} --> {DESIGN_CYCLE[0]['id']}\n"
    return mermaid.graph.Graph("design-cycle", text)
