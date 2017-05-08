[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com) [![forthebadge](http://forthebadge.com/images/badges/contains-cat-gifs.svg)](http://forthebadge.com)  

# Python Facebook Bot
*Make your life easier*  

### What is this?
----------------
  This is a Facebook Bot/Assistant, writen in Python 3 and using Facebook API for some
  specific tasks.  
  At the moment, I only implement it some functions to crawl/get Facebook's events by
  location, since Facebook shutdown that APIs.  

### What do I need? (requirements.txt)
------------------
  Right now, I'm only using [requests](https://github.com/kennethreitz/requests) for requesting APIs.  

### Installation
---------------
  To install **python-facebook-bot**, simply:  

  ```
  $ pip install python-facebook-bot
  ```  
### How to use?
---------------
  First, you need to create a Facebook App for Developer.  
  Then, run `export` command for CLIENT_ID and CLIENT_SECRET.  
  Example:  

  ```
  $ export CLIENT_ID="Your facebook app's ID"
  $ export CLIENT_SECRET="Your facebook app's secret key"
  ```  

  Then you can `import facebook_bot` and use it's methods.  
  Example with IPython:  

  ```python
  Python 3.5.2 (default, Nov 17 2016, 17:05:23)
  Type 'copyright', 'credits' or 'license' for more information
  IPython 6.0.0 -- An enhanced Interactive Python. Type '?' for help.

  In [1]: import facebook_bot

  In [2]: facebook_bot.get_events(1572248819704068)
  Out[2]:
  {'1572248819704068': {'events': {'data': [{'attending_count': 35,
       'category': 'FAMILY_EVENT',
       'cover': {'id': '1667937513468531',
        'source': 'https://scontent.xx.fbcdn.net/v/t31.0-0/p180x540/12898397_1667937513468531_267697016695005514_o.jpg?oh=1ea3755b790a6837febf9621a3b23f6f&oe=597E6E0D'},
       'declined_count': 0,
       'description': "2020 is just a few years away. Will you join the World for this epic New Years' celebration? I know that you will. I look forward to celebrating with you. \n\nThis is a virtual event and the whole planet is invited.",
       'id': '447828138744610',
       'maybe_count': 119,
       'name': 'Happy New Year 2020',
       'noreply_count': 43,
  ...........
  In [3]:
  ```

### Where are the tests?
-----------------------
  Just run `$ python setup.py test`  
  It's may take a while, because we need to scan all available pages.

*And here is your Cat*  
[](http://media3.giphy.com/media/1341dJuJNgSDgk/giphy.gif)
