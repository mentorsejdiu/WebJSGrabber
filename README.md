# WebJSGrabber
Python script that allows you to extract all JavaScript files from a given website. It takes a website URL as input and scrapes the HTML content to identify JavaScript files linked in the source code. It then downloads these JavaScript files and saves them locally for further analysis or inspection.

Features:
Extracts all JavaScript files linked in the HTML source of a website.
Downloads and saves JavaScript files locally.
Easy-to-use command-line interface.

Usage:

python jsgrabber.py <website_url>

Replace <website_url> with the URL of the website you want to extract JavaScript files from.

Dependencies:
Python 3.x
requests library
BeautifulSoup library

Installation:

Clone the repository:
  git clone https://github.com/Mentorsejdiu/WebJSGrabber.git

WebJSGrabber is a valuable tool for bug hunters and penetration testers aiming to review the JavaScript code of a target website for potential vulnerabilities or security issues. By extracting all JavaScript files linked within the HTML source of a website, WebJSGrabber enables security professionals to analyze the client-side codebase thoroughly.
