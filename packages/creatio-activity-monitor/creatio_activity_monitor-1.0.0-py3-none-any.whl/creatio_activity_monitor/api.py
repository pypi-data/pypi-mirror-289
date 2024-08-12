from datetime import datetime, timedelta
from typing import Any

import requests
from creatio_odata_api.api import CreatioODataAPI
from rich import print  # pylint: disable=redefined-builtin


def send_api_request(
    api: CreatioODataAPI, collection: str, query: dict[str, str]
) -> Any:
    """
    Send an API request to get the count of records in a collection

    Args:
        api (CreatioODataAPI): The CreatioODataAPI object
        collection (str): The collection name
        query (dict[str, str]): The query parameters

    Returns:
        Any: The response from the API
    """
    response: requests.Response = api.get_collection_data(
        collection=f"{collection}/$count",
        params=query,
    )
    if "ï»¿" in response.text:
        result: str = response.text.replace("ï»¿", "")
    else:
        result = response.text

    if "<!DOCTYPE html" in result:
        print(f"[red]Error: Unable to fetch data from {collection}[/]")
    else:
        print(f"{collection} count: {result}")


def get_data_between_dates(
    api: CreatioODataAPI, start_date: datetime, end_date: datetime
) -> Any:
    """
    Get the data between two dates

    Args:
        api (CreatioODataAPI): The CreatioODataAPI object
        start_date (datetime): The start date
        end_date (datetime): The end date

    Returns:
        Any: The response from the API
    """
    date_init: str = start_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    date_end: str = end_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    query: dict[str, str] = {
        "$filter": f"CreatedOn ge {date_init} and CreatedOn lt {date_end} or "
        f"ModifiedOn ge {date_init} and ModifiedOn lt {date_end}"
    }
    if api.base_url == "https://totalenergies.creatio.com":
        collection = "UsrClaims"
        send_api_request(api, "UsrCargaAltas", query)
    else:
        collection = "Case"

    send_api_request(api, collection, query)


def fetch_data_in_weekly_intervals(
    api: CreatioODataAPI, start_date: datetime, end_date: datetime
) -> None:
    """
    Fetch data in weekly intervals

    Args:
        api (CreatioODataAPI): The CreatioODataAPI object
        start_date (datetime): The start date
        end_date (datetime): The end date
    """
    while start_date < end_date:
        end_date_weekly = start_date + timedelta(days=7)
        print(
            f"Getting data from {start_date.strftime('%Y-%m-%d')}"
            f" to {end_date.strftime('%Y-%m-%d')}"
        )
        get_data_between_dates(api, start_date, end_date_weekly)
        start_date = end_date_weekly


def get_first_day_of_previous_week() -> datetime:
    """
    Get the first day of the previous week

    Returns:
        datetime: The first day of the previous week
    """
    today: datetime = datetime.today()
    # Calculate the number of days to subtract to reach the previous week's Monday
    days_to_subtract = (today.weekday()) % 7 + 7
    # Subtract the days from today's date to get the first day of the previous week
    first_day_of_previous_week = today - timedelta(days=days_to_subtract)
    first_day_of_previous_week = first_day_of_previous_week.replace(
        hour=0, minute=0, second=0
    )
    return first_day_of_previous_week
