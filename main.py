import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import json
import glob
import re

# Import Content Page
from welcome import content_welcome
from comparison import content_comparison
from year2023 import content_2023
from year2022 import content_2022
from newStyle import content_new_style
from parse import parseWindow
from parse import parseMac



# Custom CSS
custom_css = """
<style>
    /* Your custom CSS goes here */
   [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
    }
    .st-emotion-cache-1y4p8pa {
        max-width: 95%
    }
</style>
"""

# List of Schema available
top_20_target_classes = [
    "ListItem",
    "ImageObject",
    "BreadcrumbList",
    "Organization",
    "WebPage",
    "SearchAction",
    "Offer",
    "Person",
    "ReadAction",
    "Product",
    "EntryPoint",
    "PostalAddress",
    "Article",
    "WebSite",
    "CollectionPage",
    "NewsArticle",
    "SiteNavigationElement",
    "ContactPoint",
    "Rating",
    "Place",
]

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

def extraire_contenu_apres_backslash(ma_ligne):
    # Regex pour supprimer tout le contenu avant le dernier caractère '\'
    nouveau_contenu = re.sub(r'^.*\\', '', ma_ligne)
    return nouveau_contenu

def getCheminForImage(nomfichier):
    regexSelect = extraire_contenu_apres_backslash(nomfichier)
    # Utiliser split pour séparer la chaîne en fonction de ":"
    parts = regexSelect.split(":")

    # Concaténer les parties avec le format souhaité
    result = f"assets/plots/{parts[1]}_plot.svg"
    return result

target_classes = []
# Parese Data from target classes
parseWindow(target_classes)
#parseMac(target_classes)

# Version Window
#for file in glob.glob("assets/plots/*.svg"):
    # Utilisez split pour séparer le chemin du fichier
    #parts = file.split("/")
    
    # Extrait le premier élément après "assets"
    #fname = parts[1]  # parts[0] est "assets", parts[1] est "plots"

    #parts2 = fname.split("plots")
    # Extrait le premier élément après "plots"
    #newFname =parts2[1]

    # Utiliser split pour séparer la chaîne en fonction de "\"
    #parts = newFname.split("\\")

    # Concaténer les parties avec "schema:"
    #newFname ="".join(parts[1:])

    # Supprime l'extension ".svg"
    #cname = newFname.split("_plot.svg")[0]
    
    # Ajoute à la liste avec le préfixe "schema:"
    #target_classes.append(f"schema:{cname}")

# Version Mac
# for file in glob.glob("assets/plots/*.svg"):
# Utilisez split pour séparer le chemin du fichier
#   parts = file.split("/")

#  fname = parts[2]
# parts2 = fname.split(".")
# Extrait le premier élément après "plots"
# newFname =parts2[0]

# cname = newFname.split("_plot")[0]
# if cname != "Intangible":
# target_classes.append(f"schema:{cname}")


# sunburst
data_plotly_sunburst = {"ids": [], "names": [], "parents": [], "values": []}
with open("data/count.json", "r") as file:
    parsed_json = json.load(file)

    itemlist = sorted(item_generator(parsed_json, "children"), key=lambda x: x[0])

    nodelist = []
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

# Define content show, sidebar
def main():
    content_sidebar()
    return None

# Side Content
def content_sidebar():
    # Display custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    st.sidebar.title("Here you can navigate throught the demo")
    with st.sidebar:
        selected_tab = option_menu(
            menu_title = "Summary",
            options=["Welcome page","Data from 2022","New Data from 2023","Comparison between the two dataset","New style of chart"],
        )
    if selected_tab =="Welcome page":
        content_welcome()
    if selected_tab =="Data from 2022":
        content_2022(data_plotly_sunburst,target_classes)
    if selected_tab =="New Data from 2023":
        content_2023(data_plotly_sunburst,target_classes)
    if selected_tab =="Comparison between the two dataset":
        content_comparison(target_classes)
    if selected_tab =="New style of chart":
        content_new_style()

# Run the app
if __name__ == '__main__':
    main()