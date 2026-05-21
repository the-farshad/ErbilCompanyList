"""Scrape the public company directory of the Erbil Chamber of Commerce and
Industry (erbilchamber.org) into a CSV file."""

import csv
import urllib.parse

import bs4
import requests

# Detail pages are linked relative to this host.
BASE_URL = "https://www.erbilchamber.org"
# Paginated listing of companies (20 per page).
LISTING_URL = "http://erbilchamber.org/en/companies.html?start={start}"
OUTPUT_FILE = "ErbilChamber.csv"
COLUMNS = [
    "ManagingDirector",
    "CompanyActivity",
    "RegistrationNumber",
    "DateOfRegistration",
    "MobileNumber",
    "Address",
    "NameOfShareholders",
]


def scrape():
    session = requests.Session()
    with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(COLUMNS)
        start = 0
        try:
            for start in range(0, 8620, 20):
                page = session.get(LISTING_URL.format(start=start))
                soup = bs4.BeautifulSoup(page.content, "lxml")
                for link in soup.find_all("h3", class_="catItemTitle"):
                    company_url = BASE_URL + urllib.parse.quote(link.a["href"])
                    company_page = session.get(company_url)
                    company_soup = bs4.BeautifulSoup(company_page.content, "lxml")
                    row = [""] * len(COLUMNS)
                    fields = company_soup.find_all(
                        "span", class_="itemExtraFieldsValue"
                    )
                    for i, field in enumerate(fields):
                        if i < len(row):
                            row[i] = field.text
                    writer.writerow(row)
        except Exception as error:
            # Print the offset reached so the run can be resumed from here.
            print(f"Stopped at start={start}: {error}")


if __name__ == "__main__":
    scrape()
