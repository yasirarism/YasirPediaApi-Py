from json import dumps
from requests import get


class YasirPediaApi:
    def __init__(self):
        self.base_url = "https://yasirapi.eu.org"

    def google(self, query: str):
        try:
            url = f"{self.base_url}/google?q={query}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YasirArisM\n\n{e}"

    def textpro(self, text: str, link: str):
        try:
            url = f"{self.base_url}/textpro?q={text}&url={link}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YasirArisM\n\n{e}"

    def kbbi(self, kata: str):
        try:
            url = f"{self.base_url}/kbbi?kata={kata}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YasirArisM\n\n{e}"

    def layarkaca21(self, query: str):
        try:
            url = f"{self.base_url}/lk21?q={query}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YasirArisM\n\n{e}"

    def imdb_search(self, query: str):
        try:
            url = f"{self.base_url}/imdb-search?q={query}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YasirArisM\n\n{e}"

    def fbdl(self, link: str):
        try:
            url = f"{self.base_url}/fbdl?link={link}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YasirArisM\n\n{e}"

    def terbit21(self, query: str):
        try:
            url = f"{self.base_url}/terbit21?q={query}"
            response = get(url, timeout=15).json()
            return dumps(response, indent=2)
        except Exception as e:
            return f"An error occured report on @YasirArisM\n\n{e}"