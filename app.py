import streamlit as st

# Custom Branding for St. Beatrix
st.set_page_config(page_title="St. Beatrix Juanda", page_icon="🏛️")

st.title("🏛️ Panti Asuhan St. Beatrix Juanda")
st.subheader("Digital Management & Supply Guardian System")

st.markdown("""
### Welcome to our new system! 
This platform helps us manage our home more efficiently while teaching our children responsibility and stewardship.
""")

# Quick Glance Status
col1, col2 = st.columns(2)
with col1:
    st.info("📦 **Logistics:** Monitoring Sembako & Essentials")
with col2:
    st.success("🛡️ **Guardians:** Character & Hygiene Program")

st.divider()
st.write("Development is underway. Please check back soon!")
