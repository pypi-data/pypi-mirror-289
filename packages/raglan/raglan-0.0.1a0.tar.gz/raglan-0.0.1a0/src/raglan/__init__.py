import pyknit
from dataclasses import dataclass
from typing import Literal


@dataclass
class Measurments:    
    neck_circumference: float
    chest_circumference: float
    waist_circumference: float
    hip_circumference: float
    upper_arm_circumference: float
    wrist_circumference: float

    yoke_depth: float
    underarm_to_waist_length: float
    waist_to_hip_length: float

    cuff_length: float
    neckline_border_length: float
    body_border_length: float 

    unit: Literal["cm", "in"]


@dataclass
class Raglan:
    measurments: Measurments
    gauge: pyknit.GaugeSwatch
