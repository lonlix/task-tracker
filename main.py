from task import TaskManager, Task

def add_task_menu(manager):
    user_task = input("Введите задачу:")
    user_deadline = input("Введите дедлайн:")
    create_task = Task(user_task, user_deadline)
    manager.add_task(create_task)
    manager.save_task()
    print("Задача добавлена!")

def show_task_menu(manager):
    manager.show_tasks()

def choose_task_menu(manager):
    while True:
        try:
            user_get = int(user_input())
            manager.get_task(user_get)
            return user_get
        except (ValueError,TypeError) as e:
            print(f'Error: {e}')
            continue

def delete_task_menu(manager, number):
    manager.task_delete(number)
    manager.save_task()
    print("Готово!")

def task_done_menu(manager, number):
    manager.task_done(number)
    manager.save_task()
    print("Готово!")

def user_input(text="Ввод: "):
    return input(text)



def print_menu():
    print("     Меню выбора    ")
    print("1. Добавить задачу.")
    print("2. Показать все задачи.")
    print("3. Выбрать задачу.")
    print("0. Выход.")

def print_menu_choice():
    print("Что хотите сделать с выбранной задачей?")
    print("1. Отметить задачу выполненной.")
    print("2. Удалить задачу.")
    print("0. Выход с меню выбора.")

def main():
    manager = TaskManager()
    manager.load()
    while True:
        print_menu()
        user = user_input()
        if  user == "1":                                     #Готово
            while True:
                add_task_menu(manager)
                print("Хотите добавить еще задачу?  \n")
                if user_input("[да|нет]: ").lower() == "да":
                    continue
                else:
                    break
        elif user == "2":
            if len(manager.tasks) == 0:
                print("Нет задач")
            else:
                show_task_menu(manager)
                input("Нажмите Enter для выхода")
        elif user == "3":
            while True:
                try:
                    if len(manager.tasks) == 0:
                        print("Нет задач")
                        break
                    show_task_menu(manager)
                    number = choose_task_menu(manager)
                    print_menu_choice()
                    user = user_input()
                    if user == "1":
                        task_done_menu(manager, number)
                    elif user == "2":
                        delete_task_menu(manager, number)
                    elif user == "0":
                        break
                    else:
                        print("Нет такого номера")
                except (ValueError, TypeError) as e:
                    print(f'Error {e}')
                print("Выбрать еще задачу? \n")
                if user_input("[да|нет]: ").lower() == "да":
                    continue
                else:
                    break
        elif user == "0":
            print("До новых встреч!")
            break
        else:
            print("Такого номера нет!")
            continue

if __name__ == "__main__":
    main()
