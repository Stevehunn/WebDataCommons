import streamlit as st


def content_footer():
    st.markdown('---')
    st.markdown("<h3 style='text-align: center;'>All the plots display can be save in .svg format or directly via the "
                "link.</h2>",
                unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>If there is a problem during the generation of a Upsetplot, click on the 'Delete previous Upsetplot' button and regenerate your plot</h2>",
                unsafe_allow_html=True)
