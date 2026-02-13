import collections
import re

fname = "undefined_names_pylint.txt"
content = ""

# Try different encodings
for enc in ["utf-8", "utf-16", "cp1252", "latin1"]:
    try:
        with open(fname, "r", encoding=enc) as f:
            content = f.read()
        if content:
            print(f"Successfully read with {enc}")
            break
    except Exception as e:
        print(f"Failed with {enc}: {e}")

if not content:
    print("Could not read file content")
    exit(1)

imports = collections.defaultdict(set)

# Pylint format: filename:line: [code] message
# e.g. showcase\saas_landing.py:537: [F405] Name 'serve' is undefined from star imports: fasthtml.common

for line in content.splitlines():
    if "[F405]" in line:
        try:
            parts = line.split(":")
            filename = parts[0].strip()
            message = line.split("]", 1)[1]
            if "is undefined from star imports" in message:
                # message: " Name 'serve' is undefined from star imports: fasthtml.common"
                name = message.split("'")[1]
                imports[filename].add(name)
        except Exception as e:
            pass

if not imports:
    print("No imports found. Dumping first 10 lines of content:")
    print(content[:500])

for filename, names in imports.items():
    print(f"File: {filename}")
    print(f"Imports: {', '.join(sorted(list(names)))}")
    print("-" * 20)
