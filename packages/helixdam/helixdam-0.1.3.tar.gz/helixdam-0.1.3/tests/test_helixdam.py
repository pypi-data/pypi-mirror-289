import os
import sys
import hashlib
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
from helixdam import HelixDAM, HelixDAMAuthException, HelixDAMException


### FIXTURES ###
# Set Env Vars for authenticating against a HelixDAM instance
@pytest.fixture
def valid_url():
    return os.environ.get("HELIXDAM_URL", "http://localhost")


@pytest.fixture
def valid_account_key():
    return os.environ.get("HELIXDAM_ACCOUNT_KEY", "key_for_tests")


@pytest.fixture
def valid_company():
    return os.environ.get("HELIXDAM_COMPANY", "hth")


@pytest.fixture
def valid_username():
    return os.environ.get("HELIXDAM_USERNAME", "perforce")


@pytest.fixture
def valid_password():
    return os.environ.get("HELIXDAM_PASSWORD", "default_password")


@pytest.fixture
def valid_depot_path_with_preview():
    return os.environ.get("HELIXDAM_DEPOT_PATH_WITH_PREVIEW", "//depot/somefile.png")


@pytest.fixture
def valid_identifier():
    return os.environ.get("HELIXDAM_IDENTIFIER", "2")


@pytest.fixture
def hd():
    return HelixDAM(
        url="https://dam.demo.perforce.rocks",
        account_key="e4d8ebad9be5cc66fd4c7834f32f7cce",
    )


@pytest.fixture(scope="module")
def file_hashes():
    return {}


def file_hash(filepath):
    with open(filepath, "rb") as f:
        return str(hashlib.file_digest(f, "md5"))


class TestHelixDAMInit:
    def test_init_account_key_success(self, valid_url: str, valid_account_key: str):
        hd = HelixDAM(url=valid_url, account_key=valid_account_key)
        hd.get_session()
        assert hd.session

    @pytest.mark.parametrize(
        "params",
        [
            {"account_key": "bad_key"},
            {
                "company": "bad_company",
                "username": "default_username",
                "password": "default_password",
            },
            {
                "company": "default_company",
                "username": "bad_username",
                "password": "default_password",
            },
            {
                "company": "default_company",
                "username": "default_username",
                "password": "bad_password",
            },
        ],
    )
    def test_init_auth_failures(self, valid_url: str, params: dict[str, str]):
        with pytest.raises(HelixDAMAuthException):
            hd = HelixDAM(url=valid_url, **params)
            hd.get_session()

    def test_no_info_fail(self):
        with pytest.raises(HelixDAMAuthException):
            hd = HelixDAM("https://fake.url")
            hd.get_session()

    def test_init_url_fail(
        self, valid_company: str, valid_username: str, valid_password: str
    ):
        with pytest.raises(HelixDAMException):
            hd = HelixDAM(
                url="https://invalid.url",
                company=valid_company,
                username=valid_username,
                password=valid_password,
            )
            hd._connect()

    def test_init_login_success(
        self,
        valid_url: str,
        valid_company: str,
        valid_username: str,
        valid_password: str,
    ):
        hd = HelixDAM(
            url=valid_url,
            company=valid_company,
            username=valid_username,
            password=valid_password,
        )
        hd.get_session()
        assert hd.session

    def test_invalid_request(self, hd: HelixDAM):
        with pytest.raises(HelixDAMAuthException):
            hd.get_session()
            hd.session.headers.clear()
            hd.get_all_metadata_fields()


