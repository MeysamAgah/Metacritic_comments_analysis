from fastapi import FastAPI
import gradio as gr
from comment_analysis import comment_analysis  # Import your function

app = FastAPI()

# Function for UI
def analyze_comments(game_name, platform, aspects, reviewer="user", num_comments=50, user_agent=None):
    aspects_list = aspects.split(",")  # Convert comma-separated aspects to a list
    
    # Call your analysis function
    fig = comment_analysis(game_name, platform, aspects_list, reviewer, num_comments, user_agent)
    
    # Save figure to file
    image_path = "output.png"
    fig.savefig(image_path)
    
    return image_path  # Return saved image path

# Gradio Interface
iface = gr.Interface(
    fn=analyze_comments,
    inputs=[
        gr.Textbox(label="Game Name"),  # Game Name
        gr.Textbox(label="Platform (e.g., playstation-5)"),  # Platform
        gr.Textbox(label="Aspects (comma-separated)"),  # Aspects
        gr.Radio(["user", "critic"], label="Reviewer", value="user"),  # Reviewer
        gr.Slider(50, 500, step=50, label="Number of Comments", value=50),  # Number of Comments
        gr.Textbox(label="User Agent", value="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"),  # User Agent
    ],
    outputs=gr.Image(type="filepath"),  # Output as an image
)

@app.get("/")
def read_root():
    return {"message": "Go to /gradio to access the UI"}

@app.get("/gradio")
def launch_gradio():
    iface.launch(share=True)

# Run API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
