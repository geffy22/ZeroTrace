import requests
import concurrent.futures
import socket

def scan(domain, proxy=None):
    subdomains = [
        'www', 'mail', 'ftp', 'test', 'dev', 'admin', 'api', 'blog', 'vpn',
        'shop', 'support', 'staging', 'beta', 'portal', 'forum'
    ]

    results = []

    proxies = {"http": proxy, "https": proxy} if proxy else None

    def check_sub(sub):
        url = f"http://{sub}.{domain}"
        try:
            ip = socket.gethostbyname(f"{sub}.{domain}")
            response = requests.get(url, timeout=2, proxies=proxies)
            return f"{sub}.{domain} — {ip} ({response.status_code})"
        except Exception:
            return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_sub = {executor.submit(check_sub, sub): sub for sub in subdomains}
        for future in concurrent.futures.as_completed(future_to_sub):
            result = future.result()
            if result:
                results.append(result)

    if not results:
        return "Поддомены не найдены."

    return "\n".join(results)
