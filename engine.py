from database import CATALOGUE

def run_inference_engine(user_pref_type, user_pref_genre, user_pref_mood, user_pref_pace):
    """
    Evaluates items using explicit IF-THEN rules and scoring weights.
    """
    recommendations = []
    
    for item in CATALOGUE:
        score = 0
        triggered_rules = []
        
        # Rule 1: Media Type Hard Filter
        if item["type"].lower() == user_pref_type.lower():
            score += 3
            triggered_rules.append(f"Matched preferred type: {item['type']}")
        else:
            continue  
        # Rule 2: Genre Match
        if item["genre"].lower() == user_pref_genre.lower():
            score += 4
            triggered_rules.append(f"Matched genre rule ('{item['genre']}')")    
        # Rule 3: Mood Match
        if item["target_mood"].lower() == user_pref_mood.lower():
            score += 3
            triggered_rules.append(f"Matched target mood ('{item['target_mood']}')")    
        # Rule 4: Pace Match
        if item["pace"].lower() == user_pref_pace.lower():
            score += 2
            triggered_rules.append(f"Matched pacing ('{item['pace']}')")
        # Threshold condition: Must meet minimum score criteria
        if score >= 7:
            recommendations.append({
                "title": item["title"],
                "type": item["type"],
                "genre": item["genre"],
                "score": score,
                "rating": item["rating"],
                "image": item["image"],
                "trace": triggered_rules
            })
            
    # Sort recommendations by highest score, then rating
    recommendations.sort(key=lambda x: (x["score"], x["rating"]), reverse=True)
    return recommendations