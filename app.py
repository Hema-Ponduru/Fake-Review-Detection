import streamlit as st
import time
import matplotlib.pyplot as plt

#  Page Config  
st.set_page_config(
    page_title="Deceptive Review Detection",
    page_icon="🕵️",
    layout="centered"
)

st.title("🕵️ Deceptive Review Detection System")

st.divider()

#  Input  
review = st.text_area(
    "✍️ Enter a review to analyze",
    height=130,
    placeholder="Paste the review text here..."
)

if st.button("🔍 Analyze Review"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        with st.spinner("Analyzing review..."):
            time.sleep(2)

        text = review.lower()

        #  Simulated Deceptive Logic  
        deceptive_terms = [
            "best ever", "must buy", "guaranteed",
            "life changing", "everyone must"
        ]

        term_hits = sum(1 for t in deceptive_terms if t in text)
        exclamations = text.count("!")

        deceptive_score = term_hits + (1 if exclamations >= 3 else 0)

        # Simulated probabilities
        ml_prob = 0.45 if deceptive_score < 2 else 0.75
        llm_prob = 0.05 if deceptive_score < 2 else 0.80
        hybrid_prob = round((0.7 * ml_prob + 0.3 * llm_prob), 2)

        # Final Prediction 
        final_label = "GENUINE" if hybrid_prob < 0.5 else "DECEPTIVE"
        confidence = (1 - hybrid_prob) * 100 if final_label == "GENUINE" else hybrid_prob * 100

        st.subheader("📊 Final Prediction")

        if final_label == "GENUINE":
            st.success(f"**✅ PREDICTION: {final_label}**")
        else:
            st.error(f"**❌ PREDICTION: {final_label}**")

        st.write(f"**Confidence:** {confidence:.1f}%")

        st.divider()

        #  Graph 
        st.subheader("📈 Model Score Comparison")

        models = ["ML", "LLM", "Hybrid"]
        scores = [ml_prob, llm_prob, hybrid_prob]

        fig, ax = plt.subplots(figsize=(4, 3))  # Reduced graph size
        ax.bar(models, scores)
        ax.set_ylim(0, 1)
        ax.set_ylabel("Deceptive Probability")
        ax.set_title("Model Comparison")

        st.pyplot(fig)

        st.divider()

        #  Recommendation  
        st.subheader("💡 Recommendation")

        if final_label == "GENUINE":
            st.success("This review appears legitimate. However:")
            st.markdown("""
            - Always use your judgment  
            - Verify important information from multiple sources  
            - Consider context and consistency  
            """)
        else:
            st.error("This review appears deceptive. Please verify before trusting.")

st.caption("Deceptive Review Detection")
