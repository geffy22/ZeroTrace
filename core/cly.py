import argparse
from core.dispatcher import run_recon

def handle_args():
    parser = argparse.ArgumentParser(description="ZeroTrace: киберразведка целей")
    parser.add_argument("-g", "--go", help="Запустить разведку цели")
    parser.add_argument("-f", "--format", choices=["txt", "html"], default="txt", help="Формат отчёта")
    parser.add_argument("--no-sub", action="store_true", help="Отключить скан субдоменов")
    parser.add_argument("--no-vuln", action="store_true", help="Пропустить скан уязвимостей")
    parser.add_argument("--quick", action="store_true", help="Быстрый режим")
    parser.add_argument("--diff", action="store_true", help="Сравнить с предыдущим сканом")
    parser.add_argument("--screenshot", action="store_true", help="Сделать скриншот сайта")
    parser.add_argument("--version", action="store_true", help="Показать версию ZeroTrace")

    args = parser.parse_args()

    if args.version:
        print("ZeroTrace v1.0.0")
        return

    if args.go:
        target = args.go
        options = {
            "format": args.format,
            "quick": args.quick,
            "no_sub": args.no_sub,
            "no_vuln": args.no_vuln,
            "diff": args.diff,
            "screenshot": args.screenshot,
        }
        run_recon(target, options)
    else:
        parser.print_help()
