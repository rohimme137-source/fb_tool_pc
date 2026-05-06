import asyncio
import time
import os
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

# --- Configuration ---
INPUT_FILE = "numbers.txt"
DELAY_BETWEEN_ACCOUNTS = 20

async def create_fb_account(phone):
    async with async_playwright() as p:
        print(f"\n[*] Starting automation for: {phone}")
        
        # Termux এর জন্য Chromium পাথ সেট করা
        browser = await p.chromium.launch(
            executable_path='/usr/bin/chromium', # Termux Chromium Path
            headless=True # মোবাইল রিসোর্স বাঁচাতে ব্যাকগ্রাউন্ডে চলবে
        )
        
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
        )
        
        page = await context.new_page()
        await stealth_async(page) # ফেসবুক যাতে বট ধরতে না পারে
        
        try:
            # ফেসবুক রেজিস্ট্রেশন পেজে যাওয়া
            await page.goto("https://m.facebook.com/reg/", wait_until="networkidle")
            await asyncio.sleep(2)

            # তথ্য পূরণ
            await page.fill('input[name="firstname"]', "Rahim")
            await page.fill('input[name="lastname"]', "Khan")
            await page.fill('input[name="reg_email__"]', phone)
            
            # লিঙ্গ নির্বাচন (Male)
            await page.click('input[value="2"]')
            
            # পাসওয়ার্ড
            password = "Pass" + phone[-4:]
            await page.fill('input[name="reg_passwd__"]', password)
            
            # সাইন আপ বাটনে ক্লিক
            await page.click('button[name="submit"]')
            
            print(f"[+] Success: OTP request sent for {phone}")
            await asyncio.sleep(5) # ওটিপি ট্রিগার হওয়ার জন্য সামান্য অপেক্ষা
            
        except Exception as e:
            print(f"[-] Error for {phone}: {e}")
        
        finally:
            await browser.close()

async def main():
    if not os.path.exists(INPUT_FILE):
        print("[-] Error: numbers.txt not found!")
        return

    with open(INPUT_FILE, "r") as f:
        numbers = [line.strip() for line in f if line.strip()]

    print(f"[*] Found {len(numbers)} numbers. Starting Android Automation...")

    for index, num in enumerate(numbers):
        await create_fb_account(num)
        
        if index < len(numbers) - 1:
            print(f"[*] Waiting {DELAY_BETWEEN_ACCOUNTS} seconds...")
            await asyncio.sleep(DELAY_BETWEEN_ACCOUNTS)

if __name__ == "__main__":
    asyncio.run(main())
