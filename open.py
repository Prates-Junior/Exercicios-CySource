arquivo = open("README.md", "r")
urls = []
for linha in arquivo.readlines():
    if "http" in linha:
        url = linha[linha.find("http"):-1]
        urls.append(url)
print(urls)
arquivo.close()
