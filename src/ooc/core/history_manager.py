class HistoryManager:
    """
    Менеджер истории развития TheSelf.
    Сохраняет последовательность событий, изменений состояний и стадий развития.
    """

    def __init__(self) -> None:
        self.history: list[str] = []  # Список записей истории

    def add_record(self, record: str) -> None:
        """
        Добавить новую запись в историю.
        """
        self.history.append(record)

    def list_history(self) -> list[str]:
        """
        Получить всю историю развития.
        """
        return self.history

    def clear_history(self) -> None:
        """
        Очистить всю историю.
        """
        self.history.clear()
