from typing import Dict, List, TypeAlias
from bs4 import Tag, NavigableString

HTMLTag: TypeAlias = Tag | NavigableString
HTMLTags = List[HTMLTag]

StrDict = Dict[str, str]
