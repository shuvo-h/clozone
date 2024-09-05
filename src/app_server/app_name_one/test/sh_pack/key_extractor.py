import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser
from nltk.corpus import stopwords


# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

# Define a function to extract meaningful noun and verb phrases
def extract_linkable_phrases(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Part-of-speech tagging
    pos_tags = pos_tag(words)

    # Define chunk grammar to extract meaningful sequences (noun and verb phrases)
    grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>+}                # Noun phrase
        {<NN.*>+}                          # Consecutive nouns
    VP: {<VB.*><DT>?<JJ>*<NN.*>+}          # Verb + Noun phrase
    """

    # Create chunk parser
    chunk_parser = RegexpParser(grammar)

    # Parse the tagged words to extract phrases
    tree = chunk_parser.parse(pos_tags)

    # List of stopwords
    stop_words = set(stopwords.words('english'))

    # Extract noun and verb phrases, ensuring they are meaningful and contain 3 or more words
    phrases = []
    for subtree in tree:
        if isinstance(subtree, nltk.Tree) and subtree.label() in ['NP', 'VP']:
            phrase = ' '.join(word for word, pos in subtree.leaves())
            # Only keep phrases with 3 or more words and avoid possessives
            if len(phrase.split()) >= 3 and "’" not in phrase and phrase.lower() not in stop_words:
                phrases.append(phrase)

    # Deduplicate and return phrases
    return list(dict.fromkeys(phrases))

# Test the function with example text
text = """
When locals see your banner ads on websites or social media, the color scheme should instantly communicate that you’re a brand committed to sustainability and natural living.
This helps create a visual connection between your brand’s values and the services you provide, making your banner ads more effective and memorable.
"""

# phrases = extract_linkable_phrases(text)
# print(phrases)

# Example output to add links manually:
# for phrase in phrases:
#     print(f'Insert link in: "{phrase}"')
