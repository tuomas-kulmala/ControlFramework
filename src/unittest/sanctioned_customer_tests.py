import unittest
from unittest.mock import MagicMock

from  control.sanctioned_customer import SanctionedCustomer

class TestValidCustomerClass(unittest.TestCase):

    mock_trade = {"customer_id": "9999"}
    mockSanctionList = [{"id":"9999"}]

    def test_customer_is_sanctioned(self):
        control = SanctionedCustomer()
        control.find_in_sanctions = MagicMock(return_value=True)
        control.is_covered_by_sanctions(self.mock_trade)

    def test_customer_is_not_sanctioned(self):
        control = SanctionedCustomer()
        control.find_in_sanctions = MagicMock(return_value=True)
        control.is_covered_by_sanctions(self.mock_trade)

    def test_find_in_list_is_correct(self):
        control = SanctionedCustomer()
        control.russian_sanctions = self.mockSanctionList
        result = control.find_in_sanctions(self.mock_trade["customer_id"])
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()