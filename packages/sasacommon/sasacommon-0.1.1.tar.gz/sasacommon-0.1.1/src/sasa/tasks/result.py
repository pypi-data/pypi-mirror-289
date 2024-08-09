from __future__ import annotations
from datetime import datetime
from typing import Optional
from .severity import Severity
from sasa.applications.codes import Code
import json
import os


class Result:
    ''' Task result hander for Sasa Tasks '''

    def __init__(self, name):
        self.name: str = self.__simplify_name(name)
        self.application: int = Code.NOT_SET.value
        self.stack: Optional[str] = os.environ.get('STACK', 'Stack not set!') 
        self.success: bool = True
        self.message: Optional[dict] = {}
        self.__errors: list[str] = []
        self.start_time: datetime = datetime.now()
        self.end_time: Optional[datetime] = None
        self.imported_rows: Optional[int] = None
        self.deleted_rows: Optional[int] = None
        self.severity: Severity = Severity.MODERATE

        self.payload = {
            "name": self.name,
            "stack": self.stack,
            "start": str(self.start_time),
            "success": self.success,
        }

    def __str__(self) -> str:
        self.__finalize()
        return json.dumps(self.payload, indent=4)

    @staticmethod
    def __simplify_name(name):
        if name.find('.'):
            return name[0:name.find('.')] + name[name.rfind('.'):]
        return name

    def add_errors(self, *errors) -> None:
        for error in errors:
            self.__errors.append(error)

    def __finalize(self) -> None:
        if not self.end_time:
            self.end_time = datetime.now()
            self.payload['end_time'] = str(self.end_time)

        if (len(self.__errors) > 0):
            self.payload['errors'] = self.__errors
            self.payload['success'] = False

        if (self.message):
            self.payload['message'] = self.message

        # is not None --> to save imported_rows and deleted_rows even if they are 0
        if (self.imported_rows is not None):
            self.payload['imported_rows'] = self.imported_rows

        if (self.deleted_rows is not None):
            self.payload['deleted_rows'] = self.deleted_rows

        self.payload['severity'] = str(self.severity)
        self.payload['application'] = self.application

        return

    def to_json(self) -> dict:
        self.__finalize()
        return self.payload
    
    @staticmethod 
    def from_json(json_str: str) -> Result:
        data = json.loads(json_str)

        result = Result(data['name'])
        result.application = data.get('application', Code.NOT_SET)
        result.stack = data.get('stack','')
        result.success = data.get('success','')
        result.message = data.get('message',{})
        result.__errors = data.get('errors','')
        result.start_time = data.get('start_time','')
        result.end_time = data.get('end_time','')
        result.imported_rows = data.get('imported_rows','')
        result.deleted_rows = data.get('deleted_rows','')
        result.severity = data.get('severity','')

        return result
        
    @staticmethod 
    def from_dict(json_dict: dict) -> Result:

        result = Result(json_dict.get('name'))
        result.application = json_dict.get('application', Code.NOT_SET)
        result.stack = json_dict.get('stack','')
        result.success = json_dict.get('success','')
        result.message = json_dict.get('message',{})
        result.__errors = json_dict.get('errors','')
        result.start_time = json_dict.get('start_time','')
        result.end_time = json_dict.get('end_time','')
        result.imported_rows = json_dict.get('imported_rows','')
        result.deleted_rows = json_dict.get('deleted_rows','')
        result.severity = json_dict.get('severity','')

        return result
