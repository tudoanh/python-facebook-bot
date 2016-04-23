# Introduce
My script to crawl all events of a city on Facebook.  
Not a Scrapy project, but still work like miracle :D  
Still have to change and update a lot of codes.  


# How to use
In *config.json*:  
**client_id** & **client_secret** : Your app ID and Secret code 
**lat** & **long**: Lat and Long of location you want to crawl  
**distance** : In metter  
**keyword** : if you want to crawl with specific keyword, just fill here  
**limit** : limit the results  

In *events_fb.py*:
**CIRCLE** : A tuple contain lat and long of city your want to scan, and distance as your desire
