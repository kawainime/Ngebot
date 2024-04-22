import requests
from bs4 import BeautifulSoup
import cfscrape
from colorama import Fore, Style, init
from urllib.parse import urlparse
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk  # Import ThemedTk from ttkthemes
from tqdm import tqdm

init(autoreset=True)

fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA

log = """
   ______      __       _______ ____   ____  _       _____ 
  / __ \ \    / /\     |__   __/ __ \ / __ \| |     / ____|
 | |  | \ \  / /  \ ______| | | |  | | |  | | |    | (___  
 | |  | |\ \/ / /\ \______| | | |  | | |  | | |     \___ \ 
 | |__| | \  / ____ \     | | | |__| | |__| | |____ ____) |
  \____/   \/_/    \_\    |_|  \____/ \____/|______|_____/ 
                          OVA-TOOLS  https://t.me/ovacloud 
                          Mirror-h Scraper By OVA-TOOLS(GUI)                        
"""

print(log)

# Function to scrape websites from the specified page range of the archive
def scrapemova(first_page, last_page):
    scraper = cfscrape.create_scraper()
    domains = set()

    print(Fore.RED + "\t\t Scraping websites from page {} to Page {}...".format(first_page, last_page) + Style.RESET_ALL)

    for page in tqdm(range(first_page, last_page + 1), desc="Progress"):
        url = "https://mirror-h.org/archive/page/{}".format(page)
        response = scraper.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            rows = soup.select('tr')

            # Extract the website URLs from the HTML
            for row in rows[1:]:  # Skip the header row
                columns = row.select('td')
                if len(columns) >= 3:
                    web_url = columns[2].text.strip()
                    domain = urlparse(web_url).scheme + '://' + urlparse(web_url).netloc
                    domains.add(domain)
        else:
            print(Fore.RED + "\t\tFailed to scrape websites from page {} of the archive.".format(page) + Style.RESET_ALL)

    return domains

# Function to write websites to a file
def writeova(domains):
    with open('Results.txt', 'w') as file:
        for domain in domains:
            file.write(domain + '\n')

# Callback function for the "Scrape" button
def scrapeova():
    first_page = int(first_page_entry.get())
    last_page = int(last_page_entry.get())

    domains = scrapemova(first_page, last_page)

    if domains:
        writeova(domains)
        status_label.config(text="Domains saved to 'Results.txt'.", fg="green")
    else:
        status_label.config(text="No domains to process.", fg="red")

# Create the main window with a dark theme and non-resizable
root = ThemedTk(theme="equilux")  # Use the "equilux" theme (dark theme)
root.title("Mirror-h Scraper By OVA-TOOLS")
root.geometry("400x200")
root.resizable(False, False)  # Make the window non-resizable

# Label and entry for first page
first_page_label = Label(root, text="Enter the first page:")
first_page_label.pack()
first_page_entry = Entry(root)
first_page_entry.pack()

# Label and entry for last page
last_page_label = Label(root, text="Enter the last page:")
last_page_label.pack()
last_page_entry = Entry(root)
last_page_entry.pack()

# Scrape button
scrape_button = Button(root, text="Scrape", command=scrapeova)
scrape_button.pack()

# Status label
status_label = Label(root, text="", fg="green")
status_label.pack()

root.mainloop()
