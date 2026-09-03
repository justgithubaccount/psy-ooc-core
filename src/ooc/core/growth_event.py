from enum import Enum


class EgoStage(Enum):
    """
    Этапы развития Эго.
    """

    MERGED = "Слияние с материнским объектом"
    DIFFERENTIATION = "Начало отделения Я"
    INTEGRATION = "Формирование целостного Я"
    COHERENCE = "Осознанная стабильность Я"
    DISRUPTION = "Нарушение развития Я"


class GrowthEvent:
    """
    Событие, влияющее на развитие Ego и TheSelf.
    """

    def __init__(self, name: str, impact: float, type_: str) -> None:
        """
        :param name: Название события (например, "Забота", "Фрустрация", "Травма")
        :param impact: Влияние на устойчивость (-1.0 до +1.0)
        :param type_: Тип события ("support", "frustration", "trauma", "success", "loss")
        """
        self.name = name
        self.impact = impact
        self.type_ = type_
