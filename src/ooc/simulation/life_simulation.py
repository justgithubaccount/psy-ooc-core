import random

from ooc.core.growth_event import GrowthEvent
from ooc.core.the_self import TheSelf


class LifeSimulation:
    """
    Класс симуляции жизни для TheSelf.
    Управляет потоком событий и отслеживает развитие.
    """

    def __init__(self, self_instance: TheSelf = None):
        self.the_self = self_instance or TheSelf()
        self.history = []  # Хранит историю всех событий

    def simulate_step(self, event: GrowthEvent):
        """
        Провести один шаг симуляции: обработать одно событие.
        """
        result = self.the_self.perceive_event(event)
        self.history.append(
            {
                "event": event.name,
                "impact": event.impact,
                "type": event.type_,
                "result": result,
                "stage": self.the_self.ego.stage.name,
                "stability": round(self.the_self.ego.stability, 2),
            }
        )

    def random_event(self) -> GrowthEvent:
        """
        Сгенерировать случайное событие для симуляции.
        """
        events = [
            ("Материнская забота", 0.2, "support"),
            ("Фрустрация ожиданий", -0.3, "frustration"),
            ("Травматический опыт", -0.7, "trauma"),
            ("Успешное достижение", 0.3, "success"),
            ("Потеря близкого", -0.5, "loss"),
        ]
        name, impact, type_ = random.choice(events)
        return GrowthEvent(name, impact, type_)

    def run_simulation(self, steps: int = 10):
        """
        Запустить симуляцию на несколько шагов.
        """
        for _ in range(steps):
            event = self.random_event()
            self.simulate_step(event)

    def get_simulation_history(self):
        """
        Получить всю историю симуляции.
        """
        return self.history
