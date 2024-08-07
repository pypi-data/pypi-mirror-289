from abc import ABC, abstractmethod
from typing import Optional, Dict, List


class SesClient(ABC):
    @abstractmethod
    def send_email(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        body: Optional[str] = None,
        html_message: Optional[str] = None,
    ) -> None:
        pass

    @abstractmethod
    def send_email_with_attachments(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        attachments: List = None,
        body: Optional[str] = None,
        html_message: Optional[str] = None,
    ) -> None:
        pass

    @abstractmethod
    def send_email_with_template(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        template_name: str,
        template_data: Dict[str, str],
    ) -> None:
        pass

    @abstractmethod
    def send_email_with_template_with_attachments(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        template_name: str,
        template_data: Dict[str, str],
        attachments: List,
    ) -> None:
        pass
