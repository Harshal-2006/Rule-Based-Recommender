import streamlit as st
from database import CATALOGUE

st.set_page_config(page_title="Rule-Based Movie Recommender", page_icon="🎬", layout="centered")

st.title("🎬 Rule-Based Movie Recommendation System")
st.markdown("**Artificial Intelligence Mini-Project**")

st.markdown("---")

# Inference Engine 
def run_movie_inference(user_pref_genre, user_pref_mood, user_pref_pace):
    recommendations = []
    
    for item in CATALOGUE:
        score = 0
        triggered_rules = []    
        # Rule 1: Genre Match (High Weight)
        if item["genre"].lower() == user_pref_genre.lower():
            score += 4
            triggered_rules.append(f"Matched genre rule ('{item['genre']}')")    
        # Rule 2: Mood Match (Medium Weight)
        if item["target_mood"].lower() == user_pref_mood.lower():
            score += 3
            triggered_rules.append(f"Matched target mood ('{item['target_mood']}')")  
        # Rule 3: Pace Match (Low Weight)
        if item["pace"].lower() == user_pref_pace.lower():
            score += 2
            triggered_rules.append(f"Matched pacing ('{item['pace']}')") 
        # Threshold condition: Must meet minimum score criteria
        if score >= 4:
            recommendations.append({
                "title": item["title"],
                "genre": item["genre"],
                "score": score,
                "rating": item["rating"],
                "image": item["image"],
                "trace": triggered_rules
            })
            
    # Sort recommendations by highest score, then rating
    recommendations.sort(key=lambda x: (x["score"], x["rating"]), reverse=True)
    return recommendations

# Sidebar for User Preferences
st.sidebar.header("User Preference Profile")
selected_genre = st.sidebar.selectbox("Select Preferred Genre", ["Sci-Fi", "Mystery", "Comedy", "Fiction"])
selected_mood = st.sidebar.selectbox("Select Desired Mood", ["Thought-Provoking", "Exciting", "Lighthearted", "Inspiring", "Productive"])
selected_pace = st.sidebar.selectbox("Select Preferred Pace", ["Fast", "Moderate", "Slow"])

if st.sidebar.button("Run Inference Engine 🚀"):
    st.subheader("🎯 Recommendation Results & Reasoning Trace")
    results = run_movie_inference(selected_genre, selected_mood, selected_pace)
    if results:
        for idx, rec in enumerate(results, 1):
            with st.expander(f"{idx}. {rec['image']} {rec['title']} (Score: {rec['score']} | Rating: {rec['rating']})"):
                st.markdown(f"**Genre:** {rec['genre']} | **Type:** Movie")
                st.markdown("**Triggered Rules Trace (Explainability Module):**")
                for rule in rec['trace']:
                    st.success(f"✓ [VALID] {rule}")
    else:
        st.warning("No movies met the rule thresholds for your selected criteria. Try broadening your preferences!")
else:
    st.info("Select your preferences in the sidebar and click **Run Inference Engine** to generate recommendations.")
