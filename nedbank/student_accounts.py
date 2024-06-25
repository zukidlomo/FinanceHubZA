import requests
from bs4 import BeautifulSoup

url = 'https://personal.nedbank.co.za/bank/bank-accounts/youth-banking/migoals-youth.html'
html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')


with open("nedbankMigoals.html", "w", encoding='utf-8') as file:
    file.write(soup.prettify())


def get_basics():
    migoal = soup.find('div', class_='nbd-credit-card-banner-content')
    title = migoal.find('h1').text.strip()
    description = migoal.find('p').text.strip()
    monthly_fee = migoal.find('h3').text.strip()
    print_basics(title, description, monthly_fee)
    return title, description, monthly_fee

def print_basics(title, description, monthly_fee):
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Maintenance Fee: {monthly_fee}")

if __name__ == '__main__':
    get_basics()
