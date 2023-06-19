# Web Scraper Assignment
This is a web scraper assignment where you are required to extract specific information from an HTML file and generate a JSON string as output. The task involves extracting various details related to a hotel from the provided HTML file.

## Task Description
Scraper that reads the content from the HTML file "task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html" and extracts the following information:

* Hotel name
* Address
* Classification / stars
* Review points
* Number of reviews
* Description
* Room categories
* Alternative hotels
## Prerequisites
Before running the code, ensure that you have the following:

* Python installed on your system
* Required libraries installed (e.g., BeautifulSoup, json, etc.)
## Run the Code
* Download or clone the repository to your local machine.
* Navigate to the project directory.
* Place the "task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html" file in the project directory.
* Open the terminal or command prompt.
* Run the following command to execute the code:
```
python3 start_scraping.py 

```

* The code will read the HTML file, extract the required information, and generate a JSON string as output.
* The JSON string will be displayed in the terminal or command prompt.
## Unit Testing
Unit tests have been implemented to ensure the correctness of the code. To run the unit tests, follow these steps:

* Open the terminal or command prompt.
* Run the following command:
```
python3 -m unittest tests.test_scraper

```
* The tests will be executed, and the test results will be displayed in the terminal or command prompt.
## Code Structure
The code for the web scraper is implemented in the "web_scraper.py" file. The unit tests are implemented in the "test_web_scraper.py" file. The HTML file "task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html" is required for the code to run successfully.

Thank you and happy scraping!

