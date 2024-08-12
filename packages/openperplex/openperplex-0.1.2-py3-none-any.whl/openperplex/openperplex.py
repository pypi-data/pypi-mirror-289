import httpx
import json
from typing import Optional, Dict, Any, Generator, List
from urllib.parse import urljoin


class OpenperplexError(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        super().__init__(f"OpenperplexError: {status_code} - {detail}")


class Openperplex:
    def __init__(self, api_key: str, provider: str = 'openai', provider_key: str = None, base_url: str = "https://5e70fd93-e9b8-4b9c-b7d9-eea4580f330c.app.bhs.ai.cloud.ovh.net"):
        self.base_url = base_url
        self.api_key = api_key
        self.provider = provider.lower()
        self.provider_key = provider_key
        self.client = httpx.Client(timeout=15.0)

        if not api_key:
            raise ValueError("API key is required")

        if not provider_key:
            raise ValueError("Provider key is required")

        if self.provider not in ['openai', 'groq']:
            raise ValueError("Provider must be either 'openai' or 'groq'")

    def _make_request(self, endpoint: str, params: Dict[str, Any]) -> httpx.Response:
        url = urljoin(self.base_url, endpoint)
        headers = {
            "X-API-Key": self.api_key,
            "X-Provider": self.provider,
            "X-Provider-Key": self.provider_key
        }

        response = self.client.get(url, params=params, headers=headers)
        if not response.is_success:
            self._handle_error_response(response)
        return response

    def search_stream(self, query: str, date_context: Optional[str] = None, location: str = 'us', pro_mode: bool = False) -> Generator[Dict[str, Any], None, None]:
        endpoint = "/searchStream"
        params = {
            "query": query,
            "date_context": date_context,
            "stored_location": location,
            "pro_mode": pro_mode
        }

        with self.client.stream("GET", urljoin(self.base_url, endpoint), params=params, headers={
            "X-API-Key": self.api_key,
            "X-Provider": self.provider,
            "X-Provider-Key": self.provider_key
        }) as response:
            if not response.is_success:
                self._handle_error_response(response)
            yield from self._stream_sse_response(response)

    def search_simple_stream(self, query: str) -> Generator[Dict[str, Any], None, None]:
        endpoint = "/search_simple_stream"
        params = {"query": query}

        with self.client.stream("GET", urljoin(self.base_url, endpoint), params=params, headers={
            "X-API-Key": self.api_key,
            "X-Provider": self.provider,
            "X-Provider-Key": self.provider_key
        }) as response:
            if not response.is_success:
                self._handle_error_response(response)
            yield from self._stream_sse_response(response)

    def search(self, query: str, date_context: Optional[str] = None, location: str = 'us', pro_mode: bool = False) -> List[Dict[str, Any]]:
        endpoint = "/search"
        params = {
            "query": query,
            "date_context": date_context,
            "stored_location": location,
            "pro_mode": pro_mode
        }

        response = self._make_request(endpoint, params)
        return response.json()

    def search_simple(self, query: str) -> str:
        endpoint = "/search_simple"
        params = {"query": query}

        response = self._make_request(endpoint, params)
        return response.text

    def _stream_sse_response(self, response: httpx.Response) -> Generator[Dict[str, Any], None, None]:
        for line in response.iter_lines():
            if line:
                try:
                    # Check if line is bytes or str and decode if necessary
                    if isinstance(line, bytes):
                        line_str = line.decode('utf-8')
                    else:
                        line_str = line

                    if line_str.startswith("data:"):
                        data_str = line_str.split("data:", 1)[1].strip()
                        data = json.loads(data_str)

                        if isinstance(data, dict) and "type" in data:
                            if data["type"] == "llm":
                                yield {"type": "llm", "text": data.get("text", "")}
                            elif data["type"] == "error":
                                self._handle_error(data)
                            elif data["type"] in ["sources", "relevant", "finished"]:
                                yield data
                        else:
                            print(f"Unexpected data format: {data}")
                except json.JSONDecodeError:
                    print(f"Failed to parse JSON from line: {line_str}")
                except Exception as e:
                    print(f"Error processing line: {e}")

    def _handle_error(self, error_data: Dict[str, Any]):
        status_code = error_data.get('status_code', 500)
        detail = error_data.get('detail', 'An unknown error occurred')
        raise OpenperplexError(status_code, detail)

    def _handle_error_response(self, response: httpx.Response):
        try:
            error_data = response.json()
            status_code = error_data.get('status_code', response.status_code)
            detail = error_data.get('detail', 'An unknown error occurred')
        except json.JSONDecodeError:
            status_code = response.status_code
            detail = response.text or 'An unknown error occurred'

        raise OpenperplexError(status_code, detail)

    def __del__(self):
        self.client.close()