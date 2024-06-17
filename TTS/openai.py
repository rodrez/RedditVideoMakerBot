import random

from openai import OpenAI
from utils import settings

voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]


class OpenAITTS:
    def __init__(self):
        self.max_chars = 5000
        self.voices = voices

    def random_voice(self):
        return random.choice(self.voices)

    def run(self, text, filepath, random_voice: bool = False):
        if random_voice:
            voice = self.random_voice()
        else:
            voice = str(settings.config["settings"]["tts"]["openai_voice_name"])

        api_key = settings.config["settings"]["tts"]["openai_api_key"]
        if not api_key:
            raise ValueError(
                "You didn't set an OpenAI API key! Please set the config variable openai_api_key to a valid API key."
            )

        client = OpenAI(api_key=api_key)

        response = client.audio.speech.create(
            model="tts-1",
            voice="echo",  # Ensuring the voice is in lowercase as per API requirements
            input=text,
        )
        response.stream_to_file(filepath)
