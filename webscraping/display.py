from scrape import scrape

results = scrape()

print("Wikipedia page:")
print("\n".join(results[0]))
print("\n")
print("See also links:")
print("\n".join(results[1]))