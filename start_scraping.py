from scraping.scraper import Scraper


#from .loader import Loader


def run_scraper(url_path):

    print('***********Start Scraping***********')

    scraper = Scraper()
    soup_obj = scraper.load_html(url_path)
    return scraper.extract_data(soup_obj)


if __name__ == "__main__":
    url_path = "task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html"
    json_string =  run_scraper(url_path)
    print (json_string)
