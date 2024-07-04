import unittest
from student_accounts import *
from bs4 import BeautifulSoup


class TestMigoalsAccountFunctions(unittest.TestCase):
    def test_get_basics(self):
        mock_html = """
            <div class="nbd-credit-card-banner-content">
                <h1>MiGoals</h1>
                <p>For anytime, anywhere banking on your terms, get MiGoals.</p>
                <h3>R5</h3>
            </div>
        """

        soup = BeautifulSoup(mock_html, 'html.parser')

        title, description, monthly_fee = get_account_synopsis(soup)
        self.assertEqual(title, "MiGoals")
        self.assertEqual(description, "For anytime, anywhere banking on your terms, get MiGoals.")
        self.assertEqual(monthly_fee, "R5")



    def test_get_account_benefits(self):
        mock_html = """
            <div class="card-body m-0 p-0">
                <h5 class="card-title nb-card-heading">Rates and fees</h5>
                <p>Pay R5 monthly maintenance fees.</p>
                <p>Get free in-app transaction notifications.</p>
                <p>Add Greenbacks membership for only R30 a month.</p>
            </div>
            <div class="card-body m-0 p-0">
                <h5 class="card-title nb-card-heading">Rewards and discounts</h5>
                <p>Get 50% off Nu Metro movie tickets.</p>
                <p>Withdraw your Greenbacks as cash at any Nedbank ATM.</p>
                <p>Enjoy Greenbacks Exclusive discounts on Avo SuperShop app.</p>
            </div>
            <div class="card-body m-0 p-0">
                <h5 class="card-title nb-card-heading">Convenience and control</h5>
                <p>Open your account easily online.</p>
                <p>Switch your salary and debit orders easily on the Money app or Online Banking.</p>
                <p>Enjoy instant access to your account on the Money app, Cellphone Banking or Online Banking.</p>
            </div>
        """

        soup = BeautifulSoup(mock_html, 'html.parser')
        benefit_categories = get_account_benefits(soup)

        self.assertEqual(benefit_categories["Rates and fees"], [
            "Pay R5 monthly maintenance fees.",
            "Get free in-app transaction notifications.",
            "Add Greenbacks membership for only R30 a month."
        ])

        self.assertEqual(benefit_categories["Rewards and discounts"], [
            "Get 50% off Nu Metro movie tickets.",
            "Withdraw your Greenbacks as cash at any Nedbank ATM.",
            "Enjoy Greenbacks Exclusive discounts on Avo SuperShop app."
        ])
        self.assertEqual(benefit_categories["Convenience and control"], [
            "Open your account easily online.",
            "Switch your salary and debit orders easily on the Money app or Online Banking.",
            "Enjoy instant access to your account on the Money app, Cellphone Banking or Online Banking."
        ])


        self.assertEqual(len(benefit_categories['Rewards and discounts']), 3)
        self.assertEqual(len(benefit_categories['Convenience and control']), 3)
        self.assertEqual(len(benefit_categories['Rates and fees']), 3)
        self.assertEqual(len(benefit_categories['Security']), 0)

    def test_get_account_perks(self):
        pass



if __name__ == "__main__":
    unittest.main()