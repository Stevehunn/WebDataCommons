import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import json
import glob
import re
class Node:
    def __init__(self, id, generation, parent=None, value=-1) -> None:
        self._id = id
        self._generation = generation
        self._parent = parent
        self._value = value

    def __eq__(self, __value: object) -> bool:
        return self._id == __value._id

    def __repr__(self) -> str:
        return self._id


def item_generator(json_input, lookup_key, depth=None):
    if depth is None:
        depth = 0
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield from item_generator(v, lookup_key, depth + 1)
        yield (depth, json_input)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key, depth)

def dataBeforeWithIntangible():
    data_plotly_sunburst = {"ids": [], "names": [], "parents": [], "values": []}
    with open("dataCount/ClassCountBefore.json", "r") as file:
        parsed_json = json.load(file)

        itemlist = sorted(item_generator(parsed_json, "children"), key=lambda x: x[0])

        nodelist = []
        for generation, parent in itemlist:
            if parent.get("value") is None:
                parent["value"] = 0

            parent_node = Node(parent["@id"], generation, value=parent["value"])
            if parent_node not in nodelist:
                # print(f"Adding {parent_node} to {nodelist}")
                nodelist.append(parent_node)

            if "children" in parent.keys():
                for child in parent.get("children"):
                    if child.get("value") is None:
                        child["value"] = 0
                    child_node = Node(
                        child["@id"], generation, parent=parent["@id"], value=child["value"]
                    )
                    nodelist.append(child_node)

        for node in nodelist:
            id = node._id
            if id in data_plotly_sunburst["ids"]:
                id = f"{node._id} {node._parent} {node._generation}"
            data_plotly_sunburst["ids"].append(id)
            data_plotly_sunburst["names"].append(node._id)
            data_plotly_sunburst["values"].append(node._value)
            data_plotly_sunburst["parents"].append(node._parent)
    return data_plotly_sunburst

def dataBeforeWithoutIntangible():
    data_plotly_sunburst = {"ids": [], "names": [], "parents": [], "values": []}
    with open("dataCount/ClassCountBefore.json", "r") as file:
        parsed_json = json.load(file)

        itemlist = sorted(item_generator(parsed_json, "children"), key=lambda x: x[0])

        nodelist = []
        print(nodelist)
        for generation, parent in itemlist:
            if "schema:Intangible" in json.dumps(parent):
                continue
            if parent.get("value") is None:
                parent["value"] = 0

            parent_node = Node(parent["@id"], generation, value=parent["value"])
            if parent_node not in nodelist:
                # print(f"Adding {parent_node} to {nodelist}")
                nodelist.append(parent_node)

            if "children" in parent.keys():
                for child in parent.get("children"):
                    if child.get("value") is None:
                        child["value"] = 0
                    child_node = Node(
                        child["@id"], generation, parent=parent["@id"], value=child["value"]
                    )
                    nodelist.append(child_node)

        for node in nodelist:
            id = node._id
            if id in data_plotly_sunburst["ids"]:
                id = f"{node._id} {node._parent} {node._generation}"
            data_plotly_sunburst["ids"].append(id)
            data_plotly_sunburst["names"].append(node._id)
            data_plotly_sunburst["values"].append(node._value)
            data_plotly_sunburst["parents"].append(node._parent)
    return data_plotly_sunburst

def dataAfterWithIntangible():
    data_plotly_sunburst = {"ids": [], "names": [], "parents": [], "values": []}
    with open("dataCount/ClassCountAfter.json", "r") as file:
        parsed_json = json.load(file)

        itemlist = sorted(item_generator(parsed_json, "children"), key=lambda x: x[0])

        nodelist = []
        for generation, parent in itemlist:
            if parent.get("value") is None:
                parent["value"] = 0

            parent_node = Node(parent["@id"], generation, value=parent["value"])
            if parent_node not in nodelist:
                # print(f"Adding {parent_node} to {nodelist}")
                nodelist.append(parent_node)

            if "children" in parent.keys():
                for child in parent.get("children"):
                    if child.get("value") is None:
                        child["value"] = 0
                    child_node = Node(
                        child["@id"], generation, parent=parent["@id"], value=child["value"]
                    )
                    nodelist.append(child_node)

        for node in nodelist:
            id = node._id
            if id in data_plotly_sunburst["ids"]:
                id = f"{node._id} {node._parent} {node._generation}"
            data_plotly_sunburst["ids"].append(id)
            data_plotly_sunburst["names"].append(node._id)
            data_plotly_sunburst["values"].append(node._value)
            data_plotly_sunburst["parents"].append(node._parent)
    return data_plotly_sunburst

def dataAfterWithoutIntangible():
    data_plotly_sunburst = {"ids": [], "names": [], "parents": [], "values": []}
    with open("dataCount/ClassCountAfter.json", "r") as file:
        parsed_json = json.load(file)

        itemlist = sorted(item_generator(parsed_json, "children"), key=lambda x: x[0])

        nodelist = []
        print(nodelist)
        for generation, parent in itemlist:
            if "schema:Intangible" in json.dumps(parent):
                continue
            if parent.get("value") is None:
                parent["value"] = 0

            parent_node = Node(parent["@id"], generation, value=parent["value"])
            if parent_node not in nodelist:
                # print(f"Adding {parent_node} to {nodelist}")
                nodelist.append(parent_node)

            if "children" in parent.keys():
                for child in parent.get("children"):
                    if child.get("value") is None:
                        child["value"] = 0
                    child_node = Node(
                        child["@id"], generation, parent=parent["@id"], value=child["value"]
                    )
                    nodelist.append(child_node)

        for node in nodelist:
            id = node._id
            if id in data_plotly_sunburst["ids"]:
                id = f"{node._id} {node._parent} {node._generation}"
            data_plotly_sunburst["ids"].append(id)
            data_plotly_sunburst["names"].append(node._id)
            data_plotly_sunburst["values"].append(node._value)
            data_plotly_sunburst["parents"].append(node._parent)
    return data_plotly_sunburst