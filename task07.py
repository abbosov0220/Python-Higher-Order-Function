prices = ["$120", "$340", "$50", "$90"]
clean_prices = list(map(lambda x: x.replace('$', ''), prices))
print(clean_prices)
