import json
import sys

def check_exercise(file, exercise_name):
    # 读取 JSON 文件
    try:
        with open(file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return 2
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in '{file}'.")
        return 2

    # 查找指定的 exercise 并获取其 result
    for exercise in data.get("exercises", []):
        if exercise.get("name") == exercise_name:
            return 0 if exercise.get("result") else 1

    print("Error: Exercise not found or invalid result value.")
    return 2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python check_exercise.py <file.json> <exercise_name>")
        sys.exit(2)

    file = sys.argv[1]
    exercise_name = sys.argv[2]
    exit_code = check_exercise(file, exercise_name)
    sys.exit(exit_code)
