from ooc.core.internal_object import InternalObject


class InternalObjectMap:
    """
    Карта внутренних объектов — структура хранения всех внутренних образов внутри TheSelf.
    """

    def __init__(self) -> None:
        self.objects: dict[str, InternalObject] = {}  # Словарь вида {имя: InternalObject}

    def add_object(self, internal_object: InternalObject) -> None:
        """
        Добавить новый внутренний объект в карту.
        """
        self.objects[internal_object.name] = internal_object

    def get_object(self, name: str) -> InternalObject | None:
        """
        Получить внутренний объект по имени.
        """
        return self.objects.get(name)

    def remove_object(self, name: str) -> None:
        """
        Удалить внутренний объект из карты по имени.
        """
        if name in self.objects:
            del self.objects[name]

    def list_objects(self) -> list[InternalObject]:
        """
        Вернуть список всех внутренних объектов.
        """
        return list(self.objects.values())
