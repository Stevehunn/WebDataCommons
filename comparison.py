import json

import plotly.graph_objects as go
import streamlit as st

from chart import count, coverage, average, percentage
from dataCount import target_without_intangible
# Import Content Page
from plot import content_testplot


def content_comparison(target_classes):
    # Content
    st.title("""In this page we compare the two Dataset from 2022 and 2023""")

    on_target = st.toggle('IF filter is activate, schema Intangible and his child will be exclude', key="on_target")

    if on_target:
        st.write('Filter Activate')
        result = target_without_intangible(False, "Before")
        select = st.selectbox("", result)
    else:
        select = st.selectbox("", target_classes)

    coll1, coll2 = st.columns(2)
    with coll1:
        st.header("Data 2022")
        content_testplot(select, True, "before")

    with coll2:
        st.header("Data 2023")
        content_testplot(select, False, "after")

    # Get Data from dataEvolution
    result = select.split(":")[1]
    type_recherche = result
    resultats = data_for_type(type_recherche)
    st.subheader("Comparison between the different metric")

    # Selectbox Graph
    graphDispo = ["Global evolution", "Count", "Average", "Coverage"]
    select = st.selectbox("", graphDispo)

    # Button to show raw json file of the evolutionDataPerType
    st.link_button("Show raw json file",
                   'https://raw.githubusercontent.com/Stevehunn/WebDataCommonsStreamlit/main/dataEvolution/evolutionDataPerTypeFixed.json')

    # Display Graph
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
                  resultats['count_before'],
                  resultats['average_before'],
                  resultats['coverage_before']],
              # 3rd col
              [
                  resultats['percentage_count_evolution'],
                  resultats['percentage_average_evolution'],
                  resultats['percentage_coverage_evolution']],
              # 4th col
              [
                  resultats['count_after'],
                  resultats['average_after'],
                  resultats['coverage_after']]
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
        data_file = json.load(file)

    # Type you are looking for
    type_recherche = "isa:<schema.org/" + type_to_find + ">"

    # Dictionary to store metric values
    result = {}

    # Find the specific type in the data
    for metric in data_file:
        if metric['type'] == type_recherche:
            # Show metric type
            result["Type"] = metric['type']

            # Store other metrics and their values ​​in the dictionary
            for key, value in metric.items():
                # Exclude the type, because we already stored it
                if key != 'type':
                    result[key] = value

    return result
