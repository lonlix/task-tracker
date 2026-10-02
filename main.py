from task import TaskManager, Task
manager = TaskManager()
manager.load()
while True:
    print("     Меню выбора    ")
    print("1. Добавить задачу.")
    print("2. Показать все задачи.")
    print("3. Выбрать задачу.")
    print("0. Выход.")
    user_input = input("Ввод номера: ")
    if  user_input == "1":
        while True:
            user_task = input("Введите задачу:")
            user_deadline = input("Введите дедлайн:")
            create_task = Task(user_task, user_deadline)
            manager.add_task(create_task)
            manager.save_task()
            print("Задача добавлена!")
            user_repeat = input("Хотите добавить еще одну задачу? [да|нет] \n").lower()
            print("Выбор: ")
            if user_repeat == "да":
                continue
            else:
                break
    elif user_input == "2":
        while True:
            manager.show_tasks()
            user_repeat = input("Нажмите Tab для выхода")
            if user_repeat == "":
                break
            else:
                break
    elif user_input == "3":
        manager.show_tasks()
        user_number = int(input("Введите номер задачи: "))
        manager.get_task(user_number)
        while True:
            print("Что хотите сделать с выбранной задачей?")
            print("1. Отметить задачу выполненной.")
            print("2. Удалить задачу.")
            print("0. Выход с меню выбора.")
            user_choice = int(input("Введите номер: "))
            if user_choice == 1:
                manager.task_done(user_number)
                print("Готово!")
                user_choice = input("Вернуться в меню? [да|нет] \n")
                print("Выбор: ")
                if user_choice == "да":
                    continue
                else:
                    break
            elif user_choice == 2:
                manager.task_delete(user_number)
                print("Готово!")
                user_choice = input("Вернуться в меню? [да|нет] \nВыбор: ")
                if user_choice == "да":
                    continue
                else:
                    break
            else:
                break
    elif user_input == "0":
        print("До новых встреч!")
        break


