#ZeroTrace

ZeroTrace — это лёгкий, быстрый и модульный фреймворк для разведки по IP-адресу или доменному имени. Он собирает максимум доступной информации: от DNS и портов до технологий и уязвимостей. Настоящий "следопыт" в мире OSINT и сетевой разведки.



##Возможности

-Сканирование DNS-записей
-Определение IP-адреса, геолокации и AS
-Анализ открытых портов
-Распознавание веб-технологий
-Поиск известных уязвимостей (CVE)
-Поиск субдоменов
-Модули OSINT и расширяемая архитектура
-Красивый CLI-интерфейс с цветным выводом
-Расширяемость: легко добавляй свои модули
-Готов к использованию и настраиваем под задачи

##Установка

Рекомендуется использоваться виртуальное окружение:
python -m venv venv
source venv/bin/activate 

git clone https://github.com/geffy22/ZeroTrace.git
cd ZeroTrace
pip install -r requirements.txt
pip install jinja2 ( Если не установился из "requirements.txt")

Быстрый старт:

python zerotrace.py -g example.com

Пример вывода:

[+] Цель: example.com
[+] IP: 93.184.216.34
[+] Геолокация: United States, California
[+] DNS-записи: A, MX, NS, TXT...
[+] Открытые порты: 80 (HTTP), 443 (HTTPS)
[+] Web-технологии: Nginx, React
[+] Уязвимости: CVE-2021-12345, CVE-2023-67890


Опции CLI

python zerotrace.py --help


Редактировать
-g, --goal <цель>       IP или домен для разведки (обязательно)
--timeout <сек>         Таймаут подключения (по умолчанию: 5)
--modules               Показать доступные модули
--version               Показать версию ZeroTrace
--output <файл>         Сохранить вывод в файл

Отказ от ответственности:
Используй ZeroTrace только в образовательных целях или для тестирования своих ресурсов. Автор не несёт ответственности за любые действия, нарушающие законы.
