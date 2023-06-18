from scraping.scraper import Scraper
from unittest.case import TestCase

class TestExtractor(TestCase):
    
    
    def test_extractor_valid_file(self):
        url = "task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html"
        scraper = Scraper()
        html_content = scraper.load_html(url)
        self.assertEqual(type(html_content), type([{1:2}]))
        print ("test_extractor_valid_file testcase run successfully")

    def test_extractor_invalid_file(self):

        url = "task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html"
        scraper = Scraper()
        html_content = scraper.load_html(url)
        res = scraper.extract_data(html_content)
        self.assertEqual(res, [{}])
        print ("test_extractor_invalid_file testcase run successfully")
        
if __name__ == '__main__':
    unittest.main()   python3 -m unittest tests.test_extractor
