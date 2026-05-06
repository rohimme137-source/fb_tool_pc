import requests
import time
import os

# --- Configuration ---
INPUT_FILE = "numbers.txt"  # Put your numbers here
LOG_FILE = "sent_logs.txt"  # Results will be saved here
DELAY_BETWEEN_REQUESTS = 15 # Delay in seconds

# Your New Access Token
MY_ACCESS_TOKEN = "EAA13JdRf2RoBRfT5vVmOA6QcZAylOeVI1nPVnarJoUcKczkYU6zM3ZAXscFB8dvhm74dNoQ2fthDqo95qyKys2IlKZB3VPPLSHGrGlbEA8bkGIxb5dDTvRiCPKuz6WZCryUdlMqt6gMQZBg7sx0DtupoQMhSfZCpkU2ldtZA8TSZCNEa2jeywDxCZBYKoxvoMahA35GZBip085Bklo3E5nKutIizj2AyW7NbLxD85J0AZDZD"

def send_fb_otp(phone_number):
    print(f"\n[!] Processing: {phone_number}")
    
    # Facebook Mobile API Registration Endpoint
    url = "https://b-api.facebook.com/method/user.register"
    
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8 Pro Build/UQ1A.240205.002) [FBAN/MessengerLite;FBAV/350.0.0.12.100;FBPN/com.facebook.mlite;]",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Registration Payload
    payload = {
        "email": phone_number,
        "firstname": "Rahim",
        "lastname": "Khan",
        "gender": "MALE",
        "birthday": "2000-01-01",
        "password": "pass" + phone_number[-4:], 
        "access_token": MY_ACCESS_TOKEN,
        "format": "JSON"
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        
        # Checking if response is valid JSON
        try:
            response_data = response.json()
        except:
            print(f"[-] Error: Invalid response from server for {phone_number}")
            return "INVALID_RESPONSE"

        if response.status_code == 200:
            print(f"[+] Success: OTP request sent to {phone_number}")
            return "SUCCESS"
        else:
            error_msg = response_data.get("error_msg", "Unknown Error")
            print(f"[-] Failed for {phone_number}: {error_msg}")
            return f"FAILED ({error_msg})"
            
    except Exception as e:
        print(f"[-] System Error: {e}")
        return "SYSTEM_ERROR"

def main():
    # File Check
    if not os.path.exists(INPUT_FILE):
        print(f"[-] Error: '{INPUT_FILE}' not found!")
        print("[!] Please create a 'numbers.txt' file in this folder.")
        return

    # Loading Numbers
    with open(INPUT_FILE, "r") as f:
        numbers = [line.strip() for line in f if line.strip()]

    if not numbers:
        print("[-] No numbers found in the file.")
        return

    print(f"[*] Total {len(numbers)} numbers found. Starting process...")
    print("-" * 40)

    for index, num in enumerate(numbers):
        status = send_fb_otp(num)
        
        # Saving results to log
        with open(LOG_FILE, "a") as log:
            log.write(f"Time: {time.ctime()} | Number: {num} | Status: {status}\n")
        
        # Delay logic
        if index < len(numbers) - 1:
            print(f"[*] Waiting {DELAY_BETWEEN_REQUESTS} seconds for next number...")
            time.sleep(DELAY_BETWEEN_REQUESTS)

    print("-" * 40)
    print("[★] Task Completed! Check 'sent_logs.txt' for details.")

if __name__ == "__main__":
    main()
