import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import json
import glob
import re
import plotly.graph_objects as go
import pandas as pd

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

#-------------------Chart-----------------
# Count
def count(resultats, result):
    data = {
        'Type': ['isa:<schema.org/' + result + '>', 'isa:<schema.org/' + result + '>'],
        'Metric': ['count_before', 'count_after'],
        'Value': [resultats['count_before'], resultats['count_after']]
    }

    # Créer un DataFrame à partir des données avec un index explicite
    df = pd.DataFrame(data, index=['count_before', 'count_after'])

    # Créer un graphique à barres
    fig = px.bar(df, x=df.index, y='Value', text='Value', title='Chart of the evolution: Count')

    # Mettre en forme les étiquettes sur l'axe y avec deux chiffres après la virgule
    fig.update_layout(yaxis=dict(tickformat=".2f"))
    # Afficher le graphique
    st.plotly_chart(fig, use_container_width=True)
    pass
# -------------------------------
# Average
def average(resultats, result):
    data = {
        'Type': ['isa:<schema.org/'+result+'>', 'isa:<schema.org/'+result+'>'],
        'Metric': ['average_before', 'average_after'],
        'Value': [resultats['average_before'], resultats['average_after']]
    }

    # Créer un DataFrame à partir des données avec un index explicite
    df = pd.DataFrame(data, index=['average_before', 'average_after'])

    # Créer un graphique à barres
    fig = px.bar(df, x=df.index, y='Value', text='Value', title='Chart of the evolution: Average')

    # Mettre en forme les étiquettes sur l'axe y avec deux chiffres après la virgule
    fig.update_layout(yaxis=dict(tickformat=".2f"))
    # Afficher le graphique
    st.plotly_chart(fig, use_container_width=True)
    pass
# -------------------------------
# Coverage
def coverage(resultats, result):
    data = {
        'Type': ['isa:<schema.org/' + result + '>', 'isa:<schema.org/' + result + '>'],
        'Metric': ['coverage_before', 'coverage_after'],
        'Value': [resultats['coverage_before'], resultats['coverage_after']]
    }

    # Créer un DataFrame à partir des données avec un index explicite
    df = pd.DataFrame(data, index=['coverage_before', 'coverage_after'])

    # Créer un graphique à barres
    fig = px.bar(df, x=df.index, y='Value', text='Value', title='Chart of the evolution: Coverage')

    # Mettre en forme les étiquettes sur l'axe y avec deux chiffres après la virgule
    fig.update_layout(yaxis=dict(tickformat=".2f"))
    # Afficher le graphique
    st.plotly_chart(fig, use_container_width=True)
    pass
# -------------------------------
# Percentage
def percentage(resultats, result):
    data = {
        'Type': ['isa:<schema.org/' + result + '>', 'isa:<schema.org/' + result + '>','isa:<schema.org/' + result + '>'
                 ],
        'Metric': ['percentage_count_evolution', 'percentage_average_evolution', 'percentage_coverage_evolution'],
        'Value': [resultats['percentage_count_evolution'], resultats['percentage_average_evolution'],
                  resultats['percentage_coverage_evolution']]
    }

    # Créer un DataFrame à partir des données avec un index explicite
    df = pd.DataFrame(data, index=['percentage_count_evolution', 'percentage_average_evolution',
                                   'percentage_coverage_evolution'])

    # Créer un graphique à barres
    fig = px.bar(df, x=df.index, y='Value', text='Value', title='Chart of the evolution: Percentage')

    # Mettre en forme les étiquettes sur l'axe y avec deux chiffres après la virgule
    fig.update_layout(yaxis=dict(tickformat=".2f"))
    # Afficher le graphique
    st.plotly_chart(fig, use_container_width=True)
    pass
def content_comparaonTableau(target_classes):
    # Content
    st.title("""In this page we compare the two Dataset from 2022 and 2023""")

    select = st.selectbox("", target_classes)
    result = getCheminForImage(select)

    coll1, coll2 = st.columns(2)
    with coll1:
        st.image(result)

    with coll2:
        st.image(result)

    # Selectbox
    #select = st.selectbox("", target_classes)
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

    #Afficher Graph

    # Selectbox Graph
    graphDispo= ["Global evolution", "Count","Average","Coverage"]
    select = st.selectbox("", graphDispo )
    if select == "Count":
        count(resultats, result)
    if select == "Average":
        average(resultats, result)
    if select == "Coverage":
        coverage(resultats, result)
    if select == "Global evolution":
        percentage(resultats, result)

    # Affiche Tableau de donnee
    values = [['<b>Count</b>', '<b>Average</b>', '<b>Coverage</b>', '<b>Quality</b>'],  # 1st col
              # 2nd col
              [
                  resultats.get('count_before'),
                  resultats.get('average_before'),
                  resultats.get('coverage_before'),
                  resultats.get('quality_before')],
              # 3rd col
              [
                  resultats.get('percentage_count_evolution'),
                  resultats.get('percentage_average_evolution'),
                  resultats.get('percentage_coverage_evolution'),
                  resultats.get('percentage_quality_evolution')],
              # 4th col
              [
                  resultats.get('count_after'),
                  resultats.get('average_after'),
                  resultats.get('coverage_after'),
                  resultats.get('quality_after')]
              ]

    fig = go.Figure(data=[go.Table(
        columnorder=[1, 2, 3, 4],
        columnwidth=[20, 80, 80, 80],
        header=dict(
            values=[[], ['<b>Data from 2022</b>'], ['<b>Percentage Evolution</b>'],
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

    # Afficher les résultats
    #for key, value in resultats.items():
    #    st.write(f"{key}: {value}")



def data_for_type(type_to_find):
    # Charger le fichier JSON
    with open('dataEvolution/evolutionDataPerTypeFixed.json', 'r') as file:
        dataFile = json.load(file)

    # Type que vous recherchez
    type_recherche = "isa:<schema.org/"+type_to_find+">"

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



