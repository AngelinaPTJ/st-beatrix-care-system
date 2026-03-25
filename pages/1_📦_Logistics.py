import streamlit as st
import pandas as pd

st.set_page_config(page_title="Logistics Tracker")
st.title("📦 Essentials & Sembako Tracker")

# Sample Inventory Data
data = {
    "Item": ["Beras (Rice)", "Minyak Goreng", "Sabun Mandi", "Detergent", "Pasta Gigi"],
    "Stock": [45, 4, 12, 5, 20],
    "Threshold": [20, 5, 10, 2, 5]
}
df = pd.DataFrame(data)

# Logic for Alerts
df['Status'] = df.apply(lambda x: "🚨 CRITICAL" if x['Stock'] < x['Threshold'] else "✅ OK", axis=1)

st.table(df)

if any(df['Status'] == "🚨 CRITICAL"):
    st.error("Action Required: Some items are below the safety threshold!")
