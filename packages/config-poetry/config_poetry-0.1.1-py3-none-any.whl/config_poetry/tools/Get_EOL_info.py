#!/bin/python

"""
capture the data from 
https://www.paloaltonetworks.com/services/support/end-of-life-announcements/end-of-life-summary
TODO: 
GP, and panorama plugin version capture
Limitation:
M-100 hardcoded, 
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import re


def get_raw_sw_eol_data():

    # Define the URL
    url = "https://www.paloaltonetworks.com/services/support/end-of-life-announcements/end-of-life-summary"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the response
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the table with the id 'pan-os-panorama'
        table = soup.find("table", {"id": "pan-os-panorama"})

        if table:
            # Extract the rows of the table
            rows = table.find_all("tr")

            # Initialize a dictionary to store the table data
            table_data = {}

            # Iterate over the rows and extract the cells
            for row in rows[3:]:
                cells = row.find_all("td")
                if len(cells) == 3:  # Ensure there are exactly 3 columns
                    version = cells[0].get_text(strip=True).replace("+", "")
                    release_date_str = cells[1].get_text(strip=True)
                    eol_date_str = cells[2].get_text(strip=True)
                    # Convert the dates to the desired format
                    try:
                        release_date = datetime.strptime(
                            release_date_str, "%B %d, %Y"
                        ).strftime("%Y-%m-%d")
                        eol_date = datetime.strptime(
                            eol_date_str, "%B %d, %Y"
                        ).strftime("%Y-%m-%d")
                    except ValueError as err:
                        # Store the data in the dictionary
                        # skip header
                        print(err)
                    table_data[version] = {
                        "Release_Date": release_date,
                        "End-of-Life_Date": eol_date,
                        "Exceptions": [],
                    }

            # # Print the extracted data
            # for version, dates in table_data.items():
            #     print(f"Version: {version}, Release Date: {dates['Release_Date']}, End-of-Life Date: {dates['End-of-Life_Date']}")
            with open("PANOS_EOL.json", "w") as json_file:
                json.dump(table_data, json_file, indent=2)
        else:
            print("Couldn't find the table.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


def clean_os(os_str):
    # Remove unwanted characters and strip whitespace
    return re.sub(r"[^\w\s\-\.]", "", os_str).strip()


def get_raw_hw_eol_data():
    url = "https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware-end-of-life-dates"
    exceptions = """
    + PAN-OS 8.1 will be supported on PA-200, PA-500, PA-5000 Series and M-100 products until their respective hardware end-of-life dates. On all other products, PAN-OS 8.1 will be supported until the date listed on the software end-of-life summary page.
    * Any M-100 appliances that have been upgraded to 32 GB memory (from the default 16 GB memory) will support software releases up to PAN-OS 9.1
    ++ PAN-OS 9.1 will be supported on the PA-3000 Series until that product's respective hardware end-of-life date. On all other products, PAN-OS 9.1 will be supported until the date listed on the software end-of-life summary page.
    ^ PAN-OS 10.0 will be supported on the product(s) shown on this row until the end-of-life date listed on this row. For all other products, PAN-OS 10.0 will be supported until the date listed on the software end-of-life summary page.
    ‡ PAN-OS 10.1 will be supported on the product(s) shown on this row until the end-of-life date listed on this row. For all other products, PAN-OS 10.1 will be supported until the date listed on the software end-of-life summary page.
    ^^ PAN-OS 10.2 will be supported on the product(s) shown on this row until the end-of-life date listed on this row. For all other products, PAN-OS 10.2 will be supported until the date listed on the software end-of-life summary page.
    ^^^ PAN-OS 11.1 will be supported on the product(s) shown on this row until the end-of-life date listed on this row. For all other products, PAN-OS 11.1 will be supported until the date listed on the software end-of-life summary page."""

    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the response
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the table
        table = soup.find("table", {"class": "table table-striped table-hover"})

        if table:
            # Extract the rows of the table
            rows = table.find_all("tr")

            # Initialize a list to store the EOS data
            eos_data = []

            # Iterate over the rows, skipping the header
            for row in rows[1:]:
                cells = row.find_all("td")
                if len(cells) >= 6:  # Ensure there are at least 6 columns
                    end_of_sale_product = cells[0].get_text(strip=True)

                    end_of_life_date_str = cells[2].get_text(strip=True)
                    resources = (
                        cells[3].find("a")["href"] if cells[3].find("a") else None
                    )
                    # last_supported_os = clean_os(cells[4].get_text(strip=True))
                    last_supported_os = cells[4].get_text(strip=True)
                    recommended_replacement = cells[5].get_text(strip=True)

                # Convert dates to YYYY-MM-DD format
                date_str = re.sub(r"(\d+)(st|nd|rd|th)", r"\1", end_of_life_date_str)
                try:
                    # Handle full month names
                    end_of_life_date = datetime.strptime(
                        date_str, "%B %d, %Y"
                    ).strftime("%Y-%m-%d")
                except ValueError:
                    # Handle abbreviated month names
                    end_of_life_date = datetime.strptime(
                        date_str, "%b %d, %Y"
                    ).strftime("%Y-%m-%d")

                    # Store the extracted data in a dictionary
                eos_data.append(
                    {
                        "End_of_Sale_Product": end_of_sale_product,
                        "End_of_Life_Date": end_of_life_date,
                        "Resources": resources,
                        "Last_Supported_OS": last_supported_os,
                        "Recommended_Replacement": recommended_replacement,
                    }
                )

            # Dump the EOS data to a JSON file
            with open("HW_EOL_data.json", "w") as json_file:
                json.dump(eos_data, json_file, indent=2)

            # print("End-of-Sale data has been successfully written to 'hw_eos_data.json'")
        else:
            print("Couldn't find the table.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


get_raw_hw_eol_data()
get_raw_sw_eol_data()


# def update_sw_eol_data_refer_to_hw_eol():
#     with open("HW_EOL_data.json") as json_file:
#         hardware_eol_data = json.load(json_file)
#     with open("PANOS_EOL.json") as json_file:
#         software_eol_data = json.load(json_file)
#     for hw_eol_info in hardware_eol_data:
#         last_supported_os = hw_eol_info["Last_Supported_OS"]
#         if (
#             "+" in last_supported_os
#             or "*" in last_supported_os
#             or "‡" in last_supported_os
#             or "^" in last_supported_os
#         ):
#             software_version = last_supported_os.split()[1][:4]
#             if software_version in software_eol_data:
#                 # Create exception entry
#                 # TODO split the module name
#                 exception_entry = {
#                     "model": hw_eol_info["End_of_Sale_Product"],
#                     "description": "",
#                     "End_of_Life_Date": hw_eol_info["End_of_Life_Date"],
#                 }
#                 # Append the exception entry to the software EOL data
#                 software_eol_data[software_version]["Exceptions"].append(
#                     exception_entry
#                 )
#     # TODO hardcode for M100 (16GB) PAN-OS 8.1+
#     exception_entry = {
#         "type": "RAM",
#         "model": "M-100",
#         "module": "16GB",
#         "description": "(16GB) PAN-OS 8.1+",
#         "End_of_Life_Date": "2023-10-31",
#     }
#     software_eol_data["8.1"]["Exceptions"].append(exception_entry)
#     # TODO hardcode for M100 (32GB) PAN-OS 9.1+
#     exception_entry = {
#         "type": "RAM",
#         "model": "M-100",
#         "module": "32GB",
#         "description": "(32GB) PAN-OS 9.1",
#         "End_of_Life_Date": "2023-10-31",
#     }
#     software_eol_data["9.1"]["Exceptions"].append(exception_entry)

#     with open("PANOS_EOL_Plus_HW_EOL.json", "w") as json_file:
#         json.dump(software_eol_data, json_file, indent=2)
# update_sw_eol_data_refer_to_hw_eol()
