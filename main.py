import os
import datetime
import json
from dotenv import load_dotenv
from gateway.gemini_gateway import GeminiGateway
from gateway.x_gateway import XGateway

load_dotenv()

gateway = GeminiGateway(model_name="gemini-2.5-flash")
x_gateway = XGateway()
prompt = "こんにちは。疎通テストです。"
response = gateway.get_text_content(prompt)