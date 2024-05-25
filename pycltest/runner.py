
from pycltest.test import Test

from typing import List

class Runner:
    tests: List[Test]

    def __init__(self):
        self.tests = []
    def add_test (self, test: Test):
        self.tests.append(test)
    
    def generate_runner (self) -> str:
        headers = list(set(map(lambda test: test.location, self.tests)))

        lines = []
        for header in headers:
            lines.append(f"#include \"{header}\"")
        lines.append("#include <string>")

        lines.append("int main (int argc, char** argv) {")
        lines.append("\tif (argc != 2) return 1;")
        lines.append("\tstd::string test_name = argv[1];")
        for test in self.tests:
            lines.append(f"\tif (test_name == \"{test.name}\") " + "{ " + f"{test.name}" + "(); return 0; }")
        lines.append(f"\treturn 1;")
        lines.append("}")

        return "\n".join(lines)