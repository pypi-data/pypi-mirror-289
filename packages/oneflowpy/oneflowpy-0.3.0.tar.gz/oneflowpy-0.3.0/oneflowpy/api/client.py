from typing import Any, Dict, Optional
import os, requests
from .config.config import Config


class OneflowClient:
    """
    A client for interacting with the Oneflow API.

    This class manages sessions, authentication, making HTTP requests to the Oneflow API,
    and handles different content types including multipart/form-data for file uploads.
    """

    def set_auth_headers(self) -> None:
        """
        Configures the session to use the provided access token for simple key authentication
        in all subsequent API requests. NOTE: this is unsafe

        """

        self.session.headers.update(
            {
                "x-oneflow-api-token": self.config.api_key,
                "x-oneflow-user-email": self.config.user_email,
            }
        )

    def __init__(
        self, api_key: str | None = None, user_email: str | None = None
    ) -> None:
        """
        Initializes a new instance of the OneflowClient, setting up a session for improved
        performance through connection pooling and reuse.
        """
        self.session: requests.Session = requests.Session()
        self.config = Config(api_key, user_email)
        self.set_auth_headers()

    def _request(
        self,
        method: str,
        endpoint: str,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Performs a HTTP request to a specified endpoint of the Oneflow API with support for
        JSON payloads, form data, and file uploads.

        Parameters:
            method (str): HTTP method (e.g., 'GET', 'POST').
            endpoint (str): API endpoint path.
            json (Optional[Dict[str, Any]]): Payload to be serialized as JSON.
            data (Optional[Dict[str, Any]]): Form data to send in the body.
            files (Optional[Dict[str, Any]]): Files to upload.
            **kwargs: Additional arguments to pass to the `requests.request` method.

        Returns:
            Dict[str, Any]: The parsed JSON response from the API.

        Raises:
            requests.exceptions.HTTPError: If the request fails for any reason.
        """

        # set up spesific url with base and endpoint
        url: str = f"{self.config.base_url}/{endpoint}"

        # define local headers
        headers: Dict[str, str] = {}
        headers["accept"] = "application/json"

        if json is not None:
            headers["Content-Type"] = "application/json"

        elif data is not None:
            headers["Content-Type"] = "application/x-www-form-urlencoded"

        response: requests.Response = self.session.request(
            method, url, headers=headers, json=json, data=data, files=files, **kwargs
        )
        if response.status_code >= 400:
            raise requests.exceptions.HTTPError(response.json())

        content_type = response.headers.get("Content-Type")

        if content_type in ["application/pdf", "application/octet-stream"]:
            return response.content
        if content_type == "application/json":
            return response.json() if response.content else {}
        return response

    def get(self, endpoint: str, **kwargs: Any) -> Dict[str, Any]:
        """Sends a GET request to the specified endpoint."""
        return self._request("GET", endpoint, **kwargs)

    def post(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Dict[str, Any]:
        """Sends a POST request to the specified endpoint."""
        return self._request("POST", endpoint, json=data, **kwargs)

    def put(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Dict[str, Any]:
        """Sends a PUT request to the specified endpoint."""
        return self._request("PUT", endpoint, json=data, **kwargs)

    def delete(self, endpoint: str, **kwargs: Any) -> Dict[str, Any]:
        """Sends a DELETE request to the specified endpoint."""
        return self._request("DELETE", endpoint, **kwargs)

    def post_file(
        self, endpoint: str, data: Dict[str, Any], files: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Sends a POST request with multipart/form-data to the specified endpoint for file uploads.

        Parameters:
            endpoint (str): The API endpoint for the file upload.
            data (Dict[str, Any]): Data to accompany the file upload.
            files (Dict[str, Any]): Files to be uploaded.

        Returns:
            Dict[str, Any]: The JSON response from the API.
        """
        return self._request("POST", endpoint, data=data, files=files)

    def patch(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Dict[str, Any]:
        """Sends a PATCH request to the specified endpoint."""
        return self._request("PATCH", endpoint, json=data, **kwargs)

    def is_available(self) -> bool:
        """Checks if the Oneflow API is available."""
        try:
            response = self.get("ping")
        except requests.exceptions.HTTPError:
            return False
        return True
