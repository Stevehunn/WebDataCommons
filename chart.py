import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# -------------------Chart-----------------
# Count
def count(resultats, result):
    data = {
        'Type': ['isa:<schema.org/' + result + '>', 'isa:<schema.org/' + result + '>'],
        'Metric': ['count_before', 'count_after'],
        'Total number of this type': [resultats['count_before'], resultats['count_after']]
    }

    # Créer un DataFrame à partir des données avec un index explicite
    df = pd.DataFrame(data, index=['count_before', 'count_after'])

    # Créer un graphique à barres
    fig = px.bar(df, x=df.index, y='Total number of this type', text='Total number of this type', title='Chart of the evolution: Count')

    # Mettre en forme les étiquettes sur l'axe y avec deux chiffres après la virgule
    fig.update_layout(yaxis=dict(tickformat=".2f"))
    # Afficher le graphique
    st.plotly_chart(fig, use_container_width=True)
    pass


# -------------------------------
# Average
def average(resultats, result):
    data = {
        'Type': ['isa:<schema.org/' + result + '>', 'isa:<schema.org/' + result + '>'],
        'Metric': ['average_before', 'average_after'],
        'Average properties count': [resultats['average_before'], resultats['average_after']]
    }

    # Créer un DataFrame à partir des données avec un index explicite
    df = pd.DataFrame(data, index=['average_before', 'average_after'])

    # Créer un graphique à barres
    fig = px.bar(df, x=df.index, y='Average properties count', text='Average properties count', title='Chart of the evolution: Average')

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
        'Filling rate between 0 and 1': [resultats['coverage_before'], resultats['coverage_after']]
    }

    # Créer un DataFrame à partir des données avec un index explicite
    df = pd.DataFrame(data, index=['coverage_before', 'coverage_after'])

    # Créer un graphique à barres
    fig = px.bar(df, x=df.index, y='Filling rate between 0 and 1', text='Filling rate between 0 and 1', title='Chart of the evolution: Coverage')

    # Mettre en forme les étiquettes sur l'axe y avec deux chiffres après la virgule
    fig.update_layout(yaxis=dict(tickformat=".2f"))
    # Afficher le graphique
    st.plotly_chart(fig, use_container_width=True)
    pass


# -------------------------------
# Percentage
def percentage(resultats, result):
    data = {
        'Type': ['isa:<schema.org/' + result + '>', 'isa:<schema.org/' + result + '>', 'isa:<schema.org/' + result + '>'
                 ],
        'Metric': ['percentage_count_evolution', 'percentage_average_evolution', 'percentage_coverage_evolution'],
        'Evolution in %': [resultats['percentage_count_evolution'], resultats['percentage_average_evolution'],
                  resultats['percentage_coverage_evolution']]
    }

    # Créer un DataFrame à partir des données avec un index explicite
    df = pd.DataFrame(data, index=['percentage_count_evolution', 'percentage_average_evolution',
                                   'percentage_coverage_evolution'])

    # Créer un graphique à barres
    fig = px.bar(df, x=df.index, y='Evolution in %', text='Evolution in %', title='Chart of the evolution: Percentage')

    # Mettre en forme les étiquettes sur l'axe y avec deux chiffres après la virgule
    fig.update_layout(yaxis=dict(tickformat=".2f"))
    # Afficher le graphique
    st.plotly_chart(fig, use_container_width=True)
    pass
