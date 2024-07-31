import task_date_check
import unittest


class TestDateCheck(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertTrue(task_date_check.is_leap_year(400))
        self.assertTrue(task_date_check.is_leap_year(2000))
        self.assertFalse(task_date_check.is_leap_year(2002))
        self.assertFalse(task_date_check.is_leap_year(2100))
        self.assertTrue(task_date_check.is_leap_year(2004))

    def test_get_number_of_days_in_month(self):
        self.assertEqual(task_date_check.get_number_of_days_in_month(1, True), 31)
        self.assertEqual(task_date_check.get_number_of_days_in_month(2, True), 29)
        self.assertEqual(task_date_check.get_number_of_days_in_month(2, False), 28)
        self.assertEqual(task_date_check.get_number_of_days_in_month(3, False), 31)
        self.assertEqual(task_date_check.get_number_of_days_in_month(4, False), 30)

    def test_is_month_correct(self):
        self.assertTrue(task_date_check.is_month_correct(3))
        self.assertTrue(task_date_check.is_month_correct(11))
        self.assertFalse(task_date_check.is_month_correct(13))
        self.assertFalse(task_date_check.is_month_correct(23))

    def test_is_day_correct(self):
        self.assertTrue(task_date_check.is_day_correct(21, 2, 1990))
        self.assertTrue(task_date_check.is_day_correct(31, 3, 2231))
        self.assertFalse(task_date_check.is_day_correct(29, 2, 1990))
        self.assertFalse(task_date_check.is_day_correct(31, 4, 1990))
        





if __name__ == '__main__':
    unittest.main()
