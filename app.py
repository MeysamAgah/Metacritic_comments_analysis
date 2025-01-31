from flask import Flask, render_template, request, send_file
import os
import matplotlib.pyplot as plt
from comment_analysis import comment_analysis  # Import your function

app = Flask(__name__)

# Define default user agent
DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

@app.route("/", methods=["GET", "POST"])
def index():
    image_path = None  # Placeholder for output image
    if request.method == "POST":
        # Get inputs from form
        game_name = request.form.get("game_name")
        aspects = request.form.getlist("aspects")  # List input
        reviewer = request.form.get("reviewer", "user")
        num_comments = int(request.form.get("num_comments", 50))
        user_agent = request.form.get("user_agent", DEFAULT_USER_AGENT)

        # Ensure num_comments is a multiple of 50
        if num_comments % 50 != 0:
            return "Error: num_comments must be a multiple of 50!"

        # Call comment_analysis and save output plot
        fig = comment_analysis(game_name, aspects, reviewer, num_comments, user_agent)
        image_path = "static/output.png"
        fig.savefig(image_path)  # Save the Matplotlib figure
        plt.close(fig)  # Close plot to free memory

    return render_template("index.html", image_path=image_path)

@app.route("/download")
def download():
    return send_file("static/output.png", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
