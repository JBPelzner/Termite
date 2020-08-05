import scrapy
from scrapy.item import Item, Field
from items import WebPageItem, WebPolicyItem, ExportItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess
import sys
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup as soup

from scrapy.utils.project import get_project_settings

import re
import datetime





class finalSpider(scrapy.Spider):
  # the name is required to run the spider from the command line
  name = "refined"
    
  def __init__(self, origin_url):
    self.text = "text text"
    self.origin_url = origin_url
      
    self.updates = "date"


  # eventually this start_urls will need to contain the url from the user's active tab in Chrome
    # we are planning to use the chrome api chrome.activeTab.url and store the js variable
    # so we need to find a way to use a js variable or to directly call the url of the current tab
#   start_urls = [
#     'http://www.amazon.com'
#     # sys.argv[1]
#       ]
  def start_requests(self):
    yield SplashRequest(
    url=self.origin_url,
    callback=self.parse,
    args={'wait': 2, 'viewport': '1024x2480', 'timeout': 90, 'images': 0, 'resource_timeout': 15},
      )


#   date_updated = "07-04-1997"

  #print(sys.argv[1])
#   custom_settings = {'FEED_FORMAT':'json', 'FEED_URI':'EC2testoutput.json'}

  custom_settings = {'FEEDS':{
                              'scraped_data.json': {'format': 'json'}
                              },
                    }




  def validate(self, date_text):
      try:
          new_date = datetime.datetime.strptime(date_text, '%B %d, %Y')
          return new_date
      except ValueError:
          raise ValueError("Incorrect data format, should be something else")
          try:
            new_date = datetime.datetime.strptime(date_text, '%b %d, %Y')
            return new_date
          except ValueError:
            raise ValueError("Incorrect data format, should be something else")
            try:
              new_date = datetime.datetime.strptime(date_text, '%B %Y')
              return new_date
            except ValueError:
              raise ValueError("Incorrect data format, should be something else")


  def scrape_interesting_links(self, response):
    print('\n', '------------- IN THE SCOPE OF THE FIRST METHOD -------------')

    next_links = []

    privacy_links = []
    privacy_items = []

    terms_links = []
    terms_items = []

    conditions_links = []
    conditions_items = []

    cookies_links = []
    cookies_items = []


    p_perfect, t_perfect, cond_perfect, cook_perfect = (0,0,0,0)


    ## GO THROUGH ALL LINKS AND CATEGORIZE THEM, PICKING OUT PERFECT LINKS
    for item in response.css('a'):
      # print('LINK ITEM', item.css('a::attr(href)').get())
      
      ## PRIVACY
      if len(item.css('a *::text').re(r'.rivacy')) != 0: 
        print('\n')
        if p_perfect == 1:
          continue


        else:
          p_link = item.css('a::attr(href)').get()

          if any(p_link in sublist for sublist in [privacy_links, terms_links, conditions_links, cookies_links]):
            print('THIS IS A REPEAT PRIVACY LINK: ', p_link)
            print('PRIVACY ITEMS: ', privacy_items)
            continue

          else:
            if 'privacy' in p_link[-8:]:
              print('PERFECT PRIVACY LINK', p_link)
              p_perfect = 1

              # next_links.append(item.css('a::attr(href)').get())
              next_links.append(p_link)
              privacy_links.append(p_link)

              privacy_item = WebPolicyItem()
              # privacy_item['label'] = item.css('a *::text').get()
              # privacy_item['link'] = item.css('a::attr(href)').get()
              privacy_item['link'] = p_link

              # privacy_items.append(privacy_item)
              # self.domain[response.url]['privacy'] = privacy_item
              # self.domain[response.url]['privacy'].append(privacy_item)
              privacy_items = [privacy_item]
              print('PRIVACY ITEMS AFTER PERFECT PRIVACY LINK: ', privacy_items)

            else:
              privacy_links.append(p_link)
              print('PRIVACY LINK APPENDED', p_link)

              privacy_item = WebPolicyItem()
              # privacy_item['label'] = item.css('a *::text').get()
              privacy_item['link'] = p_link

              privacy_items.append(privacy_item)

              print('PRIVACY ITEMS AFTER IMPERFECT PRIVACY LINK: ', privacy_items)
            


      ## TERMS   
      if len(item.css('a *::text').re(r'.erms')) != 0: 
        print('\n') 
        if t_perfect == 1:
          # terms_items = [{'link': t_link}]
          continue

        else:
          t_link = item.css('a::attr(href)').get()

          if any(t_link in sublist for sublist in [privacy_links, terms_links, conditions_links, cookies_links]):
            print('THIS IS A REPEAT TERMS LINK: ', t_link)
            print('TERMS ITEMS: ', terms_items)
            continue

          else:
            if 'terms' in t_link[-6:]:
              print('PERFECT TERMS LINK', t_link)
              t_perfect = 1

              # # need to comment this line in
              next_links.append(t_link)
              terms_links.append(t_link)

              terms_item = WebPolicyItem()
              # terms_item['label'] = item.css('a *::text').get()
              terms_item['link'] = t_link

              # # need to comment this line out
              # terms_items.append(terms_item)
              # self.domain[response.url]['terms'] = terms_item

              # # need to comment this line in
              terms_items = [terms_item]
              print('TERMS ITEMS AFTER PERFECT TERMS LINK: ', terms_items)

            else:
              terms_links.append(t_link)
              print('TERMS LINK APPENDED', t_link)

              terms_item = WebPolicyItem()
              # terms_item['label'] = item.css('a *::text').get()
              terms_item['link'] = t_link

              terms_items.append(terms_item)

              print('TERMS ITEMS AFTER IMPERFECT TERMS LINK: ', terms_items)


            

      ## CONDITIONS
      if len(item.css('a *::text').re(r'.onditions')) != 0:
        print('\n')
        if cond_perfect == 1:
          continue

        else:
          cond_link = item.css('a::attr(href)').get()

          if any(cond_link in sublist for sublist in [privacy_links, terms_links, conditions_links, cookies_links]):
            print('THIS IS A REPEAT CONDITIONS LINK: ', cond_link)
            print('CONDITIONS ITEMS: ', conditions_items)
            continue

          else:
            if 'conditions' in cond_link[-11:]:
              print('PERFECT CONDITIONS LINK', cond_link)
              cond_perfect = 1

              next_links.append(cond_link)
              conditions_links.append(cond_link)

              conditions_item = WebPolicyItem()
              # conditions_item['label'] = item.css('a *::text').get()
              conditions_item['link'] = cond_link

              # conditions_items.append(conditions_item)
              # self.domain[response.url]['conditions'] = conditions_item
              conditions_items = [conditions_item]
              print('CONDITIONS ITEMS AFTER PERFECT CONDITIONS LINK: ', conditions_items)

            else:
              conditions_links.append(cond_link)
              print('CONDITIONS LINK APPENDED', cond_link)

              conditions_item = WebPolicyItem()
              # conditions_item['label'] = item.css('a *::text').get()
              conditions_item['link'] = cond_link

              conditions_items.append(conditions_item)

              print('CONDITIONS ITEMS AFTER IMPERFECT CONDITIONS LINK: ', conditions_items)

            # if cond_link not in conditions_links:
            #   conditions_links.append(item.css('a::attr(href)').get())
            #   print('CONDITIONS LINK APPENDED', cond_link)

            # if 'conditions_item' in locals():
            #   continue

            # else:
            #   conditions_item = WebPolicyItem()
            #   self.domain[response.url]['conditions'] = conditions_item



      ## COOKIES
      if len(item.css('a *::text').re(r'.ookies')) != 0: 
        print('\n')
        if cook_perfect == 1:
          continue

        else:
          cook_link = item.css('a::attr(href)').get()

          if any(cook_link in sublist for sublist in [privacy_links, terms_links, conditions_links, cookies_links]):
            print('THIS IS A REPEAT COOKIES LINK: ', cook_link)
            print('COOKIES ITEMS: ', cookies_items)
            continue

          else:
            if 'cookie' in cook_link[-8:]:
              print('PERFECT COOKIES LINK', cook_link)
              cook_perfect = 1

              next_links.append(cook_link)
              cookies_links.append(cook_link)

              cookies_item = WebPolicyItem()
              # privacy_item['label'] = item.css('a *::text').get()
              cookies_item['link'] = cook_link

              # cookies_items.append(cookies_item)

              # self.domain[response.url]['cookies'] = cookies_item
              # self.domain[response.url]['cookies'].append(cookies_item)

              cookies_items = [cookies_item]
              print('COOKIES ITEMS AFTER PERFECT COOKIES LINK: ', cookies_items)


            else:
              cookies_links.append(cook_link)
              print('COOKIES LINK APPENDED', cook_link)

              cookies_item = WebPolicyItem()
              # cookies_item['label'] = item.css('a *::text').get()
              cookies_item['link'] = cook_link

              cookies_items.append(cookies_item)

              print('COOKIES ITEMS AFTER IMPERFECT COOKIES LINK: ', cookies_items)



    # # # PEEPING STUFF

    print('\n', 'PRIVACY LINKS', privacy_links)
    print('PRIVACY ITEMS', privacy_items, '\n')

    print('TERMS LINKS', terms_links)
    print('TERMS ITEMS', terms_items, '\n')
    
    print('CONDITIONS LINKS', conditions_links)
    print('CONDITIONS ITEMS', conditions_items, '\n')
    
    print('COOKIES LINKS', cookies_links)
    print('COOKIES ITEMS', cookies_items, '\n')


    print('NEXT LINKS', next_links)




    # # # START sort_interesting_links METHOD
    print('\n', '------------ STARTING SORTING PROCESS NOW -----------')

    base_url = list(self.domain.keys())[0]
    print('BASE URL', base_url)

    inner_object = self.domain[base_url]
    print('WITHIN BASE_URL OBJECT', inner_object, '\n')
    #  # this is an object with four categories as keys and four empty lists as values
   


    if len(privacy_items) == 0:
      print('EMPTY PRIVACY ITEMS LIST')
    elif len(privacy_items) == 1:
      print('PRIVACY ITEMS LIST OF LENGTH 1')
      inner_object['privacy'].append(privacy_items[0])
      if privacy_items[0]['link'] not in next_links:
        next_links.append(privacy_items[0]['link'])
    else:
      print('MULTIPLE PRIVACY ITEMS')
      # self.link_parse(privacy_links)
      for item in privacy_items:
        print('ITEM: ', item)

        next_page = response.urljoin(item['link'])
        print('PRIVACY POLICY LINK CANDIDATE:', next_page)
        # if item['link'] in next_links:
        #   inner_object['privacy'].append(item)

        # else:
        #   next_page = response.urljoin(item['link'])
        #   print('PRIVACY POLICY LINK CANDIDATE:', next_page)

        # self.link_parse(next_page)
        # yield scrapy.Request(next_page, callback=self.link_parse) 



    if len(terms_items) == 0:
      print('EMPTY TERMS ITEMS LIST')
    elif len(terms_items) == 1:
      print('TERMS ITEMS LIST OF LENGTH 1')
      inner_object['terms'].append(terms_items[0])
      if terms_items[0]['link'] not in next_links:
        next_links.append(terms_items[0]['link'])
    else:
      print('MULTIPLE TERMS ITEMS')
      # self.link_parse(privacy_links)

      for item in terms_items:
        print('ITEM: ', item)

        next_page = response.urljoin(item['link'])
        print('TERMS POLICY LINK CANDIDATE:', next_page)
        
        # if item['link'] in next_links:
        #   inner_object['terms'].append(item)
        # else:
        #   next_page = response.urljoin(item['link'])
        #   print('TERMS POLICY LINK CANDIDATES:', next_page)

          # do we want to keep all the potential link
          # inner_object['terms'].append(item)



    if len(conditions_items) == 0:
      print('EMPTY CONDITIONS ITEMS LIST')
    elif len(conditions_items) == 1:
      print('CONDITIONS ITEMS LIST OF LENGTH 1')
      inner_object['conditions'].append(conditions_items[0])
      if conditions_items[0]['link'] not in next_links:
        next_links.append(conditions_items[0]['link'])
    else:
      print('MULTIPLE CONDITIONS ITEMS')
      # self.link_parse(privacy_links)
      for item in conditions_items:
        print('ITEM: ', item)

        next_page = response.urljoin(item['link'])
        print('CONDITIONS POLICY LINK CANDIDATE:', next_page)
          # if item['link'] in next_links:
        #   inner_object['privacy'].append(item)

        # else:
        #   next_page = response.urljoin(item['link'])
        #   print('CONDITIONS POLICY LINK CANDIDATE:', next_page)



    if len(cookies_items) == 0:
      print('EMPTY COOKIES ITEMS LIST')
    elif len(cookies_items) == 1:
      print('COOKIES ITEMS LIST OF LENGTH 1')
      inner_object['cookies'].append(conditions_items[0])
      if cookies_items[0]['link'] not in next_links:
        next_links.append(cookies_items[0]['link'])
    else:
      print('MULTIPLE COOKIES ITEMS')
      # self.link_parse(privacy_links)
      for item in cookies_items:
        print('ITEM: ', item)

        next_page = response.urljoin(item['link'])
        print('COOKIES POLICY LINK CANDIDATE:', next_page)
        # if item['link'] in next_links:
        #   inner_object['cookies'].append(item)

        # else:
        #   next_page = response.urljoin(item['link'])
        #   print('COOKIES POLICY LINK CANDIDATES:', next_page)
          # yield scrapy.Request(next_page, callback=self.link_parse)  

     

    # for link_list in [privacy_links, terms_links, conditions_links]:
    #   if len(link_list) == 1:
    #     for link in link_list:
    #       if link not in next_links:
    #         next_links.append(link)

    print('NEW NEXT LINKS', next_links)

    print('INNER OBJECT WITHIN BASE URL KEY', inner_object)
    self.domain[base_url] = inner_object

    items_list = [privacy_items, terms_items, conditions_items, cookies_items]


    return next_links, inner_object, items_list






    # this method is for scraping the text of the policy pages
  def policy_scraper(self, response):
     ## maybe we find the body text of the policy by searching by div elements
          ## we can find the length of all the divs and try to pull from the longest one
          ## but there might be a div that wraps the whole page 
    print('\n', '-------- WE ARE INSIDE THE POLICY SCRAPER --------')




    ### START INTERNAL LOGIC TO GET MAIN BODY OF POLICY PAGE

    # print(response.text)

    div_h1_dict = {}
    div_h2_dict = {}
    div_h3_dict = {}
    div_strong_dict = {}
    max_div_h1_index = []
    max_div_h2_index = []
    max_div_h3_index = []
    max_div_strong_index = []


    if len(response.css('body div')) == 0:
      print('THERE ARE NO DIVS IN THE BODY OF THIS PAGE')

      last_updated_entry = ['No entry located']
      
      entry = False

      regex = r'(.ast .pdated)'
      regex2 = r'(.ast .odified)'
      regex3 = r'(.olicy .ffective)'
      regex4 = r'(.ffective .ate)'
      regex5 = r'(.olicy .odified)'
      regex6 = r'(.pdated:)'
      regex7 = r'(.ffective:)'


    # for index, tag in enumerate(response.css('*')):
      for tag in response.css('*'):
        # print(tag)
        # print('ENTRY COUNT: ', len(last_updated_entry))
        if last_updated_entry[0] != 'No entry located':
          break

        else:
          for pattern in [regex, regex2, regex3, regex4, regex5, regex6, regex7]:
            if re.search(pattern, str(tag.css('*::text').get())):
              print('HOW MANY TEXT ITEMS IN THIS TAG: ', len(tag.css('*::text').getall()))

              if len(tag.css('*::text').getall()) > 1:
                # print(''.join(tag.css('*::text').getall()))
                # last_updated_entry.append(''.join(tag.css('*::text').getall()))
                last_updated_entry[0] = ''.join(tag.css('*::text').getall())
                break
            

      if last_updated_entry[0] != 'No entry located':
        update_entry = last_updated_entry[0]
        update_entry = update_entry.split(':')[1].strip()
        print('UPDATED ENTRY: ', update_entry)

      else:
        update_entry = last_updated_entry[0].strip()
        print('UPDATED ENTRY: ', update_entry)


      deepest_tag_tuple = (0,0)

      for index,tag in enumerate(response.css('*')): 
        # print('tag index', index)
        # print('tag', '\n', len(tag.css('*')))
        if index != 0:
          this_tag_length = len(tag.css('*'))
          if this_tag_length > deepest_tag_tuple[1]:
            deepest_tag_tuple = (index, this_tag_length)

      # print(deepest_tag_tuple)


      lucky_tag = response.css('*')[deepest_tag_tuple[0]]
      # print('The lucky tag has this many tags: ', len(lucky_tag.css('*')))


      page_text_with_tags = ['start']
      page_text = ['start']

      for index,tag in enumerate(lucky_tag.css('*')):
        # print(index, tag)


        if '<script' not in tag.get() and '<style' not in tag.get() and '<option' not in tag.get():
          # print(index)
          # print('\n', 'tag code:', '\n', tag.get())
          # print('\n', 'tag text:', '\n', tag.css('::text').getall())
          # print(''.join(tag.css('::text').getall()))
          # print('\n', '\n')

          # regex = r'^.(.ast .pdated)'
          # re.search(regex, tag.css('::text').get())

          # # if len(tag.css(' ::text').re(r'.ast .pdated')) != 0:
          # if re.search(regex, tag.css('::text').get()):
          #   print('TEXT ABOUT LAST TIME THE POLICY WAS UPDATED: ', tag.css('::text').get())

          if tag.get() not in page_text_with_tags[-1]:
            ## this one still has the html wrappers within the outside tag
            page_text_with_tags.append(tag.get())

            
            ## this one takes the text out of each tag
            page_text.append(tag.css('::text').getall())
            # page_text.append(tag.css('::text').get())
        
          # else:
            # page_text[-1] += tag.css('::text').get()
            
      del(page_text_with_tags[0])
      del(page_text[0])

      joined_page_text = ' \n'.join([''.join(i) for i in page_text])
      joined_page_text = joined_page_text.replace('"', "'")
      
      joined_html_code = ''.join(page_text_with_tags)
      joined_html_code = joined_html_code.replace('"', "'")

      soupy_text = soup(joined_html_code, 'html.parser')

      return joined_page_text, joined_html_code, last_updated_entry
    


    ## or, if there are divs on the page
    else:
      print('YEA, WE GOT DIVS IN THE BODY OF THIS PAGE')

      # # HANDLE THE 'LAST UPDATED' FIELD
      last_updated_entry = ['No entry located']
      
      entry = False

      regex = r'(.ast .pdated)'
      regex2 = r'(.ast .odified)'
      regex3 = r'(.olicy .ffective)'
      regex4 = r'(.ffective .ate)'
      regex5 = r'(.olicy .odified)'
      regex6 = r'(.pdated:)'
      regex7 = r'(.ffective:)'


    # for index, tag in enumerate(response.css('*')):
      # for tag in response.css('*'):
      for tag in response.css('body *'):
        # print('LAST UPDATED ENTRY: ', last_updated_entry[0])
        if last_updated_entry[0] != 'No entry located':
          break

        # print(tag)

        else:
          for pattern in [regex, regex2, regex3, regex4, regex5, regex6, regex7]:
            if re.search(pattern, str(tag.css('*::text').get())):
              print('HOW MANY TEXT ITEMS IN THIS TAG: ', len(tag.css('*::text').getall()))

              if len(tag.css('*::text').getall()) > 1:
                # print(''.join(tag.css('*::text').getall()))
                # last_updated_entry.append(''.join(tag.css('*::text').getall()))
                last_updated_entry[0] = ''.join(tag.css('*::text').getall())
                break
              
      

      if last_updated_entry[0] != 'No entry located':
        update_entry = last_updated_entry[0]
        update_entry = update_entry.split(':')[1].strip()
        print('UPDATED ENTRY: ', update_entry)

      else:
        update_entry = last_updated_entry[0].strip()
        print('UPDATED ENTRY: ', update_entry)



      print('DO IT GOT A MAIN THO?', '\n',len(response.css('body main').getall()), 
                                      '\n', response.css('body main').getall())

      if len(response.css('body main').getall()) > 0:
        print('WE HAVE A MAIN TAG IN THE BODY')


        # # NOW WE BEGIN THE PROCESS OF IDENTIFYING THE MAIN TEXT SECTION
        for index,tag in enumerate(response.css('body *')): 
          # if index != 0:
          div_h1_dict[index] = len(tag.css('h1'))
          div_h2_dict[index] = len(tag.css('h2'))
          div_h3_dict[index] = len(tag.css('h3'))
          div_strong_dict[index] = len(tag.css('strong'))


        for key, value in div_h1_dict.items():
          if value == max(div_h1_dict.values()): 
            max_div_h1_index.append(key) 

        if max(div_h1_dict.values()) == 0:
          max_div_h1_index.clear()
          # print('NO H1 Headers in Divs on this webpage')

        for key, value in div_h2_dict.items():
          if value == max(div_h2_dict.values()): 
            max_div_h2_index.append(key) 
        if max(div_h2_dict.values()) == 0:
          max_div_h2_index.clear()
          # print('NO H2 Headers in Divs on this webpage')

        for key, value in div_h3_dict.items():
          if value == max(div_h3_dict.values()): 
            max_div_h3_index.append(key) 
        if max(div_h3_dict.values()) == 0:
          max_div_h3_index.clear()
          # print('NO H3 Headers in Divs on this webpage')

        for key, value in div_strong_dict.items():
          if value == max(div_strong_dict.values()): 
            max_div_strong_index.append(key) 
        if max(div_strong_dict.values()) == 0:
          max_div_strong_index.clear()
          # print('NO strong text in Divs on this webpage')


        if len(max_div_h1_index) == 0:
          if len(max_div_h2_index) > 0 & len(max_div_h3_index) > 0:
            common_index = list(set(max_div_h2_index) & set(max_div_h3_index)) 
          elif len(max_div_h2_index) == 0 & len(max_div_h3_index) == 0:
            common_index = max_div_strong_index
          elif len(max_div_h2_index) == 0:
            common_index = max_div_h3_index
          else:
            common_index = max_div_h2_index

        else:
          if len(max_div_h3_index) > 0:
            print('WE HAVE H1 and H3')
            if len(max_div_h2_index) > 0:
              print('WE HAVE H2 TOO')
              common_index = list(set(max_div_h1_index) & set(max_div_h2_index) & set(max_div_h3_index))
              print('YEEERRRR COMMON INDEX OF D1, D2, AND D3:', common_index)
              if len(common_index) == 0:
                common_index = list(set(max_div_h1_index) & set(max_div_h3_index))
                print('YEEERRRR COMMON INDEX OF D1 AND D3:', common_index)
                if len(common_index) == 0:
                  common_index = list(set(max_div_h1_index) & set(max_div_h2_index))
                  print('YEEERRRR COMMON INDEX OF D1 AND D2:', common_index)
                  if len(common_index) == 0:
                    common_index = list(set(max_div_h2_index) & set(max_div_h3_index))
                    print('YEEERRRR COMMON INDEX OF D2 AND D3:', common_index)

            else:
              print('WE AINT GOT NO H2!')
              common_index = list(set(max_div_h1_index) & set(max_div_h3_index))
              print('YEEERRRR COMMON INDEX OF D1 AND D3:', common_index)
              if len(common_index) == 0:
                common_index = list(set(max_div_h1_index) & set(max_div_strong_index))
                print('YEEERRRR COMMON INDEX OF D1 AND STRONG:', common_index)
                  


          else:
            print('WE HAVE H1 BUT NO H3')

            if len(max_div_h2_index) > 0:
              print('WE HAVE H2 THO')
              common_index = list(set(max_div_h1_index) & set(max_div_h2_index))
              print('YEEERRRR COMMON INDEX OF D1 AND D2:', common_index)
              if len(common_index) == 0:
                common_index = list(set(max_div_h1_index) & set(max_div_strong_index))
                print('YEEERRRR COMMON INDEX OF D1 AND STRONG:', common_index)
            else:
              print('WE AINT GOT NO H2 EITHER!')
              common_index = list(set(max_div_h1_index) & set(max_div_strong_index))
              print('YEEERRRR COMMON INDEX OF D1 AND STRONG:', common_index)



        # elif len(max_div_h3_index) > 0 & len(max_div_h2_index) > 0:
        #   common_index = list(set(max_div_h1_index) & set(max_div_h2_index) & set(max_div_h3_index))
        #   print('YEEERRRR COMMON INDEX OF D1, D2, AND D3:', common_index)
        #   if len(common_index) == 0:
        #     common_index = list(set(max_div_h1_index) & set(max_div_h3_index))
        #     print('YEEERRRR COMMON INDEX OF D1 AND D3:', common_index)
        #     if len(common_index) == 0:
        #       common_index = list(set(max_div_h1_index) & set(max_div_h2_index))
        #       print('YEEERRRR COMMON INDEX OF D1 AND D2:', common_index)
        #       if len(common_index) == 0:
        #         common_index = list(set(max_div_h2_index) & set(max_div_h3_index))
        #         print('YEEERRRR COMMON INDEX OF D2 AND D3:', common_index)


        # elif len(max_div_h3_index) == 0:
        #   if len(max_div_h2_index) > 0:
        #     common_index = list(set(max_div_h1_index) & set(max_div_h2_index))
        #   else:
        #     common_index = max_div_strong_index

        # elif len(max_div_h2_index) == 0:
        #   if len(max_div_h3_index) > 0:
        #     common_index = list(set(max_div_h1_index) & set(max_div_h3_index))
        #   else:
        #     common_index = max_div_strong_index
          
        # else:
        #   common_index = list(set(max_div_h1_index) & set(max_div_h2_index) & set(max_div_h3_index)) 

        print('H1:', max_div_h1_index)
        print(max_div_h2_index)
        print(max_div_h3_index)
        print('strong:', max_div_strong_index)
        print('COMMON INDEX:', common_index)

        # print(response.css('body div')[min(max_div_h1_index)])
        # print('DIV TEXT FROM LUCKY DIV:', response.css('body div').getall()[min(common_index)])

        key_index = min(common_index)

        # if len(common_index) > 0:
        #   # print(common_index)
        #   key_index = common_index[0]
        # elif len(max_div_h2_index) > 0:
        #   # print(max(max_div_h2_index))
        #   key_index = max_div_h2_index[0]
        # elif len(max_div_h1_index) > 0:
        #   # print(min(max_div_h1_index))
        #   key_index = max_div_h1_index[0]
        # elif len(max_div_h3_index) > 0:
        #   # print(max(max_div_h3_index))
        #   key_index = max_div_h3_index[0]
        # elif len(max_div_strong_index) > 0:
        #   # print(max(max_div_strong_index))
        #   key_index = max_div_strong_index[0]
        # else:
        #   print('THIS WEBSITE IS FORMATTED REALLY WEIRDLY')

        lucky_tag = response.css('body *')[key_index]

      else:
        print('NO MAIN TAG IN THE BODY')

        # # NOW WE BEGIN THE PROCESS OF IDENTIFYING THE MAIN TEXT SECTION
        for index,tag in enumerate(response.css('body div')): 
          # if index != 0:
          div_h1_dict[index] = len(tag.css('h1'))
          div_h2_dict[index] = len(tag.css('h2'))
          div_h3_dict[index] = len(tag.css('h3'))
          div_strong_dict[index] = len(tag.css('strong'))


        for key, value in div_h1_dict.items():
          if value == max(div_h1_dict.values()): 
            max_div_h1_index.append(key) 

        if max(div_h1_dict.values()) == 0:
          max_div_h1_index.clear()
          # print('NO H1 Headers in Divs on this webpage')

        for key, value in div_h2_dict.items():
          if value == max(div_h2_dict.values()): 
            max_div_h2_index.append(key) 
        if max(div_h2_dict.values()) == 0:
          max_div_h2_index.clear()
          # print('NO H2 Headers in Divs on this webpage')

        for key, value in div_h3_dict.items():
          if value == max(div_h3_dict.values()): 
            max_div_h3_index.append(key) 
        if max(div_h3_dict.values()) == 0:
          max_div_h3_index.clear()
          # print('NO H3 Headers in Divs on this webpage')

        for key, value in div_strong_dict.items():
          if value == max(div_strong_dict.values()): 
            max_div_strong_index.append(key) 
        if max(div_strong_dict.values()) == 0:
          max_div_strong_index.clear()
          # print('NO strong text in Divs on this webpage')



        if len(max_div_h1_index) == 0:
          print('WE HAVE NO H1')
          if len(max_div_h2_index) > 0 & len(max_div_h3_index) > 0:
            common_index = list(set(max_div_h2_index) & set(max_div_h3_index)) 
          elif len(max_div_h2_index) == 0 & len(max_div_h3_index) == 0:
            common_index = max_div_strong_index
          elif len(max_div_h2_index) == 0:
            common_index = max_div_h3_index
          else:
            common_index = max_div_h2_index

        else:
          if len(max_div_h3_index) > 0:
            print('WE HAVE H1 and H3')
            if len(max_div_h2_index) > 0:
              print('WE HAVE H2 TOO')
              common_index = list(set(max_div_h1_index) & set(max_div_h2_index) & set(max_div_h3_index))
              print('YEEERRRR COMMON INDEX OF D1, D2, AND D3:', common_index)
              if len(common_index) == 0:
                common_index = list(set(max_div_h1_index) & set(max_div_h3_index))
                print('YEEERRRR COMMON INDEX OF D1 AND D3:', common_index)
                if len(common_index) == 0:
                  common_index = list(set(max_div_h1_index) & set(max_div_h2_index))
                  print('YEEERRRR COMMON INDEX OF D1 AND D2:', common_index)
                  if len(common_index) == 0:
                    common_index = list(set(max_div_h2_index) & set(max_div_h3_index))
                    print('YEEERRRR COMMON INDEX OF D2 AND D3:', common_index)

            else:
              print('WE AINT GOT NO H2!')
              common_index = list(set(max_div_h1_index) & set(max_div_h3_index))
              print('YEEERRRR COMMON INDEX OF D1 AND D3:', common_index)
              if len(common_index) == 0:
                common_index = list(set(max_div_h1_index) & set(max_div_strong_index))
                print('YEEERRRR COMMON INDEX OF D1 AND STRONG:', common_index)
                  


          else:
            print('WE HAVE H1 BUT NO H3')

            if len(max_div_h2_index) > 0:
              print('WE HAVE H2 THO')
              common_index = list(set(max_div_h1_index) & set(max_div_h2_index))
              print('YEEERRRR COMMON INDEX OF D1 AND D2:', common_index)
              if len(common_index) == 0:
                common_index = list(set(max_div_h1_index) & set(max_div_strong_index))
                print('YEEERRRR COMMON INDEX OF D1 AND STRONG:', common_index)
            else:
              print('WE AINT GOT NO H2 EITHER!')
              common_index = list(set(max_div_h1_index) & set(max_div_strong_index))
              print('YEEERRRR COMMON INDEX OF D1 AND STRONG:', common_index)
        # if len(max_div_h1_index) == 0:
        #   if len(max_div_h2_index) > 0 & len(max_div_h3_index) > 0:
        #     common_index = list(set(max_div_h2_index) & set(max_div_h3_index)) 
        #   elif len(max_div_h2_index) == 0 & len(max_div_h3_index) == 0:
        #     common_index = max_div_strong_index
        #   elif len(max_div_h2_index) == 0:
        #     common_index = max_div_h3_index
        #   else:
        #     common_index = max_div_h2_index


        # elif len(max_div_h3_index) == 0:
        #   common_index = list(set(max_div_h1_index) & set(max_div_h2_index))

        # elif len(max_div_h2_index) == 0:
        #   common_index = list(set(max_div_h1_index) & set(max_div_h3_index))
        #   print('COMMON INDEX OF D1 and D3:', common_index)
        # else:
        #   common_index = list(set(max_div_h1_index) & set(max_div_h2_index) & set(max_div_h3_index)) 

        print('H1:', max_div_h1_index)
        print(max_div_h2_index)
        print(max_div_h3_index)
        print('strong:', max_div_strong_index)
        print('COMMON INDEX:', common_index)

        # print(response.css('body div')[min(max_div_h1_index)])
        # print('DIV TEXT FROM LUCKY DIV:', response.css('body div').getall()[min(common_index)])

        key_index = min(common_index)

        # if len(common_index) > 0:
        #   # print(common_index)
        #   key_index = common_index[0]
        # elif len(max_div_h2_index) > 0:
        #   # print(max(max_div_h2_index))
        #   key_index = max_div_h2_index[0]
        # elif len(max_div_h1_index) > 0:
        #   # print(min(max_div_h1_index))
        #   key_index = max_div_h1_index[0]
        # elif len(max_div_h3_index) > 0:
        #   # print(max(max_div_h3_index))
        #   key_index = max_div_h3_index[0]
        # elif len(max_div_strong_index) > 0:
        #   # print(max(max_div_strong_index))
        #   key_index = max_div_strong_index[0]
        # else:
        #   print('THIS WEBSITE IS FORMATTED REALLY WEIRDLY')

        lucky_tag = response.css('body div')[key_index]
      



      page_text_with_tags = ['start']
      page_text = ['start']            

      first_header_index = []
      for index,tag in enumerate(lucky_tag.css('*')):
        if len(first_header_index) > 0:
          break

        for header in ['<h1', '<h2', '<h3', '<h4', '<h5']:
          if header in tag.get()[0:3]:
            first_header_index.append(index)
            print('OBTAINED DANK HEADER')
            break
          else:
            continue



      for index,tag in enumerate(lucky_tag.css('*')[first_header_index[0]:]):
        if index == 0:
          print('OUTERMOST OBJECT INSIDE LUCKY TAG')
          print(tag.css('* ::text').getall())


        if '<footer' in tag.get()[0:7]:
          break

        if '<script' not in tag.get() and '<style' not in tag.get() and '<option' not in tag.get():
  

          if tag.get() not in page_text_with_tags[-1]:
            
            ## this one still has the html wrappers within the outside tag
            page_text_with_tags.append(tag.get())

            # for index, code in enumerate(page_text_with_tags):
              # print('tag index', index)
              # print('tag code', '\n', code, '\n')


            if '<a' in tag.get():
              ## this one takes the text out of each tag of a layered tag and joins them
              joined_tag_text = ' '.join(tag.css('*::text').getall())
              page_text.append(joined_tag_text)

            else:
              ## this one takes the text out of each tag
              page_text.append(tag.css('*::text').getall())


      del(page_text_with_tags[0])
      del(page_text[0])

     
      joined_page_text = []

      for index,text_list in enumerate(page_text):
        # print('Tag index: ', index)
        # print('Number of text objects in tag: ', len(text_list))
        # print('Tag chunk: ', tag.get(), '\n', '\n')

        joined_page_text.append(''.join(text_list))

      ## outer join of text chunks
      joined_page_text = '\n'.join(joined_page_text)
      joined_page_text = joined_page_text.replace('"', "'")
      
      # joined_html_code = ''.join(page_text_with_tags)
      # joined_html_code = joined_html_code.replace('"', "'")


      # soupy_text = soup(joined_html_code, 'html.parser')
      # print(soupy_text.prettify())

      # return joined_page_text, joined_html_code, last_updated_entry
      return joined_page_text, update_entry




    # used for cases like Twitter where the initial website was attempted to be redirected
        # the initial 302 http status code attempted to redirect the twitter home page to a mobile version
        # however, the mobile version causes a 404 error and cannot be scraped
          # so, we want to prevent the 302 redirection to the mobile page
  # def make_requests_from_url(self, url):
  #       return scrapy.Request(url, dont_filter=True, meta = {
  #                 'dont_redirect': True,
  #                 'handle_httpstatus_list': [301,302]
  #           })








  # the parse method is run on the response, and is a required method for the spider
    #this method will get repeated for all the relevant links on the page
  def parse(self, response):

    self.logger.debug("CURRENT USER AGENT: {}".format(response.request.headers['User-Agent']))
    self.logger.debug("(parse) response: status=%d, URL=%s" % (response.status, response.url))
    self.logger.info('Parse function called on %s', response.url)



    self.domain = {}
    self.domain[response.url] = {}
    self.domain[response.url]['privacy'] = []
    self.domain[response.url]['terms'] = []
    self.domain[response.url]['conditions'] = []
    self.domain[response.url]['cookies'] = [] 


    print('\n', '------------- STARTING PARSE OF BASE URL -------------')
    print('OUTER OBJECT:', self.domain)


    links_items_return = self.scrape_interesting_links(response)

    print('\n', '------------- BACK IN PARSE NOW -------------')

    
    next_links = links_items_return[0] 
    inner_object = links_items_return[1]
    items_list = links_items_return[2]

    print('NEXT LINKS', next_links)
    print('INNER OBJECT', inner_object, '\n')
    print('ITEMS LIST', items_list, '\n')


    # # using length of items list to determine pathway for the category
    for entry in items_list:
      print('\n', 'ENTRY: ', entry)

      if len(entry) == 0:
        print('NO ITEMS FOR THIS CATEGORY')

      elif len(entry) == 1:
        print('ONE ITEM FOR THIS CATEGORY')
        next_page = response.urljoin(entry[0]['link'])
        print('ABOUT TO BE SCRAPED:', next_page)
        yield scrapy.Request(next_page, callback=self.rule_parse2)


      else:
        print('MULTIPLE ITEMS FOR THIS CATEGORY')
        print('LENGTH OF ENTRY: ', len(entry))
        for item in entry:
          next_page = response.urljoin(item['link'])
          print('NEXT PAGE TO BE PROCESSED: ', next_page)
          yield scrapy.Request(next_page, callback=self.reduce_category)


    # print('INNER OBJECT ITEMS', '\n', list(inner_object.items()))
    # for item in inner_object.items():
    #   print('CATEGORY:   ', item[0])
    #   print('ITEMS:   ', item[1])


    #   if len(item[1]) == 0:
    #     pass

    #   elif len(item[1]) == 1:
    #     next_page = response.urljoin(item[1][0]['link'])
    #     print('ABOUT TO BE SCRAPED:', next_page)
    #     yield scrapy.Request(next_page, callback=self.rule_parse2)

    #   else:
    #     for each in item[1]:
    #       print('each object inside a category')
    #       print(each)

    #       next_page = response.urljoin(each['link'])
    #       print('ABOUT TO BE PROCESSED:', next_page)
    #       yield scrapy.Request(next_page, callback=self.reduce_category)

          # # I don't think this is needed because I reduce each category in the previous method
          # if each['link'] in next_links:
          #  pass


  def reduce_category(self, response):
    print('\n', '-------------- INSIDE OF REDUCE CATEGORY FUNCTION --------------')

    print('CURRENT PATHWAY: ', response.url)

    print('SITE: ', response.css('body *::text').get())
    print('SITE COUNT: ', len(response.css('body').re(r'site')))



    return





  def rule_parse2(self, response):
    print('\n', '-------------- INSIDE OF RULE PARSE 2!! --------------')
    print('PAGE TITLE: ', response.css('title::text').get())
    print('PAGE URL: ', response.url)


    # load_ins = self.domain.keys()
    # print('LOAD IN', load_ins)

    base_url = list(self.domain.keys())[0]

    print('INNER OBJECT "self.domain[base_url]": ', '\n', self.domain[base_url])


    if len(response.css('title').re(r'.rivacy')) != 0:

      if (len(response.css('title').re(r'.tatement')) != 0) | (len(response.css('title').re(r'.olicy')) != 0) | (len(response.css('title').re(r'.otice')) != 0):

        policy_scraper_results = self.policy_scraper(response)
        joined_page_text = policy_scraper_results[0]
        last_updated_entry = policy_scraper_results[1]


        # joined_page_text = self.policy_scraper(response)[0]
        # # soupy_text = self.policy_scraper(response)[1]
        # last_updated_entry = self.policy_scraper(response)[1]

        # privacy_item = self.domain['link_dict']['privacy']
        privacy_item = self.domain[base_url]['privacy'][0]
        print('PRIVACY ITEM LOADED FROM SELF:', privacy_item)


        privacy_item['title'] = response.css('title::text').get()
        privacy_item['url'] = response.url
        privacy_item['last_updated'] = last_updated_entry
        privacy_item['text'] = joined_page_text
        # privacy_item['html'] = soupy_text

        # self.domain['link_dict']['privacy'] = privacy_item
        self.domain[base_url]['privacy'] = privacy_item

      else:
        print('LINKS ON THIS PAGE:')
        for link in response.css('a').getall():
          print(link)


    ## REPEAT ABOVE PROCESS FOR OTHER TYPES OF POLICIES

    if len(response.css('title').re(r'.erms')) != 0:

      policy_scraper_results = self.policy_scraper(response)
      joined_page_text = policy_scraper_results[0]
      last_updated_entry = policy_scraper_results[1]

      # joined_page_text = self.policy_scraper(response)[0]
      # # soupy_text = self.policy_scraper(response)[1]
      # last_updated_entry = self.policy_scraper(response)[1]

      # terms_item = self.domain['link_dict']['terms']
      terms_item = self.domain[base_url]['terms'][0]

      terms_item['title'] = response.css('title::text').get()
      terms_item['url'] = response.url
      terms_item['last_updated'] = last_updated_entry
      terms_item['text'] = joined_page_text
      # terms_item['html'] = soupy_text

      # self.domain['link_dict']['terms'] = terms_item
      self.domain[base_url]['terms'] = terms_item



    if len(response.css('title').re(r'.onditions')) != 0:

      if len(response.css('title').re(r'.erms')) == 0:

        policy_scraper_results = self.policy_scraper(response)
        joined_page_text = policy_scraper_results[0]
        last_updated_entry = policy_scraper_results[1]

        # joined_page_text = self.policy_scraper(response)[0]
        # # soupy_text = self.policy_scraper(response)[1]
        # last_updated_entry = self.policy_scraper(response)[1]

        # conditions_item = self.domain['link_dict']['conditions']
        conditions_item = self.domain[base_url]['conditions'][0]

        conditions_item['title'] = response.css('title::text').get()
        conditions_item['url'] = response.url
        conditions_item['last_updated'] = last_updated_entry
        conditions_item['text'] = joined_page_text
        # conditions_item['html'] = soupy_text

        # self.domain['link_dict']['conditions'] = conditions_item
        self.domain[base_url]['conditions'] = conditions_item



    if len(response.css('title').re(r'.ookie')) != 0:

      policy_scraper_results = self.policy_scraper(response)
      joined_page_text = policy_scraper_results[0]
      last_updated_entry = policy_scraper_results[1]

      # joined_page_text = self.policy_scraper(response)[0]
      # # soupy_text = self.policy_scraper(response)[1]
      # last_updated_entry = self.policy_scraper(response)[1]

      # conditions_item = self.domain['link_dict']['conditions']
      cookies_item = self.domain[base_url]['cookies'][0]

      cookies_item['title'] = response.css('title::text').get()
      cookies_item['url'] = response.url
      cookies_item['last_updated'] = last_updated_entry
      cookies_item['text'] = joined_page_text
      # conditions_item['html'] = soupy_text

      # self.domain['link_dict']['conditions'] = conditions_item
      self.domain[base_url]['cookies'] = cookies_item




    # print('LINK DICT BEFORE YIELD:', self.domain[base_url])


    length_list = []

    print('POLICY ITEMS:', list(self.domain[base_url].keys()))

    for index, key in enumerate(list(self.domain[base_url].keys())):
      print('INDEX: ', index)
      print('LENGTH OF VALUE: ', len(self.domain[base_url][key]))
      
      length_list.append(len(self.domain[base_url][key]))

      # item_tuple = (index, len(self.domain[base_url][key]))
      # length_list.append(item_tuple)

      # if len(self.domain[base_url][key]) != 0:
      #   if len(self.domain[base_url][key]) == 5:
      #     print('THIS CATEGORY IS COMPLETE')

    
    all_policy_names = []
    all_policy_urls = []
    all_policy_text = []
    all_update_entries = []

    new_dates_list = []

    if (length_list.count(0) + length_list.count(5) != len(length_list)):
      print('WE CAN NOT YIELD THE ITEM YET')
      yield
    else:
      print('ALL CATEGORIES ARE COMPLETE... WE CAN YIELD THE ITEM AND FINISH')
      for key in self.domain[base_url].keys():
        if len(self.domain[base_url][key]) > 0:
          print('URL OF ITEM: ', self.domain[base_url][key]['url'])

          all_policy_text.append(self.domain[base_url][key]['text'])
          all_update_entries.append(self.domain[base_url][key]['last_updated'])
          all_policy_names.append(self.domain[base_url][key]['title'])
          all_policy_urls.append(self.domain[base_url][key]['url'])


        # print('URL OF ITEM: ', self.domain[base_url][key]['url'])

      if all_update_entries.count('No entry located') == len(all_update_entries):
        all_update_entries = 'No entry located'
        most_recent_entry = 'No entry located'

      elif all_update_entries.count('No entry located') > 0:
        print('AT LEAST ONE NO ENTRY LOCATED VALUE')
        for index, entry in enumerate(all_update_entries):
          if entry == 'No entry located':
            del(all_update_entries[index])

        # # here we do datetime stuff to find the most recent one
          else:
            print('ALL UPDATE ENTRIES:', all_update_entries)
            print('UPDATED ENTRIES AT THIS INDEX:', all_update_entries[index])
            print('TYPE OF UPDATED ENTRIES AT THIS INDEX:', type(all_update_entries[index]))
            print('CONVERTING TO DATE FORMAT IN HERE')
            print('ENTRY', entry)
            
            new_date = self.validate(entry)
            print('NEW DATE: ', new_date)
            print('TYPE OF NEW DATE: ', type(new_date))
            new_dates_list.append(new_date)

        print('NEW DATES LIST:', new_dates_list)
        print('MOST RECENT DATE:', max(new_dates_list))

        most_recent_entry = max(new_dates_list)
        print('IS MOST RECENT ENTRY MORE RECENT THAN NOW: ', most_recent_entry > datetime.datetime.now())


      else:
        # # this is if there are zero 'no entry located' values
        # # do datetime stuff here too
        print('CONVERTING TO DATE FORMAT IN HEEEEERE')

        for entry in all_update_entries:
          new_date = self.validate(entry)
          print('NEW DATE: ', new_date)
          print('TYPE OF NEW DATE: ', type(new_date))
          new_dates_list.append(new_date)

        print('NEW DATES LIST:', new_dates_list)
        print('MOST RECENT DATE:', max(new_dates_list))

        most_recent_entry = max(new_dates_list)
    
    
      
      
      self.text = '\n'.join(all_policy_text)
        
      
      self.updates = most_recent_entry
        


      export_item = ExportItem()
      export_item['text'] = '\n'.join(all_policy_text)
      export_item['updates'] = most_recent_entry
      export_item['titles'] = all_policy_names
      export_item['urls'] = all_policy_urls

      #yield
      yield export_item
        
        
scraped_items = []

# class Scraper2Pipeline:
#     def process_item(self, item, spider):
#         global scraped_items
#         scraped_items.append(item)
#         return


    
# settings = get_project_settings()

# # print(settings.attributes['ITEM_PIPELINES'])
# # settings.attributes['ITEM_PIPELINES'] = {'__main__.ItemCollectorPipeline' :100}
# # print(settings.attributes['ITEM_PIPELINES'])

# #'ITEM_PIPELINES': { '__main__.ItemCollectorPipeline': 100 }

# # process = CrawlerProcess(get_project_settings())
# process = CrawlerProcess(settings)
# # # spiderguy = finalSpider() 
# process.crawl(finalSpider, origin_url='https://www.amazon.com')
# process.start()

# print(scraped_items)

# print(finalSpider(scrapy.Spider).text)
# spider = finalSpider('http://www.amazon.com')
# spider.start_requests()
# print(spider.text)

      
# print("Hi this worked")

