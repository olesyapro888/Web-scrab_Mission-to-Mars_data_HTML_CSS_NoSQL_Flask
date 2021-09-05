#!/usr/bin/env python
# coding: utf-8

# In[191]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[192]:


# Set up Splinter (Set the executable path and initialize Splinter)
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[193]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[194]:


# Parse the HTML with BeautifulSoup
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text') # (.) is used for selecting classes


# In[195]:


# Assign the title and summary text to variables
slide_elem.find('div', class_='content_title')


# In[196]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[197]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[198]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[199]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[200]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[201]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[202]:


# Use the base URL to create an absolute URL
# using an f-string for this print statement because it's a cleaner way to create print statements; 
# they're also evaluated at run-tim
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[203]:


# Scrape the entire table from galaxy...site and creat a new DataFrame from the HTML table
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth'] # Assign columns to the new DataFrame for additional clarity
df.set_index('description', inplace=True)
df


# In[204]:


df.to_html()


# In[205]:


browser.quit()


# ## Challenge 10. 

# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[224]:


# Set up Splinter (Set the executable path and initialize Splinter)
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[225]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[226]:


html = browser.html
img_soup = soup(html, 'html.parser')

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

# Find hemisphere with image link and title
# links = img_soup.find_all('div', class_='description')
links = browser.find_by_css('a.product-item img')

# Loop through each link of hemispheres on page
for i in range(len(links)):
    # Create dictionary to hold title and image url
    hemisphere = {}
    
    # Old.Solution.Find the elements and scrape data
    # hemisphere_url = image.find('a', class_='itemLink product-item')
    # Get 'href' page
    # hemisphere_page = hemisphere_url.get('href')
    # Crate a link of the page
    # hemisphere_link = url + hemisphere_page
    # Visite it and parse it to Retrieve the data
    # browser.visit(hemisphere_link)    
    # html = browser.html
    # hemispheres = soup(html, 'html.parser')

    browser.find_by_css('a.product-item img')[i].click()
    
    # Old.Solution. Find the Sample image and get the href
    # hemisphere_link = hemispheres.find('a', text='Sample').get('href')
    # hemisphere['img_url'] = hemisphere_link
    
    # Next, we find the Sample image anchor tag and extract the href
    sample_elem = browser.links.find_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
        
    # Retrieve title
    hemisphere['title'] = browser.find_by_css('h2.title').text

    # Append dictionaries to list
    hemisphere_image_urls.append(hemisphere)
    
    # Finally, we navigate backwards
    browser.back()


# In[227]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[228]:


# 5. Quit the browser
browser.quit()


# In[229]:


# pip install ipython


# In[230]:


#  pip install nbconvert


# In[237]:


get_ipython().system('ipython nbconvert --to script Mission_to_Mars_Challenge.ipynb')


# In[ ]:




