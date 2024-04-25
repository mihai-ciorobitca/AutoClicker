import pyautogui
import time
import re
import requests
import os
from PIL import Image
import os


def clicker():
    input("Please enter")
    time.sleep(3)
    try:
        while True:
            pyautogui.click()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")


def url_to_image(input_file):
    # pattern = "https://biblio.manuel-numerique.com/?openBook=9782091145099%3fdXNlclRva2VuPVNULTMyNTczLUlPV0pFbENzZXlJNjZjSHdXWmFFLXByb2RkcGY5LVBGSmlPdGlBdmdOcWswQ0NXZkIyWHh6OUxYYVJWamJ1UTUwNkliTVZSSUE9JmRlbW89ZmFsc2Umd2F0ZXJtYXJrPWZhbHNlJnNlc3Npb25JZD0xMDEyMjk0NjkmY29udGV4dGVFTlQ9c3RpbWNhcw=="
    pattern = r"https://biblio.manuel-numerique.com/epubs/web/3f5092794da76cba7c4c1bb6ac3ad6c2a88a0da5cff1d072e334fd7d20e524d4b20620b3f75975f9/BORDAS/bibliomanuels/distrib_gp/1/6/5110/online/OEBPS/chapter_\d+/Images/Page_\d+\.jpg"
    matched_urls = []
    with open(input_file, "r") as file:
        for line in file:
            matches = re.findall(pattern, line)
            if matches:
                matched_urls.extend(matches)
 
    os.makedirs("downloaded_images", exist_ok=True)
    for idx, url in enumerate(matched_urls, start=1):
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"downloaded_images/image_{idx}.jpg", "wb") as image_file:
                image_file.write(response.content)
                print(f"Image {idx} downloaded and saved successfully.")
        else:
            print(
                f"Failed to download image {idx}. Status code: {response.status_code}"
            )

    print("All images downloaded and saved.")


def image_to_pdf():
    images = [Image.open(f"./pictures/book1pictures/image_{im}.jpg") for im in range(1, 457)]
    pdf_path = "book.pdf"
    images[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )

if __name__ == "__main__":
    # url_to_image(r"./urls/urls-book1.txt")  
    image_to_pdf()  
