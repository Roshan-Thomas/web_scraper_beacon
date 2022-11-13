from autoscraper import AutoScraper
import json


def pop_duplicate_keys(grouped_list, approved_keys):
    count = 0
    for key in list(grouped_list.keys()):
        if (count < len(grouped_list)):
            if (count not in approved_keys):
                grouped_list.pop(key)
        else:
            break
        count = count + 1
    
    return list(grouped_list.keys())

url_mdlbeast = "https://aravia.mdlbeast.com/en"
categories_mdlbeast = ["DAVID GUETTA", "SHEIQ"]

url_virgin = "https://tickets.virginmegastore.me/qa"
categories_virgin = ["BLACK EYED PEAS - LIVE IN CONCERT", "Doha Golf Club", "20 Nov"]

url_tixbox = "https://www.tixbox.com/en/?gclid=CjwKCAiA9qKbBhAzEiwAS4yeDUuTx-Wo7dMiqOgejPkxueiflZb_E0fNr299dA2_6TKoswvoRqTRXBoCMdUQAvD_BwE"
categories_tikbox = ["Black Eyed Peas - Live in Concert", "20 Nov 2022", "DOHA GOLF CLUB - DOHA"]

scraper = AutoScraper()

result_mdlbeast = scraper.build(url_mdlbeast, categories_mdlbeast)

# Scrapping for Virgin Tickets

build_virgin = scraper.build(url_virgin, categories_virgin)
grouped_virgin = scraper.get_result_similar(url_virgin, grouped=True)
virgin_duplicates_removed_list = pop_duplicate_keys(grouped_virgin, approved_keys=[0, 5, 8])

scraper.set_rule_aliases({f'{virgin_duplicates_removed_list[0]}': 'concertName', f'{virgin_duplicates_removed_list[1]}': 'locations', f'{virgin_duplicates_removed_list[3]}': 'date'})
scraper.keep_rules(virgin_duplicates_removed_list)
grouped_virgin = scraper.get_result_similar(url_virgin, grouped=True)
result_virgin = scraper.get_result_similar(url_virgin, group_by_alias=True)
result_virgin_json = json.dumps(result_virgin)

# Write to JSON file - Virgin Tickets
with open("virgin_tickets_dump.json", "w") as outfile:
    outfile.write(result_virgin_json)


# Scrapping for Tikbox 

build_tikbox = scraper.build(url_tixbox, categories_tikbox)
grouped_tikbox = scraper.get_result_similar(url_tixbox, grouped=True)
tikbox_duplicates_removed_list = pop_duplicate_keys(grouped_tikbox, approved_keys=[0, 4, 5])

scraper.set_rule_aliases({f'{tikbox_duplicates_removed_list[0]}': 'concertName', f'{tikbox_duplicates_removed_list[1]}': 'date', f'{tikbox_duplicates_removed_list[2]}': 'locations'})
scraper.keep_rules(tikbox_duplicates_removed_list)
result_tikbox = scraper.get_result_similar(url_tixbox, group_by_alias=True)
result_tikbox_json = json.dumps(result_tikbox)

# Write to JSON file - Tikbox
with open("tikbox_dump.json", "w") as outfile:
    outfile.write(result_tikbox_json)





