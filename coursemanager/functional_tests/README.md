# Functional Tests

## Overview

The functional tests have been written using Selenium.

To speed the development of the tests the Katalon Recorder plugin has been used within the Chrome 
browser to record the Selenium code which is then exported to Python.

Some manual massaging of the code is necessary to make it work, there seems to be case-sensitivity
differences between how the recorder UI handles tag text and the generated source text.

## Setup 

* To use selenium the appropriate web driver needs to be downloaded.  The current tests use Chrome:
(https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Running the tests

From within the coursemanager directory:

``` bash
python manage.py test -v 2
```