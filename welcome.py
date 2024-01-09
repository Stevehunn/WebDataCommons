import streamlit as st


def content_welcome():
    # Content
    st.title("""Schema.org: How is it being used ?""")

    st.write("## Introduction")
    st.write(
        """The process of searching for information on the World Wide Web is an essential aspect of web
browsing. Often, the results we get come with cards or snippets that provide meaningful information
about the searched item. These are called Rich results. They are typically used by search engines to
improve web pages visibility by displaying them in an engaging and appealing visual format poten-
tially increasing the web page clicks. These rich results are achieved through the use of structured
data. which provides additional context about the content of a web page.""")
    #st.markdown("Link of the previous article : [Article link](https://hal.science/hal-04250523/document)")
    st.write("## Web Data Common")
    st.markdown("We used the data published by [Web Data Common](http://webdatacommons.org) that extracted web entites from the [Common Crawl](https://commoncrawl.org/) data.")

    st.write("## Characteristic Sets")
    st.markdown("To sum up the usage data we used [Characteristic Sets](https://ieeexplore.ieee.org/abstract/document/5767868) that can be represented as [upsetplots](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6876017)")

    st.write("## Measuring Quality")
    st.markdown("In order to compare the data from different years the use is necessary, we chose 3. The count, it's the number of occurence of a type. The average is the average number of properties to describe a specific type. The [coverage](https://www.csd.uoc.gr/~hy561/papers/benchmarking/ApplesandOrangesAComparisonofRDFBenchmarksandRealRDFDatasets.pdf) is measured on the top 10 most used characteristic sets following this definition")

    st.write("## Special thanks")

    col1, col2, col3 = st.columns(3)
    # Set the desired width and height
    width = 300
    height = 150

    # Colonne 1
    with col1:
        st.markdown(
            f'<a href="https://www.univ-nantes.fr/" target="_blank"><img src="https://www.univ-nantes.fr/medias/photo/logotype-nantesuniversite-vecto_1638806640657-png?ID_FICHE=1482184" width="{width}" height="{height}" alt="Image cliquable"></a>',
            unsafe_allow_html=True)

    # Colonne 2
    with col2:
        st.markdown(
            f'<a href="https://www.ls2n.fr/" target="_blank"><img src="https://ls2n.fr/wp-content/uploads/sites/43/2018/07/ls2n-300x165.jpg" width="{width}" height="{height}" alt="Image cliquable"></a>',
            unsafe_allow_html=True)

    # Colonne 3
    with col3:
        st.markdown(
            f'<a href="https://glicid.fr/" target="_blank"><img src="https://glicid.fr/images/logos/glicid-long.svg" width="{width}" height="{height}" alt="Image cliquable"></a>',
            unsafe_allow_html=True)