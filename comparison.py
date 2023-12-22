import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import json
import glob
import re

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

# Comparison page Content
def content_comparison(target_classes):
    # Content
    st.title("""In this page we compare the two Dataset from 2022 and 2023""")

    select =st.selectbox("" ,target_classes)
    result =getCheminForImage(select)

    coll1, coll2 = st.columns(2)
    with coll1:
        st.image(result)

    with coll2:
        st.image(result)

    col1, col2 , col3 = st.columns(3)
    with col1:
        st.write("Average:5")
        st.write("Coverage:3")
        st.write("Count:100")

    with col2:
        st.write("Average evolution: 20%")
        st.write("Coverage evolution: 30%")
        st.write("Count evolution:100%")

    with col3:
        st.write("Average:7")
        st.write("Coverage:5")
        st.write("Count:200")