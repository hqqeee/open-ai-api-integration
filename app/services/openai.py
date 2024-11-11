from openai import OpenAI
from flask import current_app
import json


class OpenAIClient:

    _instance = None

    _sessions = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(OpenAIClient, cls).__new__(cls, *args, **kwargs)
            cls._instance.client = OpenAI(api_key=current_app.config['OPENAI_API_KEY'])
        return cls._instance

    def get_openai_response(self, question):
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": question,
                    }
                ],
                model=current_app.config['OPENAI_MODEL'],
            )
            api_answer = response.choices[0].message.content
            return api_answer
        except Exception as e:
            return f"Error: {str(e)}"

    def _get_openai_response(self, question, session_key):
        try:
            conversation_history = self._sessions[session_key]
            conversation_history.append({"role": "user", "content": question})
            response = self._get_openai_response(json.dumps(conversation_history))
            conversation_history.append({"role": "assistant", "content": response})
            return response
        except Exception as e:
            return f"Error: {str(e)}"
