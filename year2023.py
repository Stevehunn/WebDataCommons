import streamlit as st
# Import Content Page
from dataCount import target_without_intangible
from parse import getCheminForImage
from plot import content_testplot
from treemap import content_treemap

# 2023 Analyse page Content
def content_2023(data_plotly_sunburst, data_plotly_treemap, target_classes):
    st.title("""Schema.org annotations observatory in 2022""")
    st.write("### Deep dive into WebDataCommons JSON-LD markup")

    # Display the Sunburst figure using st.plotly_chart
    # st.write("## Sunburst")
    # st.plotly_chart(figureSunburst, use_container_width=True, style=style)
    # st.markdown("---")
    # Display the Treemap figure using st.plotly_chart

    st.markdown("---")
    st.write("## Upset Plot")
    st.markdown(
        """
        Per-class top-10 property combinations.
        In the following upset plots, you can select a Schema.org class and display the most used property combinations (top-10).
        All these 776 plots have been rendered based on the Schema.org characteristic sets we pre-computed and made available at [https://zenodo.org/records/8167689](https://zenodo.org/records/8167689)

        """
    )

    on_target = st.toggle('IF filter is activate, schema Intangible and his child will be exclude', key="on_target")

    if on_target:
        st.write('Filter Activate')
        result = target_without_intangible(False,False)
        select = st.selectbox("", result)
        result = getCheminForImage(select)
    else:
        select = st.selectbox("", target_classes)

    col1, col2 = st.columns(2)

    with col1:
        # st.image(result)
        content_testplot(target_classes, select, False)

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