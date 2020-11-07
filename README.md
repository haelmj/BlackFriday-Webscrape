# BlackFriday-Webscrape

A web scraper that gathers cheapest black friday deals per category on multiple e-commerce sites

**Estimated Scrape Time**: *15 minutes*

## Requirements

This project requires preferably version 86.0.4240 of Chrome browser as well as Python 3 installed on the host system.

**Python Dependencies**

- [Selenium](https://pypi.org/project/selenium/)

**WebDriver**

- [Chrome WebDriver](https://chromedriver.chromium.org/)  
*Note:* A chrome webdriver for version 86 can be found in the assets folder of this project. If you have a different version of Chrome, download the chrome webdriver for that version and replace it with the one in the assets folder.

### Setup

1. Clone this project to your local system:
`git clone https://github.com/haelmj/BlackFriday-Webscrape.git`

2. Setup Chrome Driver:

    - Include the ChromeDriver location in your PATH environment variable

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

- **Completed**
