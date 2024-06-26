# run this file from the command line
# use --in or -i to specify input file of URLs to scrape (REQUIRED)
# use --out or -o to specify directory to output articles to (Optional, Default: ./Data/processed)

from module_1.scraper import CNNScraper
from module_2.fileIO import FileIO
from module_3.summarizer import GeminiSummarizer
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", "-i", dest="file_in", type=str, help="Path to file with a url on each line to scrape and output to file.", required=True)
    parser.add_argument("--out", "-o", dest="file_out", default="Data/processed", type=str, help="Directory to save scraped articles in.", required=False) # Defaults to the project defined output location
    parser.add_argument("--ai-out", "-O", dest="ai_out", default="Data/summaries", type=str, help="Directory to save summaries of scraped articles in.", required=False)
    args = parser.parse_args()

    try:
        gemini_api_key = os.environ["GEMINI_API_KEY"]
        summarizer = GeminiSummarizer(gemini_api_key)
    except:
        summarizer = None

    try:
        input_file = FileIO(args.file_in)
    except:
        print("File not found, please check your file name.")
    urls = input_file.get_line_list()
    for url in urls:
        try:
            scraper = CNNScraper(url) #This uses the CNN scraper. You can implement the Scraper interface with another class and change just this line for another news site
        except:
            print(f'{url} is not a valid CNN url.')
            continue #skip saving this article if it is invalid
        
        title = scraper.get_title()
        article = scraper.get_article()
        filename = args.file_out + "/" + title.replace(" ", "_") + ".txt"
        summary_filename = args.ai_out + "/" + title.replace(" ", "_") + ".txt"
        if not title or not article: # skips saving if article or title are empty
            print(f'Something went wrong while scraping {url}')
            continue
        output_file = FileIO(filename)
        output_file.write_data(article)
        if summarizer is None:
            continue
        try:
            summary = summarizer.summarize(article)
        except:
            summary = "There was an issue calling summarize() with the summarizer. Please confirm the summarizer was imported or that your api key is correct".
        summary_output_file = FileIO(summary_filename)
        summary_output_file.write_data(summary)

if __name__=="__main__":
    main()