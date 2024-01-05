import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from dataCount import target_without_intangible
# Import Content Page
from parse import getCheminForImage
from plot import content_testplot
from chart import count,coverage,average,percentage

def content_comparison(target_classes):
    # Content
    st.title("""In this page we compare the two Dataset from 2022 and 2023""")

    #select = st.selectbox("", target_classes)
    #result = getCheminForImage(select)

    on_target = st.toggle('IF filter is activate, schema Intangible and his child will be exclude', key="on_target")

    if on_target:
        st.write('Filter Activate')
        result = target_without_intangible(False, True)
        select = st.selectbox("", result)
        result = getCheminForImage(select)
    else:
        select = st.selectbox("", target_classes)

    coll1, coll2 = st.columns(2)
    with coll1:
        content_testplot(target_classes, select, True)

    with coll2:
        content_testplot(target_classes, select, False)

    # Selectbox
    result = select.split(":")[1]
    type_recherche = result
    resultats = data_for_type(type_recherche)

    # Charger le fichier JSON
    with open('dataEvolution/evolutionDataPerTypeFixed.json', 'r') as file:
        data = json.load(file)

    # Parcourir chaque objet dans le fichier JSON
    for metric in data:
        # Afficher le type de métrique
        print(f"\nType: {metric['type']}")
        isa = {metric['type']}

        # Afficher les autres métriques et leurs valeurs
        for key, value in metric.items():
            # Exclure le type, car nous l'avons déjà affiché
            if key != 'type':
                print(f"{key}: {value}")

    # Afficher Graph

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

    # Affiche Tableau de donnee
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
    # Charger le fichier JSON
    with open('dataEvolution/evolutionDataPerTypeFixed.json', 'r') as file:
        dataFile = json.load(file)

    # Type que vous recherchez
    type_recherche = "isa:<schema.org/" + type_to_find + ">"

    # Dictionnaire pour stocker les valeurs des métriques
    result = {}

    # Rechercher le type spécifique dans les données
    for metric in dataFile:
        if metric['type'] == type_recherche:
            # Afficher le type de métrique
            result["Type"] = metric['type']

            # Stocker les autres métriques et leurs valeurs dans le dictionnaire
            for key, value in metric.items():
                # Exclure le type, car nous l'avons déjà stocké
                if key != 'type':
                    result[key] = value

    return result
