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




abcblog = """

Introduction

Social media marketing has become an essential part of any successful business strategy. With billions of people using platforms like Facebook, Instagram, Twitter, and LinkedIn, businesses have a unique opportunity to reach their target audience and engage with them directly. Using social media effectively can help your business build brand awareness, generate leads, and increase sales.

However, diving into social media marketing without a plan can be overwhelming. It's important to understand how social media can benefit your business and choose the right platforms that align with your goals. Crafting engaging content that resonates with your audience is key to driving results.

Understanding the Benefits of Social Media Marketing

Social media marketing offers numerous benefits for businesses willing to engage with their audience online. One of the most significant advantages is the ability to build brand awareness. By consistently posting and interacting on social platforms, you can keep your business top of mind for potential customers. This increased visibility can lead to greater recognition and trust in your brand.

Another key benefit is the capacity to generate leads and drive sales. Social media allows you to reach people who are already interested in your products or services. Tools like targeted ads and promotions can attract new customers and encourage repeat business. Additionally, many platforms now offer features like in-app shopping, making it easy for users to purchase directly from your posts.

Social media also provides valuable insights into your audience’s preferences and behaviors. By analyzing engagement metrics, such as likes, shares, and comments, you can tailor your marketing strategies to better meet the needs of your followers. This ongoing feedback loop helps you stay relevant and responsive to your audience.

Choosing the Right Platforms for Your Business

Selecting the right social media platforms is crucial for effective marketing. Each platform has its unique strengths and user demographics, so it's essential to choose the ones that align with your business goals. Here’s a quick guide to some of the most popular platforms:

1. Facebook: With its broad user base and advanced targeting options, Facebook is ideal for building community and running detailed ad campaigns.

2. Instagram: Perfect for visual storytelling, Instagram works well for businesses with strong visual content like photos and videos. It's particularly popular among younger users.

3. Twitter: Known for real-time updates and concise messages, Twitter is great for customer service, industry news, and engaging in trending topics.

4. LinkedIn: Best for B2B marketing, LinkedIn connects you with professionals and decision-makers. It's useful for sharing industry insights and networking.

5. Pinterest: Ideal for businesses in the fashion, food, and home decor industries, Pinterest allows you to share visually appealing content that drives traffic to your site.

Before committing to a platform, research where your target audience spends their time. It’s better to focus on a few platforms and do them well rather than spreading yourself too thin across many. This targeted approach ensures that you are reaching the right people with the right message.

Creating Engaging Content That Drives Results

Creating engaging content is key to capturing the attention of your target audience and driving results. The first step is understanding what type of content resonates with your followers. This involves knowing their preferences and behaviors. For example, do they prefer videos, images, infographics, or written posts?

Quality matters more than quantity. Focus on producing high-quality content that provides value to your audience. This can include educational posts, entertaining videos, or inspiring stories. Always aim to solve a problem or fulfill a need for your followers.

Interactive content can also boost engagement. Polls, quizzes, and live Q&A sessions encourage audience participation and keep them coming back for more. Consistent branding across all posts, such as using your logo, brand colors, and unique voice, helps establish a recognizable presence.

Measuring Success and Adjusting Your Strategy

To ensure your social media marketing efforts are effective, it's important to measure your success and adjust your strategy as needed. Start by setting clear, measurable goals. These can include metrics like reach, engagement, website traffic, and conversions.

Use analytics tools provided by social media platforms to track performance. Look at key metrics such as likes, shares, comments, and click-through rates. These insights will show which types of content perform best and how your audience is responding to your posts.

Based on your findings, adjust your strategy to improve results. If a certain type of content isn’t performing well, try something different. Stay flexible and be willing to experiment. Continuously refining your approach will help you better connect with your audience and achieve your marketing goals.

Conclusion

Social media marketing is a powerful tool for any business looking to grow its online presence and engage with customers. By understanding the benefits, choosing the right platforms, creating engaging content, and measuring success, you set the groundwork for a successful social media strategy. These steps will help your business stand out and connect with your target audience in meaningful ways.

At Just Because Media, we specialize in helping businesses achieve their marketing goals through effective social media strategies. Contact us today to learn how we can assist you in maximizing your social media marketing and driving real results for your business. Let’s work together to take your marketing to the next level.

"""




restult = extract_clickable_keywords_by_rake(abcblog)

print("My ABC result = ")
keyResult = [word for(score,word) in restult]
# print(keyResult)
# for (word,score) in restult[:50]:
#     print(f"{score} = {word}")

blogs = get_all_blogs("https://justbecause.media")
print("total blogs = ",len(blogs))



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
from collections import defaultdict

# Sample input
keywords = ['keyword1', 'keyword2', 'keyword3']
blog = {
    'id': 1,
    'link': 'https://example.com/sample-blog',
    'title': 'Sample Blog Title',
    'content': """
    This is a sample blog content containing keyword1 and keyword2.
    It talks about various topics including keyword3 and how they relate to each other.
    Keyword1 is important because it shows the connection to keyword2 and keyword3.
    """
}

# Function to calculate contextual score
def calculate_contextual_score(blog, keywords):
    # Tokenize the blog content into sentences and words
    sentences = sent_tokenize(blog['content'].lower())

    # Initialize a dictionary to hold scores
    scores = defaultdict(lambda: {'id': blog['id'], 'link': blog['link'], 'score': 0})

    # Analyze each keyword
    for keyword in keywords:
        keyword_lower = keyword.lower()
        keyword_count = 0
        context_scores = []

        # Check each sentence for the keyword
        for sentence in sentences:
            # Check if the keyword is present in the sentence
            if keyword_lower in sentence:
                keyword_count += 1
                words = word_tokenize(sentence)

                # Calculate the proximity of other keywords
                proximity_scores = []
                for other_keyword in keywords:
                    if other_keyword.lower() != keyword_lower and other_keyword.lower() in words:
                        # Calculate the distance between the keywords
                        distance = abs(words.index(other_keyword.lower()) - words.index(keyword_lower))
                        proximity_scores.append(1 / (distance + 1))  # Inverse distance score

                # If there are other keywords, average their proximity scores
                if proximity_scores:
                    context_scores.append(sum(proximity_scores) / len(proximity_scores))

        # Calculate the final score
        if context_scores:
            average_proximity_score = sum(context_scores) / len(context_scores)
            total_score = (keyword_count * average_proximity_score)  # Weighted score
            scores[keyword]['score'] = total_score

    return scores


# Analyze the blog
contextual_scores = calculate_contextual_score(blogs[0], keyResult[0:10])
print(12212121,contextual_scores.items())
# Print results
for keyword, data in contextual_scores.items():
    print(f"Keyword: {keyword}, ID: {data['id']}, Link: {data['link']}, Score: {data['score']:.4f}")





# contextual_links = find_contextual_links(blogs[0:2], keyResult[0:10])

