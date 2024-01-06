import json

import plotly.graph_objects as go
import streamlit as st

from chart import count, coverage, average, percentage
from dataCount import target_without_intangible
# Import Content Page
from parse import getCheminForImage
from plot import content_testplot


def content_comparison(target_classes):
    # Content
    st.title("""In this page we compare the two Dataset from 2022 and 2023""")

    on_target = st.toggle('IF filter is activate, schema Intangible and his child will be exclude', key="on_target")

    if on_target:
        st.write('Filter Activate')
        result = target_without_intangible(False, True)
        select = st.selectbox("", result)
    else:
        select = st.selectbox("", target_classes)

    coll1, coll2 = st.columns(2)
    with coll1:
        content_testplot(select, True)

    with coll2:
        content_testplot(select, False)

    # Selectbox
    result = select.split(":")[1]
    type_recherche = result
    resultats = data_for_type(type_recherche)

    # Load JSON file
    with open('dataEvolution/evolutionDataPerTypeFixed.json', 'r') as file:
        data = json.load(file)

    # Loop through each object in JSON file
    for metric in data:
        # Show metric type
        print(f"\nType: {metric['type']}")
        isa = {metric['type']}

        # View other metrics and their values
        for key, value in metric.items():
            # Exclure le type, car nous l'avons déjà affiché
            if key != 'type':
                print(f"{key}: {value}")

    # Selectbox Graph
    graphDispo = ["Global evolution", "Count", "Average", "Coverage"]
    select = st.selectbox("", graphDispo)
    if select == "Count":
        count(resultats, result)
    if select == "Average":
        average(resultats, result)
    if select == "Coverage":
        coverage(resultats, result)
    if select == "Global evolution":
        percentage(resultats, result)

    # Data Table Poster
    values = [['<b>Count</b>', '<b>Average</b>', '<b>Coverage</b>'],  # 1st col
              # 2nd col
              [
                  resultats.get('count_before'),
                  resultats.get('average_before'),
                  resultats.get('coverage_before')],
              # 3rd col
              [
                  resultats.get('percentage_count_evolution'),
                  resultats.get('percentage_average_evolution'),
                  resultats.get('percentage_coverage_evolution')],
              # 4th col
              [
                  resultats.get('count_after'),
                  resultats.get('average_after'),
                  resultats.get('coverage_after')]
              ]

    fig = go.Figure(data=[go.Table(
        columnorder=[1, 2, 3, 4],
        columnwidth=[20, 80, 80, 80],
        header=dict(
            values=[[], ['<b>Data from 2022</b>'], ['<b>Percentage of Evolution</b>'],
                    ['<b>Data from 2023</b>']],
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


def data_for_type(type_to_find):
    # Load JSON file
    with open('dataEvolution/evolutionDataPerTypeFixed.json', 'r') as file:
        dataFile = json.load(file)

    # Type you are looking for
    type_recherche = "isa:<schema.org/" + type_to_find + ">"

    # Dictionary to store metric values
    result = {}

    # Find the specific type in the data
    for metric in dataFile:
        if metric['type'] == type_recherche:
            # Show metric type
            result["Type"] = metric['type']

            # Store other metrics and their values ​​in the dictionary
            for key, value in metric.items():
                # Exclude the type, because we already stored it
                if key != 'type':
                    result[key] = value

    return result
