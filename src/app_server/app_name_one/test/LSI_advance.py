from .sh_pack.key_extractor import extract_linkable_phrases
from .sh_pack.key_extractor_rake import extract_clickable_keywords_by_rake

from .LSI_keyword import new_blog

all_keywords = extract_linkable_phrases(new_blog)
# print(all_keywords)

all_keywords_rake = extract_clickable_keywords_by_rake(new_blog)
print("My List RAKE = ",)
for (score,keyword) in all_keywords_rake[:20]:
    print(keyword," = ", score)









