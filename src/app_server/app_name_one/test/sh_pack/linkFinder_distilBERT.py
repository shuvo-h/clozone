from .key_extractor import extract_linkable_phrases
from .key_extractor_rake import extract_clickable_keywords_by_rake
from ..LSI_keyword import new_blog
from ..fetcher import get_all_blogs

keywords = extract_linkable_phrases(new_blog)
# all_keywords_rake = [blog[1] for blog in extract_clickable_keywords_by_rake(new_blog)]


# print("RAKE = ",all_keywords_rake)

blogs = get_all_blogs('http://justbecause.media')






# without cache the trasnform existing blogs

from transformers import pipeline
from sentence_transformers import SentenceTransformer, util

# Load the sentence transformer model for contextual embedding comparison
model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')  # You can change this to BERT if needed

def find_contextual_links(blogs, keywords):
    contextual_links = []

    # Extract all blog content and their metadata (ID, link, title)
    blog_contents = [(blog['id'], blog['link'], blog['content']) for blog in blogs]

    # Get the embeddings for all blog contents
    blog_embeddings = model.encode([content for _, _, content in blog_contents], convert_to_tensor=True)

    # Iterate over each keyword
    for keyword in keywords:
        # Get the embedding for the keyword
        keyword_embedding = model.encode(keyword, convert_to_tensor=True)

        # Calculate cosine similarity between the keyword and each blog content
        similarities = util.pytorch_cos_sim(keyword_embedding, blog_embeddings).squeeze(0)

        # Find the blog with the highest similarity
        best_match_idx = similarities.argmax().item()
        best_match_score = similarities[best_match_idx].item()
        print(best_match_score)

        # Set a similarity threshold (adjust based on your needs)
        if best_match_score > 0.5:  # This threshold can be tuned
            best_blog_id, best_blog_link, _ = blog_contents[best_match_idx]
            contextual_links.append({'keyword': keyword, 'link': best_blog_link})

    return contextual_links

print(keywords)
print(len(blogs)," || ",len(keywords))

# Call the method
# contextual_links = find_contextual_links(blogs, keywords)
# print(contextual_links)
















# In-memory cache for blog embeddings
import torch
blog_cache = {}

def update_blog_cache(blogs):
    """
    Updates the cache with the new blog embeddings if they are not already cached.
    """
    for blog in blogs:
        if blog['id'] not in blog_cache:
            # Encode the blog content and store it in the cache
            blog_embedding = model.encode(blog['content'], convert_to_tensor=True)
            blog_cache[blog['id']] = {
                'link': blog['link'],
                'embedding': blog_embedding
            }

def find_contextual_links(blogs, keywords):
    """
    Find contextual links for the given keywords by searching across cached and newly added blogs.
    """
    # Update the cache with any new blogs
    update_blog_cache(blogs)

    # Get cached blog embeddings
    cached_blog_embeddings = [blog_data['embedding'] for blog_data in blog_cache.values()]
    blog_links = [blog_data['link'] for blog_data in blog_cache.values()]

    # Convert cached blog embeddings to a tensor
    cached_blog_embeddings_tensor = torch.stack(cached_blog_embeddings)

    contextual_links = []

    for keyword in keywords:
        # Encode the keyword
        keyword_embedding = model.encode(keyword, convert_to_tensor=True)

        # Calculate cosine similarity between the keyword and all cached blog embeddings
        similarities = util.pytorch_cos_sim(keyword_embedding, cached_blog_embeddings_tensor)[0]  # Get the first row

        # Find the index of the blog with the highest similarity
        best_match_idx = similarities.argmax().item()
        best_match_score = similarities[best_match_idx].item()

        # Set a similarity threshold
        if best_match_score > 0.5:  # Adjust this threshold as needed
            best_blog_link = blog_links[best_match_idx]
            contextual_links.append({'keyword': keyword, 'link': best_blog_link})

    return contextual_links

# Example usage

# First run: Process and cache the blogs
contextual_links = find_contextual_links(blogs, keywords)
print("contextual_links = ", contextual_links)
print(" ")

# Adding a new blog later
new_blogs = [
    {
        'id': 3,
        'link': 'https://example.com/blog3',
        'title': 'Blog 3',
        'content': 'This blog focuses on deep learning and neural networks...'
    }
]

# Second run: Only the new blog will be processed, existing blogs are cached
new_keywords = ['neural networks', 'deep learning']
new_contextual_links = find_contextual_links(new_blogs, new_keywords)
print("new_contextual_links = ", new_contextual_links)

# Cache now contains 3 blogs (existing + new)







