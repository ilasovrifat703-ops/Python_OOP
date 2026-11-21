class Animal:
    """Класс, содержащий информацию о животном."""

    def __init__(
            self,
            name: str,
            class_name: str,
            average_weight: float,
    ) -> None:
        """
        Метод инициализация объекта класса.

        Args:
            name: наименование животного
            class_name: класс, к которому он относится
            average_weight: средний вес
        """
        self.check_weight(average_weight)
        self.__name = name
        self.__class_name = class_name
        self.__average_weight = average_weight


    def get_name(self) -> str:
        """
        Геттер наименования животного.

        Returns:
            str: наименование животного
        """

        return self.__name


    def set_name(self, new_name: str) -> None:
        """
        Сеттер нового наименования животного.

        Args:
            new_name: новое наименование животного.

        Returns:
            None
        """
        self.__name = new_name


    def get_class(self) -> str:
        """
        Геттер наименования животного.

        Returns:
            str: наименование животного.
        """

        return self.__class_name


    def set_class(self, new_class: str) -> None:
        """
        Сеттер нового класса животного.

        Args:
            new_class: новый класс животного.

        Returns:
            None
        """
        self.__class_name = new_class


    def get_weight(self) -> float:
        """
        Геттер среднего веса животного.

        Returns:
            float: средний вес животного.
        """

        return self.__average_weight


    def set_weight(self, new_weight: float) -> None:
        """
        Сеттер нового среднего веса животного.

        Args:
            new_weight: новое значение среднего веса.

        Returns:
            None
        """
        self.check_weight(new_weight)
        self.__average_weight = new_weight


    def feed(self, food_weight: float) -> float:
        """
        Функция, обновляющая вес животного после приема пищи.

        Args:
            food_weight: масса корма.

        Returns:
            None
        """
        self.check_weight(food_weight)
        self.__average_weight += food_weight


    def find_daily_food_weight(self) -> float:
        """
        Функция, рассчитывающая дневную норму еды (5% от массы животного).


        Returns:
            float: масса корма.
        """
        food_weight = (self.__average_weight) * 0.05

        return food_weight


    def __str__(self) -> str:
        """Метод, показывающий основую информацию о животном."""

        return(f'Наименования животного: {self.__name}\n'
               f'Вес животного: {self.__average_weight}\n'
               f'Класс животного: {self.__class_name}')


    @staticmethod
    def check_weight(weight: float) -> None:
        """
        Функция проверки значения веса.

        Args:
            weight: значение веса, вводимое пользователем

        Returns:
            None
        """
        if weight <= 0:
            raise ValueError('Введите корректное значение веса(>0)')


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

        print(f"МЕНЮ УПРАВЛЕНИЯ ЖИВОТНЫМ:\n"
              f"1. Показать информацию о животном\n"
              f"2. Изменить наименование животного\n"
              f"3. Изменить класс животного\n"
              f"4. Изменить средний вес животного\n"
              f"5. Покормить животное\n"
              f"6. Рассчитать дневную норму корма\n"
              f"0. Выход из программы")

       
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