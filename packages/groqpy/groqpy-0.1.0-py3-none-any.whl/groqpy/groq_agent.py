import re
import time
from typing import Any, overload
import requests
import logging

class GroqAgent():
    '''
    Create a GroqAgent object to interact with the Groq API.
    Automatically handles chat for the agent.
    '''
    def __init__(self,
        *,
        api_key: str,
        model: str | None = None,
        frequency_penalty: float | None = None,
        function_call: str | dict | None = None,
        functions: list | None = None,
        logit_bias: dict | None = None,
        logprobs: bool | None = None,
        max_tokens: int | None = None,
        n: int | None = None,
        parallel_tool_calls: bool | None = None,
        presence_penalty: float | None = None,
        response_format: dict | None = None,
        seed: int | None = None,
        stop: str | list | None = None,
        stream: bool | None = None,
        stream_options: dict | None = None,
        temperature: float | None = None,
        tool_choice: str | dict | None = None,
        tools: list | None = None,
        top_logprobs: int | None = None,
        top_p: float | None = None,
        user: str | None = None,
    ):
        self.Set_Agent_Settings(api_key=api_key, model=model, frequency_penalty=frequency_penalty, function_call=function_call,
            functions=functions, logit_bias=logit_bias, logprobs=logprobs, max_tokens=max_tokens, n=n,
            parallel_tool_calls=parallel_tool_calls, presence_penalty=presence_penalty, response_format=response_format,
            seed=seed, stop=stop, stream=stream, stream_options=stream_options, temperature=temperature,
            tool_choice=tool_choice, tools=tools, top_logprobs=top_logprobs, top_p=top_p, user=user)
        self.chat_history: list = []

    def Set_Agent_Settings(self,
        *,
        api_key: str | None = None,
        model: str | None = None,
        frequency_penalty: float | None = None,
        function_call: str | dict | None = None,
        functions: list | None = None,
        logit_bias: dict | None = None,
        logprobs: bool | None = None,
        max_tokens: int | None = None,
        n: int | None = None,
        parallel_tool_calls: bool | None = None,
        presence_penalty: float | None = None,
        response_format: dict | None = None,
        seed: int | None = None,
        stop: str | list | None = None,
        stream: bool | None = None,
        stream_options: dict | None = None,
        temperature: float | None = None,
        tool_choice: str | dict | None = None,
        tools: list | None = None,
        top_logprobs: int | None = None,
        top_p: float | None = None,
        user: str | None = None,
    ):
        '''
        Used to update the settings.
        '''
        self.api_key = api_key or getattr(self, 'api_key', None)
        self.model = model or getattr(self, 'model', None)
        self.frequency_penalty = frequency_penalty or getattr(self, 'frequency_penalty', None)
        self.function_call = function_call or getattr(self, 'function_call', None)
        self.functions = functions or getattr(self, 'functions', None)
        self.logit_bias = logit_bias or getattr(self, 'logit_bias', None)
        self.logprobs = logprobs or getattr(self, 'logprobs', None)
        self.max_tokens = max_tokens or getattr(self, 'max_tokens', None)
        self.n = n or getattr(self, 'n', None)
        self.parallel_tool_calls = parallel_tool_calls or getattr(self, 'parallel_tool_calls', None)
        self.presence_penalty = presence_penalty or getattr(self, 'presence_penalty', None)
        self.response_format = response_format or getattr(self, 'response_format', None)
        self.seed = seed or getattr(self, 'seed', None)
        self.stop = stop or getattr(self, 'stop', None)
        self.stream = stream or getattr(self, 'stream', None)
        self.stream_options = stream_options or getattr(self, 'stream_options', None)
        self.temperature = temperature or getattr(self, 'temperature', None)
        self.tool_choice = tool_choice or getattr(self, 'tool_choice', None)
        self.tools = tools or getattr(self, 'tools', None)
        self.top_logprobs = top_logprobs or getattr(self, 'top_logprobs', None)
        self.top_p = top_p or getattr(self, 'top_p', None)
        self.user = user or getattr(self, 'user', None)

    # TODO: Remove this method in the next release.
    def ChatSettings(self,
        *,
        model: str | None = 'llama3-70b-8192',
        frequency_penalty: float | None = None,
        function_call: str | dict | None = None,
        functions: list | None = None,
        logit_bias: dict | None = None,
        logprobs: bool | None = None,
        max_tokens: int | None = None,
        n: int | None = None,
        parallel_tool_calls: bool | None = None,
        presence_penalty: float | None = None,
        response_format: dict | None = None,
        seed: int | None = None,
        stop: str | list | None = None,
        stream: bool | None = None,
        temperature: float | None = None,
        tool_choice: str | dict | None = None,
        tools: list | None = None,
        top_logprobs: int | None = None,
        top_p: float | None = None,
        user: str | None = None,
        extra_headers: Any | None = None,
        extra_query: Any | None = None,
        extra_body: Any | None = None,
        timeout: Any | None = None,
    ):
        '''
        DEPRECATED: Use Set_Agent_Settings instead.

        extra_headers, extra_query, extra_body, timeout are not used in this method.
        '''
        self.Set_Agent_Settings(model=model, frequency_penalty=frequency_penalty, function_call=function_call,
            functions=functions, logit_bias=logit_bias, logprobs=logprobs, max_tokens=max_tokens, n=n,
            parallel_tool_calls=parallel_tool_calls, presence_penalty=presence_penalty, response_format=response_format,
            seed=seed, stop=stop, stream=stream, temperature=temperature, tool_choice=tool_choice, tools=tools,
            top_logprobs=top_logprobs, top_p=top_p, user=user)

    def SystemPrompt(self, prompt: str):
        '''
        Use this method to add a system prompt to the chat history altering how the agent responds.
        example: 'Respond as a personal assistant.' or 'Respond as a customer service agent.'
        '''
        self.chat_history.append({
            "role": "system",
            "content": prompt
        })

    def Chat(self, message: str, *, remember: bool = True):
        '''
        Chat with the agent. The agent will respond to the message.

        Args:
            message (str): The message to send to the agent.
            remember (bool): Whether to remember the chat history. Default is True.
        '''
        response_message = self._post(error_message=[*self.chat_history, {"role": "user", "content": message}])
        if remember:
            self.chat_history.append({"role": "user", "content": message})
            self.chat_history.append(response_message)
        return response_message['content']

    def _post(self, *, error_message: list = None):
        '''
        POST request to the Groq API.
        '''
        URL = 'https://api.groq.com/openai/v1/chat/completions'
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }

        # Log disabled parameters FIXME: Fix this eventually
        if self.function_call is not None:
            logging.warning('\'function_call\' is currently not supported.')
        if self.functions is not None:
            logging.warning('\'functions\' is currently not supported.')
        if self.tool_choice is not None:
            logging.warning('\'tool_choice\' is currently not supported.')
        if self.tools is not None:
            logging.warning('\'tools\' is currently not supported.')

        body = {
            'messages': error_message,
            'model': self.model,
            'frequency_penalty': self.frequency_penalty,
            # 'function_call': self.function_call,
            # 'functions': self.functions,
            'logit_bias': self.logit_bias,
            'logprobs': self.logprobs,
            'max_tokens': self.max_tokens,
            'n': self.n,
            'parallel_tool_calls': self.parallel_tool_calls,
            'presence_penalty': self.presence_penalty,
            'response_format': self.response_format,
            'seed': self.seed,
            'stop': self.stop,
            'stream': self.stream,
            'stream_options': self.stream_options,
            'temperature': self.temperature,
            # 'tool_choice': self.tool_choice,
            # 'tools': self.tools,
            'top_logprobs': self.top_logprobs,
            'top_p': self.top_p,
            'user': self.user,
        }

        # NOTE: This 'while True' loop should not be broken using 'break' keyword.
        # NOTE: Must 'return' or 'raise' to exit the loop and a 'continue' keyword must be used for looping.
        loop_limit, loop_count = 3, 0
        while True and loop_count < loop_limit:
            loop_count += 1

            response = requests.post(URL, headers=headers, json=body)

            # Rate limit info
            rate_limit_info = {
                'limit_requests': response.headers.get('x-ratelimit-limit-requests'),
                'limit_tokens': response.headers.get('x-ratelimit-limit-tokens'),
                'remaining_requests': response.headers.get('x-ratelimit-remaining-requests'),
                'remaining_tokens': response.headers.get('x-ratelimit-remaining-tokens'),
                'reset_requests': response.headers.get('x-ratelimit-reset-requests'),
                'reset_tokens': response.headers.get('x-ratelimit-reset-tokens'),
            }

            try:
                # print all attributes of the response object
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                content = response.json()
                content_error = content.get('error', None)
                error_message = content_error.get('message', None)
                error_type = content_error.get('type', None)
                error_code = content_error.get('code', None)

                t_regex = r'(?<=Please try again in )(\d*?\.?\d*)(ms|s)'
                # Rate limit for tokens exceeded error handling
                if error_type == 'tokens' and error_code == 'rate_limit_exceeded':
                    match = re.search(t_regex, error_message)
                    time_str = match.group(1)
                    time_unit = match.group(2)
                    time_seconds = float(time_str) if time_unit == 's' else float(time_str) / 1000
                    logging.error(error_message)
                    time.sleep(time_seconds); continue
                
                # Rate limit for requests exceeded error handling
                if error_type == 'requests' and error_code == 'rate_limit_exceeded':
                    match = re.search(t_regex, error_message)
                    time_str = match.group(1)
                    time_unit = match.group(2)
                    time_seconds = float(time_str) if time_unit == 's' else float(time_str) / 1000
                    logging.error(error_message)
                    time.sleep(time_seconds); continue
                
                logging.error(content)
                raise e
            
            except Exception as e:
                logging.error(str(e))
                raise e
            
            response_json = response.json()

            # import json
            # print('\n', json.dumps(response_json, indent='\033[0m  '), '\n', flush=True)

            return response_json['choices'][0]['message']
        
            # NOTE: NEVER REMOVE THIS ERROR CHECK EVEN IF THE CODE IS UNREACHABLE
            raise Exception('Loop auto looped. \'continue\' must be used to loop.')
        # NOTE: NEVER REMOVE THIS ERROR CHECK EVEN IF THE CODE IS UNREACHABLE
        if loop_count >= loop_limit:
            raise Exception('Loop limit reached. Force termination.')
        # NOTE: NEVER REMOVE THIS ERROR CHECK EVEN IF THE CODE IS UNREACHABLE
        raise Exception('Loop exited. \'return\' or \'raise\' must be used to exit the loop.')
