from abc import ABC
from dataclasses import dataclass

from mani.domain.cqrs.effects import Event


@dataclass(frozen=True)
class UpdateEvent(Event, ABC):
    order: int
    total: int
