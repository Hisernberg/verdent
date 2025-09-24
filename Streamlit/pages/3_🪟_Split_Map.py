import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info(
    """
    - Web App URL: <https://streamlit.gishub.org>
    - GitHub repository:<https://github.com/Hisernberg/verdent.git>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Nabidnur-abrar at linkdin:[www.linkedin.com/in/nabidnur-abrar-6696562b9] || youtube:[https://www.youtube.com/@Team_BlackBox]
    """
)
st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            left_layer="ESA WorldCover 2020 S2 FCC", right_layer="ESA WorldCover 2020"
        )
        m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")

m.to_streamlit(height=700)

