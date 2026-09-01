from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import pengpenguin as ppeng
    
@dataclass
class PenguinLearningPlace:
    learners: list["ppeng.Penguin"]