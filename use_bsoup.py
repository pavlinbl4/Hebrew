from bs4 import BeautifulSoup
import requests
import pyperclip

HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4200.0 Iron Safari/537.36",
    "accept": "*/*"}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup


def parse(wort_to_translate):
    html = get_html(create_url_link(wort_to_translate))
    if html.status_code == 200:
        try:
            all_words = get_soup(html.text).find_all(class_="Translation_spTop_heToen")
            all_translations = get_soup(html.text).find_all(class_="normal_translation_div")
            return extract_words_from_soup_list(all_words, all_translations)

        except:
            print("There wasn't hebrew word in clip memory")
    else:
        print("error")


def extract_words_from_soup_list(all_words, all_translations):
    translations = {}
    for i in range(len(all_words)):
        translations[all_translations[i].text.strip()] = all_words[i].text.strip()
    return translations


def create_url_link(wort_to_translate):
    return f'https://www.morfix.co.il/en/{wort_to_translate}'


def take_word_to_translate():
    return pyperclip.paste()


if __name__ == '__main__':
    hebrew_word = take_word_to_translate()
    with_vowels = parse(hebrew_word)
    if with_vowels is not None:
        for k, i in with_vowels.items():
            print(i, k)
        # pyperclip.copy(with_vowels)
