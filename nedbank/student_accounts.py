import requests
from bs4 import BeautifulSoup

url = 'https://personal.nedbank.co.za/bank/bank-accounts/youth-banking/migoals-youth.html'
html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')


def get_basics():
    migoal = soup.find('div', class_='nbd-credit-card-banner-content')
    title = migoal.find('h1').text.strip()
    description = migoal.find('p').text.strip()
    monthly_fee = migoal.find('h3').text.strip()
    print_basics(title, description, monthly_fee)
    return title, description, monthly_fee


def get_account_benefits():
    benefits = soup.find_all('div', class_='card-body m-0 p-0')
    categories = {
        'Rates and fees': [],
        'Rewards and discounts': [],
        'Convenience and control': [],
        'Security': []
    }

    for benefit in benefits:
        title = benefit.find('h5', class_='card-title nb-card-heading').text.strip()
        items = benefit.find_all('p')
        category_info = [item.text.strip() for item in items if item.text.strip()]
        
        if title in categories:
            categories[title] = category_info

    print_rewards(categories)


def print_basics(title, description, monthly_fee):
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Maintenance Fee: {monthly_fee}")


def print_rewards(categories):
    for category, info in categories.items():
        print(f"\n{category}:")
        for item in info:
            print(f"- {item}")


if __name__ == '__main__':
    get_basics()
    get_account_benefits()
   
