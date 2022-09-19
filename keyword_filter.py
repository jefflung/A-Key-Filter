import urllib.request

url = input("Enter address to scan: ")
#Test with http://www.guimp.com/

response = urllib.request.urlopen(url)
data = response.read()
text = data.decode().lower()

wordList = []
with open("blocked_words.txt", mode="r") as my_file:
    found = False
    for line in my_file:
        line = line.lower()
        if line in text:
            wordList.append(line)
            #print(line)
            print("This page contains blocked words: ", wordList)
            found = True
    if not found:
        print("No blocked words here.")
