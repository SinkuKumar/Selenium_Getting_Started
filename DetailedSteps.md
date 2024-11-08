# Selenium Web Driver Setup with Chrome Browser without using Selenium Driver Manager - Detailed Steps

## Pre-requisites

### Download and install:
1. Python
2. Chrome Browser
3. Git
4. VS Code

### Setup:
1. Install python extensions in VS Code
2. Create a virtual environment in VS Code `python -m venv venv`
3. Activate the virtual environment `venv\Scripts\activate`
4. Install selenium `pip install selenium`

## Let's setup the latest version of Selenium Web Driver with Chrome Browser with using Selenium Driver Manager

1. Goto: https://selenium-python.readthedocs.io/getting-started.html and copy the latest code for setting up the selenium.
2. Create a new python file in VS Code and paste the copied code.
3. Modify the code to use the Chrome Browser instead of default Firefox Browser. `driver = webdriver.Chrome()`
4. Run the code and check if the browser opens up.

#### Comments:
- The above steps are for setting up the latest version of Selenium Web Driver with Chrome Browser without using Selenium Driver Manager.
- It is recommended to use Selenium Driver Manager for setting up the Selenium Web Driver with Chrome Browser.

**Commit:** `Default working code`

## Let's setup the latest version of Selenium Web Driver with Chrome Browser without using Selenium Driver Manager

### Pre-requisites:
1. Goto: https://developer.chrome.com/docs/chromedriver/downloads
2. Check installed Chrome Browser version: `chrome://version/` in browser address bar.
3. Download the Chrome Driver version compatible with the Chrome Browser version.
    - Visit: `https://googlechromelabs.github.io/chrome-for-testing/#stable`
    - Download the Chrome Driver version compatible with the Chrome Browser version, OS and architecture.
    - I'm going with: `https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.116/win64/chromedriver-win64.zip`
    - Extract the downloaded zip file.
    - Copy the chromedriver.exe file to the project folder.
    - Add the chromedriver.exe path to the system environment variable PATH (optional, but recommended).
    - Check if the chromedriver is working by running the command `chromedriver --version` in the command prompt.
4. Search for the way to link the latest chrome driver with the python code.
    - Use the given code to link the chrome driver with the python code in `without_webdriver_manager_selenium.py` file.

**Commit:** `without selenium driver manager`

## Let's setup the profile for Chrome Browser to make sure it's aligned with the project requirements

1. To use the profile in the Chrome Browser.
    - Open the Chrome Browser and visit: `chrome://version/`
    - Copy the Profile Path.
    - Update the chrome options for user-date-dir `chrome_options.add_argument(r"--user-data-dir=C:\Users\Sinku\AppData\Local\Google\Chrome\User Data")`
    - Update the chrome options for profile-directory `chrome_options.add_argument(r"--profile-directory=Profile 2")`
    - See `with_profile_selenium.py` file for the code.

**Commit:** `with profile`