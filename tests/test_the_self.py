from ooc.core.growth_event import GrowthEvent
from ooc.core.the_self import TheSelf


def test_create_the_self():
    theself = TheSelf()
    assert theself.name == "TheSelf"
    assert theself.ego.stability == 1.0
    assert theself.ego.stage.name == "MERGED"


def test_perceive_support_event():
    theself = TheSelf()
    support_event = GrowthEvent(name="Поддержка", impact=0.3, type_="support")
    response = theself.perceive_event(support_event)

    assert "Событие" in response
    assert theself.ego.stability > 1.0
    assert theself.ego.stage.name in ["DIFFERENTIATION", "INTEGRATION", "COHERENCE"]


def test_perceive_trauma_event():
    theself = TheSelf()
    trauma_event = GrowthEvent(name="Травма", impact=-1.0, type_="trauma")
    response = theself.perceive_event(trauma_event)

    assert "Событие" in response
    assert theself.ego.stage.name == "DISRUPTION"
