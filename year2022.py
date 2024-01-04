import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import numpy as np
import json
import glob
import re
from plot import content_testplot


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
        content_testplot(target_classes, select, True)

    with col2:
        st.write("## Treemap")

        colo1, colo2 = st.columns(2)
        with colo1:
            click = st.button("Show global Treemap")

        with colo2:
            on = st.toggle('IF Filter activate, shema:Intangible and his child exclude')
        filter_intangible = False
        if on:
            st.write('Filter Activate')
            filter_intangible = True

        dd_data_plotly_sunburst = {"ids": [], "names": [], "parents": [], "values": [], "quality": []}
        parents_d = 0

        if filter_intangible:
            df_data_plotly_treemap = pd.DataFrame(data_plotly_sunburst)
            filtered_data = df_data_plotly_treemap[df_data_plotly_treemap["names"] == select]
            # Parcourir le DataFrame et collecter les parents
            for index, row in df_data_plotly_treemap.iterrows():
                parent_name = row['parents']
                name = row['names']
                val = row['values']
                qual = row['quality']
                ids = row['ids']

            if click:
                fig_all_data = px.treemap(
                    data_plotly_sunburst,
                    ids="ids",
                    names="names",
                    parents="parents",
                    values="values",
                    color="quality",
                    color_continuous_scale='RdBu',
                    color_continuous_midpoint=np.average(filtered_data['quality'])
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
                        filtered_data,
                        ids="ids",
                        names="names",
                        parents="parents",
                        values="values",
                        color="quality",
                        color_continuous_scale='RdBu',
                        color_continuous_midpoint=np.average(filtered_data['quality']))
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
        if not filter_intangible:
            df_data_plotly_treemap = pd.DataFrame(data_plotly_treemap)
            filtered_data = df_data_plotly_treemap[df_data_plotly_treemap["names"] == select]
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
                    color_continuous_midpoint=np.average(filtered_data['quality'])
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
                        filtered_data,
                        ids="ids",
                        names="names",
                        parents="parents",
                        values="values",
                        color="quality",
                        color_continuous_scale='RdBu',
                        color_continuous_midpoint=np.average(filtered_data['quality']))
                else:
                    print(dd_data_plotly_sunburst)
                    fig_all_data = px.treemap(
                        data_plotly_treemap,
                        ids="ids",
                        names="names",
                        parents="parents",
                        values="values",
                        color="values",
                    )

        fig_all_data.update_layout(
            font=dict(size=20),  # Modifiez la taille de la police ici
            margin=dict(t=0, l=0, r=0, b=0),
        )
        style = {
            "padding": 10,
            "width": "100%",
            "display": "inline-block",
            "vertical-align": "right",
        },
        st.plotly_chart(fig_all_data, use_container_width=True, style=style, color="streamlit")
