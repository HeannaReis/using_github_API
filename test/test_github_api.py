import pytest
from src.github_api import get_github_users
import sys
import os

# Adicionando o diretório src ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'using_api_github', 'src')))


def test_get_github_users():
    url = "https://api.github.com/users/octocat/following"
    users = get_github_users(url)
    assert isinstance(users, set)
    assert "octocat" not in users  # Usuário fictício para testar
