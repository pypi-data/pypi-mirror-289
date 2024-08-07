from finalsa.ses.client import (
    SesClient,
    SesClientImpl,
    SesClientTest,
    __version__
)
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


def test_version():
    assert __version__ is not None


def test_client():
    assert SesClient is not None


def test_client_impl():
    assert SesClientImpl is not None


def test_client_test():
    client = SesClientTest()
    assert client is not None


def test_client_send_email():
    client = SesClientTest()
    client.send_email("from", "to", "subject", "body", "html")
    assert client.emails[0].email_from == "from"


def test_client_send_email_with_attachments():
    attachments = ["attachment1", "attachment2"]
    client = SesClientTest()
    client.send_email_with_attachments(
        "from", "to", "subject", attachments, "body", "html")
    assert client.emails[0].attachments == attachments


def test_client_load_template():
    client = SesClientTest("tests/templates")
    assert client.__load_template__("template") == "template content"


def test_client_render():
    client = SesClientTest("tests/templates")
    assert client.__render__(
        "template", key="value") == "template content"

    assert client.__render__(
        "template_replace", key="value") == "value"

