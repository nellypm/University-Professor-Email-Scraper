from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from bs4 import BeautifulSoup
import re

def extract_emails_with_selenium(output_file):
    try:
        # Prompt the user for the URL
        url = input("Enter the URL of the page to scrape: ")
        
        # Update the path to ChromeDriver
        driver_path = "ADD DRIVER PATH"  # macOS/Linux
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
        
        # Open the page
        driver.get(url)

        # Get the rendered page content
        page_content = driver.page_source
        soup = BeautifulSoup(page_content, 'html.parser')

        # Close the WebDriver
        driver.quit()

        # Extract email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = set(re.findall(email_pattern, soup.get_text()))

        # Save the emails to a file
        with open(output_file, 'w') as file:
            for email in sorted(emails):
                file.write(email + '\n')

        if emails:
            print(f"Extracted {len(emails)} emails and saved them to {output_file}")
        else:
            print("No emails were found on the page.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the script
output_file = "emails_extracted.txt"
extract_emails_with_selenium(output_file)

