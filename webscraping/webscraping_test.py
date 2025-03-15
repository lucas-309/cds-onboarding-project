import unittest
from scrape import scrape

class TestScraping(unittest.TestCase):
    scrape_results = scrape()
    wiki = scrape_results[0][1:]
    links = scrape_results[1]

    def test_wiki_page(self):
        self.maxDiff = None
        
        actual_text = ""
        with open("LAPD_Online.txt", "r") as f:
            for line in f:
                actual_text += (line.strip() + " ")

        for text in self.wiki:
            self.assertTrue(text.strip() in actual_text)

    def test_links(self):
        self.assertEqual(self.links[0], "https://en.wikipedia.org//wiki/Crime_in_Los_Angeles")
        self.assertEqual(self.links[1], "https://en.wikipedia.org//wiki/Law_enforcement_in_Los_Angeles_County")
        self.assertEqual(self.links[2], "https://en.wikipedia.org//wiki/List_of_law_enforcement_agencies_in_California")
        self.assertEqual(self.links[3], "https://en.wikipedia.org//wiki/LAPD_Red_Squad_raid_on_John_Reed_Club_art_show")

if __name__ == '__main__':
    unittest.main()