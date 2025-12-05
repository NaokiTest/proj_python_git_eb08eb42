import os

# ディレクトリを作成
os.makedirs('proj_python_git_eb08eb42', exist_ok=True)

# ファイルに書き込むコード
code = """def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
"""

# ファイルを作成してコードを書き込む
with open('proj_python_git_eb08eb42/basic_calculations.py', 'w') as f:
    f.write(code)