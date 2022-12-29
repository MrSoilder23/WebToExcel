from bs4 import BeautifulSoup
import pandas as pd

doc = BeautifulSoup(open("C:\\Users\\komputer\\PycharmProjects\\ScreenshotToExcel\\index.html", encoding="iso-8859-2"), "html.parser")

print("Encoding method :", doc.original_encoding)