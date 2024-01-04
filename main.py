import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import json
import glob
import re

# Import Content Page
from welcome import content_welcome
from year2023 import content_2023
from year2022 import content_2022
from parse import parseWindow, parseMac, parseAfterJsonAvailableMac, parseAfterJsonAvailableWindow , parseBeforeJsonAvailableMac, parseBeforeJsonAvailableWindow
from dataCount import dataCount
from comparaisonTableau import content_comparaonTableau
from plot import content_testplot


# Custom CSS
custom_css = """
<style>
    /* Your custom CSS goes here */
   [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
    }
    .st-emotion-cache-1y4p8pa {
        max-width: 95%
    }
</style>
"""

# Init data

target_classes = []
target_classes_available_after =[]
target_classes_available_before =[]

# Parse Data from target classes

#parseWindow(target_classes)
parseMac(target_classes)

#Parse Json Data from target classes

#parseAfterJsonAvailableWindow(target_classes_available_after)
parseAfterJsonAvailableMac(target_classes_available_after)

#parseBeforeJsonAvailableWindow(target_classes_available_before)
parseBeforeJsonAvailableMac(target_classes_available_before)


# Data sunburst before

data_plotly_sunburst_before = dataCount(False,True)
#data_plotly_sunburst_before = dataBeforeWithoutIntangible()

data_plotly_treemap_before = dataCount(True,True)
#data_plotly_treemap_before = data_before_with_intangible()

# Data sunburst after

data_plotly_sunburst_after = dataCount(False,False)
#data_plotly_sunburst_after = dataAfterWithoutIntangible()

data_plotly_treemap_after = dataCount(True,False)
#data_plotly_treemap_after = dataAfterWithIntangible()

# Define content show, sidebar
def main():
    content_sidebar()
    return None

# Side Content
def content_sidebar():
    # Display custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    st.sidebar.title("Here you can navigate through the demo")
    with st.sidebar:
        selected_tab = option_menu(
            menu_title="Summary",
            options=["Welcome page", "Data from 2022", "New Data from 2023", "Comparison between the two dataset"],
        )
    if selected_tab == "Welcome page":
        content_welcome()
    if selected_tab == "Data from 2022":
        content_2022(data_plotly_sunburst_before, data_plotly_treemap_before, target_classes_available_before)
    if selected_tab == "New Data from 2023":
        content_2023(data_plotly_sunburst_after, data_plotly_treemap_after, target_classes_available_after)
    if selected_tab == "Comparison between the two dataset":
        content_comparaonTableau(target_classes)

# Run the app
if __name__ == '__main__':
    main()