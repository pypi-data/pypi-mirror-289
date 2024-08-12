"""
This script fetches the data from Creatio for the previous week
and prints the count of records in the necessary collections
for each environment in the 'environments.json' file.

@file: main.py
@author: Alejandro Gonzalez Momblan
@date: 2024-05-15
@license: GNU General Public License v3.0
"""

import ast
import sys
from datetime import datetime, timedelta
from pathlib import Path

from creatio_odata_api.api import DEBUG, CreatioODataAPI
from creatio_odata_api.utils import print_exception
from rich import print  # pylint: disable=redefined-builtin
from rich.traceback import install


from .api import fetch_data_in_weekly_intervals, get_first_day_of_previous_week


def read_environments_file(file_path: str | Path) -> dict[str, dict[str, str]]:
    """
    Read the environments file

    The file content must be a JSON with the following format:
    {
        "url": {
            "username": "username",
            "password": "password"
        }
    }

    Args:
        file_path (str): The path to the environments file

    Returns:
        dict[str, dict[str, str]]: The environments dictionary
    """
    data_file: Path = Path(file_path)
    content: str = data_file.read_text(encoding="utf-8")

    try:
        envs = ast.literal_eval(content)
    except Exception as e:
        print_exception(e, "Error reading environments file")
        return {}

    return envs


def main() -> None:
    """
    Main function
    """
    install(show_locals=DEBUG)

    args: list[str] = sys.argv[1:]
    # Read arguments from the command line
    if not args:
        print("No arguments provided")
        return

    file_path: str = args[0]
    if not Path(file_path).exists():
        print(f"File not found: {file_path}")
        return

    environments: dict[str, dict[str, str]] = read_environments_file(file_path)
    if not environments:
        help_msg = """
Please make sure the file is in the correct format. The file content must be a JSON with the following format:
    {
        "url": {
            "username": "username",
            "password": "password"
        }
    }
        """
        print(help_msg)
        return

    # Get first day of the previous week
    start_date: datetime = get_first_day_of_previous_week()
    end_date: datetime = start_date + timedelta(days=7)
    print(start_date, end_date)

    api_calls: int = 0  # Counter for the number of API calls made
    for url, data in environments.items():
        print(f"------------ {url} ------------")
        api = CreatioODataAPI(base_url=url)
        try:
            # Authenticate with the API
            api.authenticate(username=data["username"], password=data["password"])
        except Exception as e:  # pylint: disable=broad-except
            print_exception(e, f"Unable to authenticate with {url}")
            continue
        # Fetch data in weekly intervals
        fetch_data_in_weekly_intervals(api, start_date, end_date)
        api_calls += api.api_calls

    print("Number of API calls made: ", api_calls)


if __name__ == "__main__":
    main()
