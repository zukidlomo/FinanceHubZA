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
         mock_html = """
            <div class="nbd-way-to-pay-info">
                <h4>Cash back on groceries</h4>
                <p> Up to 2% cash back on your grocery spend</p>
               
            </div>
            <div class="nbd-way-to-pay-info">
                <h4>Prepaid vouchers</h4>
                <p>Get prepaid airtime, data, electricity or water easily on the Money app or Online Banking.</p>
                
            </div>
            <div class="nbd-way-to-pay-info">
                <h4>Cash back on fuel</h4>
                <p>25c cash back for every litre of fuel at BP</p>
                
            </div>
            <div class="nbd-way-to-pay-info">
                <h4>Free savings pocket</h4>
                <p>Save and earn interest with MyPocket savings account</p>
                
            </div>
        """
        


    def get_account_perks(soup):
        pass



if __name__ == "__main__":
    unittest.main()