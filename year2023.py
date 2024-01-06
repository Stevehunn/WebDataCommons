import streamlit as st

# Import Content Page
from dataCount import target_without_intangible
from footer import content_footer
from parse import getCheminForImage
from plot import content_testplot
from treemap import content_treemap


# 2023 Analyse page Content
def content_2023(data_plotly_sunburst, data_plotly_treemap, target_classes):
    st.title("""Schema.org annotations observatory in 2023""")
    st.markdown("---")
    st.markdown(
        """
        You can select any type described by Schema.org here and generate an Upsetplot of it. You can also select the number of characteristic sets show in this plot.

        PS: Generating upserplots can take some time (minutes) and more specifically when you generate all property combinations.

        Trigger this button to filter out Intangibles from the list.
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
