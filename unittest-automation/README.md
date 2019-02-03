Unittesting with selenium
===================


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
$ git clone https://github.com/carogomezt/automation-with-selenium.git
```
 - Move to the `automation-with-selenium/fb-post-automation` folder
``` shell
$ cd automation-with-selenium/fb-post-automation
```
 - Download [geckodriver](https://github.com/mozilla/geckodriver/releases) and put the route of the executable into the PATH. 
``` shell
$ export PATH=$PATH:/path/to/gechodriver
```

Configure the script and enjoy!
----------

Run the script
``` shell
$ python3 -m unittest -v unittest_automation_script.py
```