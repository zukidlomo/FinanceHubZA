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
   



if __name__ == "__main__":
    unittest.main()