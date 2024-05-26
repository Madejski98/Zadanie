# Zadanie
# Smarfon może być włączony lub wyłączony oraz posiada określoną pamięć wewnętrzną
# Można na nim instalować aplikacje, które zużywają pamięć
# Napisz klasę, która obsłuży ten przypadek
# Stwórz jej instancję i sprawdź działanie

class Smartfon():
    aplikacje = {}
    def __init__(self, marka, model, max_pamiec):
        self.marka = marka
        self.model = model
        self.max_pamiec = max_pamiec
        self.pamiec = max_pamiec
        self.stan = 'off'

    def zainstaluj_app(self, nazwa_app, pamiec_app):
        if self.stan == 'on':
            if self.pamiec > pamiec_app:
                self.aplikacje[nazwa_app] = pamiec_app
                self.pamiec -= pamiec_app
                print(self.aplikacje)
            else:
                print("Brak miejsca. Zwolnij miejce w pamięci!")
        else:
            print("Najpierw włącz telefon.")

    def wlacz_tel(self):
        if self.stan == 'off':
            self.stan = 'on'
        else:
            print('Nie możesz włączyć włączony telefon!')

    def wylacz_tel(self):
        if self.stan == 'on':
            self.stan = 'off'
        else:
            print('Nie możesz wyłączyć wyłączony telefon!')

samsung = Smartfon('Samsung', 'S24', 16000)
samsung.wlacz_tel()
samsung.wlacz_tel()
samsung.zainstaluj_app('Angry Birds', 1000)
samsung.wylacz_tel()
samsung.wylacz_tel()