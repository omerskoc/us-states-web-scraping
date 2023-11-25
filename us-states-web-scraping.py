#!/usr/bin/env python
# coding: utf-8

# # Web Scraping US States Data from Wikipedia

# The following example extracts data about US states from Wikipedia:
# https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States

# In[3]:


# Importing Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


# In[4]:


# Fetching the Web Page
url = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


# ### Inspecting Row Structure
# By examining each row in the HTML table, the necessary data points are located.
# 
# ### State Name
# Found within the first `<th>` tag of a row, specifically inside an `<a>` (anchor) element.
# 
# ### Population Size
# Typically located in the fifth `<td>` (table data) element of a row.
# 
# ### Area Size
# Usually in the sixth `<td>` element of a row.
# 
# ### Special Case for Capital and Largest City
# ![Special Case](https://i.ibb.co/fkXPsnD/Screenshot-2023-11-24-at-6-35-59-PM.png)
# In rows where the state's capital is also its largest city, the layout shifts:
# - The population size moves to the fourth `<td>` element.
# - The area size is found in the fifth `<td>` element.
# 
# ### Identifying Special Cases
# These cases are identified by checking if the second `<td>` element has an attribute `colspan="2"`. This attribute alters the column span, indicating a different table layout for these specific states.
# 

# In[5]:


# Function to Extract Data
def get_states_data():
    """
    Extracts data about US states from the Wikipedia page.
    """
    states, populations, areas = [], [], []
    
    table = soup.find_all('table')[1]
    rows = table.find_all('tr')[2:]
    
    for row in rows:
        # Extracting state name
        state = row.th.a.text
        states.append(state)
        
        cells = row.find_all('td')
        
        # Adjusting for the layout differences in the table
        if 'colspan' in cells[1].attrs:
            population = cells[3].text
            area = cells[4].text
        else:
            population = cells[4].text
            area = cells[5].text
            
        # Cleaning and converting data
        population = int(population.replace(',', ''))
        populations.append(population)
        
        area = int(area.replace(',', ''))
        areas.append(area)
        
    return states, populations, areas


# In[7]:


# Creating DataFrame and Displaying Data
states, populations, areas = get_states_data()
states_df = pd.DataFrame({'state': states, 'population': populations, 'area': areas})
states_df.head()  # Display data for the first five states


# ### Thanks!
