from typing import Optional
from requests import Response, post
from ..applications.codes import Code

class Notification:
    def __init__(self, text, url, **kwargs):
        self.text: str = text
        self.url = url
        self.application: Optional[int] = kwargs.get('application', None)
        self.event_id: Optional[int] = kwargs.get('event_id', None) 
        self.command_json:Optional[dict] = kwargs.get('command_json', None)
        self.custom_html_body:Optional[dict] = kwargs.get('custom_html_body', None)
        self.body: Optional[dict]= kwargs.get('body', None)

    def __finalize(self) -> None:
        self.body = {
            "text": self.text,
            "application": Code.NOT_SET.value,
            "event_id": 0,
            "command_json": "",
            "custom_html_body": ""
        }

        if (self.application):
            self.body['application'] = self.application

        if (self.event_id):
            self.body['event_id'] = self.event_id

        if (self.command_json):
            self.body['command_json'] = str(self.command_json)
        
        if (self.custom_html_body):
            self.body['custom_html_body'] = str(self.custom_html_body)

    def notify(self) -> Response:
        self.__finalize()
        return post(self.url, data=self.body, verify=False)

