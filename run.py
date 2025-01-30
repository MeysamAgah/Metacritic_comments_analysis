# imports

from comment_analysis import comment_analysis

if __name__ == "__main__":
    # Example inputs
    game_name = input("Enter the game name: ")
    platform = input("Enter the platform (e.g., playstation-5): ")
    aspects = input("Enter aspects to analyze (comma-separated): ").split(", ")
    reviewer = input("Enter reviewer type (user/critic): ") or "user"
    num_comments = int(input("Enter number of comments to analyze: ") or 50)
    user_agent_string = input("Enter user agent string (press Enter for default): ") or \
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

    # Run analysis
    comment_analysis(game_name, aspects, platform, reviewer, num_comments, user_agent_string )
