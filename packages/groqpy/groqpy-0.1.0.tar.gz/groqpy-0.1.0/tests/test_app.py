import unittest
from groqpy.groq_agent import GroqAgent
import logging


GROQ_API_KEY = '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'
GROQ_MODEL = 'llama3-70b-8192'
GROQ_TEMPERATURE = 0

logging.basicConfig(filename='test.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.WARNING)

class TestApp(unittest.TestCase):
    def test_app(self):
        agent = GroqAgent(api_key=GROQ_API_KEY)
        agent.ChatSettings(model=GROQ_MODEL, temperature=GROQ_TEMPERATURE)
        # loop '1' through '31' to test the agent's chat function
        for i in range(1, 300):
            print(i, '-', 'Agent:', agent.Chat(f'say a random sentence. do not say safe ever ', remember=False), flush=True)
            import time
            time.sleep(.5)
        self.assertTrue(True)
