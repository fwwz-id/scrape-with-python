from variables.types import HTMLTags, HTMLTag
from helpers import utils


class HTMLAttributeParser:
    """ 
    Functions that helps get attribute from specific HML Tag
    """

    def __init__(self, items: HTMLTags) -> None:
        self.items = items

    def getFromImgTag(self, attr: str) -> list[str]:
        "Get attribute from `img` tag"

        def parse(item: HTMLTag) -> str:
            result: str = item[attr]
            return result

        return utils.mapToList(parse, self.items)

    def getTextFromTag(self) -> list[str]:
        "Get text from HTMLs tag"

        def parse(item: HTMLTag) -> str:
            result: str = item.get_text()
            return result

        return utils.mapToList(parse, self.items)
