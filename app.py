import streamlit as st

# 1. Setup (MUST BE FIRST)
st.set_page_config(page_title="St. Beatrix Juanda", page_icon="🏛️")

# 2. Header Section
st.title("🏛️ Panti Asuhan St. Beatrix Juanda")
st.subheader("Digital Management & Supply Guardian System")

st.markdown("""
This platform helps us manage our home more efficiently while teaching our children responsibility and stewardship.
""")

st.divider()

# 3. Status Overview (Visual)
col_a, col_b = st.columns(2)
with col_a:
    st.info("📦 **Logistics:** Monitoring Sembako & Essentials")
with col_b:
    st.success("🛡️ **Guardians:** Character & Hygiene Program")

# 4. Navigation Section (Functional Buttons)
st.write("### 🧭 Quick Navigation")
col1, col2 = st.columns(2)

with col1:
    if st.button("📦 Open Logistics Tracker", use_container_width=True):
        st.switch_page("pages/1_📦_Logistics.py")

with col2:
    if st.button("🛡️ Open Guardian Program", use_container_width=True):
        st.switch_page("pages/2_🛡️_Guardians.py")

st.divider()
st.write("Development is underway. Please check back soon!")