class TestHelixDAMDownloads:

    @pytest.mark.dependency()
    @pytest.mark.parametrize(
        "test_case",
        [
            {
                "name": "current_version",
                "changelist": None,
                "should_exist": True,
                "valid_path": True,
            },
            {
                "name": "specific_changelist",
                "changelist": True,
                "should_exist": True,
                "valid_path": True,
            },
            {
                "name": "nonexistent_changelist",
                "changelist": False,
                "should_exist": False,
                "valid_path": True,
            },
            {
                "name": "invalid_path",
                "changelist": None,
                "should_exist": False,
                "valid_path": False,
            },
        ],
    )
    def test_download_preview(
        self,
        hd: HelixDAM,
        tmp_path: Path,
        valid_depot_path_with_preview: str,
        valid_identifier: str,
        test_case: dict[str, str | bool | None] | dict[str, str | bool],
        file_hashes: dict,
    ):
        output_file = tmp_path / f"test_preview_{test_case['name']}.png"

        depot_path = (
            valid_depot_path_with_preview
            if test_case["valid_path"]
            else "//invalid/path/to/file.png"
        )

        if test_case["changelist"] is None:
            changelist = None
        elif test_case["changelist"] == True:
            changelist = valid_identifier
        else:
            changelist = 1

        if test_case["should_exist"]:
            hd.download_preview(
                depot_path=depot_path,
                output_file=str(output_file),
                changelist=changelist,
            )
            assert output_file.exists()
            assert output_file.stat().st_size > 1024
            file_hashes[f"preview_file_hash_{test_case['name']}"] = file_hash(
                output_file
            )

        else:
            with pytest.raises(HelixDAMException):
                hd.download_preview(
                    depot_path=depot_path,
                    output_file=str(output_file),
                    changelist=changelist,
                )

    @pytest.mark.dependency()
    @pytest.mark.parametrize(
        "test_case",
        [
            {
                "name": "current_version",
                "changelist": None,
                "should_exist": True,
                "valid_path": True,
            },
            {
                "name": "specific_changelist",
                "changelist": True,
                "should_exist": True,
                "valid_path": True,
            },
            {
                "name": "nonexistent_changelist",
                "changelist": False,
                "should_exist": False,
                "valid_path": True,
            },
            {
                "name": "invalid_path",
                "changelist": None,
                "should_exist": False,
                "valid_path": False,
            },
        ],
    )
    def test_download_thumbnail(
        self,
        hd: HelixDAM,
        tmp_path: Path,
        valid_depot_path_with_preview: str,
        valid_identifier: str,
        test_case: dict[str, str | bool | None] | dict[str, str | bool],
        file_hashes: dict,
    ):
        output_file = tmp_path / f"test_preview_{test_case['name']}.png"

        depot_path = (
            valid_depot_path_with_preview
            if test_case["valid_path"]
            else "//invalid/path/to/file.png"
        )

        if test_case["changelist"] is None:
            changelist = None
        elif test_case["changelist"] == True:
            changelist = valid_identifier
        else:
            changelist = 1

        if test_case["should_exist"]:
            hd.download_thumbnail(
                depot_path=depot_path,
                output_file=str(output_file),
                changelist=changelist,
            )
            assert output_file.exists()
            assert output_file.stat().st_size > 1024
            file_hashes[f"thumbnail_file_hash_{test_case['name']}"] = file_hash(
                output_file
            )
        else:
            with pytest.raises(HelixDAMException):
                hd.download_thumbnail(
                    depot_path=depot_path,
                    output_file=str(output_file),
                    changelist=changelist,
                )

    @pytest.mark.dependency()
    @pytest.mark.parametrize(
        "test_case",
        [
            {
                "name": "current_version",
                "changelist": None,
                "should_exist": True,
                "valid_path": True,
            },
            {
                "name": "specific_changelist",
                "changelist": True,
                "should_exist": True,
                "valid_path": True,
            },
            {
                "name": "nonexistent_changelist",
                "changelist": False,
                "should_exist": False,
                "valid_path": True,
            },
            {
                "name": "invalid_path",
                "changelist": None,
                "should_exist": False,
                "valid_path": False,
            },
        ],
    )
    def test_download_file(
        self,
        hd: HelixDAM,
        tmp_path: Path,
        valid_depot_path_with_preview: str,
        valid_identifier: str,
        test_case: dict[str, str | bool | None] | dict[str, str | bool],
        file_hashes: dict,
    ):
        output_file = tmp_path / f"test_preview_{test_case['name']}.fbx"

        depot_path = (
            valid_depot_path_with_preview
            if test_case["valid_path"]
            else "//invalid/path/to/file.png"
        )

        if test_case["changelist"] is None:
            changelist = None
        elif test_case["changelist"] == True:
            changelist = valid_identifier
        else:
            changelist = 1

        if test_case["should_exist"]:
            hd.download_file(
                depot_path=depot_path,
                output_file=str(output_file),
                changelist=changelist,
            )
            assert output_file.exists()
            assert output_file.stat().st_size > 1024
            file_hashes[f"full_file_hash_{test_case['name']}"] = file_hash(output_file)
        else:
            with pytest.raises(HelixDAMException):
                hd.download_file(
                    depot_path=depot_path,
                    output_file=str(output_file),
                    changelist=changelist,
                )

    @pytest.mark.dependency(
        depends=[
            "test_download_file",
            "test_download_thumbnail",
            "test_download_preview",
        ]
    )
    def test_file_contents_differ(self, file_hashes: dict):
        for name, hash_value in file_hashes.items():
            matches = [
                key
                for key, val in file_hashes.items()
                if key != name and val == hash_value
            ]
            assert (
                not matches
            ), f"File downloaded for {name} is the same as: {', '.join(matches)}"


