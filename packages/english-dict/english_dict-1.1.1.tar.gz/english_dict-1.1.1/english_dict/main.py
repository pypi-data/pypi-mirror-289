import urllib.request, os
from bs4 import BeautifulSoup

def find_word(word):
    """
    Retrieve definition for any English word.

    # Import

    `>>> import english_dict`

    # Call function with word parameter as string:

    `>>> english_dict.find_word("hello")`

    # To clear screen, type c:

    `>>> english_diction.find_word("c")`

    """
    # Checks if the user typed c and will clear the terminal if true
    if word == "c":
        os.system('clear')
    # This is what happens when the above statement is false
    else:
        # This if statement checks id the word does actually exist
        try:
            # Starting the process
            url = "https://google.com/search?q="
            url_word = url + "define+" + word.replace(" ", "%20")
            html = urllib.request.urlopen(url_word)
            htmlParse = BeautifulSoup(html, 'html.parser')
            meaning = []

            # This web-scrapes all the list elements of the webpage

            for para in htmlParse.find_all("div"):
                meaning.append(para.get_text())

            # This picks out the meaning part of the page
            result = []
            index = 35

            while index < 36:
                result.append(meaning[index])
                index = index + 1
            final = []
            # This finishes it off for the interface
            for i in result:
                final.append(f"\n{word} means - " + i)
            return final

        # This handles the code if the word doesn't exist to prevent errors
        except urllib.request.HTTPError:
            return 'The word does not exist.'
def find_synonyms(word2):
    try:
        # This prepares the URL webscrape
        url = "https://thesaurus.com/browse/"
        url_word = url + word2
        html = urllib.request.urlopen(url_word)

        # Starting the process
        htmlParse = BeautifulSoup(html, 'html.parser')
        synonyms = []

        # This webscrapes all the list elements of the webpage
        for para in htmlParse.find_all("li"):
            synonyms.append(para.get_text())
        result = []

        # This picks out the meaning part of the page
        index = 30
        while index < 50:
            result.append(synonyms[index])
            index = index + 1

        # This finsishes it off for the interface
        num = 1
        print("Here are your synonyms:\n")
        for i in result:
            print(f"{num}. {i}")
            num = num + 1

    except urllib.request.HTTPError:
        print("\nSorry, the word you typed is not in the thesaurus")
