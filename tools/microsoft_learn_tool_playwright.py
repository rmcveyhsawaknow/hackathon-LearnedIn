# Prerequisites for running this script:
# 1. Install required Python packages:
#    pip install playwright
#    playwright install

# 2. When you run the script:
#    - A browser window will open.
#    - Log in to your Microsoft account (including MFA if required).
#    - The script will automatically click the "Download" button on your Learn profile settings page.
#    - The downloaded file will be saved to the folder you specify.

import os
import requests
import json
import datetime

def download_learn_profile_with_playwright(download_dir):
    """
    Launches a browser, navigates to the Microsoft Learn profile settings page,
    and clicks the download button. User must log in interactively.
    """
    from playwright.sync_api import sync_playwright

    os.makedirs(download_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()
        # Go to the settings page
        page.goto("https://learn.microsoft.com/en-us/users/me/settings#download-data-form")
        print("Please log in to your Microsoft account in the opened browser window.")
        # Wait for user to log in and for the download button to be available
        page.wait_for_selector("button:has-text('Download')", timeout=300000)  # Wait up to 5 minutes
        print("Clicking the Download button...")
        with page.expect_download() as download_info:
            page.click("button:has-text('Download')")
        download = download_info.value
        download_path = os.path.join(download_dir, download.suggested_filename)
        download.save_as(download_path)
        print(f"Profile data downloaded to: {download_path}")
        browser.close()

if __name__ == "__main__":
    
    # Example usage for Learn profile download via browser automation
    # Specify the directory where you want to save the downloaded file
    download_dir = os.path.join(os.getcwd(), "data", "inputs", "learn_profile_downloads")
    # Ensure the directory exists
    download_learn_profile_with_playwright(download_dir)
    pass