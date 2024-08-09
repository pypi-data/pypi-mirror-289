import os
import requests


class SMSManager:
    def __init__(self) -> None:
        token = os.environ.get("SMS_WS_TOKEN")
        # TODO: check that token and url are set and raise errore if not
        self.url = os.environ.get("SMS_WS")
        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Authorization": f"Token {token}",
        }

    def _call(self, payload: dict, endpoint: str):
        url = f"{self.url}/{endpoint}/"
        response = requests.post(url, data=payload, headers=self.headers)
        return response.text

    def send(self, recipient: str, text: str):
        return self._call(
            endpoint="send", payload={"recipient": recipient, "text": text}
        )

    def bulk_send(self, recipients: str | list, text: str):
        if type(recipients) == list:
            recipients = " ".join(recipients)

        return self._call(
            endpoint="bulksend",
            payload={"recipients": recipients, "text": text},
        )

    def received_messages(self, recipient, limit=None):
        return self._call(
            endpoint="received",
            payload={
                "recipient": recipient,
                "limit": limit if limit else 1000,
            },
        )

    def get_message(self, id: int):
        raise NotImplementedError


if __name__ == "__main__":
    """Just for testing purpose"""
    pass
