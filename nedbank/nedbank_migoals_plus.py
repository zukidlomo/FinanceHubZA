import requests
from bs4 import BeautifulSoup

url = 'https://personal.nedbank.co.za/bank/bank-accounts/youth-banking/migoals-plus-youth.html'
html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')

with open("nedbankMigoalsPlus.html", "w", encoding='utf-8') as file:
    file.write(soup.prettify())

def get_account_synopsi(soup):
    migoal = soup.find('div', class_='headerbannerdesktop secondary-bg')
    title = migoal.find('h1').text.strip()
    description = migoal.find('p').text.strip()
    monthly_fee = migoal.find('h3').text.strip()
    print_basics(title, description, monthly_fee)

    return title, description, monthly_fee
    

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

def get_account_benefits(soup):
    pass


def get_account_perks(soup):
    pass



if __name__ == '__main__':
    get_account_synopsi(soup)
    get_account_benefits(soup)
    get_account_perks(soup)
   
