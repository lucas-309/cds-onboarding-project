from bs4 import BeautifulSoup
import re

def scrape():
    soup = None
    with open("LAPD.html") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    scrapes = []

    # page introduction
    current = soup.h1
    scrapes.append(current.string)

    current = current.find_next("p")
    for i in range(3):
        current = current.find_next("p")
        scrapes.append(str(current))

    # history
    current = current.find_next("h2")
    scrapes.append(current.string)

    for i in range(4):
        current = current.find_next("p")
        scrapes.append(str(current))

    # organization
    current = current.find_next("h2")
    scrapes.append(current.string)

    for i in range(3):
        current = current.find_next("p")
        scrapes.append(str(current))

    for i in range(3):
        current = current.find_next("h3")
        scrapes.append(current.string)

        current = current.find_next("p")
        scrapes.append(str(current))

    # headquarters
    current = current.find_next("h2")
    scrapes.append(current.string)

    for i in range(2):
        current = current.find_next("p")
        scrapes.append(str(current))

    # ranks
    current = current.find_next("h2")
    scrapes.append(current.string + "\n")

    # demographics
    current = current.find_next("h2")
    scrapes.append(current.string)

    for i in range(2):
        current = current.find_next("p")
        scrapes.append(str(current))

    for i in range(6):
        current = current.find_next("li")
        scrapes.append(current.text)

    current = current.find_next("p")
    scrapes.append(str(current))

    # work environment and revenue
    current = current.find_next("h2")
    scrapes.append(current.string)

    for i in range(2):
        current = current.find_next("p")
        scrapes.append(str(current))

    # resources
    current = current.find_next("h2")
    scrapes.append(current.string)

    current = current.find_next("h3")
    scrapes.append(current.string)
    for i in range(2):
        current = current.find_next("p")
        scrapes.append(str(current))

    for i in range(2):
        current = current.find_next("h3")
        scrapes.append(current.string)
        current = current.find_next("p")
        scrapes.append(str(current))

    current = current.find_next("h3")
    scrapes.append(current.string)
    for i in range(2):
        current = current.find_next("p")
        scrapes.append(str(current))

    # awards and commendations
    current = current.find_next("h2")
    scrapes.append(current.string)

    for i in range(2):
        current = current.find_next("p")
        scrapes.append(str(current))

    # public opinion
    current = current.find_next("h2")
    scrapes.append(current.string)

    current = current.find_next("p")
    scrapes.append(str(current))

    # controversies, corruption, misconducts and scandals
    current = current.find_next("h2")
    scrapes.append(current.text)

    current = current.find_next("p")
    scrapes.append(str(current))

    for i in range(2):
        current = current.find_next("h3")
        scrapes.append(current.text)
        for j in range(3):
            current = current.find_next("p")
            scrapes.append(str(current))

    current = current.find_next("h3")
    scrapes.append(current.text)
    for i in range(5):
        current = current.find_next("p")
        scrapes.append(str(current))

    current = current.find_next("h3")
    scrapes.append(current.text)
    for i in range(11):
        current = current.find_next("p")
        scrapes.append(str(current))

    current = current.find_next("h3")
    scrapes.append(current.text)
    for i in range(12):
        current = current.find_next("p")
        scrapes.append(str(current))

    # fallen officers
    current = current.find_next("h2")
    scrapes.append(current.string)

    for i in range(2):
        current = current.find_next("p")
        scrapes.append(str(current))

    # in popular culture
    current = current.find_next("h2")
    scrapes.append(current.string)

    current = current.find_next("p")
    scrapes.append(str(current))

    current = current.find_next("h3")
    scrapes.append(current.text)
    for j in range(2):
        current = current.find_next("p")
        scrapes.append(str(current))

    current = current.find_next("h3")
    scrapes.append(current.text)
    current = current.find_next("h4")
    scrapes.append(current.text)
    for j in range(2):
        current = current.find_next("p")
        scrapes.append(str(current))
    current = current.find_next("h4")
    scrapes.append(current.text)
    current = current.find_next("p")
    scrapes.append(str(current))

    # final cleaning
    final_text = []
    for page in scrapes:
        final_text.append(re.sub("&amp;", "&", re.sub("<.*?>", "", re.sub("\\[.*?\\]", "", page))))#.strip())
    #print("\n".join(final_text))


    links = []
    current = current.find_next("h2")
    current = current.find_next("li")
    for i in range(4):
        current = current.find_next("li")
        current = current.find_next("a")
        links.append("https://en.wikipedia.org/" + current["href"])
    #print("\n".join(links))


    return [final_text, links]


results = scrape()

f = open("webscraping_results.txt", "w")
f.write("Wikipedia page:\n")
f.write("\n".join(results[0]))
f.write("\n\n")
f.write("See also links:\n")
f.write("\n".join(results[1]))
f.close()