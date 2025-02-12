# pip install aiohttp asyncio

import asyncio
import aiohttp


async def fetch(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)


# Example usage
if __name__ == '__main__':
    urls = [
        'https://www.example.com',
        'https://www.python.org',
        'https://www.asyncio.org'
    ]
    results = asyncio.run(fetch_all(urls))
    for url, content in zip(urls, results):
        if content:
            print(f"Fetched {len(content)} characters from {url}")
        else:
            print(f"Failed to fetch content from {url}")


# Why? This snippet demonstrates how to perform concurrent web requests using asyncio and aiohttp. It’s perfect for
# building scalable web scrapers, handling multiple HTTP requests efficiently, and improving performance in I/O-bound
# applications.
