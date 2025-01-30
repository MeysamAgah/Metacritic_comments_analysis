import streamlit as st
import matplotlib.pyplot as plt
from comment_analysis import comment_analysis
import io

st.title("🎮 Game Review Sentiment Analysis")
st.write("Enter the details below to analyze the reviews of the game!")

game_name = st.text_input("Enter game name:", "lies-of-p")
platform = st.text_input("Enter platform:", "playstation-5")
aspects = st.text_area("Enter aspects (comma-separated):", "graphics, gameplay, story").split(", ")
reviewer = st.radio("Reviewer Type:", ["user", "critic"], index=0)
num_comments = st.number_input("Number of comments:", min_value=50, max_value=500, value=50)
user_agent_string = st.text_area("Enter user agent string (leave blank for default):",
                                 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

# Button to run the analysis
if st.button("Run Analysis"):
    st.write("🔄 Running analysis, please wait...")
    try:
        # Call your comment analysis function and get the plot figure
        fig = comment_analysis(game_name, aspects, platform, reviewer, num_comments, user_agent_string)

        # Save the figure to a BytesIO object (in memory)
        img_bytes = io.BytesIO()
        fig.savefig(img_bytes, format='png')
        img_bytes.seek(0)

        # Display the plot image in Streamlit
        st.image(img_bytes, caption="Sentiment Analysis Results", use_column_width=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")
