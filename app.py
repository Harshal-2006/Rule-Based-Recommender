import streamlit as st
from engine import run_inference_engine

st.set_page_config(page_title="Rule-Based Recommender", page_icon="🤖", layout="centered")

st.title("🤖 Rule-Based Recommendation System")
st.markdown("**Artificial Intelligence Mini-Project**")

st.markdown("---")

# Sidebar for User Preferences
st.sidebar.header("User Preference Profile")
selected_type = st.sidebar.selectbox("Select Media Type", ["Book", "Movie"])
selected_genre = st.sidebar.selectbox("Select Preferred Genre", ["Self-Help", "Fiction", "Sci-Fi", "Mystery", "Comedy"])
selected_mood = st.sidebar.selectbox("Select Desired Mood", ["Productive", "Inspiring", "Thought-Provoking", "Exciting", "Lighthearted"])
selected_pace = st.sidebar.selectbox("Select Preferred Pace", ["Fast", "Moderate", "Slow"])

if st.sidebar.button("Run Inference Engine 🚀"):
    st.subheader("🎯 Recommendation Results & Reasoning Trace")
    
    results = run_inference_engine(selected_type, selected_genre, selected_mood, selected_pace)
    
    if results:
        for idx, rec in enumerate(results, 1):
            with st.expander(f"{idx}. {rec['image']} {rec['title']} (Score: {rec['score']} | Rating: {rec['rating']})"):
                st.markdown(f"**Genre:** {rec['genre']} | **Type:** {rec['type']}")
                st.markdown("**Triggered Rules Trace (Explainability Module):**")
                for rule in rec['trace']:
                    st.success(f"✓ [VALID] {rule}")
    else:
        st.warning("No items met the rule thresholds for your selected criteria. Try broadening your preferences!")
else:
    st.info("👈 Select your preferences in the sidebar and click **Run Inference Engine** to generate recommendations.")






