# USW SoSe 2025
Code for lecture USW 2025

## Prerequisites

Every folder contains exercises related to the PCÜ sessions throughout the semester.
Create a venv by running `python -m venv venv`, activate (`source venv/bin/activate` on WSL/Linux) 
and install all requirements for the exercises (`pip install -r requirements.txt`).

Activate the virtual environment on Windows with PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```
or on Windows with Command Prompt:
```cmd
.\venv\Scripts\activate.bat
```

Every exercise that uses Jupyter Notebooks requires the Jupyter server to run locally.
Start the server with the following command:
```bash
jupyter notebook
```

## PCÜ 1: SPAM Detection

In this first exercise, we develop a supervised machine learning model for spam detection, based on the following dataset:
[SMS SPAM Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection).

This excercise will be carried out with [Jupyter Notebooks](https://docs.jupyter.org/en/latest/install/notebook-classic.html).

## PCÜ 2: News and Web Crawling

This exercise uses the scrapy framework. Find more information about the
architecture of the framework [here](https://docs.scrapy.org/en/latest/topics/architecture.html).

Also, in this tutorial we cover [website rendering with JavaScript](https://docs.scrapy.org/en/latest/topics/dynamic-content.html#pre-rendering-javascript).

Javascript rendering requires to install a headless browser.
Therefore
- Run `pip install -r requirements.txt` again
- Install headless chromium using `playwright install chromium`


Once the installation is finished, you are ready to run the code.

1. Go into the directory `02_web_and_news_scraping/scrapy_tutorial`
2. Run `scrapy crawl htw_berlin` in the command prompt/bash
