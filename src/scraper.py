from typing import Union, Optional
from cloudscraper import create_scraper, requests

from helpers import HTMLAttributeParser, getChildrenFrom, writeToCSV, writeToExcel
from variables import attributes as attr, baseUrl, params, headers
from variables.types import HTMLTag, StrDict
from bs4 import BeautifulSoup


def createRequest(url: str = '', params: StrDict = {}) -> requests.Response:
    scraper = create_scraper(disableCloudflareV1=True, debug=True, delay=2)
    response: requests.Response = scraper.get(url=url, params=params, headers=headers)

    return response


def getProductHavePrice(item: HTMLTag) -> Union[HTMLTag, None]:
    result = item.find("span", attrs=attr.priceContainerAttributes)

    if (type(result) != None):
        return result

    return None


def getData(url: str, params: StrDict) -> dict[str, list[str]]:
    response = createRequest(url, params)
    soup = BeautifulSoup(response.text, parser='lxml')

    # define containers
    containers = soup.find_all("div", attrs=attr.searchResultContainerAttributes)

    containers = list(filter(getProductHavePrice, containers))
    pricesContainer = getChildrenFrom(containers, "span", attr.priceContainerAttributes)

    # extract container
    images = getChildrenFrom(containers, "img", attr.imageAttributes)

    titles = getChildrenFrom(containers, "h2")
    titles = getChildrenFrom(titles, "span")

    prices = getChildrenFrom(pricesContainer, "span", attr.priceAttributes)

    # extract data
    images = HTMLAttributeParser(images).getFromImgTag("src")
    titles = HTMLAttributeParser(titles).getTextFromTag()
    prices = HTMLAttributeParser(prices).getTextFromTag()

    result = {
        "images": images,
        "titles": titles,
        "prices": prices,
    }

    return result


def run(paginations: int = 20) -> None:
    result: dict[str, list[str]] = {
        "images": [],
        "titles": [],
        "prices": []
    }

    pagination: int = 1

    for pagination in range(paginations):
        paramsWithPagination = {
            **params,
            "page": f"{pagination}",
        }

        data = getData(baseUrl, paramsWithPagination)

        result["images"].extend(data["images"])
        result["titles"].extend(data["titles"])
        result["prices"].extend(data["prices"])

    filename = "computer-monitors"

    writeToCSV(filename, result)
    writeToExcel(filename, result)


run()
