#!/usr/bin/env python3
""" Module to fetch weather information from wttr.in """

import sys
import requests


def main():
    """ 
    Main function to fetch and display weather information for a given location.
    """
    if len(sys.argv) == 2:
        location = sys.argv[1]
    else:
        print("Usage: python main.py <location>")
        sys.exit(1)
    url = f"https://wttr.in/{location}"
    response = requests.get(url, timeout=10)
    print(response.text)


if __name__ == "__main__":
    main()