class TestHelixDAMMetadata:
    def test_get_file_metadata(self, hd: HelixDAM, valid_depot_path_with_preview: str):
        metadata = hd.get_file_metadata(depot_path=valid_depot_path_with_preview)
        assert metadata == []

    def test_get_metadata_field_uuid_by_name(self, hd: HelixDAM):
        uuid = hd.get_metadata_field_uuid_by_name("Project Name")
        assert uuid == "ffdc75fe-17f8-4211-a491-fe240e198ebc"

    def test_timed_cache(self, hd: HelixDAM, monkeypatch):
        call_count = 0

        mock_result = [
            {
                "api_status": 200,
                "api_timestamp": "2024-08-07T19:32:11Z",
                "id": "300fd571-4fbe-4d0e-8bd1-84487d456d5b",
                "created_at": "2024-07-26T10:08:25Z",
                "updated_at": "2024-07-26T10:08:25Z",
                "uuid": "300fd571-4fbe-4d0e-8bd1-84487d456d5b",
                "name": "Coding Language",
                "type": "text",
                "available_values": [],
                "hidden": False,
            },
            {
                "api_status": 200,
                "api_timestamp": "2024-08-07T19:32:11Z",
                "id": "8b365169-9a08-47d2-ab9b-55cd3d90e37e",
                "created_at": "2023-09-18T22:24:12Z",
                "updated_at": "2024-07-31T05:01:03Z",
                "uuid": "8b365169-9a08-47d2-ab9b-55cd3d90e37e",
                "name": "License",
                "type": "single-select",
                "available_values": ["standard", "restricted", "open"],
                "hidden": False,
            },
        ]

        def mock_get(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            return {
                "metadata": {
                    "more_results": False,
                    "next_offset": 24,
                    "total_count": 24,
                    "count": 24,
                },
                "results": mock_result,
            }

        monkeypatch.setattr(hd, "_get", mock_get)

        all_fields = hd.get_all_metadata_fields()
        assert all_fields == mock_result
        assert call_count == 1

        all_fields_2 = hd.get_all_metadata_fields()
        assert all_fields == all_fields_2
        assert call_count == 1

        hd._cached_metadata["expiration"] = 0

        all_fields_3 = hd.get_all_metadata_fields()
        assert all_fields == all_fields_3
        assert call_count == 2

    def test_clear_cache(self, hd: HelixDAM):
        all_fields = hd.get_all_metadata_fields()
        hd.account_key = "bad_key"
        saved_headers = hd.session.headers.copy()
        hd.session.headers.clear()
        hd._cached_metadata["expiration"] = 0
        with pytest.raises(HelixDAMAuthException):
            hd.get_all_metadata_fields()
        hd.session.headers = saved_headers
\
    def test_update_metadata_field(
        self, hd: HelixDAM, valid_depot_path_with_preview: str
    ):
        hd.update_file_metadata_by_name(
            depot_path=valid_depot_path_with_preview,
            name_value_dict={"project nAmE": "Testing"},
        )

        metadata = hd.get_file_metadata(depot_path=valid_depot_path_with_preview)
        assert len(metadata) == 1
        assert metadata[0]["name"] == "Project Name"
        assert metadata[0]["value"] == "Testing"

        hd.delete_file_metadata(
            depot_path=valid_depot_path_with_preview, uuids=[metadata[0]["uuid"]]
        )

        metadata = hd.get_file_metadata(depot_path=valid_depot_path_with_preview)
        assert len(metadata) == 0

    def test_add_existing_field(self, hd: HelixDAM):
        res = hd.create_metadata_field("Project Name", "text")
        assert res == "ffdc75fe-17f8-4211-a491-fe240e198ebc"
