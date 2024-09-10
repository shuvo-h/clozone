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

# Download necessary NLTK data
nltk.download('punkt')

# Load spaCy model for word embeddings
nlp = spacy.load("en_core_web_md")  # You can also use 'en_core_web_lg' for more accuracy

def clean_html(content):
    soup = BeautifulSoup(content, "html.parser")
    return soup.get_text()

def is_keyword_suitable_for_linking(content, keyword):
    clean_content = clean_html(content)

    # Tokenize the cleaned text
    tokenized_sentences = sent_tokenize(clean_content)

    # Process the content and keyword using spaCy's word vectors
    doc_content = nlp(clean_content.lower())
    doc_keyword = nlp(keyword.lower())

    keyword_found = False
    keyword_in_context = False
    highest_similarity = 0

    # Scan for sentences with the keyword and evaluate the context
    for sentence in tokenized_sentences:
        if keyword.lower() in sentence.lower():
            keyword_found = True

            # Check the similarity of the sentence context to the keyword
            sentence_doc = nlp(sentence.lower())
            similarity_score = doc_keyword.similarity(sentence_doc)
            print(similarity_score," = ",keyword)
            if similarity_score > 0.7:  # You can adjust this threshold for context matching
                keyword_in_context = True
                highest_similarity = max(highest_similarity, similarity_score)
                break  # We found a suitable context

    if keyword_found and keyword_in_context:
        return {
            'similarity_score': highest_similarity,
            'keyword_in_context': keyword_in_context
        }

    return None

def find_matching_blogs_for_keywords(blogs, keywords):
    """
    Iterate through each blog and keyword, returning blogs that contextually match any of the keywords.
    """
    matched_blogs = []

    for blog in blogs:
        for keyword in keywords:
            suitability = is_keyword_suitable_for_linking(blog['content'], keyword)

            if suitability:
                matched_blogs.append({
                    'blog': {
                        'id': blog['id'],
                        'link': blog['link'],
                        'title': blog['title'],
                        'content': blog['content']
                    },
                    'keyword': keyword,
                    'reason': suitability
                })

    return matched_blogs if matched_blogs else None

# Example usage:
blogs = get_all_blogs('http://justbecause.media')  # Assume this fetches blog data
matched_blogs = find_matching_blogs_for_keywords(blogs, all_keywords)

if matched_blogs:
    for match in matched_blogs:
        print(f"'{match['keyword']}': {match['blog']['title']} ({match['blog']['link']})")
        print(f"Reason: {match['reason']}")
else:
    print("No suitable blog found.")










# contextual_links = find_contextual_links(blogs[0:2], keyResult[0:10])

