import streamlit as st

# Import Content Page
from dataCount import target_without_intangible
from dataEvolution import content_data_evolution
from footer import content_footer
from plot import content_testplot
from treemap import content_treemap


# 2023 Analyse page Content
def content_2022(data_plotly_sunburst, data_plotly_treemap, target_classes):
    st.title("""Schema.org annotations observatory in 2022""")
    st.markdown("---")
    st.markdown(
        """
        You can select any type described by Schema.org here and generate an Upsetplot of it. You can also select the number of characteristic sets show in this plot.

        PS: Generating upserplots can take some time (minutes) and more specifically when you generate all property combinations.
        """
    )

    on_target = st.toggle('Trigger this button to filter out Intangibles from the list.', key="on_target")
    if on_target:
        st.write('Filter Activate')
        result = target_without_intangible(False, "Before")
        select = st.selectbox("", result)
    else:
        select = st.selectbox("", target_classes)

    col1, col2 = st.columns(2)
    with col1:
        st.write("## Upset Plot")
        content_testplot(select, True, "before")

    with col2:
        st.write("## Treemap")

        colo1, colo2 = st.columns(2)
        with colo1:
            click = st.button("Show global Treemap")

        with colo2:
            on = st.toggle('Trigger this button to filter out Intangibles from the Treemap.')
        filter_intangible = False
        if on:
            st.write('Filter Activate')
            filter_intangible = True
        # Generates a treemap and display it
        content_treemap(filter_intangible, data_plotly_treemap, data_plotly_sunburst, select, click)

    # Display table for the year 2022
    content_data_evolution(select, "before")

    content_footer()
