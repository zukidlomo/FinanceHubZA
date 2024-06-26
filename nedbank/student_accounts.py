import requests
from bs4 import BeautifulSoup

url = 'https://personal.nedbank.co.za/bank/bank-accounts/youth-banking/migoals-youth.html'
html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')


def get_account_synopsis(soup):
    """
    Retrieves the basic information about the Migoals Youth account from the webpage.
    
    Returns:
    - title (str): The title of the account.
    - description (str): The description of the account.
    - monthly_fee (str): The monthly maintenance fee of the account.
    """
    migoal = soup.find('div', class_='nbd-credit-card-banner-content')
    title = migoal.find('h1').text.strip()
    description = migoal.find('p').text.strip()
    monthly_fee = migoal.find('h3').text.strip()
    print_basics(title, description, monthly_fee)
    
    return title, description, monthly_fee


def get_account_benefits():
    """
    Retrieves the account benefits of the Migoals Youth account from the webpage.
    
    Returns:
    - benefit_categories (dict): A dictionary containing the different categories of benefits and their corresponding information.
    """
    benefits = soup.find_all('div', class_='card-body m-0 p-0')
    benefit_categories = {
        'Rates and fees': [],
        'Rewards and discounts': [],
        'Convenience and control': [],
        'Security': []
    }

    for benefit in benefits:
        title = benefit.find('h5', class_='card-title nb-card-heading').text.strip()
        items = benefit.find_all('p')
        category_info = [item.text.strip() for item in items if item.text.strip()]
        
        if title in benefit_categories:
            benefit_categories[title] = category_info

    print_rewards(benefit_categories)


def get_account_perks(soup):
    
    perks = soup.find_all('div', class_='nbd-way-to-pay-info')
    perks_categories = {
        'Movie discounts': [],
        'Free card purchases': [],
        'Free statements': [],
        'Free savings pocket': []
    }

    for perk in perks:
        title = perk.find('h4').text.strip()
        items = perk.find_all('p')
        category_info = [item.text.strip() for item in items if item.text.strip()]
        
        if title in perks_categories:
            perks_categories[title] = category_info

    print_perks(perks_categories)
    return perks_categories

def print_basics(title, description, monthly_fee):
    """
    Prints the basic information of the account.
    
    Parameters:
    - title (str): The title of the account.
    - description (str): The description of the account.
    - monthly_fee (str): The monthly maintenance fee of the account.
    """
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Maintenance Fee: {monthly_fee}")


def print_rewards(benefit_categories):
    """
    Prints the account benefits categorized by different benefit_categories.
    
    Parameters:
    - benefit_categories (dict): A dictionary containing the different categories of benefits and their corresponding information.
    """
    for category, info in benefit_categories.items():
        print(f"\n{category}:")
        for item in info:
            print(f"- {item}")

def print_perks(perks_categories):
     for category, info in perks_categories.items():
        print(f"\n{category}:")
        for item in info:
            print(f"- {item}")
    # print(perks)


if __name__ == '__main__':
    get_account_synopsis(soup)
    get_account_benefits()
    get_account_perks(soup)
   
