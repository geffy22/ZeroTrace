import dns.resolver

def scan(target, proxy=None):
    result = {}
    # Прокси в dns.resolver не поддерживается, игнорируем proxy

    try:
        answers = dns.resolver.resolve(target, 'A')
        result['A'] = [rdata.to_text() for rdata in answers]
    except Exception as e:
        result['A'] = f"Ошибка: {e}"

    try:
        answers = dns.resolver.resolve(target, 'AAAA')
        result['AAAA'] = [rdata.to_text() for rdata in answers]
    except Exception as e:
        result['AAAA'] = f"Ошибка: {e}"

    try:
        answers = dns.resolver.resolve(target, 'MX')
        result['MX'] = [rdata.to_text() for rdata in answers]
    except Exception as e:
        result['MX'] = f"Ошибка: {e}"

    try:
        answers = dns.resolver.resolve(target, 'NS')
        result['NS'] = [rdata.to_text() for rdata in answers]
    except Exception as e:
        result['NS'] = f"Ошибка: {e}"

    return result
