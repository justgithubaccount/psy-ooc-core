class FalseSelf:
    """
    Ложное Я — адаптивная оболочка, сформированная для выживания.
    Основана на подстройке под ожидания окружающих и защите от боли.
    """

    def __init__(self) -> None:
        self.defensive_roles: list[str] = []  # Роли и маски, которые человек принимает
        self.adaptive_behaviors: list[str] = []  # Стратегии поведения для угождения
        self.split_from_true_self: bool = True  # Указывает на разрыв с Истинным Я

    def adopt_role(self, role: str) -> None:
        """
        Принять новую защитную роль.
        """
        self.defensive_roles.append(role)

    def add_adaptive_behavior(self, behavior: str) -> None:
        """
        Добавить новое адаптивное поведение.
        """
        self.adaptive_behaviors.append(behavior)

    def reconnect_to_true_self(self) -> None:
        """
        Попытка восстановить связь с Истинным Я.
        """
        self.split_from_true_self = False

    def disconnect_from_true_self(self) -> None:
        """
        Зафиксировать отрыв от Истинного Я.
        """
        self.split_from_true_self = True
