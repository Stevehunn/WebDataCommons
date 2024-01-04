import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import numpy as np
import json
import glob
import re
def content_treemap(filter_intangible,data_plotly_treemap,data_plotly_sunburst, select, click):
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
            if parent_name == select:
                print("entree")
                parents_d = 1
                dd_data_plotly_sunburst["parents"].append(parent_name)
                dd_data_plotly_sunburst["names"].append(name)
                dd_data_plotly_sunburst["values"].append(val)
                dd_data_plotly_sunburst["quality"].append(qual)
                dd_data_plotly_sunburst["ids"].append(ids)

        if click:
            fig_all_data = px.treemap(
                data_plotly_sunburst,
                ids="ids",
                names="names",
                parents="parents",
                values="values",
                color="quality",
                color_continuous_scale='RdBu',
                color_continuous_midpoint=np.average(data_plotly_sunburst['quality'])
            )
        else:
            if parents_d == 0:
                fig_all_data = px.treemap(
                    filtered_data,
                    ids="ids",
                    names="names",
                    parents="parents",
                    values="values",
                    color="quality",
                    color_continuous_scale='RdBu',
                    color_continuous_midpoint=np.average(dd_data_plotly_sunburst['quality'])
                )
            else:
                print(dd_data_plotly_sunburst)
                fig_all_data = px.treemap(
                    dd_data_plotly_sunburst,
                    ids="ids",
                    names="names",
                    parents="parents",
                    values="values",
                    color="quality",
                    color_continuous_scale='RdBu',
                    color_continuous_midpoint=np.average(dd_data_plotly_sunburst['quality'])
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
            if parent_name == select:
                print("entree")
                parents_d = 1
                dd_data_plotly_sunburst["parents"].append(parent_name)
                dd_data_plotly_sunburst["names"].append(name)
                dd_data_plotly_sunburst["values"].append(val)
                dd_data_plotly_sunburst["quality"].append(qual)
                dd_data_plotly_sunburst["ids"].append(ids)

        if click:
            fig_all_data = px.treemap(
                data_plotly_treemap,
                ids="ids",
                names="names",
                parents="parents",
                values="values",
                color="quality",
                color_continuous_scale='RdBu',
                color_continuous_midpoint=np.average(data_plotly_treemap['quality'])
            )
        else:
            if parents_d == 0:
                fig_all_data = px.treemap(
                    filtered_data,
                    ids="ids",
                    names="names",
                    parents="parents",
                    values="values",
                    color="quality",
                    color_continuous_scale='RdBu',
                    color_continuous_midpoint=np.average(data_plotly_treemap['quality']))
            else:
                print(dd_data_plotly_sunburst)
                fig_all_data = px.treemap(
                    dd_data_plotly_sunburst,
                    ids="ids",
                    names="names",
                    parents="parents",
                    values="values",
                    color="quality",
                    color_continuous_scale='RdBu',
                    color_continuous_midpoint=np.average(data_plotly_treemap['quality'])
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