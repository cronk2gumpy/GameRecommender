from googlesearch import search

def searcher(game):
    term = game + " how long to beat"
    results = search(term, stop=1)
    for url in results:
        return url


def find_game(game):
    url = searcher(game)
    if url.startswith("https://howlongtobeat.com/"):
        return url
    else:
        return None