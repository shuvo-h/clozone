import requests

def get_all_blogs(domain):
    # WordPress REST API endpoint for retrieving all posts
    api_url = f"{domain}/wp-json/wp/v2/posts"
    blogs = []
    page = 1
    per_page = 100  # Number of posts per page

    while True:
        print("Fetching page:", page)

        # Send a request to the WordPress API to get posts from a specific page
        response = requests.get(api_url, params={'page': page, 'per_page': per_page})

        # If the response is unsuccessful, break the loop
        if response.status_code != 200:
            print(f"Failed to retrieve data from page {page}: {response.status_code}")
            break

        # Process the posts
        posts = response.json()

        # If no posts are returned, break the loop
        if not posts:
            break

        # Append each post's details to the list
        for post in posts:
            # Check if the post has an 'id', if not, break the loop
            if 'id' not in post:
                print(f"Post on page {page} is missing an 'id', breaking loop.")
                return blogs  # Return the list up to this point

            blog = {
                'id': post['id'],
                'link': post['link'],
                'title': post['title']['rendered'],
                'content': post['content']['rendered']
            }
            blogs.append(blog)

        # Increment page number to get the next batch of posts
        page += 1

    return blogs

# Example usage
# domain = "https://example.com"
# blog_list = get_all_blogs(domain)
# for blog in blog_list:
#     print(blog)
