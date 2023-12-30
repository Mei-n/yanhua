import os

file_path = os.path.abspath("index.html")
url = "file://" + file_path
print(url)