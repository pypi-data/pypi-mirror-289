# WhatsApp Library

A Python library to interact with WhatsApp Web using Selenium.
Created by Fioruci, used mainly by VJ Bots.

## Installation

Install the required packages using pip:

```bash
pip install selenium
```

## Usage Example
```python
from vjwhats import WhatsApp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path

def main():
    # Configures of the current folder of Chrome/User Data and the desired profile directory
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=C:/Users/EXAMPLE/AppData/Local/Google/Chrome/User Data")
    chrome_options.add_argument("profile-directory=Default")  # It should be the same user as the connected to the WhatsApp Web

    # Creating the WebDriver with Options
    driver = webdriver.Chrome(options=chrome_options)

    # Creating WhatsApp Instance
    wpp = WhatsApp(driver)

    # Sending a message to Contact 1
    wpp.find_by_username("Contact 1")
    wpp.send_message("Hello, this is a test message!")

    # Sending a file to Contact 2
    wpp.find_by_username("Contact 2")
    wpp.send_file(Path("path/to/file"), which=1)

    # Sending a file to a new Conversation
    wpp.start_conversation("+55999977885")
    wpp.send_file(Path("path/to/file"), which=1)

if __name__ == "__main__":
    main()
```

## Licence
This project is licensed under the MIT License - see the LICENSE file for details.
