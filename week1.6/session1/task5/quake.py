# Week 1.6, Session 1: Task 5

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Quake:
    """
    Details of a single earthquake.
    """

    when: datetime
    longitude: float
    latitude: float
    depth: float
    magnitude: float

    def __init__(self,when,longitude,latitude,depth,magnitude):
        self.when = when
        self.longitude = longitude
        self.latitude = latitude
        self.depth = depth
        self.magnitude = magnitude

