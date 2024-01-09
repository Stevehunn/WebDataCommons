import json

import pandas as pd
import streamlit as st


# Convert "new" to empty
def convert_to_numeric(value):
    try:
        return float(value)
    except ValueError:
        return float("inf")


def content_all_data_display():
    # Load JSON file
    with open('dataEvolution/evolutionDataPerTypeFixed.json', 'r') as file:
        data = json.load(file)
    file.close()

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

    # Show DataFrame of all data
    st.write("## Comparison dataframe between the years 2022 and 2023")
    df_rows = []
    for resultats in data:
        df_rows.append({
            "Name": resultats.get('type'),
            "Count 2022": resultats.get('count_before'),
            "Count 2023": resultats.get('count_after'),
            "Percentage count evolution": convert_to_numeric(resultats['percentage_count_evolution']),
            "Average 2022": resultats.get('average_before'),
            "Average 2023": resultats.get('average_after'),
            "Percentage average evolution": convert_to_numeric(resultats['percentage_average_evolution']),
            "Coverage 2022": resultats.get('coverage_before'),
            "Coverage 2023": resultats.get('coverage_after'),
            "Percentage coverage evolution": convert_to_numeric(resultats['percentage_coverage_evolution'])
        })

    # Create the DataFrame from the constructed list
    df_all_data = pd.DataFrame(df_rows)
    st.dataframe(df_all_data, use_container_width=True)

    st.link_button("Show raw json file",
                   'https://raw.githubusercontent.com/Stevehunn/WebDataCommonsStreamlit/main/dataEvolution/evolutionDataPerTypeFixed.json')
