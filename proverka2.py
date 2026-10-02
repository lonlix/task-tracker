import json

class Product:
    def __init__(self, product,price, status_buy=False):
        self.product = product
        self.status_buy = status_buy
        self.price = price

    def __str__(self):
        return f"Продукт: {self.product}, Цена: {self.price}, Купленно: {self.status_buy}"

    def __repr__(self):
        return f"Продукт: {self.product}, Цена: {self.price}, Купленно: {self.status_buy}"

    def to_dict(self):
        return {
            "product": self.product,
            "price" : self.price,
            "status_buy": self.status_buy
        }

    def stat(self):
        self.status_buy = True

    def sum(self):
        return self.price

class ShoppingList:
    def __init__(self, filename="show.json"):
        self.shop_list = []
        self.filename = filename

    def add_product(self, note):
        self.shop_list.append(note)

    def shop_tr(self, number):
        shop = self.get_shop(number)
        shop.stat()

    def show_products(self):
        for number,item in enumerate(self.shop_list, start=1):
            print(f'{number}. {item}')

    def get_shop(self,number):
        if not isinstance(number, int):
            raise TypeError("Ошибка типа данных")
        elif number > len(self.shop_list) or number < 1:
            raise ValueError("Ошибка Значения")
        else:
            return self.shop_list[number - 1]

    def delete_product(self, number):
        shop = self.get_shop(number)
        self.shop_list.remove(shop)

    def save_shop(self):
        data = []
        for prod in self.shop_list:
            data.append(prod.to_dict())
        with open(self.filename, "w", encoding = "utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_shop(self):
        try:
            with open(self.filename, "r", encoding='utf-8') as f:
                data = json.load(f)
            for item in data:
                self.shop_list.append(Product(item["product"],item["price"], item["status_buy"]))
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def all_price(self):

        summ = 0
        for i in self.shop_list:
            summ += i.sum()
        return summ

if __name__ == "__main__":
    manager = ShoppingList()
    b = Product("майнез", 120)
    v = Product("Перец", 100)
    manager.add_product(b)
    manager.add_product(v)
    manager.show_products()
    manager.shop_tr(2)
    manager.show_products()
    print(manager.all_price())












