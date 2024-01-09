import streamlit as st


def content_welcome():
    # Content
    st.title("""TheMiKroloG: The Microdata Knowledge Graph""")

    st.write("## Introduction")
    st.write(
        """Welcome to an immersive experience, we invite you to explore the rich tapestry of web data collected through the "Common Crawl" initiative over two distinct years.""")
    st.markdown("[Previous demo in Dash](https://schema-obs-demo.onrender.com/) ")
    st.markdown("Link of the article relate to this demo : [Article link](https://hal.science/hal-04250523/document)")
    st.write("## About Common Crawl")
    st.write(
        "Common Crawl is a monumental effort to index and archive the vast expanse of the World Wide Web. Through meticulous crawling, it captures web pages, providing a comprehensive snapshot of the internet's content at different points in time. Leveraging the open nature of Common Crawl data. Our research delves into those data and aim to extract valuable insights between years.")
    st.write("## Content")
    st.write(
        """To make it simple and interactive, you can select each type and show an Upsetplot corresponding to the top 10,15,20,30,40,50 or all of the properties of the type. A treemap is available to view the global type present and there child. This demo also show 3 metrics and there evolution during those two different years. """)
    st.write("## Begin Your Journey")
    st.write(
        """Click on the Summary menu in the side to commence your exploration of Common Crawl data across time.""")
