from class_task import Animal

class Menu:
    """Класс для взаимодействия с пользователем через консольное меню."""

    def __init__(self, animal: Animal) -> None:
        """
        Инициализация меню с переданным объектом животного.

        Args:
            animal: экземпляр класса Animal.
        """
        self.__animal = animal

    @staticmethod
    def show_commands() -> None:
        """Выводит список доступных пунктов меню на экран."""
        print("МЕНЮ УПРАВЛЕНИЯ ЖИВОТНЫМ:")
        print("1. Показать информацию о животном")
        print("2. Изменить наименование животного")
        print("3. Изменить класс животного")
        print("4. Изменить средний вес животного")
        print("5. Покормить животное")
        print("6. Рассчитать дневную норму корма")
        print("0. Выход из программы")

    def run(self) -> None:
        """Запускает основной цикл работы меню."""
        choise = ""
        while choise != '0':
            self.show_commands()
            choice = input("Выберите номер действия: ")

            match choice:
                case "1":
                    print("Информация о животном:")
                    print(self.__animal)
                    
                case "2":
                    new_name = input("Введите новое наименование: ")
                    self.__animal.set_name(new_name)
                    print("Наименование успешно изменено.")

                case "3":
                    new_class = input("Введите новый класс животного: ").strip()
                    self.__animal.set_class(new_class)
                    print("Класс успешно изменен.")

                case "4":
                    new_weight = float(input("Введите новый средний вес (кг): "))
                    self.__animal.set_weight(new_weight)
                    print("Средний вес успешно обновлен.")

                case "5":
                    food = float(input("Введите массу корма (кг): "))
                    self.__animal.feed(food)
                    print(f"Текущий вес: {self.__animal.get_weight()} кг.")

                case "6":
                    daily_food = self.__animal.find_daily_food_weight()
                    print(f"Дневная норма корма для '{self.__animal.get_name()}': {daily_food:.2f} кг.")

                case "0":
                    print("Работа программы завершена.")
                    break

                case _:
                    print("Неверный номер действия. Пожалуйста, выберите пункт от 0 до 6.")




animal_obj = Animal("Амурский тигр", "Млекопитающие", 200.0)

menu = Menu(animal_obj)
menu.run()