Selenium Facebook Group Poster
===================
**A Selenium Script to post text on the Facebook Groups you are member.**

Setup
----------

 - Verify you have Python 3.6.X installed
``` shell
$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more informatio
```
 - Install pip
``` shell
$ sudo apt install python3-pip
```
 - Install [Python bindings for Selenium](https://pypi.python.org/pypi/selenium)
``` shell
$ pip3 install selenium
```
 - Clone this repo
``` shell
$ git clone https://github.com/carogomezt/automatization-with-selenium.git
```
 - Move to the `automatization-with-selenium/fb-post-automatization` folder
``` shell
$ cd automatization-with-selenium/fb-post-automatization
```
 - Download [geckodriver](https://github.com/mozilla/geckodriver/releases) and put the route of the executable into the PATH. 
``` shell
$ export PATH=$PATH:/path/to/gechodriver
```

Configure the script and enjoy!
----------

You need to pass your Facebook user and password as environments variables:
``` shell
$ export FB_USR="username@gmail.com"
$ export FB_PWD="password"
```

There is a method in the script you need to edit with the message you want to post and the links of the Facebook Groups you are member of:
``` shell 
if __name__ == '__main__':
    messagge = 'This is a message to post in a group'
    group_links = ['https://www.facebook.com/groups/pythonco/']
    post_fb_group(messagge, group_links)
 ```

 Run the script
``` shell
$ python3 facebook_group_script.py
```