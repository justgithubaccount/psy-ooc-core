class DefenseSystem:
    """
    Система защитных механизмов Эго.
    Отвечает за активацию психологических защит при угрозе внутренней целостности.
    """

    def __init__(self) -> None:
        self.active_defenses: list[str] = []  # Активированные защиты

    def activate_defense(self, defense: str) -> None:
        """
        Активировать новый защитный механизм.
        """
        if defense not in self.active_defenses:
            self.active_defenses.append(defense)

    def deactivate_defense(self, defense: str) -> None:
        """
        Деактивировать защитный механизм.
        """
        if defense in self.active_defenses:
            self.active_defenses.remove(defense)

    def is_defense_active(self, defense: str) -> bool:
        """
        Проверить, активирован ли защитный механизм.
        """
        return defense in self.active_defenses

    def list_active_defenses(self) -> list[str]:
        """
        Вернуть список всех активных защит.
        """
        return self.active_defenses
