import google.generativeai as genai
import json
import os

class CogniCore:
    def __init__(self, api_key, config_file=None, debug=True):
        if debug:
            print("Debug mode is enabled, all the status will be printed.")
        if not api_key:
            raise ValueError("API key is required")
        genai.configure(api_key=api_key)

        # If no config file is provided, create a default one
        if config_file is None:
            project_dir = os.getcwd()
            if debug:
                print(project_dir)
            config_file = os.path.join(project_dir, 'config.json')

        if os.path.exists(config_file):
            if debug:
                print("Config file found! Loading...")
            try:
                with open(config_file) as f:
                    self.config = json.load(f)
                # Empty check
                if not self.config:
                    raise ValueError("Config file is empty")
                # Value check
                required_keys = ['model_name', 'generation_config', 'system_instruction', 'safety_settings']
                if not all(key in self.config for key in required_keys):
                    raise ValueError("Config file is missing required keys")
            except (json.JSONDecodeError, ValueError):
                # If value incomplete
                if debug:
                    print("Config file is empty, malformed, or missing required keys. Using default config.")
                    print("Token limiter set to 512 by default. Change this or remove this key and value for more generation.")
                default_config = {
                    'model_name': 'gemini-1.5-pro-latest',
                    'generation_config': {
                        "temperature": 1,
                        "top_p": 1,
                        "top_k": 1,
                        "max_output_tokens": 512,
                    },
                    'system_instruction': 'You are a virtual assistant, your job is to be as informative as possible. Try to be neutral on your answers.',
                    'safety_settings': [
                        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
                    ]
                }
                with open(config_file, 'w') as f:
                    json.dump(default_config, f, indent=4)
                self.config = default_config
                if debug:
                    print("Config created! Dont forget to change the system instruction!")
        else:
            # If the config file does not exist, create a default one
            if debug:
                print("Creating config file.")
                print("Token limiter set to 512 by default. Change this or remove this key and value for more generation.")
            default_config = {
                'model_name': 'gemini-1.5-pro-latest',
                'generation_config': {
                    "temperature": 1,
                    "top_p": 1,
                    "top_k": 1,
                    "max_output_tokens": 512,
                },
                'system_instruction': 'You are a virtual assistant, your job is to be as informative as possible. Try to be neutral on your answers.',
                'safety_settings': [
                    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
                ]
            }
            with open(config_file, 'w') as f:
                json.dump(default_config, f, indent=4)
            self.config = default_config
            if debug:
                print("Config created! Dont forget to change the system instruction!")

        # Create a model
        self.model = genai.GenerativeModel(model_name=self.config['model_name'],
                                           generation_config=self.config['generation_config'],
                                           system_instruction=self.config['system_instruction'],
                                           safety_settings=self.config['safety_settings'])

    def generate_content(self, prompt):
        if not prompt:
            raise ValueError("Prompt is required")
        response = self.model.generate_content(prompt)
        return response.text

    def upload_to_gemini(self, path, mime_type=None):
        if not path:
            raise ValueError("Path is required")
        file = genai.upload_file(path, mime_type=mime_type)
        print(f"Uploaded file '{file.display_name}' as: {file.uri}")
        return file