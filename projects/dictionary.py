import requests as req

def search(word):
    link = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = req.get(link)
        if response.status_code != 200:
            print(f"No definitions found for {word.title()}")
        else:
            data = response.json()
            print(f'{word} definition:\n{data[0]["meanings"][0]["definitions"][0]["definition"]}')
    except Exception as e:
        print("Unexpected Error Occurred")

if __name__ == "__main__":
    while True:
        word = input("What would you like to query: ")
        if not word: break
        search(word)