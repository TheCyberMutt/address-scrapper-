" # address-scrapper-" 

///////Before scraping anything, READ the Terms & Condition page at the bottom of the website to make sure that you are NOT breaking any restrictions placed by web page owner. This is for educational and learning purposes////////////

Taking "https://stores.footlocker.com" as an example base URL, we find that each store has its own webpage. 

To get a file of all the urls we run the linux commands;

$wget -r https://stores.footlocker.com | grep --only-matching 'stores.footlocker.com/us/*' | sort --unique > url_store_list.txt

INSPECT a store webpage and take  note of the HTML tags associated with the address you want to scrape. The tags used in "scrape.py" are the tags of the address, zipcode and phone number. This is probably going to be different for another company store page. 


The lists "address","phone_number" and "zipcode" start as empty sets.

The function get_the_address() takes parameter "url" from "url_store_list.txt", parsers the data and appends it to lists "address", "phone_number" and "zipcode" with related information. 

You can use this on companies that have multiple stores and dedicate a webpage for each store. 










