# ps5-smyths-bot
  a selenium-python made ps5 smyths bot - this bot doesnt automatically type in your credit card info and purchase the whole thing for you, it only keeps refreshing until its avaliable and when its avaliable, it adds to cart and takes you to checkout, you have to input your details when making a purchase into the website.

# credits
  - https://github.com/azaini101
    He made the original bot for walmart in the US, i used it to convert it for the UK

# requirements
  - python 3.6 or higher; Install latest at https://www.python.org/downloads/
  - latest google chrome version (version 88.0+) - check your chrome version chrome://settings/help and update to latest if needed. - If you dont already have google chrome installed, install at https://www.google.com/intl/en_uk/chrome/
  - latest chrome driver for chrome version 88; this can be installed at https://chromedriver.chromium.org/downloads
  - any sort of unzipping program, i'd recommend winrar since its free and easy to use
  -- If you dont meet any single one of these requirements, the program will NOT work
  
# required modules
  - Selenium - installable by typing 'pip install selenium' into the command prompt. Make sure you install everything above, in the requirements.
  -- If you dont install selenium, the program will NOT work
  
# instructions
  1. Install the included, zipped, python program - install automatically by clicking https://github.com/MMZaini/ps5-smyths-bot/archive/main.zip - it should be in your downloads folder, you can drag it over to your desktop or anywhere else if you'd like.
  2. Locate and unzip 'ps5-smyths-bot-main.zip' using winrar by right clicking the zip and selecting 'Extract Here'
  3. Open the new folder that can be found in the same directory that you have the zip in when unzipping.
  4. You can now delete the zip since its no longer needed but make sure you keep the folder.
  5. Open the folder and move the chromedriver you installed to that folder. Then double click the chromedriver and you'll see a little command prompt looking window come up. It'll say something like Starting ChromeDriver, Only local connections are allowed and ChromeDriver was started successfully. If you see somehting like this on the window you've comleted the hard part.
  6. Minimise the chromedriver into your taskbar and double click the 'ps5.py' file that can be found. It'll then bring up another command prompt looking window which should say something like 'DevTools listening'. Then It'll open chrome and depending on the performance (speed) of your computer, it'll refresh the page constantly until the ps5 is avaliable for to be added to cart and purchasesd, when it is avaliable, it will add to cart and take you straight to the checkout page and make a beep sound to alert you to the availbility of the item. Then you'd just checkout normally.
  
# Things to keep in mind
  - Smyths requires you to either login or create an account to make a purchase, so when you first open the program, i'd recommend opening a new tab inn the same window, typing in "smyths create account" or "smyths login" if you already have an account and login/create an account, make sure when doing this you select 'save password' or 'autosave details'. This is much quicker than having to login everytime you want to purchase an item, especially when the item is in high demand like the ps5 because it may become sold out before you're able to check out. 
  
# Customisability
  -- Keep in mind, if you want to customise or change the code and use it your self, make sure to read the license before doing anything --
  
  - You can really easily change the item you want to bot, here are some instructions on how to do it. (you only need common sense for this and make sure you read the license before distrubuting it or passing it off as your own!)
  
    1. Open the included ps5.py program in your prefered code editor, such as VScode, Sublime Text, ect.
    2. Find the 'item' variable, it's on line 6 from the top. Change the link inside the apostrophes (the '') to the link of the item you want to bot!
