Selenium Grid
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
 - Move to the `automation-with-selenium/selenium-grid` folder
``` shell
$ cd automation-with-selenium/selenium-grid
```
 - Download [geckodriver](https://github.com/mozilla/geckodriver/releases) and put the route of the executable into the PATH. 
``` shell
$ export PATH=$PATH:/path/to/gechodriver
```
 - Download [Selenium Standalone Server](https://docs.seleniumhq.org/download/) 

 - Install [Java](https://java.com/en/download/help/linux_x64_install.xml)

Configure the script and enjoy!
----------

 - Start Grid Hub:
``` shell
$ java -jar selenium-server-standalone-<your-version>.jar -role hub
```
 - Configure Grid Nodes
``` shell
$ java -jar selenium-server-standalone-<your-version>.jar -host localhost -port 5555 -role node -hub http://localhost:4444/grid/register -browser browserName=firefox,platform=LINUX,maxInstances=5 -browser browserName=chrome,platform=LINUX,maxInstances=5
```
If you want more than one node in the same machine, just run the command again with some other port that is not use.

Go to your browser and type “http://localhost:4444/grid/console” to see Selenium Grid console up and running.

 - Configure the driver to connect remotely on your script
``` python 
desired_caps = {}
desired_caps['platform'] = self.PLATFORM
desired_caps['browserName'] = self.BROWSER
self.driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=desired_caps)
 ```

Run the script passing arguments platform and browser
``` shell
$ python3 -W ignore node_script.py LINUX chrome
```

More info [Selenium wiki](https://github.com/SeleniumHQ/selenium/wiki/Grid2)