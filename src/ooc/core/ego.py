from __future__ import annotations

from typing import TYPE_CHECKING

from ooc.core.growth_event import EgoStage, GrowthEvent

if TYPE_CHECKING:
    from ooc.core.the_self import TheSelf


class Ego:
    """
    Эго — интерфейс между TheSelf и реальностью.
    Отвечает за восприятие событий, активацию защит и развитие стадий.
    """

    def __init__(self, self_ref: TheSelf) -> None:
        self.self_ref = self_ref
        self.stage = EgoStage.MERGED
        self.reality_map: dict = {}
        self.active_defenses: list[str] = []
        self.current_focus: str | None = None
        self.stability: float = 1.0  # Устойчивость Эго

    def handle_event(self, event: GrowthEvent) -> str:
        """
        Обработка внешнего события для развития или защиты.
        """
        response = f"Событие: {event.name} (Тип: {event.type_}, Влияние: {event.impact})"
        if event.type_ == "support":
            self.stability += event.impact
            self.progress_stage()
        elif event.type_ == "frustration":
            if self.stability + event.impact < 0.5:
                self.disrupt()
            else:
                self.stability += event.impact
        elif event.type_ == "trauma":
            self.disrupt()
        elif event.type_ == "success":
            self.stability += event.impact
            self.progress_stage()
        elif event.type_ == "loss":
            self.stability -= abs(event.impact)
            if self.stability < 0.5:
                self.disrupt()

        return f"{response} → Стадия: {self.stage.name}, Устойчивость: {round(self.stability, 2)}"

    def progress_stage(self) -> None:
        """
        Продвижение Эго на следующую стадию развития.
        """
        next_stage = {
            EgoStage.MERGED: EgoStage.DIFFERENTIATION,
            EgoStage.DIFFERENTIATION: EgoStage.INTEGRATION,
            EgoStage.INTEGRATION: EgoStage.COHERENCE,
            EgoStage.COHERENCE: EgoStage.COHERENCE,
            EgoStage.DISRUPTION: EgoStage.DISRUPTION,
        }
        self.stage = next_stage.get(self.stage, self.stage)

    def disrupt(self) -> None:
        """
        Нарушение развития Эго — фиксация на стадии Disruption.
        """
        self.stage = EgoStage.DISRUPTION
