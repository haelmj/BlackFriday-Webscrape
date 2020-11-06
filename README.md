# BlackFriday-Webscrape

A web scraper that gathers cheapest black friday deals per category on multiple e-commerce sites

## Requirements

This project requires version 86.0.4240 of Chrome browser as well as Python 3 installed on the host system.

**Python Dependencies**

- [Selenium](https://pypi.org/project/selenium/)

**WebDriver**

- [Chrome WebDriver](https://chromedriver.chromium.org/)
*Note:* A chrome webdriver for version 86 can be found in the assets folder of this project

### Setup

1. Clone this project to your local system:
`git clone https://github.com/haelmj/BlackFriday-Webscrape.git`

2. Setup Chrome driver:
    - Copy the chromedriver from the assets folder

3. Setup a virtual environment:

```
python -m venv venv
```

4. Activate the virtual environment:
For Windows Command Line Users:

```
venv\Scripts\activate.bat
```

For bash users:

```
source /venv/Scripts/activate
```

5. Install module dependencies:
`pip install selenium`

6. Run app:

```
python main.py
```

## Development Status

- **In progress**
