import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import numpy as np
import json
import glob
import re
from plot import content_testplot_before


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
def content_2022(data_plotly_sunburst, data_plotly_treemap, target_classes):
    st.title("""Schema.org annotations observatory in 2022""")
    st.write("### Deep dive into WebDataCommons JSON-LD markup")

    style = {
        "padding": 10,
        "width": "100%",
        "display": "inline-block",
        "vertical-align": "right",
    },

    st.markdown("---")
    st.write("## Upset Plot")
    st.markdown(
        """
        Per-class top-10 property combinations.
        In the following upset plots, you can select a Schema.org class and display the most used property combinations (top-10).
        All these 776 plots have been rendered based on the Schema.org characteristic sets we pre-computed and made available at [https://zenodo.org/records/8167689](https://zenodo.org/records/8167689)

        """
    )

    select = st.selectbox("", target_classes)
    result = getCheminForImage(select)
    col1, col2 = st.columns(2)

    with col1:
        content_testplot_before(target_classes, select)

    with col2:
        dd_data_plotly_sunburst = {"ids": [], "names": [], "parents": [], "values": [], "quality": []}
        parents_d = 0

        df_data_plotly_treemap = pd.DataFrame(data_plotly_treemap)

        filtred_data = df_data_plotly_treemap[df_data_plotly_treemap["names"] == select]
        click = st.button("Show global Treemap")

        # Parcourir le DataFrame et collecter les parents
        for index, row in df_data_plotly_treemap.iterrows():
            parent_name = row['parents']
            name = row['names']
            val = row['values']
            qual = row['quality']
            ids = row['ids']

        if click:
            fig_all_data = px.treemap(
                data_plotly_treemap,
                ids="ids",
                names="names",
                parents="parents",
                values="values",
                color="quality",
                color_continuous_scale='RdBu',
                color_continuous_midpoint=np.average(filtred_data['quality'])
            )
        else:
            if parent_name == select:
                print("entree")
                parents_d = 1
                dd_data_plotly_sunburst["parents"].append(parent_name)
                dd_data_plotly_sunburst["names"].append(name)
                dd_data_plotly_sunburst["values"].append(val)
                dd_data_plotly_sunburst["quality"].append(qual)
                dd_data_plotly_sunburst["ids"].append(ids)
            if parents_d == 0:
                fig_all_data = px.treemap(
                    filtred_data,
                    ids="ids",
                    names="names",
                    parents="parents",
                    values="values",
                    color="quality",
                    color_continuous_scale='RdBu',
                    color_continuous_midpoint=np.average(filtred_data['quality']))
            else:
                print(dd_data_plotly_sunburst)
                fig_all_data = px.treemap(
                    dd_data_plotly_sunburst,
                    ids="ids",
                    names="names",
                    parents="parents",
                    values="values",
                    color="values",
                )
        st.write("## Treemap")
        fig_all_data.update_layout(margin=dict(t=50, l=25, r=25, b=25))
        st.plotly_chart(fig_all_data, use_container_width=True, style=style, color="streamlit")