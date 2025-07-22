import subprocess

def scan(target, proxy=None):
    # nmap не поддерживает прокси — игнорируем proxy
    try:
        result = subprocess.run(
            ["nmap", "--script", "vuln", "-Pn", target],
            capture_output=True,
            text=True,
            timeout=120
        )
        output = result.stdout.strip()
        if not output:
            return "Уязвимости не найдены."
        return output
    except FileNotFoundError:
        return "Ошибка: nmap не установлен или не найден в PATH."
    except subprocess.TimeoutExpired:
        return "Ошибка: сканирование nmap заняло слишком много времени и было прервано."
    except Exception as e:
        return f"Ошибка при запуске nmap: {e}"
