class Animal:
    def __init__(
            self,
            name: str,
            class_name: str,
            average_weight: float,
    ) -> None:
        """
        Инициализатор класса Animal
        :param name:
        :param class_name:
        :param average_weight:
        """
        self.check_weight(average_weight)
        self.__name = name
        self.__class_name = class_name
        self.__average_weight = average_weight

    @staticmethod
    def check_weight(weight):
        """
        Функция проверки значения веса
        :param weight:
        :return:
        """
        if weight <= 0:
            raise ValueError('Вес должен быть больше 0')

    def get_name(self):
        """
        Геттер наименования животного
        :return:
        """
        return self.__name

    def set_name(self,new_name: str) -> None:
        """
        Сеттер нового наименования животного
        :param new_name:
        :return:
        """
        self.__name = new_name

    def get_class(self):
        """
        Геттер наименования животного
        :return:
        """
        return self.__class_name

    def set_class(self, new_class: str) -> None:
        """
        Сеттер нового наименования животного
        :param new_name:
        :return:
        """
        self.__class_name = new_class

    def get_weight(self):
        """
        Геттер наименования животного
        :return:
        """
        return self.__average_weight

    def set_weight(self, new_weight: str) -> None:
        """
        Сеттер нового наименования животного
        :param new_name:
        :return:
        """
        self.__average_weight = new_weight
    
    def __str__(self):
        return(f'Наименования животного: {self.__name}\n')
p = Animal('ss','sss',9)
p.set_name('yuo')
print(p.__dict__)
