# CS325 Project 1: Web Scraper
This is a simple web scraper written in Python using PyQuery and requests. The scraper module has functions built in for scraping CNN articles but has functions that accept jQuery selectors that could be used for other sites.

## Usage
Clone and change directory to the repository by running the following commands

    $ git clone https://github.com/loglug1/cs325-scraper.git
    $ cd cs325-scraper

Verify you have the conda command by running

    $ conda --version

If you get an error please visit https://docs.anaconda.com/free/miniconda/miniconda-install/ for instructions on installing miniconda.

Import conda environment from requirements.yml using the following command

    $ conda env create -f requirements.yml
    $ conda activate scraper

This project utilizes Google Gemini for writing summaries. Please create an API key by following these steps:
1. Go to https://aistudio.google.com/app/apikey.
2. Sign in with your Google Account.
3. Accept the terms of service if prompted.
4. Click 'Create API Key' and then 'Create API key in new project' (If you do not have this option, use the Google Cloud search to add the key to an existing project)
5. Copy the API key to your clipboard.
6. Create a file called `.env` in the root directory of this project containing the following (make sure to replace placeholder):

```
GEMINI_API_KEY=<YOUR API KEY>
```

Run the program:

    $ python main.py --in url.in --out output

This example will scrape articles from each site listed in the file `url.in` and export them to txt files inside the `output` directory.