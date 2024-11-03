import json
import sys
import shutil
import subprocess

def get_exercise_src_file(exercise_name):
    try:
        with open("info.toml", 'r') as f:
            toml_str = f.read()
    except FileNotFoundError:
        print("  Error: File 'info.toml' not found.")
        return None
    except toml.TomlDecodeError:
        print("  Error: Failed to parse TOML in 'info.toml'.")
        return None

    lines = toml_str.strip().split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if line == f'name = "{exercise_name}"':
            result = {}
            # 向下检查接下来的几行，提取 path 和 mode
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if next_line.startswith('path ='):
                    # 提取 path
                    result['path'] = next_line.split('=', 1)[1].strip().strip('"')
                elif next_line.startswith('mode ='):
                    # 提取 mode
                    result['mode'] = next_line.split('=', 1)[1].strip().strip('"')
                elif next_line.startswith('name =') or next_line.startswith('[[exercises]]'):
                    # 遇到下一个练习，结束循环
                    break
                j += 1
            return result
    return None

def prepare_format_check(exercise_path):
    destination = "format_check/src/main.rs"
    shutil.copyfile(exercise_path, destination)

def cargo_fmt_check(manifest_path):
    try:
        result = subprocess.run(
            ["cargo", "fmt", "--check", "--manifest-path", manifest_path],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        print(e.stderr)
        return False

def cargo_clippy_check(manifest_path):
    try:
        result = subprocess.run(
            ["cargo", "clippy", "--manifest-path", manifest_path],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        print(e.stderr)
        return False

def check_format_result(exercise_name):
    print("Checking source code format...")
    info = get_exercise_src_file(exercise_name)

    if info is None:
        return False

    # skips 'buildscript' and 'clippy' exercises
    if info['mode'] != 'compile' and info['mode'] != 'test':
        print(f"[!] {exercise_name} is a {info['mode']} exercise. Skipping format check.")
        return True

    file = info['path']

    print("  Preparing source code for format check...")
    prepare_format_check(file)

    print("  Running format check...")

    print("// =====================================================")
    print("//  Running cargo fmt...")
    print("// =====================================================")
    fmt_result = cargo_fmt_check("format_check/Cargo.toml")

    print("// =====================================================")
    print("//    Running cargo clippy...")
    print("// =====================================================")
    
    clippy_result = cargo_clippy_check("format_check/Cargo.toml")

    return fmt_result and clippy_result

def check_run_result(file, exercise_name):
    print("Checking test execution result...")
    try:
        with open(file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"  Error: File '{file}' not found.")
        return False
    except json.JSONDecodeError:
        print(f"  Error: Failed to parse JSON in '{file}'.")
        return False

    # 查找指定的 exercise 并获取其 result
    for exercise in data.get("exercises", []):
        if exercise.get("name") == exercise_name:
            return exercise.get("result")

    print("  Error: Exercise not found or invalid result value.")
    return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python check_exercise.py <file.json> <exercise_name>")
        sys.exit(2)

    file = sys.argv[1]
    exercise_name = sys.argv[2]
    execution_result = check_run_result(file, exercise_name)

    if execution_result:
        print("[!] Test execution result: PASSED")
    else:
        print("[!] Test execution result: FAILED")

    format_result = check_format_result(exercise_name)

    if format_result:
        print("[!] Source code format check: PASSED")
    else:
        print("[!] Source code format check: FAILED")

    if execution_result and format_result:
        sys.exit(0)
    else:
        sys.exit(1)
        
