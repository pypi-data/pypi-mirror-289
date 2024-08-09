import time
from typing import Dict
import aiohttp
from . import val


class DataSender:
    def __init__(self):
        self.base_url = val.url
        self.start_time = time.time()

    async def send_metric(self, data: Dict):
        url = f"{self.base_url}/api/v1/experiment/"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, json=data, ssl=False, timeout=10):
                    pass
            except aiohttp.ClientError as e:
                print(f"Request failed: {e}")
                return None
