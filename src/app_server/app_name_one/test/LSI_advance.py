from .sh_pack.key_extractor import extract_linkable_phrases
from .sh_pack.key_extractor_rake import extract_clickable_keywords_by_rake

from .LSI_keyword import new_blog
from .fetcher import get_all_blogs

all_keywords = extract_linkable_phrases(new_blog)
# print(all_keywords)

all_keywords_rake = extract_clickable_keywords_by_rake(new_blog)
# print("My List RAKE = ",)
# for (score,keyword) in all_keywords_rake[:20]:
#     print(keyword," = ", score)



# ------------------- find links -----------
"""
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

nlp = spacy.load('en_core_web_sm')

# Function to preprocess text
def preprocess_text(text):
    doc = nlp(text.lower())
    return ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

# Function to score the context of the keyword in the blog
def calculate_context_score(keyword, blog_content):
    keyword_processed = preprocess_text(keyword)
    content_processed = preprocess_text(blog_content)

    # Create TF-IDF vectors for both
    vectorizer = TfidfVectorizer().fit([keyword_processed, content_processed])
    vectors = vectorizer.transform([keyword_processed, content_processed])

    # Calculate cosine similarity as a measure of contextual relevance
    score = cosine_similarity(vectors[0], vectors[1]).flatten()[0]
    return score

# Main function to find contextual links
def find_contextual_links(blogs, keywords):
    results = []

    for keyword in keywords:
        for blog in blogs:
            blog_content = blog['content']
            score = calculate_context_score(keyword, blog_content)
            print(score,blog['id'])
            if score > 0.3:  # Threshold for contextual relevance
                result = {
                    'id': blog['id'],
                    'score': score,
                    'keyword': keyword,
                    'link': blog['link']
                }
                results.append(result)

    return results


# Run the function
contextual_links = find_contextual_links(blogs, keyResult)

# Print results
for link in contextual_links:
    print(link)
"""








import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from bs4 import BeautifulSoup
import spacy
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

# Download necessary NLTK data
nltk.download('punkt')

# Load spaCy model for word embeddings
nlp = spacy.load("en_core_web_md")  # You can also use 'en_core_web_lg' for more accuracy

def clean_html(content):
    soup = BeautifulSoup(content, "html.parser")
    return soup.get_text()

def preprocess_blogs(blogs):
    """
    Preprocess and cache the cleaned content and embeddings for each blog.
    """
    preprocessed_blogs = []
    for blog in blogs:
        clean_content = clean_html(blog['content'])
        doc_content = nlp(clean_content.lower())
        preprocessed_blogs.append({
            'id': blog['id'],
            'link': blog['link'],
            'title': blog['title'],
            'clean_content': clean_content,
            'doc_content': doc_content
        })
    return preprocessed_blogs

def is_keyword_suitable_for_linking(clean_content, doc_content, keyword):
    """
    Check if the keyword is suitable for linking based on similarity score.
    """
    # Process the keyword using spaCy's word vectors
    doc_keyword = nlp(keyword.lower())

    # Check if the keyword exists in the cleaned content
    if keyword.lower() not in clean_content.lower():
        return None  # Keyword not found in the content

    # Calculate the similarity of the entire content to the keyword
    similarity_score = doc_keyword.similarity(doc_content)

    # Return the similarity score regardless of the threshold
    return {
        'similarity_score': similarity_score,
        'content_length': len(clean_content.split()),  # Word count for additional context
        'keyword_found': True
    }

def analyze_keyword_across_blogs(keyword, blogs):
    """
    Analyze each blog for a single keyword and return the blog with the highest similarity score.
    """
    best_match = None
    best_score = -1

    for blog in blogs:
        suitability = is_keyword_suitable_for_linking(blog['clean_content'], blog['doc_content'], keyword)

        if suitability and suitability['similarity_score'] > best_score:
            best_match = {
                'blog': {
                    'id': blog['id'],
                    'link': blog['link'],
                    'title': blog['title']
                },
                'keyword': keyword,
                'reason': suitability
            }
            best_score = suitability['similarity_score']

    return best_match

def find_best_blogs_for_keywords(blogs, keywords):
    """
    Find the best matching blog for each keyword by comparing all blogs for that keyword.
    """
    preprocessed_blogs = preprocess_blogs(blogs)  # Preprocess once
    best_matches = []

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(analyze_keyword_across_blogs, keyword, preprocessed_blogs) for keyword in keywords]
        for future in futures:
            best_match = future.result()
            if best_match:
                best_matches.append(best_match)

    return best_matches if best_matches else None

print(len(all_keywords))
# Fetch blogs and find matches
blogs = get_all_blogs('http://justbecause.media')  # Assume this fetches blog data
best_blogs = find_best_blogs_for_keywords(blogs, all_keywords)

# Display the best-matching blogs for each keyword
if best_blogs:
    for match in best_blogs:
        print(f"'{match['keyword']}': {match['blog']['title']} ({match['blog']['link']})")
        print(f"Similarity Score: {match['reason']['similarity_score']}, Content Length: {match['reason']['content_length']} words\n")
else:
    print("No suitable blog found.")








# contextual_links = find_contextual_links(blogs[0:2], keyResult[0:10])

