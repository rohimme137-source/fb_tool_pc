import requests
import time
import os
import random

# --- Configuration ---
INPUT_FILE = "numbers.txt"
DELAY = 60  # ওটিপি আসার সম্ভাবনা বাড়াতে ১ মিনিট বিরতি

# আপনার দেওয়া OwlProxy তথ্য অনুযায়ী সাজানো ফরম্যাট
PROXY_HOST = "change4.owlproxy.com"
PROXY_PORT = "7778"
PROXY_USER = "TvUQjdMO5aA0_custom_zone_MM"
PROXY_PASS = "3011185"

# Proxies dictionary
PROXIES = {
    "http": f"http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}",
    "https": f"http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}"
}

def trigger_otp(phone):
    print(f"\n[*] Processing Number: {phone}")
    print(f"[!] Using Proxy: {PROXY_HOST}")
    
    url = "https://m.facebook.com/reg/submit/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://m.facebook.com',
        'Referer': 'https://m.facebook.com/reg/',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    payload = {
        'firstname': 'Rahim',
        'lastname': 'Khan',
        'reg_email__': phone,
        'sex': '2',
        'birthday_day': str(random.randint(1, 28)),
        'birthday_month': str(random.randint(1, 12)),
        'birthday_year': str(random.randint(1994, 2005)),
        'reg_passwd__': 'Pass' + str(random.randint(1111, 9999)),
        'submit': 'Sign Up'
    }

    try:
        # প্রক্সি এবং টাইমআউট সহ রিকোয়েস্ট
        # verify=False দেওয়া হয়েছে যাতে SSL সার্টিফিকেটে সমস্যা না হয়
        response = requests.post(url, data=payload, headers=headers, proxies=PROXIES, timeout=30)
        
        if response.status_code == 200:
            print(f"[+] Success: OTP Request sent for {phone}")
            print("[?] Check your OTP panel (MK Network) now.")
        else:
            print(f"[-] Failed: Server returned status {response.status_code}")
            
    except requests.exceptions.ProxyError:
        print("[-] Error: Proxy Authentication Failed! Check if your IP is whitelisted in OwlProxy panel.")
    except Exception as e:
        print(f"[-] Unexpected Error: {e}")

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"[-] Error: {INPUT_FILE} not found!")
        return

    with open(INPUT_FILE, "r") as f:
        numbers = [line.strip() for line in f if line.strip()]

    print(f"[*] Total {len(numbers)} numbers. Starting process with OwlProxy...")
    print("-" * 45)

    for num in numbers:
        trigger_otp(num)
        print(f"[*] Waiting {DELAY} seconds for next session...")
        time.sleep(DELAY)

    print("-" * 45)
    print("[★] All tasks completed.")

if __name__ == "__main__":
    main()
