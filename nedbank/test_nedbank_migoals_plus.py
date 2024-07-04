import unittest
from nedbank_migoals_plus import *
from bs4 import BeautifulSoup


class TestMigoalsPlusAccountFunctions(unittest.TestCase):
    def test_get_account_basics(self):
        url = 'https://personal.nedbank.co.za/bank/bank-accounts/youth-banking/migoals-plus-youth.html'
        html = requests.get(url)

        soup = BeautifulSoup(html.content, 'html.parser')
        
        title, description, monthly_fee = get_account_synopsi(soup)
        self.assertEqual(title, "MiGoals Plus")
        self.assertEqual(description, "Enjoy the full range of benefits with MiGoals Plus: the bank account that means business, with great benefits for youth.")
        self.assertEqual(monthly_fee, "R99")


    def get_account_benefits(soup):
        pass


    def get_account_perks(soup):
        pass



if __name__ == "__main__":
    unittest.main()