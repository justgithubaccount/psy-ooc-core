import random
import time

from ooc.core.growth_event import GrowthEvent
from ooc.core.the_self import TheSelf


def simulate_life(steps: int = 20, delay: float = 1.0):
    """
    Автоматическая симуляция развития TheSelf.

    :param steps: количество шагов симуляции
    :param delay: задержка между шагами в секундах
    """
    theself = TheSelf()

    events_pool = [
        ("Материнская забота", 0.3, "support"),
        ("Фрустрация ожиданий", -0.3, "frustration"),
        ("Травматический опыт", -0.7, "trauma"),
        ("Поддержка отца", 0.2, "support"),
        ("Потеря друга", -0.5, "loss"),
        ("Успех на соревновании", 0.4, "success"),
        ("Игнорирование потребностей", -0.4, "neglect"),
        ("Новый опыт", 0.1, "growth"),
    ]

    print("\n🚀 Старт симуляции жизни!\n")

    for step in range(1, steps + 1):
        name, impact, type_ = random.choice(events_pool)
        event = GrowthEvent(name=name, impact=impact, type_=type_)

        print(f"Шаг {step}: событие -> {event.name} ({event.type_}, {event.impact:+})")
        result = theself.perceive_event(event)
        print(f"👉 {result}")
        print(
            f"🔎 Текущая стадия: {theself.ego.stage.name} | "
            f"Устойчивость: {theself.ego.stability:.2f}\n"
        )

        time.sleep(delay)

    print("\n🏁 Симуляция завершена.\n")
    print("Финальное состояние:")
    print(f"🔹 Эго стадия: {theself.ego.stage.name}")
    print(f"🔹 Устойчивость: {theself.ego.stability:.2f}")


if __name__ == "__main__":
    simulate_life()
