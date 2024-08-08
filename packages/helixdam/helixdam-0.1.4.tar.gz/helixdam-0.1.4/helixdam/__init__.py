import base64
import re
import time
import io
import weakref
from pathlib import Path
from functools import wraps, lru_cache
from typing import Optional, Any, Dict, List, Union, Literal, BinaryIO

import requests

CACHE_DURATION = 5  # seconds


class HelixDAMException(Exception):
    def __init__(self, message, original_exception=None):
        self.message = str(message)
        self.original_exception = original_exception
        super().__init__(self.message)

    def __str__(self):
        base_message = super().__str__()
        if self.original_exception:
            return f"{base_message}\nOriginal exception: {self.original_exception}"
        return base_message


class HelixDAMAuthException(HelixDAMException):
    pass


# Custom decorator for metadata uuid caching
def cache_if_exists(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) > 1:
            field_name = args[1]
        else:
            field_name = kwargs.get("field_name")

        if field_name in cache:
            return cache[field_name]
        result = func(*args, **kwargs)
        if result is not None:
            cache[field_name] = result
        return result

    return wrapper


class HelixDAM:
    def __init__(
        self,
        url: str,
        company: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        account_key: Optional[str] = None,
    ):
        self.url = url
        self.company = company
        self.username = username
        self.password = password
        self.account_key = account_key
        self._session = None
        self.last_refresh = 0
        self.refresh_interval = 3600  # 1 Hour
        self.json_headers = {"Content-Type": "application/json"}
        self._cached_metadata = {"data": [], "expiration": 0}

    def _connect(self):
        if not self.account_key and not (
            self.company and self.username and self.password
        ):
            raise HelixDAMAuthException(
                "Must provide account_key or company, username and password"
            )
        if not self.account_key:
            self.account_key = self._login(self.company, self.username, self.password)
        self.session.headers.update(
            {
                "Authorization": f"account_key='{self.account_key}'",
            }
        )
        try:
            self.get_session()
        except requests.HTTPError as e:
            print(e)
            raise HelixDAMAuthException("Invalid account_key", e)
        return self

    @property
    def session(self):
        current_time = time.time()
        if (
            not self._session
            or (current_time - self.last_refresh) > self.refresh_interval
        ):
            if self._session:
                self._session.close()
            self._session = requests.Session()
            self.last_refresh = current_time
            self._connect()
        return self._session

    def __del__(self):
        if self._session:
            self._session.close()

    def _login(self, company, username, password):
        endpoint = "/api/account/session"
        try:
            response = self._post(
                endpoint=endpoint,
                data={"company": company, "login": username, "password": password},
            )
            return response["account_key"]
        except requests.HTTPError as e:
            if e.response.status_code == 401 and e.response.reason == "Unauthorized":
                raise HelixDAMAuthException(
                    "Invalid company, username or password. Please check your credentials.",
                    e,
                )
            raise HelixDAMAuthException("Login failed", e)
        except requests.ConnectionError as e:
            raise HelixDAMException(f"Unable to connect to {self.url}{endpoint}", e)

    def _get(self, endpoint, params=None):
        response = self.session.get(f"{self.url}{endpoint}", params=params)
        raise_for_status(response)
        return response.json()

    def _post(self, endpoint: str, data: Any, params: Optional[Dict] = None):
        response = self.session.post(
            f"{self.url}{endpoint}",
            headers=self.json_headers,
            params=params,
            json=data,
        )
        raise_for_status(response)
        return response.json()

    def _put(self, endpoint: str, data: Any, params: Optional[Dict] = None):
        response = self.session.put(
            f"{self.url}{endpoint}",
            headers=self.json_headers,
            params=params,
            json=data,
        )
        raise_for_status(response)
        return response.json()

    def _patch(self, endpoint: str, data: Any, params: Optional[Dict] = None):
        response = self.session.patch(
            f"{self.url}{endpoint}",
            headers=self.json_headers,
            params=params,
            json=data,
        )
        raise_for_status(response)
        return response.json()

    def _delete(self, endpoint: str, params: Optional[Dict] = None):
        response = self.session.delete(f"{self.url}{endpoint}", params=params)
        raise_for_status(response)
        return response.json()

    def get_session(self):
        return self._get(endpoint="/api/account/session")

    def download_file(
        self,
        depot_path: Union[str, Path],
        output_file: Optional[Union[str, Path, BinaryIO]] = None,
        changelist: Optional[int] = None,
    ) -> Union[Path, bytes, BinaryIO]:
        """Downloads a file asset from the depot

        Args:
            depot_path: In `//depot/stream/depot_path.ext` format
            output_file (optional): File path OR File-like object to save the downloaded file contents to. If not specified, the content is returned as bytes.
            changelist (optional): Set to download asset as a specific changelist (aka identifier)

        Returns:
            File path of output file if specified or bytes of the downloaded file
        """
        return self._download_file(
            endpoint="/api/p4/files",
            depot_path=depot_path,
            output_file=output_file,
            changelist=changelist,
        )

    def download_preview(
        self,
        depot_path: Union[str, Path],
        output_file: Optional[Union[str, Path, BinaryIO]] = None,
        changelist: Optional[int] = None,
    ) -> Union[Path, bytes, BinaryIO]:
        """Downloads a preview image for a file in DAM

        Args:
            depot_path: In `//depot/stream/depot_path.ext` format
            output_file (optional): File path OR File-like object to save the downloaded file contents to. If not specified, the content is returned as bytes.
            changelist (optional): Set to download asset as a specific changelist (aka identifier)

        Returns:
            File path of output file if specified or bytes of the downloaded image
        """
        return self._download_file(
            endpoint="/api/p4/files/preview",
            depot_path=depot_path,
            output_file=output_file,
            changelist=changelist,
        )

    def download_thumbnail(
        self,
        depot_path: Union[str, Path],
        output_file: Optional[Union[str, Path, BinaryIO]] = None,
        changelist: Optional[int] = None,
    ) -> Union[Path, bytes, BinaryIO]:
        """Downloads a thumbnail image for a file in DAM

        Args:
            depot_path: In `//depot/stream/depot_path.ext` format
            output_file (optional): File path OR File-like object to save the downloaded file contents to. If not specified, the content is returned as bytes.
            changelist (optional): Set to download asset as a specific changelist (aka identifier)

        Returns:
            File path of output file if specified or bytes of the downloaded image
        """
        return self._download_file(
            endpoint="/api/p4/files/thumbnail",
            depot_path=depot_path,
            output_file=output_file,
            changelist=changelist,
        )

    def _download_file(
        self,
        endpoint: str,
        depot_path: Union[str, Path],
        output_file: Optional[Union[str, Path, BinaryIO]] = None,
        changelist: Optional[int] = None,
    ) -> Union[Path, bytes, BinaryIO]:
        params = {"depot_path": depot_path}
        if changelist:
            params["identifier"] = changelist
        try:
            response = self.session.get(
                url=f"{self.url}{endpoint}",
                params={"depot_path": depot_path, "identifier": changelist},
            )
            raise_for_status(response)
            if b'{"errors":' in response.content[:11]:
                errors = [
                    error.get("detail", "") for error in response.json()["errors"]
                ]
                raise HelixDAMException(
                    f"Error downloading file: {errors}",
                )
            if output_file is None:
                return response.content
            if is_file_like(output_file):
                output_file.seek(0)
                for chunk in response.iter_content(chunk_size=8192):
                    output_file.write(chunk)
            elif isinstance(output_file, (str, Path)):
                with open(output_file, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

            return output_file

        except requests.HTTPError as e:
            raise HelixDAMException("Error downloading file", e)

    def upload_preview(
        self,
        depot_path: Union[str, Path],
        image: Union[str, Path, bytes],
        changelist: Optional[int] = None,
    ) -> None:
        """Uploads a preview image for a file in DAM

        Args:
            depot_path: In `//depot/stream/depot_path.ext` format
            image: May be bytes, base64 string, hex string, or file path
            changelist (optional): Set to upload to asset at a specific changelist (aka identifier)
        """
        if isinstance(image, str):
            if is_base64(image):
                b64_image = image
            elif is_hex(image):
                b64_image = hex_to_base64(image)
            elif Path(image).is_file():
                with open(image, "rb") as f:
                    image_bytes = f.read()
                    b64_image = base64.b64encode(image_bytes).decode("utf-8")
            else:
                raise HelixDAMException(
                    "Unsupported string data format. Use base64, hex, or file path"
                )
        elif isinstance(image, bytes):
            b64_image = base64.b64encode(image).decode("utf-8")
        else:
            raise HelixDAMException(
                "Unsupported image data format. Use bytes, base64, hex, or file path"
            )
        params = {
            "depot_path": depot_path,
        }
        if changelist:
            params["identifier"] = changelist
        payload = {"content": b64_image, "encoding": "base64"}

        try:
            self._put(
                endpoint="/api/p4/files/preview",
                data=payload,
                params=params,
            )
        except requests.HTTPError as e:
            raise HelixDAMException("Error uploading file", e)

    def get_file_metadata(
        self, depot_path: Union[str, Path], changelist: Optional[int] = None
    ) -> List[Dict[str, str]]:
        """
        Retrieves the metadata of a file in Helix DAM

        Args:
            depot_path: The depot path of the file in the format '//depot/stream/depot_path.ext'.
            changelist (optional): The changelist (identifier) of the file. If not set, will download the latest revision.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing the metadata of the file. Each dictionary has the following keys:
                - name (str): The name of the metadata attribute.
                - uuid (str): The UUID of the metadata attribute.
                - available_values (List[str]): The available values for the metadata attribute.
                - value (str): The value of the metadata attribute.

        Raises:
            HelixDAMException: If there is an error getting the file metadata.
        """
        params = {"depot_path": depot_path, "include": "custom_attributes"}
        if changelist:
            params["identifier"] = changelist
        try:
            response = self._get(
                endpoint="/api/p4/tree",
                params=params,
            )
        except requests.HTTPError as e:
            raise HelixDAMException("Error getting file metadata", e)
        custom_attributes = response["custom_attributes"]
        return [
            {
                "name": attr["template"]["name"],
                "uuid": attr["template"]["uuid"],
                "available_values": attr["template"]["available_values"],
                "value": attr["value"],
            }
            for attr in custom_attributes
        ]

    def _update_files_metadata(
        self,
        paths: List[dict],
        update: List[dict],
        delete: List[dict],
        propagatable: bool = False,
    ) -> None:
        # MUST enforce that all values are strings or else the entire p4search and elasticsearch fortress will crumble
        update = [{"uuid": u["uuid"], "value": str(u["value"])} for u in update]
        try:
            self._put(
                endpoint="/api/p4/batch/custom_file_attributes",
                data={
                    "paths": paths,
                    "create": update,
                    "delete": delete,
                    "propagatable": propagatable,
                },
            )
        except requests.HTTPError as e:
            raise HelixDAMException("Error updating files metadata", e)

    def update_files_metadata(
        self,
        depot_paths: List[str],
        uuid_value_dict: Dict[str, str],
        changelist: Optional[int] = None,
        propagatable: Optional[bool] = False,
    ) -> None:
        """
        Updates the metadata of multiple files in the Helix DAM system.

        Args:
            depot_paths (List[str]): A list of depot paths for the files to be updated.
            uuid_value_dict (Dict[str, str]): A dictionary mapping UUIDs to new values for the metadata fields. eg. {"300fd571-4fbe-4d0e-8bd1-84487d456d5b": "Project A", "300fd571-4fbe-4d0e-8bd1-84487d2ab45dc": "Copyright 2024"}
            changelist (optional): The changelist identifier. If provided, the metadata will be added to files at the specified changelist.
            propagatable (optional): Whether the metadata changes should be propagated to future revisions. Defaults to False.

        Raises:
            HelixDAMException: If there is an error updating the files metadata.
        """
        if changelist:
            paths = [{"path": p, "identifier": changelist} for p in depot_paths]
        else:
            paths = [{"path": p} for p in depot_paths]
        self._update_files_metadata(
            paths=paths,
            update=[{"uuid": k, "value": v} for k, v in uuid_value_dict.items()],
            delete=[],
            propagatable=propagatable,
        )

    def update_file_metadata(
        self,
        depot_path: str,
        uuid_value_dict: Dict[str, str],
        changelist: Optional[int] = None,
        propagatable: Optional[bool] = False,
    ) -> None:
        """
        Updates the metadata of a single file in the Helix DAM system.

        Args:
            depot_path (str): A depot path for the file to be updated.
            uuid_value_dict (Dict[str, str]): A dictionary mapping UUIDs to new values for the metadata fields. eg. {"300fd571-4fbe-4d0e-8bd1-84487d456d5b": "Project A", "300fd571-4fbe-4d0e-8bd1-84487d2ab45dc": "Copyright 2024"}
            changelist (optional): The changelist identifier. If provided, the metadata will be added to file revision at the specified changelist.
            propagatable (optional): Whether the metadata changes should be propagated future revisions. Defaults to False.

        Raises:
            HelixDAMException: If there is an error updating the files metadata.
        """
        self.update_files_metadata(
            depot_paths=[depot_path],
            uuid_value_dict=uuid_value_dict,
            changelist=changelist,
            propagatable=propagatable,
        )

    def update_files_metadata_by_name(
        self,
        depot_paths: List[str],
        name_value_dict: Dict[str, str],
        changelist: Optional[int] = None,
        propagatable: Optional[bool] = False,
    ) -> None:
        names_and_values = [{"name": k, "value": v} for k, v in name_value_dict.items()]
        uuids_and_values = [
            {
                "uuid": self.get_metadata_field_uuid_by_name(item["name"]),
                "value": item["value"],
            }
            for item in names_and_values
        ]
        missing_fields = [
            names_and_values[i]["name"]
            for i, item in enumerate(uuids_and_values)
            if item["uuid"] is None
        ]
        if missing_fields:
            raise HelixDAMException(
                f"Metadata fields don't exist: {', '.join(missing_fields)}\nCreate them first using create_metadata_field()"
            )

        if changelist:
            paths = [{"path": p, "identifier": changelist} for p in depot_paths]
        else:
            paths = [{"path": p} for p in depot_paths]
        self._update_files_metadata(
            paths=paths, update=uuids_and_values, delete=[], propagatable=propagatable
        )

    def update_file_metadata_by_name(
        self,
        depot_path: str,
        name_value_dict: dict,
        changelist: Optional[int] = None,
        propagatable: Optional[bool] = False,
    ) -> None:
        self.update_files_metadata_by_name(
            depot_paths=[depot_path],
            name_value_dict=name_value_dict,
            changelist=changelist,
            propagatable=propagatable,
        )

    def delete_files_metadata(
        self, depot_paths: List[str], uuids: List[str], changelist: Optional[int] = None
    ) -> None:
        if changelist:
            paths = [{"path": p, "identifier": changelist} for p in depot_paths]
        else:
            paths = [{"path": p} for p in depot_paths]
        self._update_files_metadata(
            paths=paths,
            update=[],
            delete=[{"uuid": uuid} for uuid in uuids],
            propagatable=False,
        )

    def delete_file_metadata(
        self, depot_path: str, uuids: List[str], changelist: Optional[int] = None
    ) -> None:

        if changelist:
            paths = [{"path": depot_path, "identifier": changelist}]
        else:
            paths = [{"path": depot_path}]
        self._update_files_metadata(
            paths=paths,
            update=[],
            delete=[{"uuid": uuid} for uuid in uuids],
            propagatable=False,
        )

    def get_all_metadata_fields(self) -> List[Dict]:
        now = time.time()
        if now < self._cached_metadata["expiration"]:
            return self._cached_metadata["data"]
        metadata_fields = []
        try:
            data = self._get(
                endpoint=f"/api/company/file_attribute_templates",
                params={"limit": 1000},
            )
            metadata_fields += data["results"]
            while data["metadata"]["more_results"]:
                data = self._get(
                    endpoint=f"/api/company/file_attribute_templates",
                    params={
                        "limit": 1000,
                        "offset": data["metadata"]["next_offset"],
                    },
                )
                metadata_fields += data["results"]
            self._cached_metadata["data"] = metadata_fields.copy()
            self._cached_metadata["expiration"] = now + CACHE_DURATION
            return metadata_fields
        except requests.HTTPError as e:
            raise HelixDAMException("Error getting metadata fields", e)

    @cache_if_exists
    def get_metadata_field_by_name(self, field_name: str) -> Union[Dict, None]:
        all_fields = self.get_all_metadata_fields()
        return next(
            (f for f in all_fields if f["name"].lower() == field_name.lower()), None
        )

    @cache_if_exists
    def get_metadata_field_by_uuid(self, field_uuid: str) -> Union[Dict, None]:
        all_fields = self.get_all_metadata_fields()
        return next((f for f in all_fields if f["uuid"] == field_uuid), None)

    def get_metadata_field_uuid_by_name(self, field_name: str) -> Union[str, None]:
        """Gets the UUID of a metadata field if it exists, otherwise returns None

        Args:
            field_name: Name of the field

        Returns:
            (str) UUID of the field if it exists, otherwise None
        """
        field = self.get_metadata_field_by_name(field_name)
        return field["uuid"] if field is not None else None

    def create_metadata_field(
        self,
        field_name: str,
        field_type: Optional[Literal["text", "single-select"]] = "text",
        available_values: Optional[List[str]] = None,
        hidden: Optional[bool] = False,
    ) -> str:
        """Creates a metadata field

        Args:
            field_name: Name of the field
            field_type (optional): Either 'text' or 'single-select'. Defaults to 'text'.
            available_values (optional): List of available values for a single-select field
            hidden (optional): Whether the field should be hidden

        Returns:
            (str) UUID of the field
        """
        payload = {
            "name": field_name,
            "type": field_type,
            "hidden": hidden,
        }
        if available_values is not None:
            payload["available_values"] = available_values

        try:
            data = self._post(
                endpoint="/api/company/file_attribute_templates", data=payload
            )
            self.get_all_metadata_fields.cache_clear()
            return data["uuid"]
        except requests.HTTPError as e:
            # Check if the error is because the field already exists and return its UUID if so.
            if e.response.status_code == 422:
                if (
                    e.response.json()
                    .get("api_errors", {})
                    .get("id", {})
                    .get("reserved", False)
                    == True
                ):
                    return self.get_metadata_field_uuid_by_name(field_name)
            raise HelixDAMException("Error creating metadata field", e)

    def update_metadata_field(
        self,
        field_uuid: str,
        field_name: Optional[str] = None,
        available_values: Optional[List[str]] = None,
        hidden: Optional[bool] = None,
    ) -> None:
        if field_name is None and available_values is None and hidden is None:
            raise HelixDAMException(
                "Must provide at least one of field_name, available_values, or hidden"
            )

        data = {}
        if field_name is not None:
            data["name"] = field_name
        if available_values is not None:
            data["available_values"] = available_values
        if hidden is not None:
            data["hidden"] = hidden
        try:
            self._patch(
                endpoint=f"/api/company/file_attribute_templates/{field_uuid}",
                data=data,
            )
        except requests.HTTPError as e:
            raise HelixDAMException("Error updating metadata field", e)


def raise_for_status(response):
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        if e.response.status_code == 401 and e.response.reason == "Unauthorized":
            raise HelixDAMAuthException(
                f"Invalid credentials: {e.response.json().get('api_message', '')}",
                e,
            )
        raise


def is_file_like(obj):
    return hasattr(obj, "write") and hasattr(obj, "seek")


def is_base64(s):
    return bool(re.match(r"^[A-Za-z0-9+/]*={0,2}$", s))


def is_hex(s):
    return all(c in "0123456789ABCDEFabcdef" for c in s)


def hex_to_base64(hex_string):
    return base64.b64encode(bytes.fromhex(hex_string)).decode()


if __name__ == "__main__":
    print(__file__)
