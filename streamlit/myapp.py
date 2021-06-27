import streamlit as st
import numpy as np
import pandas as pd

st.title('LimeGuru App')

st.write("This is distribution of technical sessions by technology")

tech_courses = pd.DataFrame(
    [[10,20,30,40], [20,30,40,50],[5,38,45,53] ],
     columns=["java", "big data", "python", "cloud"])

st.write(tech_courses)

tech_courses

st.bar_chart(tech_courses)

st.line_chart(tech_courses)

if st.checkbox('Show Tech Course Distribution'):
    st.bar_chart(tech_courses)
