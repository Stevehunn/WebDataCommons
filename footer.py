import streamlit as st

# Import Content Page
from delete import content_delete_svg


def content_footer():
    st.markdown('---')
    st.markdown("<h3 style='text-align: center;'>All the plots display can be save in .svg format or directly via the "
                "link.</h2>",
                unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>If there is a problem during the generation of a Upsetplot, click on the reload button below</h2>",
                unsafe_allow_html=True)
    # Display button to remove previous upsetplot who are not properly generate
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)
    with col5:
        if st.button("Reload Upsetplot", type="primary"):
            content_delete_svg()
            st.write("Upsetplot Reload")