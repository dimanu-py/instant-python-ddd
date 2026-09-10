import json
import tempfile
import uuid
from pathlib import Path

import pytest
from expects import be_a, be_true, equal, expect, have_keys

from instant_python.metrics.infra.user_identity_manager import UserIdentityManager


@pytest.mark.integration
class TestUserIdentityManager:
    def test_should_create_metrics_file_and_store_distinct_id_for_new_user(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_dir = Path(temp_dir)
            metrics_file = config_dir / "metrics.json"
            user_identity_manager = UserIdentityManager(config_dir=config_dir)

            distinct_id = user_identity_manager.get_or_create_distinct_id()

            expect(metrics_file.exists()).to(be_true)
            stored_distinct_id = json.loads(metrics_file.read_text())
            expect(stored_distinct_id).to(have_keys("distinct_id"))
            expect(stored_distinct_id["distinct_id"]).to(equal(distinct_id))

    def test_should_return_same_id_on_consecutive_calls(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_dir = Path(temp_dir)
            user_identity_manager = UserIdentityManager(config_dir=config_dir)

            first_id = user_identity_manager.get_or_create_distinct_id()
            second_id = user_identity_manager.get_or_create_distinct_id()

            expect(first_id).to(equal(second_id))

    def test_should_regenerate_id_when_metrics_file_is_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_dir = Path(temp_dir)
            metrics_file = config_dir / "metrics.json"
            metrics_file.write_text("invalid json content")

            user_identity_manager = UserIdentityManager(config_dir=config_dir)
            distinct_id = user_identity_manager.get_or_create_distinct_id()

            stored_data = json.loads(metrics_file.read_text())
            expect(stored_data["distinct_id"]).to(equal(distinct_id))

    def test_should_load_and_validate_existing_uuid_from_metrics_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_dir = Path(temp_dir)
            metrics_file = config_dir / "metrics.json"
            existing_uuid = str(uuid.uuid4())
            metrics_file.write_text(json.dumps({"distinct_id": existing_uuid}))

            user_identity_manager = UserIdentityManager(config_dir=config_dir)
            distinct_id = user_identity_manager.get_or_create_distinct_id()

            expect(distinct_id).to(equal(existing_uuid))
            expect(uuid.UUID(distinct_id)).to(be_a(uuid.UUID))

    def test_should_regenerate_id_when_stored_value_is_not_a_valid_uuid(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_dir = Path(temp_dir)
            metrics_file = config_dir / "metrics.json"
            metrics_file.write_text(json.dumps({"distinct_id": "not-a-valid-uuid"}))

            user_identity_manager = UserIdentityManager(config_dir=config_dir)
            distinct_id = user_identity_manager.get_or_create_distinct_id()

            expect(distinct_id).not_to(equal("not-a-valid-uuid"))
            stored_data = json.loads(metrics_file.read_text())
            expect(stored_data["distinct_id"]).to(equal(distinct_id))
