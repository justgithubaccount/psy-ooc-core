from ooc.core.growth_event import GrowthEvent
from ooc.core.the_self import TheSelf


def test_ego_handle_support():
    theself = TheSelf()
    ego = theself.ego

    event = GrowthEvent(name="Поддержка", impact=0.2, type_="support")
    response = ego.handle_event(event)

    assert "Событие" in response
    assert ego.stability > 1.0
    assert ego.stage.name in ["DIFFERENTIATION", "INTEGRATION", "COHERENCE"]


def test_ego_handle_frustration():
    theself = TheSelf()
    ego = theself.ego

    event = GrowthEvent(name="Фрустрация", impact=-0.3, type_="frustration")
    response = ego.handle_event(event)

    assert "Событие" in response
    assert ego.stability < 1.0
    assert ego.stage.name in [
        "MERGED",
        "DIFFERENTIATION",
        "INTEGRATION",
        "COHERENCE",
        "DISRUPTION",
    ]


def test_ego_handle_trauma():
    theself = TheSelf()
    ego = theself.ego

    event = GrowthEvent(name="Травма", impact=-1.0, type_="trauma")
    response = ego.handle_event(event)

    assert "Событие" in response
    assert ego.stage.name == "DISRUPTION"
    assert ego.stability <= 1.0  # В состоянии травмы стабильность может быть любой, но важна стадия


def test_ego_disruption_directly():
    theself = TheSelf()
    ego = theself.ego

    ego.disrupt()

    assert ego.stage.name == "DISRUPTION"
