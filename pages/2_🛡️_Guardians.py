import streamlit as st

st.set_page_config(page_title="Supply Guardians", layout="wide")

st.title("🛡️ Supply Guardians Program")
st.subheader("Stewardship & Character Building for St. Beatrix Juanda")

# 1. Initialize Points in Session State
if 'guardian_points' not in st.session_state:
    st.session_state.guardian_points = {"Jessica & Anabella": 85, "Budi & Tono": 92}

# 2. Top Row: Leaderboard / Points
st.write("### 🏆 Stewardship Leaderboard")
cols = st.columns(2)
for i, (team, points) in enumerate(st.session_state.guardian_points.items()):
    cols[i].metric(label=f"Team: {team}", value=f"{points} XP", delta="Excellent Progress")

st.divider()

# 3. Task Submission Section
st.write("### 📝 Weekly Hygiene & Supply Inspection")
st.info("Guardians: Please complete your physical inspection before submitting this digital log.")

tab1, tab2 = st.tabs(["Restroom A (Jessica & Anabella)", "Pantry (Budi & Tono)"])

with tab1:
    st.markdown("#### 🚽 Restroom A Checklist")
    q1 = st.checkbox("Floors are dry and scrubbed?")
    q2 = st.checkbox("Soap dispensers are refilled?")
    q3 = st.checkbox("Cleaning tools (mops/brushes) are stored neatly?")
    
    if st.button("Submit Restroom A Log"):
        if q1 and q2 and q3:
            st.session_state.guardian_points["Jessica & Anabella"] += 10
            st.success("✅ Log verified! +10 XP added to Jessica & Anabella. Great stewardship!")
            st.balloons()
        else:
            st.warning("⚠️ Please ensure all hygiene tasks are finished before submitting.")

with tab2:
    st.markdown("#### 🍱 Pantry Checklist")
    p1 = st.checkbox("Rice containers are sealed?")
    p2 = st.checkbox("Shelves are organized by expiry date?")
    p3 = st.checkbox("No spills on the floor?")
    
    if st.button("Submit Pantry Log"):
        if p1 and p2 and p3:
            st.session_state.guardian_points["Budi & Tono"] += 10
            st.success("✅ Log verified! +10 XP added to Budi & Tono. Excellent work!")
            st.balloons()
        else:
            st.warning("⚠️ Please ensure the pantry is fully organized before submitting.")

st.divider()
st.caption("Admin Note: Digital logs are used for character evaluation and stock threshold verification.")
