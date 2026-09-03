from typing import Literal

from fastapi import APIRouter, Depends, Header
from pydantic import BaseModel, Field

from ooc.api.deps import DEFAULT_SESSION, get_self, reset_self
from ooc.core.growth_event import GrowthEvent
from ooc.core.the_self import TheSelf

router = APIRouter()

# Типы, которые умеет разбирать Ego.handle_event.
EventType = Literal["support", "frustration", "trauma", "success", "loss"]


class EventRequest(BaseModel):
    name: str = Field(description="Название события.")
    impact: float = Field(ge=-1.0, le=1.0, description="Влияние на устойчивость.")
    type_: EventType = Field(description="Тип события.")


class EventResponse(BaseModel):
    message: str
    current_stage: str
    current_stability: float


class SelfStateResponse(BaseModel):
    name: str
    ego_stage: str
    ego_stability: float
    active_states: list
    active_defenses: list


@router.post("/event", response_model=EventResponse)
def send_event(event: EventRequest, the_self: TheSelf = Depends(get_self)):
    """Отправить событие во внутренний мир TheSelf."""
    growth_event = GrowthEvent(
        name=event.name,
        impact=event.impact,
        type_=event.type_,
    )
    result = the_self.perceive_event(growth_event)
    return EventResponse(
        message=result,
        current_stage=the_self.ego.stage.name,
        current_stability=round(the_self.ego.stability, 2),
    )


@router.get("/self", response_model=SelfStateResponse)
def get_self_state(the_self: TheSelf = Depends(get_self)):
    """Получить текущее состояние TheSelf и Ego."""
    return SelfStateResponse(
        name=the_self.name,
        ego_stage=the_self.ego.stage.name,
        ego_stability=round(the_self.ego.stability, 2),
        active_states=the_self.state_manager.list_active_states(),
        active_defenses=the_self.defense_system.list_active_defenses(),
    )


@router.post("/self/reset", status_code=204)
def reset_self_state(x_session_id: str = Header(default=DEFAULT_SESSION)):
    """Сбросить психику сессии в начальное состояние."""
    reset_self(x_session_id)
