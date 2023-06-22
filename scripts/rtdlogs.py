import asyncio
from pyppeteer import launch
import argparse


async def get_logs(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.content()

    element = await page.querySelector("#build-detail")

    text = await page.evaluate("e => e.innerText", element)

    print(text)

    await browser.close()


def main():
    parser = argparse.ArgumentParser(
        description="Get the logs from a readthedocs build"
    )
    parser.add_argument("url", help="The readthedocs URL")
    args = parser.parse_args()

    asyncio.run(get_logs(args.url))


if __name__ == "__main__":
    main()
