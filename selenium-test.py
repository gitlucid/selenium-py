# import web driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('../chromedriver.exe')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.google.com')

# locate search form by_name
search_query = driver.find_element_by_name('q')

# send_keys() to simulate the search text key strokes
search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "London"')

# .send_keys() to simulate the return key 
search_query.send_keys(Keys.RETURN)

# locate URL by_class_name
linkedin_urls = driver.find_elements_by_class_name('iUh30')

# variable linkedin_url is equal to the list comprehension 
linkedin_urls = [url.text for url in linkedin_urls]

# to print all elements within our list 
linkedin_urls





#######################

# For loop to iterate over each URL in the list
for linkedin_url in linkedin_urls:

   # get the profile URL 
   driver.get(linkedin_url)

   # add a 5 second pause loading each URL
   sleep(5)

   # assigning the source code for the webpage to variable sel
   sel = Selector(text=driver.page_source) 
    
    
    
# xpath to extract the text from the class containing the name
name = sel.xpath('//*[starts-with(@class, 
"pv-top-card-section__name")]/text()').extract_first()

if name:
    name = name.strip()


# xpath to extract the text from the class containing the job title
job_title = sel.xpath('//*[starts-with(@class, 
"pv-top-card-section__headline")]/text()').extract_first()

if job_title:
    job_title = job_title.strip()


# xpath to extract the text from the class containing the company
company = sel.xpath('//*[starts-with(@class, 
"pv-top-card-v2-section__entity-name pv-top-card-v2-section__company-name")]/text()').extract_first()

if company:
    company = company.strip()


# xpath to extract the text from the class containing the college
college = sel.xpath('//*[starts-with(@class, 
"pv-top-card-v2-section__entity-name pv-top-card-v2-section__school-name")]/text()').extract_first()

if college:
    college = college.strip()


# xpath to extract the text from the class containing the location
location = sel.xpath('//*[starts-with(@class, 
"pv-top-card-section__location")]/text()').extract_first()

if location:
    location = location.strip()


linkedin_url = driver.current_url

# terminates the application
driver.quit()    


