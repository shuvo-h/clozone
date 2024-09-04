from .LSI_keyword import new_blog



from rake_nltk import Rake

# Initialize RAKE
rake = Rake()

# Text for keyword extraction


# Extract keywords
rake.extract_keywords_from_text(new_blog)

# Get ranked phrases
keywords = rake.get_ranked_phrases()

# Print the top 3 phrases
print(keywords[:10])






# __________________________________



