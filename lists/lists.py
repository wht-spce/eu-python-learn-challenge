class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """

        result: list[int] = []

        if input_list:
            max_value: int = max(input_list)
            for item in input_list:
                if item > 0:
                    result.append(max_value)
                else:
                    result.append(item)
        return result

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        low: int = 0
        high: int = len(input_list) - 1

        while low <= high:
            avg: int = (low + high) // 2
            if input_list[avg] == query:
                return avg
            elif input_list[avg] < query:
                low = avg + 1
            else:
                high = avg - 1
        return -1
