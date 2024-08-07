from finalsa.ses.client.interface import SesClient
from typing import List, Optional
from .email import Email


class SesClientTest(SesClient):

    def __init__(
        self,
        templates_path: Optional[str] = None,
    ) -> None:
        self.emails: List[Email] = []
        self.templates_path = templates_path

    def send_email(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        body: str,
        html_message: str,
    ) -> None:
        real_body = body if body else html_message
        email = Email(
            email_from=email_from,
            email_to=email_to,
            subject=subject,
            body=real_body,
            attachments=[],
        )
        self.emails.append(email)

    def send_email_with_attachments(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        attachments: List,
        body: str,
        html_message: str,
    ) -> None:
        real_body = body if body else html_message
        email = Email(
            email_from=email_from,
            email_to=email_to,
            subject=subject,
            body=real_body,
            attachments=attachments,
        )
        self.emails.append(email)

    def __load_template__(self, template_name: str) -> str:
        file = open(f"{self.templates_path}/{template_name}", "r")
        content = file.read()
        file.close()
        return content

    def __render__(self, template_name: str, **kwargs) -> str:
        template = self.__load_template__(template_name)
        for key, value in kwargs.items():
            k = "{{" + key + "}}"
            template = template.replace(k, value)
        return template

    def send_email_with_template(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        template_name: str,
        template_data: dict,
    ) -> None:
        body = self.__render__(template_name, **template_data)
        email = Email(
            email_from=email_from,
            email_to=email_to,
            subject=subject,
            body=body,
            attachments=[],
        )
        self.emails.append(email)

    def send_email_with_template_with_attachments(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        template_name: str,
        template_data: dict,
        attachments: List,
    ) -> None:
        body = self.__render__(template_name, **template_data)
        email = Email(
            email_from=email_from,
            email_to=email_to,
            subject=subject,
            body=body,
            attachments=attachments,
        )
        self.emails.append(email)
