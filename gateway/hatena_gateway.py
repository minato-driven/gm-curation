import os
import requests
from .gateway import Gateway
from html import escape as escape_xml
import markdown


class HatenaGateway(Gateway):
    def __init__(self):
        self.domain = os.getenv("HATENA_DOMAIN")
        self.username = os.getenv("HATENA_USERNAME")
        self.blog_id = os.getenv("HATENA_BLOG_ID")
        self.api_key = os.getenv("HATENA_API_KEY")
        self.endpoint = f"{self.domain}/{self.username}/{self.blog_id}/atom/entry"
        print(self.endpoint, self.username, self.api_key, self.blog_id)

    def post(
        self, title: str, markdown_content: str, categories: list[str]
    ) -> requests.Response:
        content = markdown.markdown(
            markdown_content, extensions=["extra", "codehilite"]
        )
        # XMLテンプレート作成
        xml = '<?xml version="1.0" encoding="utf-8"?>'
        xml += '<entry xmlns="http://www.w3.org/2005/Atom" '
        xml += 'xmlns:app="http://www.w3.org/2007/app">'
        xml += f"<title>{escape_xml(title)}</title>"
        xml += f'<content type="text/markdown">{escape_xml(content)}</content>'
        for category in categories:
            xml += f'<category term="{escape_xml(category)}" />'
        xml += "</entry>"
        # APIリクエストの実行
        headers = {"Content-Type": "application/atom+xml; charset=utf-8"}
        self.log(xml)
        response = requests.post(
            self.endpoint,
            data=xml.encode("utf-8"),
            auth=(self.username, self.api_key),
            headers=headers,
        )
        self.log(str(response))
        return response
