import requests
import json
from datetime import datetime
from datetime import date
from dateutil import parser
import sys 
import os


from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import refinedscraper
from refinedscraper import finalSpider
from scrapy.utils.project import get_project_settings

import RunModel
from RunModel import getModelScores as gms
#import TermiteModels.RunModel.getModelScores as gms

import json

origin = sys.argv[1] 
print(origin)

process = CrawlerProcess(get_project_settings())
# # spiderguy = finalSpider() 
process.crawl(finalSpider, origin_url=origin)
process.start()


with open("scraped_data.json", 'r') as data:
    print(data)
    data = json.load(data)
    
os.remove("scraped_data.json")








# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------

# process = CrawlerProcess(get_project_settings())
# process.crawl(finalSpider, origin_url='https://www.amazon.com')
# #process.crawl(finalSpider, origin_url=sys.argv[1])
# # output = process.start()
# process.start()

# # print(output)
# # print(export_item)
      

####### scraper stuff goes here #######


# ### this gets redefined to be the scraper output 

body = data[0]['text']

user_id = sys.argv[2]



# #user_id = "Jen Jen Jen"

date_updated = data[0]['updates']
print(date_updated)


if "No entry located" in date_updated:
    date_updated = "7/4/1997"

print(date_updated)


# # ## import the model pyfile and the main function for it (getModelScores(body))


def model_run(text):
    scores = gms(text)
    return scores
    
    




###### actually running everything after scraping ####




hostname = 'http://ec2-18-224-6-72.us-east-2.compute.amazonaws.com'
website_info_request = hostname + ':3005/data/website?website_address=' + origin

request_date = parser.parse(date_updated).date()



pre_website_info = requests.get(website_info_request).text
print(pre_website_info)

if pre_website_info != "[]":    
    
    website_info = json.loads(pre_website_info)[0]

    db_id = website_info['id']


    db_date = parser.parse(website_info['date_terms_update'][:10]).date()



    if request_date == db_date:

        ## if they're equal we want to push this agreement into the user's list of agreements (if it isn't there already)

        # hey pull user's agreements
        # is db_id in this user's agreements 
        # if not it goes there now

        user_check_request = hostname + ":3005/user/verifySingleAgreement?user_id=" + user_id + "&website_id=" + origin

        
        
        user_check_return = requests.get(user_check_request).text
        
        if user_check_return == '' or len(json.loads(user_check_return)) == 0:
            requests.post(hostname + ":3005/user/agreements", {'website_address':origin,'user_id':user_id})
            
        ### also set it to 
        
        website_date_eval_post = hostname + ':3005/website/today_date?website_address=' + origin
        
        requests.post(website_date_eval_post)
        
        
        

    else:

        output = model_run(body) 


        ##at the end of everything website is added to metadata table...

        website_add_request = hostname + ":3005/data/website"
        added_website_id = json.loads(requests.post(website_add_request, {'website_url':origin, 'date_last_eval':datetime.now().date(), 'date_terms_update':str(request_date)}).text)[0]['id']

        output['website_id'] = added_website_id

        ###...the new scores get pushed to raw_scores... 
        scores_add_request = hostname + ":3005/data/model"
        requests.post(scores_add_request, output)

        ##...new agreement also gets logged into user agreements table

        adding_novel_site_to_user = requests.post(hostname + ":3005/user/agreements_by_id", {'user_id':user_id,'website_id':added_website_id})
else:
    output = model_run(body) 
    
    
    ##at the end of everything website is added to metadata table...
  
    website_add_request = hostname + ":3005/data/website"
    added_website_id = json.loads(requests.post(website_add_request, {'website_url':origin, 'date_last_eval':datetime.now().date(), 'date_terms_update':str(request_date)}).text)[0]['id']
    
    output['website_id'] = added_website_id
    
    ###...the new scores get pushed to raw_scores... 
    scores_add_request = hostname + ":3005/data/model"
    requests.post(scores_add_request, output)
        
    ##...new agreement also gets logged into user agreements table
        
    adding_novel_site_to_user = requests.post(hostname + ":3005/user/agreements_by_id", {'user_id':user_id,'website_id':added_website_id})
    
    




    
    
    
    
    

    
