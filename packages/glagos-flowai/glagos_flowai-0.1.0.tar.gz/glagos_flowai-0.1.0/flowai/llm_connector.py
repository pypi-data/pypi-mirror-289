import os
import anthropic
from openai import OpenAI
from groq import Groq
import google.generativeai as genai
import requests
import json
from typing import Generator, List
import traceback

class LLMConnector:
    def __init__(self, config, provider, model, system_prompt=None):
        self.config = config
        self.provider = provider
        self.model = model or config.get('DEFAULT', 'default_model', fallback='gpt-3.5-turbo')
        self.system_prompt = system_prompt
        self.setup_api_keys()
        self.openai_client = OpenAI(api_key=self.config.get('DEFAULT', 'openai_api_key', fallback=''))
        self.anthropic_client = anthropic.Anthropic(api_key=self.config.get('DEFAULT', 'anthropic_api_key', fallback=''))
        self.groq_client = Groq(api_key=self.config.get('DEFAULT', 'groq_api_key', fallback=''))
        genai.configure(api_key=self.config.get('DEFAULT', 'google_api_key', fallback=''))

    def setup_api_keys(self):
        for key in ['openai_api_key', 'anthropic_api_key', 'groq_api_key', 'google_api_key']:
            if key not in self.config['DEFAULT'] or not self.config['DEFAULT'][key]:
                self.config['DEFAULT'][key] = os.environ.get(key.upper(), '')

    def get_available_models(self) -> List[str]:
        try:
            if self.provider == "openai":
                return self.get_openai_models()
            elif self.provider == "anthropic":
                return self.get_anthropic_models()
            elif self.provider == "ollama":
                return self.get_ollama_models()
            elif self.provider == "groq":
                return self.get_groq_models()
            elif self.provider == "google":
                return self.get_google_models()
            else:
                raise ValueError(f"Unsupported provider: {self.provider}")
        except Exception as e:
            print(f"Error fetching models for {self.provider}: {str(e)}")
            print("Traceback:")
            traceback.print_exc()
            return ["Error fetching models"]

    def get_openai_models(self) -> List[str]:
        try:
            openai_models = self.openai_client.models.list()
            return [model.id for model in openai_models.data if model.id.startswith("gpt")]
        except Exception as e:
            print(f"Error fetching OpenAI models: {str(e)}")
            return ["Error fetching models"]

    def get_anthropic_models(self) -> List[str]:
        # Anthropic doesn't provide a method to list models via API
        # We'll return a list of known models
        # Claude 3.5 Sonnet: claude-3-5-sonnet-20240620
        # Claude 3 Opus: claude-3-opus-20240229
        # Claude 3 Sonnet: claude-3-sonnet-20240229
        # Claude 3 Haiku: claude-3-haiku-20240307

        return ["claude-3-5-sonnet-20240620", "claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240307"]

    def get_ollama_models(self) -> List[str]:
        try:
            ollama_url = "http://localhost:11434/api/tags"
            response = requests.get(ollama_url)
            if response.status_code == 200:
                ollama_models = response.json().get('models', [])
                return [model['name'] for model in ollama_models]
            else:
                raise Exception(f"HTTP {response.status_code}: {response.text}")
        except Exception as e:
            print(f"Error fetching Ollama models: {str(e)}")
            return ["Error fetching models"]

    def get_groq_models(self) -> List[str]:
        try:
            groq_models = self.groq_client.models.list()
            return [model.id for model in groq_models.data]
        except Exception as e:
            print(f"Error fetching Groq models: {str(e)}")
            return ["Error fetching models"]

    def get_google_models(self) -> List[str]:
        try:
            google_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            return google_models
        except Exception as e:
            print(f"Error fetching Google models: {str(e)}")
            return ["Error fetching models"]

    def send_prompt(self, prompt: str, debug: bool = False) -> Generator[str, None, None]:
        try:
            if self.provider == "openai":
                yield from self.send_prompt_openai(prompt, debug)
            elif self.provider == "anthropic":
                yield from self.send_prompt_anthropic(prompt, debug)
            elif self.provider == "ollama":
                yield from self.send_prompt_ollama(prompt, debug)
            elif self.provider == "groq":
                yield from self.send_prompt_groq(prompt, debug)
            elif self.provider == "google":
                yield from self.send_prompt_google(prompt, debug)
            else:
                raise ValueError(f"Unsupported provider: {self.provider}")
        except Exception as e:
            yield f"Error: {str(e)}"
            print("Traceback:")
            traceback.print_exc()

    def send_prompt_openai(self, prompt: str, debug: bool = False) -> Generator[str, None, None]:
        try:
            if debug:
                print(f"Debug: Sending prompt to OpenAI:\n{prompt}")
            stream = self.openai_client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                stream=True
            )
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"Error: {str(e)}"

    def send_prompt_anthropic(self, prompt: str, debug: bool = False) -> Generator[str, None, None]:
        try:
            if debug:
                print(f"Debug: Sending prompt to Anthropic:\n{prompt}")
            stream = self.anthropic_client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=self.system_prompt,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                stream=True
            )
            for chunk in stream:
                if chunk.type == 'content_block_delta':
                    yield chunk.delta.text
        except Exception as e:
            yield f"Error: {str(e)}"

    def send_prompt_ollama(self, prompt: str, debug: bool = False) -> Generator[str, None, None]:
        try:
            if debug:
                print(f"Debug: Sending prompt to Ollama:--------------\n{prompt}\n--------------\n")
            ollama_url = "http://localhost:11434/api/generate"
            full_prompt = f"{self.system_prompt}\n\nHuman: {prompt}\n\nAssistant:"
            response = requests.post(ollama_url, json={"model": self.model, "prompt": full_prompt}, stream=True)
            for line in response.iter_lines():
                if line:
                    data = json.loads(line)
                    if 'response' in data:
                        yield data['response']
        except Exception as e:
            yield f"Error: {str(e)}"

    def send_prompt_groq(self, prompt: str, debug: bool = False) -> Generator[str, None, None]:
        try:
            if debug:
                print(f"Debug: Sending prompt to Groq:\n{prompt}")
            stream = self.groq_client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                stream=True
            )
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"Error: {str(e)}"

    def send_prompt_google(self, prompt: str, debug: bool = False) -> Generator[str, None, None]:
        try:
            if debug:
                print(f"Debug: Sending prompt to Google:\n{prompt}")
            model = genai.GenerativeModel(self.model)
            response = model.generate_content(prompt, stream=True)
            for chunk in response:
                if chunk.text:
                    yield chunk.text
        except Exception as e:
            yield f"Error: {str(e)}"