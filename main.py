from bs4 import BeautifulSoup
import pandas as pd

data = []

for turn in range(1, 56):

    Usr_input = input("Its page " + str(turn) + " awaiting for next page...")
    if Usr_input != "":
        continue

    doc = BeautifulSoup(open("./index.html", encoding="utf8"), "html.parser")

    for a in range(1, 5):

        table = doc.find_all('table', class_="invest-wallet-table")[a]
        # then we can iterate through each row and extract either header or row values:
        nameB = []
        priceB = []
        for i, row in enumerate(table.find_all('tr')):
            nameB = [el.text.strip() for el in row.find_all('td', class_="name")]
            priceB = [el.text.strip() for el in row.find_all('td', class_="market-price")]

            name = (''.join(nameB))
            price = (''.join(priceB))

            data.append({
                'name': name,
                'price': price,
                'turn': turn,
            })

        #print(name)
        #print(price)

df = pd.DataFrame(data)

df.to_csv(r'./dane.csv', index=False)

print("Program has stopped")

