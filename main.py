import os
import datetime
import json
from dotenv import load_dotenv
from gateway.gemini_gateway import GeminiGateway
from gateway.x_gateway import XGateway
from gateway.hatena_gateway import HatenaGateway

load_dotenv()

gemini_gw = GeminiGateway(model_name="gemini-2.5-flash")
hatena_gw = HatenaGateway()
prompt = "モテるための秘訣として記事を書きます。以下の要綱に従いJSONを返却しなさい"
prompt += "JSONのキーは以下の通りです\n"
prompt += "title: 記事のタイトル\n"
prompt += "content: 記事の内容\n"
prompt += "categories: 記事のカテゴリーの配列\n"
response = gemini_gw.get_json_content(prompt)
data = json.loads(response)
hatena_gw.post(data["title"], data["content"], data["categories"])
