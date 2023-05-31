
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

from django.http import HttpResponseServerError
from .models import ScrapingCounter
from django.core.exceptions import ObjectDoesNotExist

import time
import json
import time
import datetime

class AbstractScrapingClass:
    def process(self):
        # Start timer for the scraping process
        start_timer = time.time()
        print(start_timer)

        # Create a new Selenium WebDriver instance
        driver = webdriver.Chrome()
        # Load the web page
        driver.get('https://bandcamp.com/')
        # Find the <a> tag based on its inner HTML content
        target_inner_html = 'log in'  # Replace with the inner HTML you want to search for
        target_a = driver.find_element('xpath', f'//a[contains(text(), "{target_inner_html}")]')

        # Click in login option
        target_a.click()

        # 
        # User name input
        data_element_input_user = driver.find_element(By.ID, 'username-field')
        data_element_input_user.clear()  # Clear any existing value
        data_element_input_user.send_keys('abacotestscraping')

        # Password input
        data_element_input_password = driver.find_element(By.ID, 'password-field')
        data_element_input_password.clear()  # Clear any existing value
        data_element_input_password.send_keys('TEst1234$')
        
        target_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        target_button.click()

        try:        
            captcha_resolved = False

            while not captcha_resolved:
                # Find elements with the specific innerHTML string
                elements = driver.find_elements(By.XPATH, f".//*[contains(text(), 'abacotestscraping')]")
                if elements:
                    print('resuelto....')
                    captcha_resolved = True
                    return True
                else:
                    # CAPTCHA is not resolved, wait for a certain duration before checking again.
                    time.sleep(5)  # Adjust the delay time as per your requirements.
                    print('resolviendo....')
            
            pass

        except Exception as e:
            return HttpResponseServerError("An error occurred: {}".format(str(e)))
        finally:   

            data_scraped_aux = []   
            data_scraped = {}

            data_followings = []
            data_followings_json = {}

            elements_a = driver.find_elements(By.CLASS_NAME, "item-link")  

            for element in elements_a:            
                data_tags = []

                tags_finder = element.get_attribute("href")
                if tags_finder:                          
        
                    data_scraped['Song_Artis'] = element.text
                    
                    # Find Tags
                    driver02 = webdriver.Chrome()
                    driver02.get(tags_finder)
                    tags_aux = driver02.find_elements(By.CLASS_NAME, "tag")
    
                    for tag in tags_aux: 
                        if tag:                   
                            data_tags.append(tag.text)
                    data_scraped['Tag'] = data_tags

                    driver02.quit()

                    json_array = json.dumps(data_scraped, ensure_ascii=False)
                    data_scraped_aux.append(json_array)

            #element_follow = driver.find_elements(By.CLASS_NAME, "genre-name")
            element_li_click = driver.find_element(By.XPATH, f"//li[@data-grid-id='following-grid']")
            element_li_click.click()

            time.sleep(5)

            element_follow = driver.find_elements(By.CLASS_NAME, "genre-name")

            for element in element_follow:
                data_followings.append(element.text)
            data_followings_json['Genders'] = data_followings

            #print(data_followings_json)
            #driver.quit()

            output_list = [json.loads(json_string) for json_string in data_scraped_aux]

            #print(output_list)
            #print(data_followings_json)

            reliability = reliability_data(output_list, data_followings_json)

            # End timer por scraping
            end_timer = time.time()
            # print(start_timer)
            elapsed_time = end_timer - start_timer
            elapsed_time_formatted = str(datetime.timedelta(seconds=elapsed_time))
            # print(elapsed_time_formatted)

            # DB register
            new_reg = ScrapingCounter()
            try:                
                reg_cout = ScrapingCounter.objects.latest('scraping_date_at')
                
                reg_count_aux = reg_cout.count + 1
                new_reg.count = reg_count_aux
                new_reg.scraping_time = elapsed_time_formatted

                new_reg.save()

            except ObjectDoesNotExist:
                reg_count_aux = 1
                new_reg.count = reg_count_aux
                new_reg.scraping_time = elapsed_time_formatted
                new_reg.save()
                #print("No matching object found in the database.")


            return [output_list, data_followings_json, reliability, elapsed_time_formatted, reg_count_aux]
    
# Function reliability
def reliability_data(output_list, data_followings_json):
    reliability_count = 0

    for item in output_list:
        tag_list = item.get('Tag', [])
        #print(tag_list)  
        if any(gender in tag_list for gender in data_followings_json.get('Genders', [])):
            #print("Gender key found in the tag list. ")
            reliability_count += 1

    if(len(output_list) == 0):
        reliability_count_return = 0
    else:
        reliability_count_return = reliability_count / len(output_list)

    return reliability_count_return        