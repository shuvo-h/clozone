from sentence_transformers import SentenceTransformer, util

from ..sh_pack import key_extractor
from ..fetcher import get_all_blogs

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
            contextual_links.append({'keyword': keyword, 'link': best_blog_link, 'score':best_match_score})

    return contextual_links


def collect_context_links(new_blog,domain):
    keywords= key_extractor.extract_linkable_phrases(new_blog)
    blogs= get_all_blogs(domain)
    contextual_links= find_contextual_links(blogs=blogs,keywords=keywords)


    return {
        "keywords":keywords,
        "contextual_links": contextual_links,
    }