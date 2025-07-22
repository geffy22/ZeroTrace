import socket
import concurrent.futures

def scan_ports(host, ports=[21,22,23,25,53,80,110,139,143,443,445,3389], timeout=1):
    open_ports = []

    def scan(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((host, port))
                if result == 0:
                    return port
        except:
            return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan, port) for port in ports]
        for future in concurrent.futures.as_completed(futures):
            port = future.result()
            if port:
                open_ports.append(port)

    return open_ports

def scan(target, proxy=None):
    # proxy не поддерживается сокетами
    open_ports = scan_ports(target)

    if open_ports:
        result_lines = ["[✅] Открытые порты обнаружены:\n"]
        for port in open_ports:
            result_lines.append(f" ├─ 🟢 Порт {port} открыт")
        return "\n".join(result_lines)
    else:
        return "[❌] Открытые порты не обнаружены."
