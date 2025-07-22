from pathlib import Path
from datetime import datetime
import json
from concurrent.futures import ThreadPoolExecutor

from rich.console import Console
from rich.table import Table
from jinja2 import Environment, FileSystemLoader

console = Console()

BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"
TEMPLATE_DIR = BASE_DIR / "templates"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))

def _save_json(path: Path, data: dict):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def _save_html(path: Path, content: str):
    with path.open("w", encoding="utf-8") as f:
        f.write(content)

def write_report(target: str, report: dict):
    if not report:
        console.print("[bold red]Отчёт пуст — ничего сохранять.[/bold red]")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    base_filename = f"{target}_{timestamp}"
    json_path = REPORTS_DIR / f"{base_filename}.json"
    html_path = REPORTS_DIR / f"{base_filename}.html"

    # Рендерим HTML через Jinja2
    template = env.get_template("report_template.html")
    html_content = template.render(target=target, report=report, timestamp=timestamp)

    # Параллельно сохраняем JSON и HTML
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(_save_json, json_path, report)
        executor.submit(_save_html, html_path, html_content)

    # Красивый вывод
    table = Table(title=f"📊 Отчёт ZeroTrace: [bold cyan]{target}[/bold cyan]")

    table.add_column("Модуль", style="magenta", no_wrap=True)
    table.add_column("Результат", style="white")

    for module, output in report.items():
        preview = str(output).replace("\n", " ")[:100]
        if len(str(output)) > 100:
            preview += "..."
        table.add_row(module, preview)

    console.print(table)
    console.print(f"\n[green]✔ Отчёт сохранён:[/green] [blue]{json_path.name}[/blue], [blue]{html_path.name}[/blue]\n")
