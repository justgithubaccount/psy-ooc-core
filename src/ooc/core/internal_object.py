class InternalObject:
    """
    Внутренний объект — образ значимого Другого внутри психики.
    Содержит эмоциональный тон и ассоциированные воспоминания.
    """

    def __init__(self, name: str, emotion_tone: str) -> None:
        """
        :param name: Имя или обозначение объекта (например, "Мать", "Отец", "Учитель")
        :param emotion_tone: Эмоциональный окрас (например, "любящий", "отвергающий")
        """
        self.name = name
        self.emotion_tone = emotion_tone
        self.associated_memories: list[str] = []  # Список воспоминаний, связанных с объектом

    def add_memory(self, memory: str) -> None:
        """
        Добавить воспоминание, связанное с этим объектом.
        """
        self.associated_memories.append(memory)

    def update_emotion_tone(self, new_tone: str) -> None:
        """
        Обновить эмоциональный тон объекта.
        """
        self.emotion_tone = new_tone
