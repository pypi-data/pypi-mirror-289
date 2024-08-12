from os import getenv

from openai import OpenAI
from loguru import logger

OPENAI_API_KEY = getenv("MEMICIAN_OPENAI_API_KEY")

class Rewriter:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def rewrite(self, text):
        result = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Explain this given meme in 15 words or less"},
                {"role": "user", "content": text},
            ],
            max_tokens=200,
        )
        return result.choices[0].message.content

class Structurer:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def structure(self, text):
        result = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                # TODO: Use JSON schema of the meme here
                {"role": "system", "content": "Structure this given text"},
                {"role": "user", "content": text},
            ],
            max_tokens=200,
        )
        return result.choices[0].message.content

if __name__ == "__main__":
    rewriter = Rewriter()
    logger.debug(rewriter.rewrite("distracted boyfriend meme"))
