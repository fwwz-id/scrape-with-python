from bs4.element import ResultSet, Tag, NavigableString
from typing import Iterable, Optional, Callable, Any, Union
from variables.types import HTMLTags, HTMLTag, StrDict


def getChildrenFrom(items: Union[ResultSet, Tag, NavigableString], tag: str, attrs: StrDict = {}) -> HTMLTags:
    """Function that helps extract children
        from a bs4.element.ResultSet

        :param items: A bs4.element.ResultSet
        :param tag: HTML's valid tag, such as: `p, a, span`
        :param attrs: HTML's Attribute, helps to get specific HTML element with attributes
        :rtype: list[bs4.element.Tag | bs4.element.NavigableString]
        """
    result: HTMLTags = []

    items_type = type(items)

    temp: Optional[HTMLTag] = None

    isItems = items_type == ResultSet or items_type == list
    isItem = items_type == Tag or items_type == NavigableString

    if (isItems):
        item: Optional[HTMLTag] = None
        for item in items:
            temp = item.find(tag, attrs)

            if (temp != None):
                result.append(temp)

    elif (isItem):
        temp = items.find(tag, attrs)

        if (temp != None):
            result.append(temp)

    return result


def mapToList(func: Callable[[Any], Any], iterable: Iterable[Any]) -> list[Any]:
    return list(map(func, iterable))