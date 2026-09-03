import json

import typer

from ooc.config.logging_config import setup_logging

app = typer.Typer()


@app.command()
def simulate(
    steps: int = typer.Option(20, help="Количество шагов симуляции."),
    delay: float = typer.Option(1.0, help="Задержка между шагами, в секундах."),
    as_json: bool = typer.Option(
        False,
        "--json",
        help="Прогнать без задержек и вывести историю в JSON.",
    ),
):
    """Запуск симуляции сознания."""
    setup_logging()

    if as_json:
        from ooc.simulation.life_simulation import LifeSimulation

        simulation = LifeSimulation()
        simulation.run_simulation(steps=steps)
        print(json.dumps(simulation.get_simulation_history(), ensure_ascii=False, indent=2))
        return

    from ooc.scripts.simulate_life import simulate_life

    simulate_life(steps=steps, delay=delay)


@app.command()
def create_self(
    name: str = typer.Option("TheSelf", help="Имя создаваемого объекта."),
):
    """Создание нового объекта TheSelf."""
    setup_logging()
    from ooc.core.the_self import TheSelf

    theself = TheSelf(name=name)
    print(f"Создан новый TheSelf: {theself.name}")


if __name__ == "__main__":
    app()
