import importlib.util
import unittest
from pathlib import Path


VALIDATOR_PATH = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "asu-resume-audit-skill"
    / "scripts"
    / "validate_report.py"
)
SPEC = importlib.util.spec_from_file_location("validate_report", VALIDATOR_PATH)
validate_report = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_report)


def claim(metric=None):
    result = {
        "id": "C-001",
        "normalized_claim": "付费转化率",
        "status": "unverifiable",
        "risk": "medium",
        "confidence": "medium",
        "analysis": "等待补充指标口径。",
    }
    if metric is not None:
        result["metric"] = metric
    return result


def report(metric=None):
    return {
        "metadata": {
            "title": "测试报告",
            "subject": "匿名候选人",
            "generated_at": "2026-08-14T00:00:00+08:00",
        },
        "sources": [{"id": "S-001"}],
        "claims": [claim(metric)],
    }


class MetricConsistencyTests(unittest.TestCase):
    def validate(self, metric=None):
        errors = []
        validate_report.validate_data(report(metric), errors)
        return errors

    def test_matching_ratio_passes(self):
        self.assertEqual(
            self.validate(
                {"numerator": 200, "denominator": 2000, "displayed_percent": 10}
            ),
            [],
        )

    def test_mismatched_ratio_fails(self):
        errors = self.validate(
            {"numerator": 200, "denominator": 2000, "displayed_percent": 38}
        )
        self.assertTrue(any("百分比与分子分母不一致" in error for error in errors))

    def test_non_numeric_metric_fails(self):
        errors = self.validate(
            {"numerator": "two hundred", "denominator": 2000, "displayed_percent": 10}
        )
        self.assertTrue(any("指标字段无法计算" in error for error in errors))

    def test_zero_denominator_fails(self):
        errors = self.validate(
            {"numerator": 200, "denominator": 0, "displayed_percent": 10}
        )
        self.assertTrue(any("指标字段无法计算" in error for error in errors))

    def test_claim_without_metric_remains_valid(self):
        self.assertEqual(self.validate(), [])


if __name__ == "__main__":
    unittest.main()
