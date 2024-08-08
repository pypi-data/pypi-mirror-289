from abc import ABC, abstractmethod
from lxml.etree import HTMLParser
from mylistanalyzer.types import UserDetails, FailedReason


class AskFrom(ABC):
    user_name: str
    user_details: UserDetails

    def __init__(self, user_name):
        self.user_name = user_name
        self.parser = HTMLParser()

    @property
    @abstractmethod
    def get_user_details(self) -> FailedReason | UserDetails:
        pass

    @abstractmethod
    def user_profile_link(self) -> str:
        pass
