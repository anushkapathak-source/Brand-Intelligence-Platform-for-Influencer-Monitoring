# import instaloader

# def fetch_instagram_posts(username, max_posts=3):
#     L = instaloader.Instaloader()
#     profile = instaloader.Profile.from_username(L.context, username)

#     posts = []
#     for post in profile.get_posts():
#         posts.append(f"Caption: {post.caption}\n")
#         if len(posts) == max_posts:
#             break

#     return posts
