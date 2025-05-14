import streamlit as st
import requests

st.title("AI Social Media Post Generator")

platform = st.selectbox("Platform", ["LinkedIn", "X"])
tone = st.selectbox("Tone", ["Professional", "Conversational", "Witty"])
type_ = st.selectbox("Post Type", ["Thought Leadership", "Promo", "Thread"])
audience = st.text_input("Target Audience", "Product Managers")
goal = st.text_input("Goal", "Build personal brand")
topic = st.text_area("Topic or Post Idea")

if st.button("Generate Post"):
    if not topic:
        st.error("Please enter a topic")
    else:
        with st.spinner("Generating..."):
            try:
                response = requests.post("http://localhost:8000/generate", json={
                    "platform": platform,
                    "tone": tone,
                    "type": type_,
                    "audience": audience,
                    "goal": goal,
                    "topic": topic
                })
                response.raise_for_status()  # Raise an exception for bad status codes
                data = response.json()
                post = data.get("post")
                if post:
                    st.success("Done!")
                    st.markdown("### Generated Post")
                    st.write(post)

                    feedback = st.text_area("Your feedback about this post")
                    if st.button("Submit Feedback"):
                        try:
                            feedback_res = requests.post("http://localhost:8000/feedback", json={
                                "post": post,
                                "feedback": feedback
                            })
                            feedback_res.raise_for_status()
                            st.success("Feedback submitted! Thank you.")
                        except Exception as e:
                            st.error(f"Error submitting feedback: {str(e)}")
                else:
                    st.error("No post content received from the server")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to the server: {str(e)}")
            except ValueError as e:
                st.error(f"Error processing server response: {str(e)}") 