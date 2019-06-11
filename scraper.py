from bs4 import BeautifulSoup
import requests


def get_times(html_soup):
    body = html_soup.find_all("div", class_="in scrollable shadow_box back_primary")
    times = body[0].find_all('tbody', class_='spreadsheet')
    heads = ["Main Story", "Main + Extras", "Completionist"]
    out = {}

    for i in range(len(heads)):
        key, val = heads[i], times[i]
        val = (val.find_all('td')[2]).text
        out[key] = val.strip()

    return out


def data_extractor(url):
    response = requests.get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    title = html_soup.select('div.profile_header')[0].text
    times = get_times(html_soup)

    try:
        developer = html_soup.find_all('strong', string='\nDeveloper:\n')[0].next_sibling
    except:
        developer = 'N/A'

    try:
        publisher = html_soup.find_all('strong', string='\nPublisher:\n')[0].next_sibling
    except:
        publisher = 'N/A'

    try:
        platform = html_soup.find_all('strong', string='\nPlayable On:\n')[0].next_sibling
    except:
        platform = 'N/A'

    try:
        genres = html_soup.find_all('strong', string='\nGenres:\n')[0].next_sibling
    except:
        genres = 'N/A'

    try:
        year = html_soup.find_all('strong', string='JP:')[0].next_sibling
        year = year.strip()[-4:]
    except:
        try:
            year = html_soup.find_all('strong', string='NA:')[0].next_sibling
            year = year.strip()[-4:]
        except:
            year = 'N/A'


    out = {'Title': title.strip(),
           'Year': year,
           'Times': times,
           'Developer': developer.strip(),
           'Publisher': publisher.strip(),
           'Platform': platform.strip().split(", "),
           'Genres': genres.strip().split(", ")}

    return out


def add_to_csv(filename, d):
    with open(filename, 'a') as f:
        out = []
        out.append(d['Title'])
        out.append(d['Year'])
        for k, v in d['Times'].items():
            out.append(v)

        out.append(d['Developer'])
        out.append(d['Publisher'])

        platforms = []
        for item in d['Platform']:
            platforms.append(item)
        out.append( "/".join(platforms))

        genres = []
        for item in d['Genres']:
            genres.append(item)
        out.append("/".join(genres))

        f.write(", ".join(out) + "\n")


def print_game(d):
    print("")
    print(d['Title'], end=", ")
    print(d['Year'])
    for k,v in d['Times'].items():
        print(f"{k}: {v}")
    print("")

    print(f"Developer: {d['Developer']}")
    print(f"Publisher: {d['Publisher']}")

    print("Platform: ", end="")
    for item in d['Platform'][:-1]:
        print(item, end=", ")
    print(d['Platform'][-1])

    print("Genres: ", end="")
    for item in d['Genres'][:-1]:
        print(item, end=", ")
    print(d['Genres'][-1])

    print("\n----------")