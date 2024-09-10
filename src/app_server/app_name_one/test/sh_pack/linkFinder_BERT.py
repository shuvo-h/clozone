from .key_extractor import extract_linkable_phrases
from .key_extractor_rake import extract_clickable_keywords_by_rake
from ..LSI_keyword import new_blog
from ..fetcher import get_all_blogs

all_keywords = extract_linkable_phrases(new_blog)
# all_keywords_rake = [blog[1] for blog in extract_clickable_keywords_by_rake(new_blog)]


print("BERT = ",all_keywords)
# print("RAKE = ",all_keywords_rake)

blogs = get_all_blogs('http://justbecause.media')











