# Web Scraper Assignment
This is a web scraper assignment where you are required to extract specific information from an HTML file and generate a JSON string as output. The task involves extracting various details related to a hotel from the provided HTML file.

## Task Description
Write a data extractor that reads the content from the HTML file "task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html" and extracts the following information:

* Hotel name (marked in red)
* Address (marked in red)
* Classification / stars (marked in red)
* Review points (marked in pink)
* Number of reviews (marked in pink)
* Description (marked in blue)
* Room categories (marked in green)
* Alternative hotels (marked in yellow)
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
python web_scraper.py

```

* The code will read the HTML file, extract the required information, and generate a JSON string as output.
* The JSON string will be displayed in the terminal or command prompt.
## Unit Testing
Unit tests have been implemented to ensure the correctness of the code. To run the unit tests, follow these steps:

* Open the terminal or command prompt.
* Run the following command:
```
python -m unittest test_web_scraper.py
```
* The tests will be executed, and the test results will be displayed in the terminal or command prompt.
## Code Structure
The code for the web scraper is implemented in the "web_scraper.py" file. The unit tests are implemented in the "test_web_scraper.py" file. The HTML file "task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html" is required for the code to run successfully.

Thank you and happy scraping!

