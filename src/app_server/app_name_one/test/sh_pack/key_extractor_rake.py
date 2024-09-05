from rake_nltk import Rake

def extract_clickable_keywords_by_rake(blog_text):
    # Initialize RAKE
    r = Rake()

    # Extract keywords
    r.extract_keywords_from_text(blog_text)

    # Get ranked phrases
    keywords_with_scores = r.get_ranked_phrases_with_scores()

    # Define a function to determine if a keyword is contextually clickable
    def is_contextually_clickable(phrase):
        # Basic checks for context relevance
        if len(phrase.split()) > 1:  # Example: Prefer multi-word phrases
            return True
        return False

    # Create a list of clickable contextual keywords with scores
    clickable_keywords_with_scores = [
        (score, phrase) for score, phrase in keywords_with_scores if is_contextually_clickable(phrase)
    ]

    return clickable_keywords_with_scores

# Sample blog text
blog_text = """
Python is a versatile programming language. It is widely used in data science,
machine learning, web development, and automation. Many developers appreciate
Python for its simplicity and readability.
"""

# Extract clickable keywords
# clickable_keywords = extract_clickable_keywords(blog_text)

# Display the clickable keywords with scores
# print("Clickable Contextual Keywords with Scores:")
# for score, keyword in clickable_keywords:
#     print(f"- Score: {score}, Keyword: '{keyword}'")
