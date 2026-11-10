"""Tests for ytconverter.core.version."""

import httpx

from ytconverter.core import version as version_module


def test_check_version_offline_returns_local_without_exiting(monkeypatch):
    """A failed PyPI check (e.g. no network) must not kill the CLI."""

    def _boom(*args, **kwargs):
        raise httpx.ConnectError("no network")

    monkeypatch.setattr(version_module.httpx, "get", _boom)

    local, remote = version_module.check_version()

    assert remote is None
    assert isinstance(local, str) and local
