import streamlit as st
import pandas as pd

st.set_page_config(page_title="Logistics Tracker", layout="wide")

st.title("📦 Essentials & Sembako Tracker")
st.write("Manage the stock for St. Beatrix Juanda below.")

# 1. Initialize Data (This keeps the numbers "alive" during your session)
if 'inventory' not in st.session_state:
    st.session_state.inventory = pd.DataFrame({
        "Item": ["Beras (Rice)", "Minyak Goreng", "Sabun Mandi", "Detergent", "Pasta Gigi"],
        "Stock": [45, 4, 12, 5, 20],
        "Threshold": [20, 5, 10, 2, 5]
    })

# 2. Logic: Calculate Status
df = st.session_state.inventory.copy()
df['Status'] = df.apply(lambda x: "🚨 CRITICAL" if x['Stock'] < x['Threshold'] else "✅ OK", axis=1)

# 3. Display the Dashboard Table
st.subheader("Current Inventory Status")
st.table(df)

st.divider()

# 4. THE UPDATE FORM (The Clickable Part)
st.subheader("Update Stock Levels")
with st.form("update_form"):
    item_to_update = st.selectbox("Select Item", df['Item'])
    new_quantity = st.number_input("Enter New Quantity (kg/pcs/liters)", min_value=0)
    submit_button = st.form_submit_button("Update Inventory")

    if submit_button:
        # Update the specific row in our session state
        st.session_state.inventory.loc[st.session_state.inventory['Item'] == item_to_update, 'Stock'] = new_quantity
        st.success(f"Updated {item_to_update} to {new_quantity}!")
        st.rerun() # This refreshes the table at the top instantly

st.divider()
if any(df['Status'] == "🚨 CRITICAL"):
    st.error("Action Required: Some items are below the safety threshold! Please notify the procurement officer.")
