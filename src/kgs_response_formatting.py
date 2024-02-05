from urllib.parse import urlparse


def kgs_response_formatting(response_dict: dict) -> list[dict]:
    """

    :param response_dict:
    :param query:
    :return:
    """
    list_of_entities: list = []

    if response_dict["itemListElement"]:
        for item_dict in response_dict["itemListElement"]:

            entity: dict = {
                "name": "",
                "urls": []
            }

            item = item_dict["result"]

            entity["name"] = item["name"]

            entity["urls"] = _get_urls(item)

            list_of_entities.append(entity)

    return list_of_entities


def _get_urls(item: dict) -> list[str]:
    """

    :param item:
    :return:
    """
    urls: list[str] = []

    for key in item.keys():

        # Check if the key is "url" - trusting it is a valid url
        if key == "url":

            urls.append(item[key])

        # If the value is string type, check if it's a valid url
        elif isinstance(item[key], str):

            result = urlparse(item[key])

            if result.scheme and result.netloc:

                urls.append(item[key])

        # if the item[key] is a dictionary pass back to itself for further investigation
        elif isinstance(item[key], dict):

            urls += _get_urls(item[key])

        # if the item[key] is a list, check each element, and if it's a dict do the same as in previous elif
        elif isinstance(item[key], list):

            for elem in item[key]:

                if isinstance(elem, dict):

                    urls += _get_urls(elem)

    return urls
