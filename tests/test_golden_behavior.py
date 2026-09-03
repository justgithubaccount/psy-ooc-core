"""Инвариант поведения модели психики.

Ядро описывает развитие Я: правила перехода стадий, арифметику устойчивости
и условия срыва. Рефакторинг, форматирование и типизация не должны менять
это поведение — только читаемость кода.

Тест прогоняет симуляцию с фиксированным сидом и сверяет историю событий
с эталоном. Если он падает, значит изменилась модель, а не оформление.
Осознанное изменение модели требует обновления эталона отдельным коммитом.
"""

import json
import random
from pathlib import Path

from ooc.simulation.life_simulation import LifeSimulation

GOLDEN = Path(__file__).parent / "golden" / "life_simulation_seed42_30steps.json"
SEED = 42
STEPS = 30


def run_simulation() -> list[dict]:
    random.seed(SEED)
    simulation = LifeSimulation()
    simulation.run_simulation(steps=STEPS)
    return simulation.get_simulation_history()


def test_simulation_matches_golden_run():
    """История событий совпадает с эталоном шаг в шаг."""
    expected = json.loads(GOLDEN.read_text(encoding="utf-8"))
    actual = run_simulation()

    assert len(actual) == len(
        expected
    ), f"Число шагов изменилось: {len(actual)} вместо {len(expected)}"

    for index, (got, want) in enumerate(zip(actual, expected, strict=True)):
        assert got == want, (
            f"Шаг {index + 1} разошёлся с эталоном.\n" f"Ожидалось: {want}\n" f"Получено:  {got}"
        )


def test_simulation_is_deterministic():
    """Один и тот же сид даёт один и тот же прогон."""
    assert run_simulation() == run_simulation()
