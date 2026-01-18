import os

def to_lf(path):
    with open(path, 'rb') as f:
        content = f.read()
    
    new_content = content.replace(b'\r\n', b'\n')
    
    if new_content != content:
        with open(path, 'wb') as f:
            f.write(new_content)
        return True
    return False

count = 0
for root, _, files in os.walk('.'):
    if '.git' in root or '.venv' in root or '__pycache__' in root:
        continue
    for file in files:
        if file.endswith('.py'):
            path = os.path.join(root, file)
            if to_lf(path):
                print(f"Fixed: {path}")
                count += 1

print(f"Total files normalized: {count}")
