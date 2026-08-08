import subprocess
import sys
import tempfile
import os
import logging

logger = logging.getLogger(__name__)

TIMEOUT = 5

BLOCKED = [
    'import os', 'import sys', 'import subprocess',
    'import socket', 'import shutil', '__import__',
    'open(', 'exec(', 'eval(', 'import importlib',
]

def is_safe(code):
    code_lower = code.lower()
    for b in BLOCKED:
        if b.lower() in code_lower:
            return False, f"Use of '{b}' is not allowed."
    return True, ""

def run_function(student_code, wrapper_code, input_data, timeout=TIMEOUT):
    # Strip ALL carriage returns aggressively
    student_code = student_code.replace('\r\n', '\n').replace('\r', '\n')
    wrapper_code = wrapper_code.replace('\r\n', '\n').replace('\r', '\n')
    input_data = input_data.replace('\r\n', '\n').replace('\r', '\n')

    # Log what we actually received for debugging
    logger.debug("STUDENT CODE REPR: %r", student_code)

    safe, reason = is_safe(student_code)
    if not safe:
        return "", f"Security Error: {reason}", False

    full_code = (
        student_code + "\n\n" +
        wrapper_code + "\n\n" +
        "import sys\n"
        "input_data = sys.stdin.read()\n"
        "try:\n"
        "    output = _run(input_data)\n"
        "    print(output, end='')\n"
        "except Exception as e:\n"
        "    print(f'Runtime Error: {e}', file=sys.stderr)\n"
    )

    # Log the full code being written
    logger.debug("FULL CODE REPR: %r", full_code[:300])

    # Write as BINARY to avoid Windows text-mode \r\n injection
    with tempfile.NamedTemporaryFile(mode='wb', suffix='.py', delete=False) as f:
        f.write(full_code.encode('utf-8'))
        tmp = f.name

    # Verify file on disk has no \r
    with open(tmp, 'rb') as f:
        raw = f.read()
    if b'\r' in raw:
        logger.error("CARRIAGE RETURN FOUND IN TEMP FILE! Removing...")
        clean = raw.replace(b'\r\n', b'\n').replace(b'\r', b'\n')
        with open(tmp, 'wb') as f:
            f.write(clean)

    try:
        result = subprocess.run(
            [sys.executable, tmp],
            input=input_data,
            capture_output=True, text=True,
            timeout=timeout,
        )
        logger.debug("STDOUT: %r  STDERR: %r", result.stdout, result.stderr)
        return result.stdout.strip(), result.stderr.strip(), False
    except subprocess.TimeoutExpired:
        return "", "Time Limit Exceeded (5 seconds)", True
    finally:
        try:
            os.unlink(tmp)
        except:
            pass

def judge(student_code, wrapper_code, test_cases):
    results = []
    for tc in test_cases:
        stdout, stderr, timed_out = run_function(student_code, wrapper_code, tc.input_data)
        actual = stdout.strip()
        expected = tc.expected_output.strip()
        passed = (actual == expected) and not timed_out and not stderr
        results.append({
            'test_case': tc,
            'passed': passed,
            'actual_output': actual if not timed_out else 'Time Limit Exceeded',
            'expected_output': expected,
            'error': stderr if stderr else '',
        })
    return results