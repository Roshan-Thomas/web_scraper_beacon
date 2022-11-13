from autoscraper import AutoScraper


def pop_duplicate_keys(grouped_list, approved_keys):
    count = 1
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

result_virgin = scraper.build(url_virgin, categories_virgin)
grouped_virgin = scraper.get_result_similar(url_virgin, grouped=True)
virgin_duplicates_removed_list = pop_duplicate_keys(grouped_virgin, approved_keys=[1, 5, 8])

scraper.set_rule_aliases({f'{virgin_duplicates_removed_list[0]}': 'concertName', f'{virgin_duplicates_removed_list[1]}': 'locations', f'{virgin_duplicates_removed_list[2]}': 'date'})
scraper.keep_rules(virgin_duplicates_removed_list)
grouped_virgin = scraper.get_result_similar(url_virgin, grouped=True)
print(grouped_virgin)

# final = []
# result_virgin = [final.append(virgin_duplicates_removed_list[i]) for i in range(len(virgin_duplicates_removed_list))]

# print(final)

result_tikbox = scraper.build(url_tixbox, categories_tikbox)

# print(type(result_mdlbeast))



