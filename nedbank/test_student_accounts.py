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
            <div class="card-body m-0 p-0">
                <h5 class="card-title nb-card-heading">Security</h5>
                <p>Accept or reject transactions on your account with access to a 24/7 anti-fraud hotline.</p>
                <p>Block, freeze or replace your card on the Money app, Online Banking, or our 24/7 call centre.</p>
                <p>Set payment limits or activate and deactivate your cards as needed.</p>
                <p>Enjoy the added security of our chip-and-PIN enabled cards.</p>
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
        self.assertEqual(benefit_categories["Security"], [
            "Accept or reject transactions on your account with access to a 24/7 anti-fraud hotline.",
            "Block, freeze or replace your card on the Money app, Online Banking, or our 24/7 call centre.",
            "Set payment limits or activate and deactivate your cards as needed.",
            "Enjoy the added security of our chip-and-PIN enabled cards."
        ])

        self.assertEqual(len(benefit_categories["Rewards and discounts"]), 3)
        self.assertEqual(len(benefit_categories["Convenience and control"]), 3)
        self.assertEqual(len(benefit_categories["Rates and fees"]), 3)
        self.assertEqual(len(benefit_categories["Security"]), 4)


    def test_get_account_perks(self):
        mock_html = """
            <div class="nbd-way-to-pay-info">
                <h4>Movie discounts</h4>
                <p>50% off at Nu Metro</p> 
            </div>
            <div class="nbd-way-to-pay-info">
                <h4>Free card purchases</h4>
                <p>Swipe your card for free at any retail store at no extra charge</p> 
            </div>
            <div class="nbd-way-to-pay-info">
                <h4>Free statements</h4>
                <p>Free statements on the Money app (up to 3 months)</p>
            </div>
            <div class="nbd-way-to-pay-info">
                <h4>Free savings pocket</h4>
                <p>Save and earn interest with a MyPocket savings account</p>
            </div>
        """
        
        soup = BeautifulSoup(mock_html, 'html.parser')
        perk_categories = get_account_perks(soup)

        self.assertEqual(perk_categories["Movie discounts"], [
            "50% off at Nu Metro"
        ])
        self.assertEqual(perk_categories["Free card purchases"], [
            "Swipe your card for free at any retail store at no extra charge"
        ])
        self.assertEqual(perk_categories["Free statements"], [
            "Free statements on the Money app (up to 3 months)"
        ])
        self.assertEqual(perk_categories["Free savings pocket"], [
            "Save and earn interest with a MyPocket savings account"
        ])

        self.assertEqual(len(perk_categories), 4)


if __name__ == "__main__":
    unittest.main()