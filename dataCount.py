import json

class Node:
    def __init__(self, id_node, generation, value, quality, parent=None) -> None:
        self.id = id_node
        self.generation = generation
        self.parent = parent
        self.value: float = float(value)
        self.quality: float = float(quality)

    def __eq__(self, value) -> bool:
        if isinstance(value, Node):
            return self.id == value.id
        return False

    def __repr__(self) -> str:
        return self.id

def item_generator(json_input, lookup_key, depth=None):
    if depth is None:
        depth = 0
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield from item_generator(v, lookup_key, depth + 1)
        yield depth, json_input
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key, depth)

def dataCount(withintangible, before):
    if before is True:
        path = "dataCount/ClassCountBefore.json"
    else:
        path = "dataCount/ClassCountAfter.json"

    data_plotly_sunburst = {"ids": [], "names": [], "parents": [], "values": [], "quality": []}
    with open(path, "r") as file:
        parsed_json = json.load(file)

        item_list = sorted(item_generator(parsed_json, "children"), key=lambda x: x[0])

        nodelist = []
        print(nodelist)
        for generation, parent in item_list:
            if withintangible is False:
                if "schema:Intangible" in json.dumps(parent):
                    continue
                if parent.get("value") is None:
                    parent["value"] = 0
                if parent.get("quality") is None:
                    parent["quality"] = 0

                parent_node = Node(parent["@id"], generation, parent["value"], parent["quality"])
                if parent_node not in nodelist:
                    nodelist.append(parent_node)

                if "children" in parent.keys():
                    for child in parent.get("children"):
                        if child.get("value") is None:
                            child["value"] = 0
                        if child.get("quality") is None:
                            child["quality"] = 0
                        child_node = Node(
                            child["@id"], generation, child["value"], child["quality"], parent["@id"]
                        )
                        nodelist.append(child_node)
            else:
                if parent.get("value") is None:
                    parent["value"] = 0
                if parent.get("quality") is None:
                    parent["quality"] = 0

                parent_node = Node(parent["@id"], generation, parent["value"], parent["quality"])
                if parent_node not in nodelist:
                    nodelist.append(parent_node)

                if "children" in parent.keys():
                    for child in parent.get("children"):
                        if child.get("value") is None:
                            child["value"] = 0
                        if child.get("quality") is None:
                            child["quality"] = 0
                        child_node = Node(
                            child["@id"], generation, child["value"], child["quality"], parent["@id"]
                        )
                        nodelist.append(child_node)

        for node in nodelist:
            id_node = node.id
            if id_node in data_plotly_sunburst["ids"]:
                id_node = f"{node.id} {node.parent} {node.generation}"
            data_plotly_sunburst["ids"].append(id_node)
            data_plotly_sunburst["names"].append(node.id)
            data_plotly_sunburst["values"].append(node.value)
            data_plotly_sunburst["quality"].append(node.quality)
            data_plotly_sunburst["parents"].append(node.parent)
    return data_plotly_sunburst

def target_without_intangible(withintangible, before):
    result =dataCount(withintangible, before)
    #st.write(result)
    for i in range(0,len(result["parents"])):
        if result["parents"] !="schema:Intagible":
            target =result["names"]
    #st.write(target)
    return target