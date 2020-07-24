import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from bs4 import BeautifulSoup as soup

website_dict = {}
# link_dict = {'privacy': {}, 'terms': {}, 'conditions': {}}
parse_count = 0

next_links = []

class generalSpider(scrapy.Spider):
  # the name is required to run the spider from the command line
  name = "twitter"

  # eventually this start_urls will need to contain the url from the user's active tab in Chrome
    # we are planning to use the chrome api chrome.activeTab.url and store the js variable
    # so we need to find a way to use a js variable or to directly call the url of the current tab
  start_urls = [
      'https://www.amazon.com/'
  ]

  # idk if this is necessary
  rules = [Rule(LinkExtractor(allow='terms'), callback='parse_item', follow = False)]


  # create the dictionary method
  def create_dictionary(self, response):
    link_dict = {'privacy': {}, 'terms': {}, 'conditions': {}}
    # global link_dict

    self.root_url = response.url
    
    website_dict[response.url] = link_dict

    return website_dict, link_dict


  # create the parse counter method
  def parse_counter(self, response):
    global parse_count

    parse_count += 1
    return parse_count


  # create a method that can store the state of how many important links gathered from the root page
    # still need to be scraped
  def scrape_interesting_links(self, response):
    # global next_links
    # global link_dict 
    # next_links = {}
    # next_links[response.url] = []
    next_links = []

    website_dict = self.create_dictionary(response)[0]
    link_dict = self.create_dictionary(response)[1]
    print('Outer Dictionary: ', website_dict)
    print('Inner Dictionary: ', link_dict)

    

    for item in response.css('a'):
      if len(item.css('a::text').re(r'.rivacy')) != 0:  
          link_dict['privacy'] = {
            'label' : item.css('a::text').get(),
            'link': item.css('a::attr(href)').get()
            }

      if len(item.css('a::text').re(r'.erms')) != 0:  
          link_dict['terms'] = {
            'label' : item.css('a::text').get(),
            'link': item.css('a::attr(href)').get()
            }

      if len(item.css('a::text').re(r'.onditions')) != 0:  
          link_dict['conditions'] = {
            'label' : item.css('a::text').get(),
            'link': item.css('a::attr(href)').get()
            }

    self.website_dict = website_dict
    self.link_dict = link_dict


    for key,value in link_dict.items():
      if len(value) != 0:
        next_links.append(link_dict[key]['link'])
        # next_links[response.url].append(link_dict[key]['link'])
    print('NEXT LINKS: ', next_links)

    print('OUTER DICTIONARY: ', website_dict)
    
    self.next_links = next_links
    return next_links


    # this method will count the number of links yet to be scraped
  def remaining_link_counter(self, response):
    print('NUMBER OF ADDITIONAL LINKS TO BE SCRAPED: ', len(self.next_links))
    # print('NUMBER OF ADDITIONAL LINKS TO BE SCRAPED: ', len(self.next_links))
    # print('WEBSITE DICTIONARY: ', self.website_dict)
    # print(next_links)


  def remaining_link_trigger(self, response, next_links):
    # print(response.url)
    for index, link in enumerate(next_links):
      print(link)
      next_page = response.urljoin(link)
      yield scrapy.Request(next_page, callback=self.parse)
      

      # print('Link {}: {}'.format(index+1, link))
      # if self.parse_count == (len(self.next_links) + 1):
      #   print('LAST LINK --------------')
      
     
    #   ## The next goal is to save all relevant links in an array so that the href can be pulled
    # ## and used as the next page
    #   ## I think this is working for now
    # next_links = []
    # for key,value in link_dict.items():
    #   if len(value) != 0:
    #     next_links.append(link_dict[key]['link'])

    # print('NUMBER OF ADDITIONAL LINKS TO BE SCRAPED: ', len(next_links))
    # print(next_links)
    # print(website_dict)

    # for index, link in enumerate(next_links):
    #   # print('Link {}: {}'.format(index+1, link))
    #   if parse_count == (len(next_links) + 1):
    #     print('LAST LINK --------------')
    #     # yield {
    #     #   'link_dict': link_dict, 
    #     #   'website_dict': website_dict
    #     #   }
    #     if link is not None:
    #       # next_page = response.urljoin(link)
    #       next_page = response.urljoin(link)
    #       yield scrapy.Request(next_page, callback=self.parse)  
    



  # this method is for scraping the text of the policy pages
  def policy_scraper(self, response):

    ### START INTERNAL LOGIC TO GET MAIN BODY OF POLICY PAGE

    div_h1_dict = {}
    div_h2_dict = {}
    div_h3_dict = {}
    div_strong_dict = {}
    max_div_h1_index = []
    max_div_h2_index = []
    max_div_h3_index = []
    max_div_strong_index = []




    if len(response.css('body div')) == 0:

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
        print(index, tag)


        if '<script' not in tag.get() and '<style' not in tag.get() and '<option' not in tag.get():
          # print(index)
          # print('\n', 'tag code:', '\n', tag.get())
          # print('\n', 'tag text:', '\n', tag.css('::text').getall())
          # print(''.join(tag.css('::text').getall()))
          # print('\n', '\n')

          if tag.get() not in page_text_with_tags[-1]:
            ## this one still has the html wrappers within the outside tag
            page_text_with_tags.append(tag.get())

            
            ## this one takes the text out of each tag
            page_text.append(tag.css('::text').getall())
        
          # else:
            print(tag.css('::text').get())
            print(tag.get())

            # page_text[-1] += tag.css('::text').get()
            
      del(page_text_with_tags[0])
      del(page_text[0])

      # print(page_text)
      joined_page_text = ' \n'.join([''.join(i) for i in page_text])
      # joined_page_text = joined_page_text.replace('"', "'")
      

      # print(joined_page_text)
      # print(len(joined_page_text))

      # print(page_text_with_tags)
      # print(len(page_text_with_tags))
      joined_html_code = ''.join(page_text_with_tags)
      joined_html_code = joined_html_code.replace('"', "'")

      soupy_text = soup(joined_html_code, 'html.parser')
      # print(soupy_text.prettify())


    ## or, if there are divs on the page
    else:

      for index,div in enumerate(response.css('body div')): 
        div_h1_dict[index] = len(div.css('h1'))
        div_h2_dict[index] = len(div.css('h2'))
        div_h3_dict[index] = len(div.css('h3'))
        div_strong_dict[index] = len(div.css('strong'))


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

      if len(max_div_h2_index) == 0:
        common_index = list(set(max_div_h1_index) & set(max_div_h3_index)) 
      elif len(max_div_h3_index) == 0:
        common_index = list(set(max_div_h1_index) & set(max_div_h2_index))
      elif len(max_div_h1_index) == 0:
        common_index = list(set(max_div_h2_index) & set(max_div_h3_index)) 
      else:
        common_index = list(set(max_div_h1_index) & set(max_div_h2_index) & set(max_div_h3_index)) 

      print(max_div_h1_index)
      print(max_div_h2_index)
      print(max_div_h3_index)
      print(max_div_strong_index)

      if len(common_index) > 0:
        # print(common_index)
        key_index = max(common_index)
      elif len(max_div_h2_index) > 0:
        # print(max(max_div_h2_index))
        key_index = max(max_div_h2_index)
      elif len(max_div_h1_index) > 0:
        # print(min(max_div_h1_index))
        key_index = min(max_div_h1_index)
      elif len(max_div_h3_index) > 0:
        # print(max(max_div_h3_index))
        key_index = max(max_div_h3_index)
      elif len(max_div_strong_index) > 0:
        # print(max(max_div_strong_index))
        key_index = max(max_div_strong_index)
      else:
        print('THIS WEBSITE IS FORMATTED REALLY WEIRDLY')


      # lucky_tag = response.css('body div')[min(common_index)]
      lucky_tag = response.css('body div')[key_index]

      # print('This is the lucky div: ', '\n', lucky_tag.css('*'))
      # print('\n', 'The lucky div, div{}, has {} tags'.format(key_index, len(lucky_tag.css('*'))))
      # print('\n', '\n')
      

      page_text_with_tags = ['start']
      page_text = ['start']            

      for index,tag in enumerate(lucky_tag.css('*')):
        # print(index, tag)
        if '<h1' in tag.get()[0:3]:
          first_h1_tag_index = index
          print(index)

      for index,tag in enumerate(lucky_tag.css('*')[first_h1_tag_index:]):
        # print(index, tag)

        if '<footer' in tag.get()[0:7]:
          break

        # if '<script' in tag.get():
          # print(index, tag.get())



        if '<script' not in tag.get() and '<style' not in tag.get() and '<option' not in tag.get():
          if tag.get() not in page_text_with_tags[-1]:
            # print('index:', index, '\n')
            # print('tag:', tag, '\n')
            # print('\n', 'tag code:', '\n', tag.get())
            # print('\n', 'tag text:', '\n', tag.css('::text').getall())
            # print('\n', 'joined text:', '\n', ''.join(tag.css('::text').getall()))
            # print('\n', '\n')

            # tag_text = ''
            # tag_text += ' '.join(tag.css('*::text').getall())
            # if tag.css('::text').get() is not None:
            #   tag_text += tag.css('::text').get()
            # print(tag_text)

            
            # if tag.css('::text').get() is not None:
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


            # if '<a' in tag.get():
            # joined_tag_text = ''.join(tag.css('::text').getall())

            # if '<a' in page_text_with_tags[-1]:
            #   page_text.append(''.join(tag.css('::text').getall()))
            # else:
            #   ## this one takes the text out of each tag
            #   page_text.append(tag.css('::text').getall())

      del(page_text_with_tags[0])
      del(page_text[0])

      ## page text is a list of lists
      # print(page_text)
      # print(len(page_text))


      joined_page_text = []

      for index,text_list in enumerate(page_text):
        # print('Tag index: ', index)
        # print('Number of text objects in tag: ', len(text_list))
        # print('Tag chunk: ', tag.get(), '\n', '\n')

        joined_page_text.append(''.join(text_list))

        # if '<a' in ''.join(tag):
          # print(index,tag)
        #   ## inner join of text within each text chunk
        #   if len(tag) <= 1:
        #     joined_page_text.append(''.join(tag))

        #   else:
        #     inner_text_join = '\n'.join(tag)
        #     joined_page_text.append(inner_text_join)

      ## outer join of text chunks
      joined_page_text = '\n'.join(joined_page_text)
      joined_page_text = joined_page_text.replace('"', "'")
      # print(joined_page_text)

      # print(page_text_with_tags)
      # print(len(page_text_with_tags))
      joined_html_code = ''.join(page_text_with_tags)
      joined_html_code = joined_html_code.replace('"', "'")


      soupy_text = soup(joined_html_code, 'html.parser')
      # print(soupy_text.prettify())

      return joined_page_text, soupy_text

  
  # the parse method is run on the response, and is a required method for the spider
    #this method will get repeated for all the relevant links on the page
  def parse(self, response):

    ## initialize the counter so that we only scrape for relevant pathways on the first go
    parse_count = self.parse_counter(response)
    print('SCRAPE COUNT: ', parse_count)

 
    # self.remaining_link_trigger(response)

    if parse_count == 1:    
  
      next_links = self.scrape_interesting_links(response)

      self.remaining_link_counter(response)
      
      # print(self.remaining_link_trigger(response, next_links))

      print(self.next_links)

      for index, link in enumerate(next_links):
          next_page = response.urljoin(link)
          yield scrapy.Request(next_page, callback=self.parse)

      # print(self.next_links)

      # yield scrapy.Request(next_page, callback=self.parse)




    
    if parse_count >= 2:

    #   link_dict = self.link_dict

      print('PAGE TITLE: ', response.css('title::text').get())
      print('PAGE URL: ', response.url)

      if len(response.css('title').re(r'.rivacy')) != 0:
        
        # #possible way to get the 'title' of the page
        # print(response.css('title::text').get().strip())

        ## maybe we find the body text of the policy by searching by div elements
          ## we can find the length of all the divs and try to pull from the longest one
          ## but there might be a div that wraps the whole page 

        joined_page_text = self.policy_scraper(response)[0]
        soupy_text = self.policy_scraper(response)[1]

        link_dict = self.link_dict

        link_dict['privacy'].update({
                                    'title': ''.join(response.css('h1 ::text').getall()).strip(),
                                    'url': response.url,
                                    'text': joined_page_text,
                                    'html': soupy_text.prettify()
                                    })
        self.link_dict = link_dict
        # print(self.link_dict.keys())
        # yield(self.link_dict)

        website_dict = self.website_dict


        # this is where we want to return the root url website and its corresponding link_dict values
        yield website_dict


      
      ## REPEAT ABOVE PROCESS FOR OTHER TYPES OF POLICIES

      if len(response.css('title').re(r'.erms')) != 0:

        joined_page_text = self.policy_scraper(response)[0]
        soupy_text = self.policy_scraper(response)[1]

        link_dict = self.link_dict

        link_dict['terms'].update({
                                    'title': ''.join(response.css('h1 ::text').getall()).strip(),
                                    'url': response.url,
                                    'text': joined_page_text,
                                    'html': soupy_text.prettify()
                                    })
        self.link_dict = link_dict
        # print(self.link_dict.keys())
        # yield(self.link_dict)

        website_dict = self.website_dict

        yield website_dict




      if len(response.css('title').re(r'.onditions')) != 0:

        joined_page_text = self.policy_scraper(response)[0]
        soupy_text = self.policy_scraper(response)[1]

        link_dict = self.link_dict

        link_dict['conditions'].update({
                                    'title': ''.join(response.css('h1 ::text').getall()).strip(),
                                    'url': response.url,
                                    'text': joined_page_text,
                                    'html': soupy_text.prettify()
                                    })
        self.link_dict = link_dict
        # print(self.link_dict.keys())
        # yield(self.link_dict)

    #   print(link_dict)

    # # if parse_counter == (index + 1):
    # #   yield 'website_dict': website_dict

        website_dict = self.website_dict

        yield website_dict
      
