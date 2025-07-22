import requests

GITHUB_API = "https://api.github.com/search/code"

def scan(target, proxy=None, github_token=None):
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    if github_token:
        headers["Authorization"] = f"token {github_token}"

    proxies = {"http": proxy, "https": proxy} if proxy else None

    query = f'"{target}" in:file'
    params = {"q": query}

    try:
        response = requests.get(GITHUB_API, headers=headers, params=params, timeout=10, proxies=proxies)

        if response.status_code == 403:
            return "Ошибка: превышен лимит GitHub API. Добавьте токен."
        if response.status_code != 200:
            return f"Ошибка GitHub API: {response.status_code}"

        items = response.json().get("items", [])
        results = []

        for item in items:
            repo = item["repository"]["full_name"]
            path = item["path"]
            html_url = item["html_url"]

            results.append({
                "repo": repo,
                "path": path,
                "url": html_url
            })

        return results if results else "Ничего подозрительного не найдено в GitHub."

    except Exception as e:
        return f"Ошибка OSINT GitHub: {e}"
