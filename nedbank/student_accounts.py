import requests
from bs4 import BeautifulSoup

url = 'https://personal.nedbank.co.za/bank/bank-accounts/youth-banking/migoals-youth.html'
html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')


with open("nedbankMigoals.html", "w", encoding='utf-8') as file:
    file.write(soup.prettify())


#     youth_accounts = youth_accounts_section.find_all('div', class_='product-card-wrapper')  # Adjust class name if necessary
def get_basics(soup):
    title = soup.find('h1').text.strip()
    description = soup.find('p').text.strip()
    monthly_fee = soup.find('h3').text.strip()
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Maintenance Fee: {monthly_fee}")
    return title, description, monthly_fee

def get_details(soup):
    details = soup.find('div', class_='nbd-credit-card-banner-content')
    if details:
        title, description, monthly_fee = get_basics(details)
        return title, description, monthly_fee
    else:
        print("MyMo Bank Account not found on the page.")
        return None, None, None
