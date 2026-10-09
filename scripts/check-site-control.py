"""Exercise real start/stop processes; run after npm run build, with port 4324 free."""
import os
import signal
from pathlib import Path
import subprocess
import time
from urllib.request import urlopen

project = Path(__file__).resolve().parent.parent
script = project / 'scripts/site.sh'

def control(action, expected=0):
    result = subprocess.Popen(['bash', str(script), action], cwd='/tmp', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True)
    stdout, stderr = result.communicate(timeout=25)
    try:
        os.killpg(result.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    assert result.returncode == expected, (action, result.returncode, stdout, stderr)
    return stdout

def listener():
    result = subprocess.run(['lsof', '-nP', '-t', '-iTCP:4324', '-sTCP:LISTEN'], capture_output=True, text=True)
    return result.stdout.strip()

assert not listener(), 'Port 4324 is occupied; stop its service before running this test.'
foreign = None
adopted = None
try:
    assert '未运行' in control('status')
    control('start')
    pid = listener()
    assert pid
    with urlopen('http://127.0.0.1:4324/', timeout=5) as response:
        assert response.status == 200
    control('start')
    assert listener() == pid, 'Repeated start must not spawn another server'
    control('restart')
    assert listener() and listener() != pid
    control('stop')
    assert not listener()
    control('stop')
    # Reused or stale PID files must never cause an unrelated process to be killed.
    state = project / 'work/site-control'
    state.mkdir(parents=True, exist_ok=True)
    (state / 'preview.pid').write_text(str(os.getpid()))
    control('stop')
    assert not (state / 'preview.pid').exists()

    foreign = subprocess.Popen(['python3', '-m', 'http.server', '4324', '--bind', '127.0.0.1'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(50):
        if listener():
            break
        time.sleep(0.1)
    assert listener() == str(foreign.pid)
    for action in ('start', 'stop', 'restart', 'status'):
        control(action, expected=1)
        assert foreign.poll() is None, 'Controller must not kill a foreign port owner'
    foreign.terminate()
    foreign.wait(timeout=5)
    foreign = None

    adopted = subprocess.Popen(['node', str(project / 'node_modules/.bin/astro'), 'preview', '--host', '127.0.0.1', '--port', '4324'], cwd=project, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(50):
        if listener():
            break
        time.sleep(0.1)
    assert listener() == str(adopted.pid)
    control('start')
    assert listener() == str(adopted.pid), 'Existing project preview should be reused'
    control('stop')
    adopted.wait(timeout=5)
    assert not listener()
    print('Control checks passed: start/status, idempotency, restart/stop, stale PID, foreign port protection, existing preview adoption, arbitrary working directory and launcher-session independence.')
finally:
    if foreign is not None:
        foreign.terminate()
        foreign.wait(timeout=5)
    if adopted is not None and adopted.poll() is None:
        adopted.terminate()
        adopted.wait(timeout=5)
    subprocess.run(['bash', str(script), 'stop'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
