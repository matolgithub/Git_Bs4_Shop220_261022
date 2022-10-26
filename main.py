import requests
from fake_headers import Headers
from pprint import pprint
from bs4 import BeautifulSoup

URL = "https://shop220.ru/svetodiodnye-lampy-led.htm"
# url = "https://habr.com/ru/news/"
HEADERS = Headers(browser="chrom", os="win", headers=True).generate()


# HEADERS = {"Accept": "*/*",
#            "Accept-Encoding": "gzip, deflate, br",
#            "Accept-Language": "en-US;q=0.5,en;q=0.3",
#            "Cache-Control": "max-age=0",
#            "Connection": "keep-alive",
#            "DNT": "1",
#            "Referer": "https://google.com",
#            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                          "(KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}


def get_function():
    lamp_groups_list = []
    # response = requests.get(url=url, headers=HEADERS)
    # response.raise_for_status()  # raises exception when not a 2xx response
    # print(f"The requests status is: {response.status_code}.")
    # pprint(HEADERS)
    # if response.status_code != 204:
    #     pprint(response)
    page = requests.get(url=URL, headers=HEADERS)
    soup = BeautifulSoup(page.text, "html.parser")
    all_lamp_groups = soup.find_all('a', class_="label")
    pprint(all_lamp_groups)
    print(len(all_lamp_groups))
    for num, data in enumerate(all_lamp_groups):
        #     lamp_groups_list.append(data.text)
        # pprint(lamp_groups_list)
        print(num + 1, data.text)


def main():
    get_function()


if __name__ == "__main__":
    main()
