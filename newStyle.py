import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import json
import glob
import re

def content_new_style():

    loadTreemapImage ="assets/images/Treemap.png"
    st.write("Treemap")
    st.image(loadTreemapImage)
    st.markdown("---")
    loadVerticalTableAndChart ="assets/images/VerticalTableAndChart.png"
    st.write("Vertical Table and Chart (Histogramme)")
    st.image(loadVerticalTableAndChart)
    st.markdown("---")
    st.write("Image Dynamique URL")
    st.write("lien google drive partagé")
    #possible solution https://docs.streamlit.io/knowledge-base/tutorials/databases/public-gsheet
    st.markdown("![Alt Text](https://drive.google.com/file/d/1UUl6KM01_qK2JD5ZJjCqURiZ3PTxW69Z/view?usp=sharing)")
    st.write("lien google image")
    st.markdown("![Alt Text](https://media.geeksforgeeks.org/wp-content/uploads/20200707212630/treemapplotlypython3.png)")
    st.write("lien giphy.gif")
    st.markdown("![test](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
