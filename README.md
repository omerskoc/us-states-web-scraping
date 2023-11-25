# Web Scraping US States Data from Wikipedia

## Project Overview
This project demonstrates a Python script to extract data about the United States' states from Wikipedia, specifically from [this page](https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States). The script fetches information such as the name of each state, its population, and area.

## Technologies Used
- Python
- Libraries: requests, BeautifulSoup, pandas, re

## Features
- **Data Extraction:** The script navigates through a Wikipedia page, parsing the HTML content to extract relevant data.
- **Data Points:** For each state, the script retrieves the state's name, population size, and area.
- **Special Cases Handling:** The script is capable of adjusting the extraction logic for states where the capital is the same as the largest city, which affects the HTML structure.
- **Data Cleaning:** Extracted data is cleaned (e.g., removing commas in numbers) and converted into appropriate data types.
- **Data Representation:** The final output is a pandas DataFrame, showcasing the data in a structured format.

## How It Works
1. **Importing Libraries:** The script begins by importing necessary Python libraries.
2. **Fetching the Web Page:** Using the `requests` library, the script fetches the Wikipedia page.
3. **Parsing HTML:** The `BeautifulSoup` library is used to parse the HTML content.
4. **Inspecting Row Structure:** The script systematically examines each row in the HTML table to locate and extract the state name, population, and area.
5. **Handling Layout Shifts:** For states where the table layout differs (capital is the largest city), the script adjusts its extraction logic accordingly.
6. **Creating DataFrame:** Extracted data is then structured into a pandas DataFrame for easy viewing and analysis.
7. **Displaying Data:** The script finally displays the data for the first five states as an example.

## Sample Output
The output is a DataFrame with columns for state name, population, and area. Here's a sample for the first five states:

state	population	area
0	Alabama	5024279	52420
1	Alaska	733391	665384
2	Arizona	7151502	113990
3	Arkansas	3011524	53179
4	California	39538223	163695


## Conclusion
This project is a practical example of using web scraping techniques to gather valuable data from a public webpage. It demonstrates the power of Python and its libraries in simplifying the task of data extraction and manipulation.
