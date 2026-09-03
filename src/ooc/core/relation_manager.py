class RelationManager:
    """
    Менеджер связей между внутренними объектами.
    Отвечает за динамику любви, страха, агрессии, привязанности и других связей.
    """

    def __init__(self) -> None:
        self.relations: dict[tuple[str, str], str] = {}  # Словарь вида {(имя1, имя2): тип связи}

    def add_relation(self, object_name_1: str, object_name_2: str, relation_type: str) -> None:
        """
        Установить связь между двумя внутренними объектами.
        :param relation_type: Например, "любовь", "страх", "агрессия"
        """
        key = tuple(sorted([object_name_1, object_name_2]))
        self.relations[key] = relation_type

    def get_relation(self, object_name_1: str, object_name_2: str) -> str | None:
        """
        Получить тип связи между двумя объектами.
        """
        key = tuple(sorted([object_name_1, object_name_2]))
        return self.relations.get(key)

    def remove_relation(self, object_name_1: str, object_name_2: str) -> None:
        """
        Удалить связь между двумя объектами.
        """
        key = tuple(sorted([object_name_1, object_name_2]))
        if key in self.relations:
            del self.relations[key]

    def list_relations(self) -> list[tuple[tuple[str, str], str]]:
        """
        Вернуть список всех существующих связей.
        """
        return list(self.relations.items())
