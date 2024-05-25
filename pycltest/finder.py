
import os

from pycltest.runner import Runner, Test

def find_tests (path, runner: Runner):
    if os.path.isdir(path):
        for x in os.listdir(path): find_tests(os.path.join(path, x), runner)
    elif os.path.isfile(path):
        with open(path, "r") as file:
            text = file.read()

            while "//" in text:
                i = text.index("//")
                try:
                    j = text.index("\n", i)
                except ValueError:
                    j = len(text)
                text = text[:i] + text[j:]
            while "/*" in text:
                i = text.index("/*")
                try:
                    j = text.index("*/", i)
                except ValueError:
                    j = len(text) - 2
                text = text[:i] + text[j + 2:]
            
            idx = 0
            while idx < len(text):
                if text[idx] == "\"":
                    jdx = idx + 1
                    while jdx < len(text) and text[jdx] != "\"":
                        if text[jdx] == "\\": jdx += 1
                        jdx += 1
                    if jdx >= len(text): jdx -= 2
                    text = text[:idx] + text[jdx + 1:]
                else: idx += 1
            
            tests = text.split("CLTEST")
            for test in tests[1:]:
                start_paren = -1
                endof_paren = -1
                for i, c in enumerate(test):
                    if start_paren == -1:
                        if c == '(': start_paren = i
                    elif endof_paren == -1 and c == ')': endof_paren = i
                if endof_paren == -1: continue

                runner.add_test(Test(path, test[start_paren + 1:endof_paren]))