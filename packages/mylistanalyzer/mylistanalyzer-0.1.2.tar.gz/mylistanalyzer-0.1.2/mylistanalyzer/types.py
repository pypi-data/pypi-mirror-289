from typing import TypedDict


class UserStats(TypedDict):
    Watching: int
    Completed: int
    OnHold: int
    Dropped: int
    PlannedToWatch: int


class TotalValues(TypedDict):
    TotalEntries: int
    ReWatched: int
    Episodes: int


class UserDetails(TypedDict):
    userName: str
    profile: str
    stats: UserStats
    totals: TotalValues
    meanScore: int
    daysSpent: int


class FailedReason(TypedDict):
    shortName: str
    description: str
