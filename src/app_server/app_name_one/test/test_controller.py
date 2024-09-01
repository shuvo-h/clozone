#  pip install requests beautifulsoup4 nltk
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import json

# download stopwords
nltk.download('punkt')
# nltk.download() # use only when need manual select which models need to download
nltk.download('stopwords')

"""
# use this two line to open the manual download & install of punket, punkt_tab and others
import nltk
nltk.download()

"""

# fetch all articles from wp
def fetch_wp_posts(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Faild to fetch posts")

# clean and extract key phrases from html content
def extract_key_phrases(content):
    soup = BeautifulSoup(content,"html.parser")
    text = soup.get_text()

    # tokenize the text and remove stopwords
    words = word_tokenize(text=text)
    words = [word.lower() for word in words if word.isalnum()]
    filtered_words = [word for word in words if word not in stopwords.words('english')]

    # frequency distribution of words
    fdist = FreqDist(filtered_words)

    # return the most common phrases
    return fdist.most_common(10)

def createContexualInternalLink(new_blog_content):
    api_url = "https://biddrup.com/wp-json/wp/v2/posts?_embed&per_page=20&page=3"
    # get posts and extract title and contents tupple
    posts = fetch_wp_posts(api_url)
    articles = [(post['title']['rendered'], post['content']['rendered'], post['link']) for post in posts]

    # parse the new blog content to insert internal links
    soup = BeautifulSoup(new_blog_content,'html.parser')
    # new_text = soup.get_text()

    for title, content, link in articles:
        key_phrases = extract_key_phrases(content)
        for phrase, _ in key_phrases:
            # Find the text elements in the soup that contain the phrase
            for text_element in soup.find_all(string=lambda text: phrase in text.lower()):
                new_text = text_element.replace(phrase, f'<a href="{link}">{phrase}</a>')
                text_element.replace_with(BeautifulSoup(new_text, 'html.parser'))

    # Return the final HTML content with internal links inserted
    updated_html_content = str(soup)


    return {
        "ab":123,
        "res":updated_html_content,
        # "articles":articles,
        # "posts":posts,

    }