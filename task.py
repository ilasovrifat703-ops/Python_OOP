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

    def set_name(self,new_name: str) -> None:
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

    def set_weight(self, new_weight: str) -> None:
        """
        Сеттер нового среднего веса животного.

        Args:
            new_weight: новое значение среднего веса.

        Returns:
            None
        """
        self.check_weight(new_weight)
        self.__average_weight = new_weight

    def __str__(self):
        return(f'Наименования животного: {self.__name}\n')

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
            raise ValueError('Вес должен быть больше 0')


p = Animal('ss','sss',10)

