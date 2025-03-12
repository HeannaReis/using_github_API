import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

GITHUB_USER = os.getenv("GITHUB_USER")
TOKEN = os.getenv("GITHUB_TOKEN")
API_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

print(f"Token carregado com sucesso para {GITHUB_USER}!")  # Para verificar se foi carregado


def get_github_users(url):
    users = set()
    while url:
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            users.update(user['login'] for user in data)
            url = response.links.get('next', {}).get('url')
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter dados da API: {e}")
            return None
    return users

def unfollow_users(users_to_unfollow):
    unfollowed_users = []
    for user in users_to_unfollow:
        unfollow_url = f"{API_URL}/user/following/{user}"
        try:
            response = requests.delete(unfollow_url, headers=HEADERS)
            response.raise_for_status()
            unfollowed_users.append(user)
            print(f"Deixou de seguir: {user}")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao deixar de seguir {user}: {e}")
    return unfollowed_users

def main():
    following_url = f"{API_URL}/users/{GITHUB_USER}/following"
    followers_url = f"{API_URL}/users/{GITHUB_USER}/followers"

    following = get_github_users(following_url)
    followers = get_github_users(followers_url)

    if following is None or followers is None:
        return
    
    not_following_back = following - followers
    print("Usuários que você segue, mas que não te seguem de volta:")
    print(not_following_back)

    unfollowed_users = unfollow_users(not_following_back)
    print("Usuários que você deixou de seguir:")
    print(unfollowed_users)

if __name__ == "__main__":
    main()
