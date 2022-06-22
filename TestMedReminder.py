import random
import unittest
from MedReminder import days_of_week
import Medications
from Clients.TimothyMedList import MedList as test_meds


class TestEndcodeImage(unittest.TestCase):

    def test_get_meds_today(self):
        print("Med List Test: Get Meds Today \t\t\t| Started")
        today = random.choice(days_of_week)
        for hour in range(24):
            hour_24 = "0" + str(hour) + "00" if hour < 10 else str(hour) + "00"

        # Test Case
        expected_test_data = test_meds[today]
        our_method_results = Medications.get_meds(test_meds, today, hour_24)
        error_message = f'Error Result are not what we wantExpected: {expected_test_data} | Actual: {our_method_results}'
        self.assertDictEqual(our_method_results,
                             expected_test_data, error_message)


if __name__ == '__main__':
    unittest.main()
