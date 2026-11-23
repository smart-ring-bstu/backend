"""Show PMD violations at their source lines in GitHub Actions."""

from pathlib import Path
import xml.etree.ElementTree as ET


def escape_data(value):
    return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def escape_property(value):
    return escape_data(value).replace(":", "%3A").replace(",", "%2C")


report = ET.parse("target/pmd.xml")
for source in report.findall("{*}file"):
    path = Path(source.attrib["name"]).resolve().relative_to(Path.cwd())
    for violation in source.findall("{*}violation"):
        line = int(violation.attrib["beginline"])
        rule = escape_property(violation.attrib["rule"])
        message = escape_data(violation.text.strip())
        print(f"::warning file={escape_property(str(path))},line={line},title=PMD {rule}::{message}")
