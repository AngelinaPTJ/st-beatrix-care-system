import streamlit as st

st.set_page_config(page_title="Supply Guardians")
st.title("🛡️ Supply Guardians Program")

st.info("Teaching Stewardship and Responsibility to our residents.")

# Duty Roster
st.subheader("Weekly Responsibility Matrix")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Zone: Restroom A**")
    st.write("Guardians: Jessica & Anabella")
    if st.button("Complete Monday Check (Restroom A)"):
        st.success("Log submitted for Jessica & Anabella!")

with col2:
    st.markdown("**Zone: Pantry**")
    st.write("Guardians: Budi & Tono")
    if st.button("Complete Monday Check (Pantry)"):
        st.success("Log submitted for Budi & Tono!")
