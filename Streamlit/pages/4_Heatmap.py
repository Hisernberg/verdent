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

st.title("Heatmap")

with st.expander("See source code"):
    with st.echo():
        filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
        m = leafmap.Map(center=[40, -100], zoom=4)
        m.add_heatmap(
            filepath,
            latitude="latitude",
            longitude="longitude",
            value="pop_max",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)

