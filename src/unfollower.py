from github_api import get_github_users, unfollow_users
from config import API_URL, GITHUB_USER

def get_non_followers() -> set[str]:
    """
    Obtém a lista de usuários que você segue, mas que não te seguem de volta.

    Returns:
        set[str]: Conjunto de usuários que não te seguem de volta.
    """
    following_url = f"{API_URL}/users/{GITHUB_USER}/following"
    followers_url = f"{API_URL}/users/{GITHUB_USER}/followers"

    following = get_github_users(following_url)
    followers = get_github_users(followers_url)

    return following - followers  # Quem você segue, mas não te segue

def remove_non_followers():
    """
    Remove usuários que não seguem de volta.
    """
    non_followers = get_non_followers()
    if non_followers:
        print("Usuários que você segue, mas que não te seguem de volta:")
        print("\n".join(non_followers))
        confirm = input("Deseja parar de segui-los? (s/n): ").strip().lower()
        if confirm == "s":
            unfollowed_users = unfollow_users(non_followers)
            print(f"🚀 Deixou de seguir {len(unfollowed_users)} usuários.")
    else:
        print("🎉 Todos os usuários que você segue também te seguem de volta!")
