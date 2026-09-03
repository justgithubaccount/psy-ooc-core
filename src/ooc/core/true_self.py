class TrueSelf:
    """
    Истинное Я — аутентичная, живая часть личности.
    Основана на спонтанности, искренних потребностях и чувствах.
    """

    def __init__(self) -> None:
        self.authentic_needs: list[str] = []  # Настоящие потребности и желания
        self.spontaneous_reactions: list[str] = []  # Реакции без давления внешнего мира
        self.vitality: float = 1.0  # Уровень жизненности (0.0 - 1.0)

    def express_need(self, need: str) -> None:
        """
        Добавить новое искреннее желание.
        """
        self.authentic_needs.append(need)

    def express_reaction(self, reaction: str) -> None:
        """
        Выразить спонтанную реакцию на мир.
        """
        self.spontaneous_reactions.append(reaction)

    def decrease_vitality(self, amount: float) -> None:
        """
        Уменьшить уровень жизненности (например, при подавлении).
        """
        self.vitality = max(0.0, self.vitality - amount)

    def increase_vitality(self, amount: float) -> None:
        """
        Восстановить уровень жизненности (например, при поддержке).
        """
        self.vitality = min(1.0, self.vitality + amount)
