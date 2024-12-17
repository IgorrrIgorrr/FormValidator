import subprocess


def run_tests():
    print("Running tests...")
    result = subprocess.run(
        ["python", "tests/test_requests.py"], capture_output=True, text=True
    )
    print(result.stdout)
    if result.returncode == 0:
        print("All tests passed!")
    else:
        print("Tests failed!")
        print(result.stderr)


if __name__ == "__main__":
    run_tests()
