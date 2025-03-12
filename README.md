# 🚀 GitHub Unfollower - Automatize quem não te segue de volta! 🚀

## 📌 Sobre o Projeto

Este projeto é uma aplicação Python que utiliza a API do GitHub para identificar usuários que você segue, mas que não te seguem de volta. Além disso, permite que você deixe de seguir automaticamente esses usuários com apenas alguns comandos.

Ideal para manter sua lista de seguidores organizada e evitar aqueles usuários que seguem apenas para ganhar seguidores e depois deixam de seguir.

## 🎯 Funcionalidades

- ✅ Identifica automaticamente usuários que você segue, mas que não te seguem de volta.
- ✅ Permite deixar de seguir automaticamente esses usuários.
- ✅ Utiliza cache para otimizar requisições à API do GitHub.
- ✅ Logs detalhados para acompanhar o processo.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Requests**: Biblioteca para requisições HTTP.
- **Dotenv**: Gerenciamento seguro de variáveis de ambiente.
- **Logging**: Monitoramento e registro de eventos.
- **Functools (lru_cache)**: Otimização de requisições repetidas.

## ⚙️ Como Usar

### 1. Clone o repositório

```bash
git clone https://github.com/HeannaReis/using_github_API.git
cd using_github_API
```
### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure suas variáveis de ambiente
Crie um arquivo .env na raiz do projeto com suas credenciais do GitHub:

```
GITHUB_USER=seu_usuario_github
GITHUB_TOKEN=seu_token_github
```
⚠️ Nota: Gere seu token pessoal em GitHub TokensOpens in a new window; external. com permissão para seguir e deixar de seguir usuários.

### 4. Execute o script
```bash
python main.py
```
## 📂 Estrutura do Projeto
```bash
using_github_API/
├── config.py             # Configuração das variáveis de ambiente e API
├── github_api.py         # Funções para interação com a API do GitHub
├── unfollower.py         # Lógica principal para identificar e remover usuários
├── main.py               # Arquivo principal para execução do script
├── requirements.txt      # Dependências do projeto
└── .env                  # Arquivo com variáveis de ambiente (não versionado)
```

## 🤝 Contribuições
Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.

## ⭐ Apoie o Projeto
Se você gostou do projeto, não esqueça de deixar uma estrela ⭐ no repositório e seguir meu perfil no GitHub HeannaReisOpens in a new window; external..

## 📢 Redes Sociais
Compartilhe sua experiência com o projeto nas redes sociais.