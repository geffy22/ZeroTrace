import requests

def scan(target, proxy=None):
    url = target
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + target

    proxies = {"http": proxy, "https": proxy} if proxy else None

    try:
        r = requests.get(url, proxies=proxies, timeout=5)
        headers = r.headers
        server = headers.get('Server', 'Не найден')
        x_powered_by = headers.get('X-Powered-By', 'Не найден')

        info = {
            "Server": server,
            "X-Powered-By": x_powered_by,
            "Status Code": r.status_code
        }

        return info
    except Exception as e:
        return f"Ошибка при получении HTTP заголовков: {e}"
