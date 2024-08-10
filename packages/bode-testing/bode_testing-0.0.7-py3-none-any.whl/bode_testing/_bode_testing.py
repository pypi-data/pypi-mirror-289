import os
import pytest
import uuid


@pytest.fixture
def url():
    deploy_url = os.environ["DEPLOY_URL"]
    if not deploy_url.startswith("http"):
        raise ValueError(
            f"incorrect deploy url value '{deploy_url}' does not start with http "
        )
    return deploy_url


@pytest.fixture(scope="function")
def request_headers(request) -> dict[str, str]:
    test_id = request.node.nodeid.replace("/", ".").replace(".py", "")
    headers = {
        "X-Test-Id": test_id,
        "X-Session-Id": os.environ["SESSION_ID"],
        "X-Request-Id": str(uuid.uuid4()).replace("-", "")[:8],
    }
    if os.environ["CLOUD"] == "true":
        id_token = os.environ["IDTOKEN"]
        auth_header = {"Authorization": f"Bearer {id_token}"}
        headers = {**headers, **auth_header}
    return headers
