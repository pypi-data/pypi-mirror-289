#!/usr/bin/env python

import shodan
import random
import ipaddress
import argparse
import webbrowser

import os
from pathlib import Path
import csv
import random


parser = argparse.ArgumentParser()
parser.add_argument("-b", "--browser", help="Open found link in a browser",
                    action="store_true")
parser.add_argument("key", help="Your shodan API key")
args = parser.parse_args()

def generate_random_ip():
    random_ip = ipaddress.IPv4Address(random.randint(0, 2 ** 32 - 1))
    return str(random_ip)


# set a limit on the tries
def get_info():
    for i in range(0, 100):
        while True:
            try:
                ip = generate_random_ip()

                api = shodan.Shodan(args.key)

                # print(f"searching {ip}")

                # Lookup the host
                host = api.host(ip)

                # Print general info
                print("""
                IP: {}
                Organization: {}
                Operating System: {}
                """.format(host['ip_str'], host.get('org', 'n/a'),
                           host.get('os', 'n/a')))

                # Print all banners
                for item in host['data']:
                    print("""
                    Banner: {}
                    """.format(item['port'], item['data']))

                if args.browser:
                    webbrowser.open_new_tab(f"https://shodan.io/host/{ip}")

                break

            except Exception:
                continue

        break


if __name__ == "__main__":
    get_info()
