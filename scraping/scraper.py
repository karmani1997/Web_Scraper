#Import Packages

from bs4 import BeautifulSoup
import json


class Scraper:
    """
    This class extract the field from the HTML string
    """
    
    def __init__(self):

        self.json_string = None

    def load_html(self, url):

        # Open the file in read mode
        with open(url, 'r') as file:
            # Read the contents of the file
            html_content = file.read()

        # Create BeautifulSoup object from HTML string
        return BeautifulSoup(html_content, 'html.parser')

    def extract_data(self, soup):
        """
        Parse the HTML Content
        """

        # Find the hotel name from span tag
        hotel_name = soup.find('span', attrs={'id': 'hp_hotel_name'}).text.strip()


        # Find the address from the span tag with id attribute "hp_address_subtitle"
        address = soup.find('span', attrs={'id': 'hp_address_subtitle'})
        # Get the address within the <span> tag
        address = address.text.strip()

        # Find the hotel classification
        span_tag = soup.find('span', attrs={'class': 'nowrap hp__hotel_ratings'})
        # Find the <i> tag with class attribute "b-sprite stars ratings_stars_5 star_track"
        i_tag = span_tag.find('i')
        # Extract the class attribute value
        rating = i_tag['class'][2]


        # Find the <div> tag with id
        div_tag = soup.find('div', attrs={'class': 'hotel_description_wrapper_exp'})
        # Find all <p> tags within the <div> tag
        p_tags = div_tag.find_all('p')
        # Concatenate the text from all <p> tags
        description = '\n'.join([p_tag.text.strip() for p_tag in p_tags])


        # Find the <table> tag with id
        table_tag = soup.find('table', attrs={'id': 'maxotel_rooms'})
        # Find all <td> tags within the <div> tag
        td_tags = table_tag.find_all('td', attrs = {'class':"ftd"})
        # Concatenate the text from all <p> tags
        room_categories = []
        room_categories.append([td_tag.text.strip() for td_tag in td_tags])

        # Find review_point and total_number_of_reviews from div
        div_tag = soup.find('div', attrs={'id': 'js--hp-gallery-scorecard'})
        span_tags = div_tag.find_all('span')
        review_points = span_tags[1].text
        number_of_reviews = span_tags[-1].text

        #Find the alternative hotel
        div_tag = soup.find('div', attrs={'id': 'LastViewedHotels'})
        li_tags = div_tag.find_all('li')
        alternative_hotels = []
        alternative_hotels = []
        for li_tag in li_tags:
            alternative_hotels.append(li_tag.find_all('a')[1].text.strip())

        # Create a dictionary with the variable names as keys and their values
        data = {
        "hotel_name": hotel_name,
        "address": address,
        "rating": rating,
        "description": description,
        "room_categories": room_categories[0],
        "review_points": review_points,
        "number_of_reviews": number_of_reviews,
        "alternative_hotels": alternative_hotels
        }

        # Convert the dictionary to a JSON string
        self.json_string = json.dumps(data)
        
        return self.json_string
 