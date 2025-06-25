from bs4 import BeautifulSoup
import requests

def get_soup():
    headers: dict= {
        'User-Agent': ""} #search user agent in browser and paste it here
    request = requests.get('https://www.bbc.com/news', headers=headers)
    html: bytes= request.content

    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_headlines(soup):
    headlines: set = set()
    for h in soup.find_all('h2', attrs={"data-testid": "card-headline"}):
        headline: str = h.contents[0].lower()
        headlines.add(headline)
    return sorted(headlines)

def check_match(word, headlines):
    headline_words: dict = {}
    match_news: list = []
    final_list: list = []
    for i, headline in enumerate(headlines, start=1):
        i = str(i)
        headline_words[i] = headline.split()
    for i in headline_words:
        if word in headline_words[i]:
            match_news.append(headline_words[i])
    for i in match_news:
        final_list.append(" ".join(i))
    for no, word in enumerate(final_list, start=1):
        print(no, word, sep=': ')

def main():
    soup = get_soup()
    headlines = get_headlines(soup)
    check_match(word='trump', headlines=headlines)

if __name__ == "__main__":
    main()
