import json

class Note:
    def __init__(self, text, pinned=False):
        self.text = text
        self.pinned = pinned

    def __str__(self):
        return f'Закреп: {self.text}, pin: {self.pinned}'

    def pin(self):
        self.pinned = True

    def __repr__(self):
        return f'Закреп: {self.text}, pin: {self.pinned}'

    def to_dict(self):
        return {
            "text": self.text,
            "pinned": self.pinned
        }

class Notebook:
    def __init__(self, filename='xuy.json'):
        self.works = []
        self.filename = filename

    def add_works(self, note):
        self.works.append(note)

    def show_works(self):
        for number,item in enumerate(self.works, start=1):
            print(f"{number}, {item}")

    def get_work(self, number):
        if not isinstance(number, int):
            raise TypeError("Должно быть число")
        elif number > len(self.works) or number < 1:
            raise ValueError("Некорректное значение")
        else:
            return self.works[number - 1]

    def delete_work(self, number):
        work = self.get_work(number)
        self.works.remove(work)

    def save_work(self):
        data = []
        for work in self.works:
            data.append(work.to_dict())
        with open(self.filename, "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_work(self):
        try:
            with open(self.filename, "r", encoding='utf-8') as f:
                data = json.load(f)
            for item in data:
                self.works.append(Note(item["text"], item["pinned"]))
        except FileNotFoundError as e:
            print(f'Error {e}')








