import requests
import time
import os

# --- কনফিগারেশন ---
INPUT_FILE = "numbers.txt"  # এই ফাইলে আপনার নাম্বারগুলো রাখুন
LOG_FILE = "sent_logs.txt"  # কাজের রেজাল্ট এখানে সেভ হবে
DELAY_BETWEEN_REQUESTS = 15 # এক নাম্বারের পর ১৫ সেকেন্ড বিরতি

# আপনার দেওয়া লেটেস্ট টোকেন
MY_ACCESS_TOKEN = "EAA13JdRf2RoBRfT5vVmOA6QcZAylOeVI1nPVnarJoUcKczkYU6zM3ZAXscFB8dvhm74dNoQ2fthDqo95qyKys2IlKZB3VPPLSHGrGlbEA8bkGIxb5dDTvRiCPKuz6WZCryUdlMqt6gMQZBg7sx0DtupoQMhSfZCpkU2ldtZA8TSZCNEa2jeywDxCZBYKoxvoMahA35GZBip085Bklo3E5nKutIizj2AyW7NbLxD85J0AZDZD"

def send_fb_otp(phone_number):
    print(f"\n[!] প্রসেস করা হচ্ছে: {phone_number}")
    
    # ফেসবুক মোবাইল এপিআই রেজিস্ট্রেশন এন্ডপয়েন্ট
    url = "https://b-api.facebook.com/method/user.register"
    
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8 Pro Build/UQ1A.240205.002) [FBAN/MessengerLite;FBAV/350.0.0.12.100;FBPN/com.facebook.mlite;]",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # রেজিস্ট্রেশন ডাটা (Payload)
    payload = {
        "email": phone_number,
        "firstname": "Rahim",
        "lastname": "Khan",
        "gender": "MALE",
        "birthday": "2000-01-01",
        "password": "pass" + phone_number[-4:], # নাম্বারের শেষ ৪ ডিজিট দিয়ে পাসওয়ার্ড
        "access_token": MY_ACCESS_TOKEN,
        "format": "JSON"
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        response_data = response.json()
        
        # সফল হলে সাধারণত ফেসবুক থেকে একটি কনফার্মেশন মেসেজ আসে
        if response.status_code == 200:
            print(f"[√] {phone_number} এ কোড পাঠানোর রিকোয়েস্ট সফল।")
            return "SUCCESS"
        else:
            error_msg = response_data.get("error_msg", "Unknown Error")
            print(f"[×] {phone_number} এ সমস্যা হয়েছে: {error_msg}")
            return f"FAILED ({error_msg})"
            
    except Exception as e:
        print(f"[-] এরর: {e}")
        return "ERROR"

def main():
    # ফাইল চেক করা
    if not os.path.exists(INPUT_FILE):
        print(f"[-] এরর: '{INPUT_FILE}' ফাইলটি খুঁজে পাওয়া যায়নি!")
        print("[!] একই ফোল্ডারে একটি 'numbers.txt' ফাইল তৈরি করে তাতে নাম্বারগুলো লিখুন।")
        return

    # নাম্বারগুলো লিস্টে নেওয়া
    with open(INPUT_FILE, "r") as f:
        numbers = [line.strip() for line in f if line.strip()]

    if not numbers:
        print("[-] ফাইলে কোনো নাম্বার নেই।")
        return

    print(f"[*] মোট {len(numbers)} টি নাম্বার পাওয়া গেছে। কাজ শুরু হচ্ছে...")
    print("-" * 40)

    for index, num in enumerate(numbers):
        status = send_fb_otp(num)
        
        # লগ ফাইলে রেজাল্ট সেভ করা
        with open(LOG_FILE, "a") as log:
            log.write(f"Time: {time.ctime()} | Number: {num} | Status: {status}\n")
        
        # শেষ নাম্বারের পর আর বিরতি দেবে না
        if index < len(numbers) - 1:
            print(f"[*] পরবর্তী নাম্বারের জন্য {DELAY_BETWEEN_REQUESTS} সেকেন্ড বিরতি...")
            time.sleep(DELAY_BETWEEN_REQUESTS)

    print("-" * 40)
    print("[★] কাজ শেষ! রেজাল্ট দেখতে 'sent_logs.txt' ফাইলটি দেখুন।")

if __name__ == "__main__":
    main()
