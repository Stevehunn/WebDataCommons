import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import numpy as np
import json
import glob
import re
from filtred_data import filters
def content_treemap(filter_intangible,data_plotly_treemap,data_plotly_sunburst, select, click):
    
    if filter_intangible:
        df_data_plotly_treemap = pd.DataFrame(data_plotly_sunburst)
        filters(df_data_plotly_treemap,data_plotly_sunburst, click, select)
       
    if not filter_intangible:
        df_data_plotly_treemap = pd.DataFrame(data_plotly_treemap)
        filters(df_data_plotly_treemap,data_plotly_treemap, click, select)
      