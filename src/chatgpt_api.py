import openai
import openai.error
from typing import List, Dict
from config import OPENAI_API_KEY, MODEL
import logging
import time
import traceback
import tiktoken
from multiprocessing import Value
import rich
import rich_utils

logger = logging.getLogger(__name__)
console = rich.get_console()

SYSTEM_MESSAGE = (
    "You are a smart contract auditor. You will be asked questions related to code properties. "
    "You can mimic answering them in the background five times and provide me with the most frequently appearing answer. "
    "Furthermore, please strictly adhere to the output format specified in the question; there is no need to explain your answer."
)

encoder = tiktoken.encoding_for_model(MODEL)

tokens_sent = Value("d", 0)
tokens_received = Value("d", 0)


class Chat:
    def __init__(self) -> None:
        self.currentSession: List[Dict[str, str]] = []
        openai.api_key = OPENAI_API_KEY  # Set the OpenAI API key once during initialization
    
    def newSession(self) -> None:
        self.currentSession = []
    
    def sendMessages(self, message: str) -> str:
        self.currentSession.append({"role": "system", "content": SYSTEM_MESSAGE})
        self.currentSession.append({"role": "user", "content": message})
        while True:
            try:
                response = openai.ChatCompletion.create(
                    model=MODEL,  # Use the model from config.py
                    messages=self.currentSession,
                    temperature=0,
                    top_p=1.0
                )
                break
            except openai.error.RateLimitError:
                logger.warning("Trigger rate limit error, sleeping for 30 seconds")
                time.sleep(30)
            except openai.InvalidRequestError as e2:
                if e2.code == 'context_length_exceeded':
                    logger.error("Too long context, skipping")
                    return "KeySentence: "
                else:
                    logger.warning("Retrying due to InvalidRequestError")
            except openai.error.APIConnectionError:
                logger.warning("API Connection Error, retrying")
            except openai.error.Timeout:
                logger.warning("Timeout, retrying")
            except openai.error.APIError as e5:
                if "502" in e5._message:
                    logger.warning("502 Bad Gateway, retrying")
                    logger.warning(traceback.format_exc())

        global tokens_sent
        global tokens_received

        tokens_sent.value += len(encoder.encode(SYSTEM_MESSAGE))
        tokens_sent.value += len(encoder.encode(message))
        tokens_received.value += len(encoder.encode(response['choices'][0]['message']['content']))

        self.currentSession.append(response['choices'][0]['message'])

        console.print(rich_utils.make_response_panel(response['choices'][0]['message']['content'], "Response"))
        return response['choices'][0]['message']['content']
    
    def makeYesOrNoQuestion(self, question: str) -> str:
        prompt = f"{question}. Please answer in one word, yes or no."
        return prompt
    
    def makeCodeQuestion(self, question: str, code: str):
        prompt = f'Please analyze the following code, and answer the question "{question}"\n{code}'
        return prompt
