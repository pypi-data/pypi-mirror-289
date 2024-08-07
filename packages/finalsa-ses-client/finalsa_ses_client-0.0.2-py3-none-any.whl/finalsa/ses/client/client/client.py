from finalsa.ses.client.interface import SesClient, CHARSET
from typing import Any, List, Dict, Optional
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import boto3
import logging


class SesClientImpl(SesClient):

    def __init__(
        self,
        templates_path: Optional[str] = None,
    ) -> None:
        self.templates_path = templates_path
        self.templates = {}
        self.client = boto3.client('ses')
        self.logger = logging.getLogger("finalsa.clients")

    def __send_raw_email__(
        self,
        email_from: str,
        email_to: str,
        email: MIMEMultipart,
    ) -> Any:
        self.logger.info(
            f"Sending email from {email_from} to {email_to}")
        response = self.client.send_raw_email(
            Source=email_from,
            Destinations=[
                email_to,
            ],
            RawMessage={
                'Data': email.as_string(),
            },
        )
        self.logger.info(f"Email sent with message id {response['MessageId']}")

    def __load_default_email__(
            self,
            email_from: str,
            email_to: str,
            subject: str,
            body: str,
            html_message: str,) -> MIMEMultipart:

        if not email_from:
            raise ValueError("email_from is required")
        if not email_to:
            raise ValueError("email_to is required")
        if not subject:
            raise ValueError("subject is required")
        if not body and not html_message:
            raise ValueError("body or html_message is required")
        email = MIMEMultipart('mixed')
        email['Subject'] = subject
        email['From'] = email_from
        email['To'] = email_to
        if body:
            email.attach(MIMEText(body.encode(CHARSET), 'plain', CHARSET))
        if html_message:
            email.attach(MIMEText(html_message.encode(CHARSET), 'html', CHARSET))
        return email

    def send_email(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        body: str,
        html_message: str,
    ) -> Any:
        email = self.__load_default_email__(
            email_from=email_from,
            email_to=email_to,
            subject=subject,
            body=body,
            html_message=html_message
        )
        return self.__send_raw_email__(
            email_from=email_from,
            email_to=email_to,
            email=email
        )

    def send_email_with_attachments(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        body: str,
        html_message: str,
        attachments: List[bytes]
    ) -> Any:
        email = self.__load_default_email__(
            email_from=email_from,
            email_to=email_to,
            subject=subject,
            body=body,
            html_message=html_message
        )
        for attachment in attachments:
            part = MIMEApplication(attachment)
            part.add_header('Content-Disposition', 'attachment', filename='attachment')
            email.attach(part)
        return self.__send_raw_email__(
            email_from=email_from,
            email_to=email_to,
            email=email
        )

    def __render__(self, template_name: str, **kwargs) -> str:
        template = self.__get_template__(template_name)
        for key, value in kwargs.items():
            k = "{{" + key + "}}"
            template = template.replace(k, value)
        return template

    def __get_template__(self, template_name: str) -> str:
        if template_name not in self.templates:
            self.__load_template__(template_name)
        return self.templates[template_name]

    def __load_template__(self, template_name: str) -> None:
        file = open(f"{self.templates_path}/{template_name}", "r")
        content = file.read()
        file.close()
        self.templates[template_name] = content

    def send_email_with_template(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        template_name: str,
        template_data: Dict[str, str],
    ) -> Any:
        body = self.__render__(template_name, **template_data)
        email = self.__load_default_email__(
            email_from=email_from,
            email_to=email_to,
            subject=subject,
            html_message=body
        )
        return self.__send_raw_email__(
            email_from=email_from,
            email_to=email_to,
            email=email
        )

    def send_email_with_template_with_attachments(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        template_name: str,
        template_data: Dict[str, str],
        attachments: List[bytes],
    ) -> Any:
        body = self.__render__(template_name, **template_data)
        email = self.__load_default_email__(
            email_from=email_from,
            email_to=email_to,
            subject=subject,
            html_message=body
        )
        for attachment in attachments:
            part = MIMEApplication(attachment)
            part.add_header('Content-Disposition', 'attachment', filename='attachment')
            email.attach(part)
        return self.__send_raw_email__(
            email_from=email_from,
            email_to=email_to,
            email=email
        )
