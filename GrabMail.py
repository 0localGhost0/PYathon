'''
###################################################################################
                                                                          #########
                      "ALL INFORMATION SHALL FOREVER REMAIN FREE"         #########
                          -//GHOST                                        #########
                                                                          #########
                                  aghostlyghoul@pm.me                     #########
                                  -------------------                     #########
###################################################################################
'''
import re
import requests

def find_email_addresses(url):

    try:
        response = requests.get(url)

        if response.status_code == 200:
            # REGEX EMAIL EXTRACTION
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            email_addresses = re.findall(email_pattern, response.text)

            return email_addresses
        else:
            raise ValueError("Failed to retrieve the website content.")
    except requests.exceptions.RequestException:
        raise ValueError("Invalid or inaccessible URL.")

website_url = "URL GOES HERE"
email_list = find_email_addresses(website_url)
print(f"Email addresses found on {website_url}:")
for email in email_list:
    print(email)
