"""Regression tests for the JSON validators."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载模块：{relative_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validate_report = load_module(
    "validate_report",
    "skills/asu-resume-audit-skill/scripts/validate_report.py",
)


def minimal_report(url: str) -> dict:
    return {
        "metadata": {
            "title": "简历审计",
            "subject": "匿名候选人",
            "generated_at": "2026-08-13T12:00:00+08:00",
        },
        "sources": [{"id": "S-001", "title": "来源", "url": url}],
        "claims": [
            {
                "id": "C-001",
                "normalized_claim": "一条可核验主张",
                "status": "unverifiable",
                "risk": "medium",
                "confidence": "low",
                "analysis": "当前证据不足。",
                "evidence_for": ["S-001"],
                "evidence_against": [],
            }
        ],
    }


class AuditSourceUrlTests(unittest.TestCase):
    def validate(self, url: str) -> list[str]:
        errors: list[str] = []
        validate_report.validate_data(minimal_report(url), errors)
        return errors

    def test_accepts_http_and_https_sources(self) -> None:
        self.assertEqual(self.validate("https://example.com/evidence"), [])
        self.assertEqual(self.validate("http://example.com/evidence"), [])

    def test_rejects_executable_source_url(self) -> None:
        errors = self.validate("javascript:alert(document.domain)")
        self.assertTrue(any("URL 必须使用 http 或 https" in error for error in errors))

    def test_rejects_relative_source_url(self) -> None:
        errors = self.validate("/local/evidence")
        self.assertTrue(any("URL 必须使用 http 或 https" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
