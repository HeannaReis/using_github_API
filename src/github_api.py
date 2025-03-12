import requests
import logging
from functools import lru_cache
from config import API_URL, HEADERS

# Configuração de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@lru_cache(maxsize=10)  # Cache para evitar requisições repetidas
def get_github_users(url: str) -> set[str]:
    """
    Obtém a lista de usuários a partir da API do GitHub.

    Args:
        url (str): URL da API para buscar usuários.

    Returns:
        set[str]: Conjunto de nomes de usuários.
    """
    users = set()
    while url:
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            users.update(user['login'] for user in data)
            url = response.links.get('next', {}).get('url')  # Paginação
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro ao obter dados da API: {e}")
            return set()
    return users

def unfollow_users(users_to_unfollow: set[str]) -> list[str]:
    """
    Deixa de seguir usuários que não seguem de volta.

    Args:
        users_to_unfollow (set[str]): Lista de usuários para parar de seguir.

    Returns:
        list[str]: Lista de usuários que foram removidos.
    """
    unfollowed_users = []
    for user in users_to_unfollow:
        unfollow_url = f"{API_URL}/user/following/{user}"
        try:
            response = requests.delete(unfollow_url, headers=HEADERS)
            response.raise_for_status()
            unfollowed_users.append(user)
            logging.info(f"✅ Deixou de seguir: {user}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro ao deixar de seguir {user}: {e}")
    return unfollowed_users
