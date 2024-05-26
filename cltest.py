
import argparse
import os
import subprocess

from pycltest.finder import *
from pycltest.test import TEST_OK, TEST_ERR

def run_test (executable: str, name: str):
    if "&" in name or "|" in name or ">" in name: return
    if "&" in executable or "|" in executable or ">" in executable: return

    process = subprocess.Popen([executable, name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout, stderr, TEST_OK if process.returncode == 0 else TEST_ERR
def main ():
    parser = argparse.ArgumentParser()
    parser.add_argument("tests")
    parser.add_argument("src", nargs="?", default="")
    args = parser.parse_args()

    runner = Runner()
    find_tests( args.tests, runner )

    if not os.path.exists("build"): os.mkdir("build")
    with open("build/runner.cpp", "w") as file: file.write(runner.generate_runner())

    command = ["g++", "-o", "build/out", "build/runner.cpp", "-I./"]
    if args.src != "":
        sources = find_files(args.src)
        print(sources)
        command += sources
    if "&" in command or "|" in command or ">" in command:
        print("Command contains unexpected characters")
        exit()
    process = subprocess.Popen(command)
    process.wait()

    executable = "./build/out.exe" if os.path.exists("build/out.exe") else "./build/out"

    results = []

    test_ok = 0
    test_cn = len(runner.tests)
    for test in runner.tests:
        print("Running", test.location + "::" + test.name, end=" ")
        args = run_test(executable, test.name)
        results.append((args, test))
        
        print(args[2])
        if args[2] == TEST_OK: test_ok += 1
    
    for [ stdout, stderr, result ], test in results:
        if result == TEST_OK: continue

        if stdout != b"":
            print("\n====================", test.location + "::" + test.name, "STDOUT ====================")
            print(stdout.decode(encoding="utf-8"), end="")
        if stderr != b"":
            print("\n====================", test.location + "::" + test.name, "STDERR ====================")
            print(stderr.decode(encoding="utf-8"), end="")

    print()
    print()
    print("Result of local test run")
    print()
    print("        VALID TESTS", test_ok)
    print("        ERROR TESTS", test_cn - test_ok)
    print("        TOTAL TESTS", test_cn)
    print()

    if test_ok == test_cn:
        print("The software is ready for production.")
        exit(0)
    print("WARNING, SOME ERROR OCCURED, THE SOFTWARE ISN'T READY")
    exit(1)

if __name__ == "__main__":
    main()
