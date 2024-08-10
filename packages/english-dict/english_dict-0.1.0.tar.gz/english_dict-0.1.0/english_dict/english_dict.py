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

            # This finishes it off for the interface
            for i in result:
                print(f"\n{word} means - " + i)

        # This handles the code if the word doesn't exist to prevent errors
        except urllib.error.HTTPError:
            print('The word does not exist.')
find_word("c")