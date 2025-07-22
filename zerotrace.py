import argparse
import sys
from core.dispatcher import run_recon
from rich.console import Console
from rich.table import Table

console = Console()

def banner():
    print(r"""
███████╗███████╗██████╗  ██████╗     ████████╗██████╗  █████╗  ██████╗███████╗
╚══███╔╝██╔════╝██╔══██╗██╔═══██╗       ██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
  ███╔╝ █████╗  ██████╔╝██║   ██║       ██║   ██████╔╝███████║██║     █████╗  
 ███╔╝  ██╔══╝  ██╔══██╗██║   ██║       ██║   ██╔═══╝ ██╔══██║██║     ██╔══╝  
███████╗███████╗██║  ██║╚██████╔╝       ██║   ██║     ██║  ██║╚██████╗███████╗
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝        ╚═╝   ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝
                         
""")

def print_help():
    table = Table(title="Доступные команды")

    table.add_column("Флаг", style="cyan", no_wrap=True)
    table.add_column("Описание", style="white")

    table.add_row("-g, --goal <цель>", "Запустить полную разведку по IP или домену")
    table.add_row("-m, --modules mod1,mod2", "Указать конкретные модули (через запятую)")
    table.add_row("-p, --proxy <прокси>", "Прокси-сервер для сетевых запросов (http://ip:port)")
    table.add_row("-h, --help", "Показать эту справку")

    console.print(table)

def main():
    banner()

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-g", "--goal", type=str, help="Цель для разведки (IP или домен)")
    parser.add_argument("-m", "--modules", type=str, help="Список модулей через запятую")
    parser.add_argument("-p", "--proxy", type=str, help="Прокси-сервер для сетевых запросов")
    parser.add_argument("-h", "--help", action="store_true", help="Показать справку")

    args = parser.parse_args()

    if args.help or not args.goal:
        print_help()
        sys.exit(0)

    target = args.goal
    modules = args.modules.split(",") if args.modules else None
    proxy = args.proxy

    run_recon(target, modules, proxy)

if __name__ == "__main__":
    main()
