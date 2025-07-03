#!/usr/bin/env python3
""" """

import sys
import requests


def main():
    if len(sys.argv) == 2:
        location = sys.argv[1]
    else:
        print("Usage: python main.py <location>")
        sys.exit(1)
    url = f"https://wttr.in/{location}"
    response = requests.get(url)
    print(response.text)


if __name__ == "__main__":
    main()
