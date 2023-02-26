import openai
import os


class OpenAI:
    def start_prompt(self, prompt):
        openai.api_key = os.getenv("OPEN_API_KEY")
        response = openai.Completion.create(
            engine="text-davinci-003", prompt=prompt, n=1, stop=None, max_tokens=4000
        )
        return response.choices[0].text

