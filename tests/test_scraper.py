from scraping.scraper import Scraper
from unittest.case import TestCase
from bs4 import BeautifulSoup
from unittest.mock import patch

class TestScraper(TestCase):

    def test_load_html(self):
        # Create an instance of the Scraper class
        scraper = Scraper()

        # Mock the open() function to return a file-like object
        with patch('builtins.open', create=True) as mock_open:
            # Configure the read() method of the file-like object
            mock_open.return_value.__enter__.return_value.read.return_value = '<html><body><h1>Hello, World!</h1></body></html>'

            # Call the load_html() method
            url = "task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html"
            result = scraper.load_html(url)

            # Assert that BeautifulSoup object is returned
            self.assertIsInstance(result, BeautifulSoup)

            # Assert the expected HTML content is present in the result
            self.assertEqual(str(result), '<html><body><h1>Hello, World!</h1></body></html>')            

    def test_extract_data(self):
        # Create an instance of the Scraper class
        scraper = Scraper()

        # Create a sample BeautifulSoup object for testing
        html_content = '''
        <html>
            <body>
                <span id="hp_hotel_name">Hotel Name</span>
                <span id="hp_address_subtitle">Address</span>
                <span class="nowrap hp__hotel_ratings">
                    <i class="b-sprite stars ratings_stars_5 star_track"></i>
                </span>
                <div class="hotel_description_wrapper_exp">
                    <p>Description line 1</p>
                    <p>Description line 2</p>
                </div>
                <table id="maxotel_rooms">
                    <tr>
                        <td class="ftd">Room Category 1</td>
                        <td class="ftd">Room Category 2</td>
                    </tr>
                </table>
                <div id="js--hp-gallery-scorecard">
                    <span>Review Points</span>
                    <span>Number of Reviews</span>
                </div>
                <div id="LastViewedHotels">
                    <ul>
                        <li><a href="#">Alternative Hotel 1</a><a></a></li>
                        <li><a href="#">Alternative Hotel 2</a><a></a></li>
                    </ul>
                </div>
            </body>
        </html>
        '''
        soup = BeautifulSoup(html_content, 'html.parser')

        # Call the extract_data() method
        result = scraper.extract_data(soup)

        # Assert that the result is a JSON string
        self.assertIsInstance(result, str)
        
if __name__ == '__main__':
    unittest.main()
