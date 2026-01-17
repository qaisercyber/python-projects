#This program will check multip websites whether they are down or up
import threading

import requests
import time


def check_url(url):
    try:
        response = requests.get(url , timeout=10)
        print(f" url: {url} is up with status code: {response.status_code}")
    except requests.exceptions.RequestException:
        print(f" url: {url} is down")


def get_websites():
    websites = []
    print("Enter the websites url(type done to finish)")

    while True:
        website = input("> ").strip()

        if website.lower()=="done":
            break
        if not website.startswith(("http://" , "https://")):
            website = "https://" + website

        websites.append(website)

    return websites

def main():
    websites = get_websites()

    if not websites:
        print("No websites entered")
        return

    threads = []

    start_time = time.time()

    for website in websites:
        thread = threading.Thread(target = check_url , args = (website,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    print(f" Completed in {end_time-start_time} seconds")


if __name__ == "__main__":
    main()







