import requests
import openai
import os
import json
from requests.structures import CaseInsensitiveDict


class Imagine:
    def start_imagine(self, prompt):
        openai.api_key = os.getenv("OPEN_API_KEY")

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        headers["Authorization"] = f"Bearer {openai.api_key}"

        initial_data = {"prompt": prompt, "num_images": 1}
        data = json.dumps(initial_data)

        response = requests.post(
            "https://api.openai.com/v1/images/generations", headers=headers, data=data
        )
        if response.status_code != 200:
            raise ValueError("Failed to generate image: " + response.text)

        response_json = response.json()
        if "data" not in response_json or len(response_json["data"]) == 0:
            raise ValueError("No image URL found in response: " + response.text)

        image_url = response_json["data"][0]["url"]
        image = requests.get(image_url).content
        with open(f"{prompt}.jpg", "wb") as f:
            f.write(image)
