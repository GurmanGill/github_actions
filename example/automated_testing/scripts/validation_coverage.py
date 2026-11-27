import argparse
import sys
import xml.etree.ElementTree as ET


def validate_coverage(report_path: str, threshold: float) -> None:
    root = ET.parse(report_path).getroot()

    lines_covered = int(root.attrib["lines-covered"])
    lines_valid = int(root.attrib["lines-valid"])

    branches_covered = int(root.attrib["branches-covered"])
    branches_valid = int(root.attrib["branches-valid"])

    covered = lines_covered + branches_covered
    total = lines_valid + branches_valid

    if total == 0:
        raise ValueError("No measurable coverage data")

    coverage = (covered / total) * 100

    print(f"Report: {report_path}")
    print(f"Coverage: {coverage:.2f}%")
    print(f"Threshold: {threshold}%")

    if coverage < threshold:
        print("Coverage gate FAILED")
        sys.exit(1)

    print("Coverage gate PASSED")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--report", required=True)
    parser.add_argument("--threshold", type=float, default=80)

    args = parser.parse_args()

    validate_coverage(args.report, args.threshold)