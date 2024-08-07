from typing import List


class Email:

    def __init__(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        body: str,
        attachments: List[bytes],
    ) -> None:
        self.email_from = email_from
        self.email_to = email_to
        self.subject = subject
        self.body = body
        self.attachments = attachments

    email_from: str
    email_to: str
    subject: str
    body: str
    attachments: List[bytes]
