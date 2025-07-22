import whois

def scan(target, proxy=None):
    # whois не поддерживает прокси — игнорируем proxy
    try:
        w = whois.whois(target)
        data = {}
        for key in ['domain_name', 'registrar', 'creation_date', 'expiration_date', 'name_servers', 'emails', 'status']:
            value = getattr(w, key, None)
            if value:
                data[key] = value
        return data
    except Exception as e:
        return f"Ошибка whois: {e}"
