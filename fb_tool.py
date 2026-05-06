import requests
import time
import os
import random

# --- [১. কনফিগারেশন] ---
INPUT_FILE = "numbers.txt"
DELAY = 60  # এক নাম্বার থেকে অন্য নাম্বারের বিরতি (সেকেন্ড)

# আপনার OwlProxy তথ্য
PROXY_HOST = "change4.owlproxy.com"
PROXY_PORT = "7778"
PROXY_USER = "TvUQjdMO5aA0_custom_zone_MM"
PROXY_PASS = "3011185"

PROXIES = {
    "http": f"http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}",
    "https": f"http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}"
}

# --- [২. ফাংশনসমূহ] ---

def trigger_otp(phone):
    print(f"\n[*] Processing: {phone}")
    
    url = "https://m.facebook.com/reg/submit/"
    
    # শক্তিশালী এবং লেটেস্ট ইউজার এজেন্ট
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
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
        'birthday_year': str(random.randint(1995, 2005)),
        'reg_passwd__': 'Pass' + str(random.randint(1111, 9999)),
        'submit': 'Sign Up'
    }

    # এরর আসলে ২ বার চেষ্টা করার লুপ
    for attempt in range(2):
        try:
            print(f"[!] Attempt {attempt + 1}: Using Proxy {PROXY_HOST}...")
            
            # Timeout ৬০ সেকেন্ড করা হয়েছে যাতে প্রক্সি স্লো হলেও সমস্যা না হয়
            response = requests.post(
                url, 
                data=payload, 
                headers=headers, 
                proxies=PROXIES, 
                timeout=60,
                verify=True
            )
            
            if response.status_code == 200:
                print(f"[+] Success: OTP Request sent for {phone}")
                print("[?] Check your MK Network panel now.")
                return True
            else:
                print(f"[-] Server returned status: {response.status_code}")
                return False
                
        except requests.exceptions.Timeout:
            print(f"[!] Read Timeout on attempt {attempt + 1}. The proxy is slow.")
            if attempt == 0:
                print("[*] Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("[-] Max retries reached. Moving to next number.")
        except requests.exceptions.ProxyError:
            print("[-] Proxy Connection Failed! Check if your IP is Whitelisted.")
            return False
        except Exception as e:
            print(f"[-] Unexpected Error: {e}")
            return False
    return False

def main():
    # টার্মিনাল ক্লিয়ার এবং ব্যানার
    os.system('clear')
    print("="*45)
    print("      FB OTP TOOL - PROXY EDITION")
    print("="*45)

    if not os.path.exists(INPUT_FILE):
        print(f"[-] Error: {INPUT_FILE} not found!")
        return

    with open(INPUT_FILE, "r") as f:
        numbers = [line.strip() for line in f if line.strip()]

    if not numbers:
        print("[-] No numbers found in the file.")
        return

    print(f"[*] Total Numbers: {len(numbers)}")
    print(f"[*] Proxy Zone: {PROXY_USER.split('_')[-1]}") # জোন কোড দেখাবে (MM)
    print("-" * 45)

    for num in numbers:
        trigger_otp(num)
        print(f"[*] Waiting {DELAY} seconds for security...")
        time.sleep(DELAY)

    print("-" * 45)
    print("[★] All Numbers Processed Successfully!")

if __name__ == "__main__":
    main()
