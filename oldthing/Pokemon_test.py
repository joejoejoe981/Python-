from oldthing.Pokemon_scraper import PokemonScraper,PokemonscraperError
# scraper = PokemonScraper()
try:
    a = scraper = PokemonScraper()
    title = scraper.get_title()
    print(title)
    print('-----------------------------')
    image = scraper.get_image_url()
    print(image)
    print('-----------------------------')
    infocard = a.get_infocard()
    print(infocard)
    print('-----------------------------')
    small = a.get_small()
    print(small)


except PokemonscraperError as e:
    print(e)




