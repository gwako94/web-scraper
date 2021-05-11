import requests
import csv
from bs4 import BeautifulSoup

page_url = "https://www.inclusivebusiness.net/intermediary/search"

page = requests.get(page_url)

soup = BeautifulSoup(page.content, 'html.parser')

org_infos  = soup.find_all('div', {"class" : "views-row"})


organisation_list = []

for org_info in org_infos:
    org_name = org_info.find('div', class_="views-field-field-title")
    org_type = org_info.find('div', class_="views-field-field-type-of-organisation")
    org_region = org_info.find('div', class_="views-field-field-region")

    if None in (org_name, org_type, org_region):
        continue

    name = org_name.text.strip()
    type_of_organisation = org_type.find('span', class_="field-content").text.strip()
    region = org_region.find('span', class_="field-content").text.strip()

    try:
        org_finance = org_info.find('div', class_="views-field-field-financial-offering")
        finance_offering = org_finance.find('span', class_="field-content").text.strip()
    except AttributeError:
        finance_offering = ""

    try:
        org_amount = org_info.find('div', class_="views-field-field-amount-of-financial-suppor")
        amount = org_amount.find('span', class_="field-content").text.strip()
    except AttributeError:
        amount = ""

    try:
        org_sector = org_info.find('div', class_="views-field-field-sector")
        sector = org_sector.find('span', class_="field-content").text.strip()
    except AttributeError:
        sector = ""

    try:
        org_focus_type = org_info.find('div', class_="views-field-field-type-organ-focus")
        focus_type = org_focus_type.find('span', class_="field-content").text.strip()
    except AttributeError:
        focus_type = ""

    try:
        org_focus_stage = org_info.find('div', class_="views-field-field-stage-of-organizational-fo")
        focus_stage = org_focus_stage.find('span', class_="field-content").text.strip()
    except AttributeError:
        focus_stage = ""

    rows = [name, type_of_organisation, region, finance_offering, amount, sector, focus_type, focus_stage]

    organisation_list.append(rows)


with open ('organisation.csv','w') as file:
   writer=csv.writer(file)
   for row in organisation_list:
      writer.writerow(row)