import streamlit as st

# Import Content Page
from dataCount import target_without_intangible
from footer import content_footer
from parse import getCheminForImage
from plot import content_testplot
from treemap import content_treemap


# 2023 Analyse page Content
def content_2023(data_plotly_sunburst, data_plotly_treemap, target_classes):
    st.title("""Schema.org annotations observatory in 2022""")
    st.markdown("---")
    st.markdown(
        """
        In the following upset plots, you can select a Schema.org class and display the most used property combinations.
        You can select top 10, 15,20,30,40,50 or All property combinations. 
        All these 805 plots have been rendered based on the Schema.org characteristic sets we generate dynamically and made available [here](https://zenodo.org/records/8167689)

        In the Treemap, you display the select schema class and display and schema class below.
        You can show the entire Treemap with just a click.

        If need, you can filter the schema or treemap schema to exclude the property combinations "Intangible".

        PS: Generate upserplot can take some time (min) and more specifically when you generate all property combinations.
        """
    )

    on_target = st.toggle('IF filter is activate, schema Intangible and his child will be exclude', key="on_target")

    if on_target:
        st.write('Filter Activate')
        result = target_without_intangible(False, False)
        select = st.selectbox("", result)
        result = getCheminForImage(select)
    else:
        select = st.selectbox("", target_classes)

    col1, col2 = st.columns(2)

    with col1:
        st.write("## Upset Plot")
        content_testplot(select, False)

    with col2:
        st.write("## Treemap")

        colo1, colo2 = st.columns(2)
        with colo1:
            click = st.button("Show global Treemap")

        with colo2:
            on = st.toggle('IF filter is activate, schema Intangible and his child will be exclude')
        filter_intangible = False
        if on:
            st.write('Filter Activate')
            filter_intangible = True
        # Generates a treemap and display it
        content_treemap(filter_intangible, data_plotly_treemap, data_plotly_sunburst, select, click)

    content_footer()
