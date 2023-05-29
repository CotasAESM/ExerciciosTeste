def stripTags(pageContents):
    pageContents = str(pageContents)
    stratLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")

    pageContents = pageContents[stratLoc:endLoc]

    inside = 0
    text = ''

    for char in pageContents:
        if char == '<':
            inside = 1
        elif(inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char
        return text

def webPageToText(url):
    import urllib.request, urllib.error, urllib.parse
    response = urllib.request.urlopen(url)
    html = response.read().decode('UTF-8')
    text = stripTags(html).lower()
    return text
#não pode ter espaço no url
print(webPageToText('file:///C:/Users/Administrador/OneDrive/Escola/Segundo%20Semestre/Programa%C3%A7%C3%A3o%20Avan%C3%A7ada/Exercicios%20Aulas/Hello%20World'))