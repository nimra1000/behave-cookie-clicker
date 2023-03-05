# behave-cookie-clicker

##  Description

 The Cookie Clicker game is simple in concept but highly addictive in gameplay. The goal of the game is to click on a cookie as many times as possible to accumulate points, which can be used to buy upgrades and automate the cookie-clicking process.

More information can be found below

[Original](https://orteil.dashnet.org/cookieclicker/)

[Wikipedia](https://en.wikipedia.org/wiki/Cookie_Clickern)

## Tech stack used

- [Python behave framework](https://behave.readthedocs.io/en/stable/)

- [Selenium](https://www.selenium.dev/)

## Dependencies

1. [Front-end UI app](https://seun-akinbode-2022-09-29.cookieclickertechtest.airelogic.com/)

2. [Back-end API](https://example.com)


##  Application environment preparation

1. Project Structure

   - The structure of the project consists of:
     - feature file: this has a natural language format describing a feature with examples and expected outcomes. It
       is found under the features folder.
     - steps file: this where the feature is actually implemented using Python. It is found under the steps folder


3. Installation

   [![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

   Clone the repo:

   - SSH:

    ```git clone git@github.com:nimra1000/behave-cookie-clicker.git```

   - HTTP:
    ```git clone https://github.com/nimra1000/behave-cookie-clicker.git```

   Then

   **Note:** It is highly recommended creating a Python Virtual Environment on your local machine before installing any
   dependencies

   ```cd behave-cookie-clicker```

   then run :

   ```pip3 install -r requirements.txt```

   Then

   Download the appropriate Firefox webdriver named Geckodriver
   from [github](https://github.com/mozilla/geckodriver/releases).

   Save the extracted .exe file to usr/local/bin and specify location in $PATH

   If you have a Windows machine, save it in your home folder. If not recognised then
   it is recommended to save it in a directory that is included in your system's PATH environment variable.
   Or add the location of the geckodriver executable to your system's PATH environment variable.

   Please ensure you have the actual Firefox web application installed on your device.
   Otherwise the firefox geckodriver will not be able to run.

   ```geckodriver --version``` should confirm the installation by responding with a version number.

### TODO: Setup pre-commit hooks

We use pre-commit hooks to ensure formatting and code standards. Please ensure you're correctly set up ...

  If there are issues with the pre-commit hooks running, then do the following:

  Install pre-commit. The official instructions are here https://pre-commit.com/.

 ```pre-commit install```

##  Run automated tests

1. Run scripts for all types of file or selected types

   You keep or remove the tag(s):

 ```behave --tags=@one```

 ```behave --tags=@cookie --no-skipped```

 ```behave -t=@factory```


1. Run scripts for a specific environment or browser (other than the default)

   Setting config data

   Change default browser temporarily for this test run

   ```behave -D browser=firefox --tags=@one```


2. Start debugging automatically on failure

   ```behave -D debug --tags=@cookie```

3. Run tests that generate reports

   We are using [Allure](https://docs.qameta.io/allure/#_behave).

   - To run the tests and store results in directory called `allure_results` as json data:
   
   ```behave -f allure_behave.formatter:AllureFormatter -o allure_results ./features```

- To serve the report as HTML file:

  ```allure serve allure_results```
  The report should open in a new browser tab
