import plotly.graph_objects as go
import streamlit as st

from comparison import data_for_type


def content_data_evolution(select, subdir: str):
    st.subheader("Metrics")

    # Button to show raw json file of the evolutionDataPerType
    st.link_button("Show raw json file",
                   'https://raw.githubusercontent.com/Stevehunn/WebDataCommonsStreamlit/main/dataEvolution/evolutionDataPerTypeFixed.json')

    # Get Data from dataEvolution
    result = select.split(":")[1]
    type_recherche = result
    resultats = data_for_type(type_recherche)

    if subdir == "before":
        title = "<b>Data from 2022</b>"
    else:
        title = "<b>Data from 2023</b>"

    # Data Table Poster
    values = [[title],  # 1st col
              # 2nd col
              [
                  resultats['count_' + subdir]],
              # 3rd col
              [
                  resultats['average_' + subdir]],
              # 4th col
              [
                  resultats['coverage_' + subdir]]
              ]

    fig = go.Figure(data=[go.Table(
        columnorder=[1, 2, 3, 4],
        columnwidth=[20, 80, 80, 80],
        header=dict(
            values=[[], ['<b>Count</b>'], ['<b>Average</b>'],
                    ['<b>Coverage</b>']],
            line_color='darkslategray',
            fill_color='royalblue',
            align=['left', 'center'],
            font=dict(color='white', size=12),
            height=40
        ),
        cells=dict(
            values=values,
            line_color='darkslategray',
            fill=dict(color=['paleturquoise', 'white']),
            align=['left', 'center', 'center'],
            font_size=12,
            height=30)
    )

    ])
    style = {
        "padding": 10,
        "width": "100%",
        "display": "inline-block",
        "vertical-align": "right",
    },
    st.plotly_chart(fig, use_container_width=True, style=style)
