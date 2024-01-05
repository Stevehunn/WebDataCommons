import streamlit as st


def content_welcome():
    # Content
    st.title("""TheMiKroloG: The Microdata Knowledge Graph""")

    st.write("## Introduction")
    st.write(
        """Welcome to an immersive experience that transcends the boundaries of time! In this cutting-edge technical demo, we invite you to explore the rich tapestry of web data collected through the "Common Crawl" initiative over two distinct years. Embark on a journey that unveils the evolution of the digital landscape, showcasing the power of longitudinal data analysis.""")
    st.markdown("[Previous demo in Dash](https://schema-obs-demo.onrender.com/) ")
    st.markdown("Link of the article relate to this demo : [Article link](https://hal.science/hal-04250523/document)")
    st.write("## About Common Crawl")
    st.write(
        "Common Crawl is a monumental effort to index and archive the vast expanse of the World Wide Web. Through meticulous crawling, it captures web pages, providing a comprehensive snapshot of the internet's content at different points in time. Leveraging the open nature of Common Crawl data, our research delves into the depths of this treasure trove, extracting valuable insights that bridge the gap between past and present.")
    st.write("## Key Features")
    st.write("""1. Temporal Evolution Analysis
Dive into a comparative analysis of web content spanning two different years. Witness how the digital landscape has transformed, identify emerging trends, and understand the dynamics that have shaped the online world over time.

2. Data Visualization Showcase
Experience the power of data visualization as we present captivating representations of key trends and patterns. Our interactive visualizations bring to life the wealth of information hidden within the Common Crawl dataset, making complex data accessible and engaging.

3. Innovative Research Findings
Discover groundbreaking research findings derived from the analysis of Common Crawl data. Our team has unearthed compelling correlations, identified influential factors, and examined the nuances that define the evolution of web content over the selected time periods.""")
    st.write("## How to Navigate")
    st.write("""Temporal Selection: Choose the years you wish to explore using the interactive timeline.
Category Insights: Delve into specific content categories to uncover niche trends.
Data Filters: Tailor your exploration by applying filters based on keywords, domains, or geographical regions.""")
    st.write("## Join Us on this Journey")
    st.write(
        """Embark on a captivating exploration of the internet's history. Whether you are a researcher, data enthusiast, or simply curious about the evolution of the digital landscape, our Web Data Time Travel Demo promises a unique and enlightening experience.""")
    st.write("## Begin Your Journey")
    st.write(
        """Click on the Summary menu in the side to commence your exploration of Common Crawl data across time. Uncover the past, understand the present, and glimpse into the future of the World Wide Web.""")
