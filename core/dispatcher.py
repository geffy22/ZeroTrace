import json
import os
import concurrent.futures
from rich.console import Console

# Импортируем модули разведки
import modules.dns_scan as dns_scan
import modules.whois_scan as whois_scan
import modules.port_scan as port_scan
import modules.web_tech as web_tech
import modules.vuln_scan as vuln_scan
import modules.subdomain_scan as subdomain_scan
import modules.osint_scan as osint_scan

from core.report_writer import write_report

console = Console()

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.json")

MODULES_MAP = {
    "dns_scan": dns_scan,
    "whois_scan": whois_scan,
    "port_scan": port_scan,
    "web_tech": web_tech,
    "vuln_scan": vuln_scan,
    "subdomain_scan": subdomain_scan,
    "osint_scan": osint_scan
}

def load_config():
    if os.path.isfile(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Все модули по умолчанию включены
        return {name: True for name in MODULES_MAP.keys()}

def run_module(mod_name, target, proxy=None):
    console.print(f"[bold blue]🔎 Запуск модуля:[/bold blue] {mod_name}")
    try:
        module = MODULES_MAP[mod_name]
        # Проверяем, принимает ли scan аргумент proxy
        if "proxy" in module.scan.__code__.co_varnames:
            result = module.scan(target, proxy=proxy)
        else:
            result = module.scan(target)
    except Exception as e:
        result = f"Ошибка выполнения модуля {mod_name}: {e}"
    return mod_name, result

def run_recon(target: str, modules_list=None, proxy=None):
    config = load_config()
    report = {}

    if modules_list:
        modules_to_run = [m for m in modules_list if config.get(m, False)]
    else:
        modules_to_run = [m for m, enabled in config.items() if enabled]

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(run_module, mod, target, proxy) for mod in modules_to_run]
        for future in concurrent.futures.as_completed(futures):
            mod_name, output = future.result()
            report[mod_name] = output

    write_report(target, report)
