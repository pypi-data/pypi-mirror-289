from mylistanalyzer.blueprint import AskFrom
from mylistanalyzer.types import UserDetails, FailedReason
from urllib.request import urlopen
from urllib.error import HTTPError
from lxml.etree import parse, fromstring
from mylistanalyzer.utils import dict_num_zip
from typing import Optional


class AskFromMLA(AskFrom):
    @property
    def user_profile_link(self) -> str:
        return f"https://myanimelist.net/profile/{self.user_name}"

    def get_user_details(self, raw_string: Optional[str] = None) -> FailedReason | UserDetails:
        try:
            if raw_string:
                parsed_content = fromstring(raw_string, parser=self.parser)
            else:
                parsed_content = parse(urlopen(
                    self.user_profile_link
                ), self.parser)
        except HTTPError as error:
            return {
                "shortName": f"HTTPError - {str(error.code)}",
                "description": str(error.reason)
            }

        return {
            "userName": self.user_name,
            "profile": parsed_content.xpath("string(*//*[@class='user-profile']//img/@data-src)"),
            "stats": dict_num_zip(
                parsed_content.xpath(
                    "*//*[contains(@class, 'stats') and "
                    "contains(@class, 'anime')]//"
                    "ul[contains(@class, 'stats-status')]/li/span/text()"
                    , smart_strings=False
                ),
                ("Watching", "Completed", "OnHold", "Dropped", "PlannedToWatch")
            ),
            "totals": dict_num_zip(
                parsed_content.xpath(
                    "*//*[contains(@class, 'stats') and "
                    "contains(@class, 'anime')]//"
                    "ul[contains(@class, 'stats-data')]/li/span[last()]/text()", smart_strings=False),
                ("TotalEntries", "ReWatched", "Episodes")
            ),
            "meanScore": parsed_content.xpath(
                "number(translate(*//*[contains(@class, 'stats') and contains(@class, 'anime')]"
                "//*[contains(@class, 'stat-score')]"
                "//*[contains(@class, 'score-label')]"
                "/text(), ',', ''))", smart_strings=False
            ),
            "daysSpent": parsed_content.xpath(
                "number(translate(*//*[contains(@class, 'stats') and contains(@class, 'anime')]"
                "//*[contains(@class, 'stat-score')]"
                "/div"
                "/text(), ',', ''))", smart_strings=False
            )
        }


if __name__ == "__main__":
    print(AskFromMLA("RahulARanger").get_user_details())
