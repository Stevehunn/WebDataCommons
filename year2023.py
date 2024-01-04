import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import json
import glob
import re
from plot import content_testplot_after

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

# 2023 Analyse page Content
def content_2023(data_plotly_sunburst, target_classes):
    # Content
    st.title("""Schema.org annotations observatory in 2023""")
    st.write("### Deep dive into WebDataCommons JSON-LD markup")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        figure =px.sunburst(
            data_plotly_sunburst,
            ids="ids",
            names="names",
            parents="parents",
            values="values",
        )
        style ={
            "width": "100%",
            "display": "inline-block",
            "vertical-align": "right",
        },

        # Display the Plotly figure using st.plotly_chart
        st.plotly_chart(figure, use_container_width=True, style=style)

    with col2:
        st.markdown(
            """
            Per-class top-10 property combinations.
            In the following upset plots, you can select a Schema.org class and display the most used property combinations (top-10).
            All these 776 plots have been rendered based on the Schema.org characteristic sets we pre-computed and made available at [https://zenodo.org/records/8167689](https://zenodo.org/records/8167689)
    
            """
        )
        select =st.selectbox("" ,target_classes)
        result =getCheminForImage(select)
        #st.image(result)
        content_testplot_after(target_classes, select)
        st.markdown("---")
