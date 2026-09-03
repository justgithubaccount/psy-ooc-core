from ooc.core.defense_system import DefenseSystem
from ooc.core.ego import Ego
from ooc.core.false_self import FalseSelf
from ooc.core.growth_event import GrowthEvent
from ooc.core.history_manager import HistoryManager
from ooc.core.internal_object_map import InternalObjectMap
from ooc.core.relation_manager import RelationManager
from ooc.core.state_manager import StateManager
from ooc.core.true_self import TrueSelf


class TheSelf:
    """
    Основная структура субъективного опыта.
    Создаёт внутреннюю целостность, управляет Эго и внутренними объектами.
    """

    def __init__(self, name: str = "TheSelf") -> None:
        self.name = name
        self.ego = Ego(self)
        self.true_self = TrueSelf()
        self.false_self = FalseSelf()
        self.internal_object_map = InternalObjectMap()
        self.state_manager = StateManager()
        self.defense_system = DefenseSystem()
        self.relation_manager = RelationManager()
        self.history_manager = HistoryManager()

    def perceive_event(self, event: GrowthEvent) -> str:
        """
        Передать событие для восприятия Эго.
        """
        return self.ego.handle_event(event)
