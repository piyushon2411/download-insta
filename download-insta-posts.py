import instaloader
from instaloader.exceptions import ConnectionException

def download_instagram_profile(username):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Load the profile by its username
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile '{username}' not found")
        return

    failed_posts = []

    # Iterate over the posts and download them
    for post in profile.get_posts():
        try:
            print(f"Downloading {post.url}")
            loader.download_post(post, target=f"{username}")
        except ConnectionException as e:
            print(f"Error downloading {post.url}: {e}")
            failed_posts.append(post.url)

    # Save the list of failed posts to a text file
    if failed_posts:
        with open(f"{username}_failed_posts.txt", "w") as file:
            for url in failed_posts:
                file.write(f"{url}\n")

        print(f"\nFailed to download {len(failed_posts)} posts. The list of failed posts has been saved to '{username}_failed_posts.txt'")

if __name__ == "__main__":
    # Replace this with the Instagram profile's username you want to download
    username = "awaara.kalam"
    download_instagram_profile(username)
