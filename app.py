import streamlit as st
import pandas as pd
import subprocess
import components 

st.set_page_config(
    page_icon="🌌",
    layout="wide",
    page_title="Andrew B.",
    initial_sidebar_state="auto"
)

components.render_content()

# if __name__ == "__main__":
#     main()