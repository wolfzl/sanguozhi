#!/bin/bash
# Local Astro preview controller. Also works when copied beside sanguozhi-simplified.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
if [ -f "$SCRIPT_DIR/sanguozhi-simplified/package.json" ]; then
  PROJECT_DIR="$SCRIPT_DIR/sanguozhi-simplified"
elif [ -f "$SCRIPT_DIR/../package.json" ]; then
  PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd -P)"
else
  echo "找不到网站目录 sanguozhi-simplified。" >&2
  exit 1
fi

PORT=4324
URL="http://127.0.0.1:$PORT/"
ASTRO_BIN="$PROJECT_DIR/node_modules/.bin/astro"
STATE_DIR="$PROJECT_DIR/work/site-control"
PID_FILE="$STATE_DIR/preview.pid"
LOG_FILE="$STATE_DIR/preview.log"
LOCK_DIR="$STATE_DIR/control.lock"

listener_pid() {
  lsof -nP -t -iTCP:"$PORT" -sTCP:LISTEN 2>/dev/null | sort -u || true
}

is_our_preview() {
  local pid="${1:-}" command
  case "$pid" in ''|*[!0-9]*) return 1 ;; esac
  command="$(ps -p "$pid" -o command= 2>/dev/null || true)"
  case "$command" in
    *"$ASTRO_BIN preview --host 127.0.0.1 --port $PORT") return 0 ;;
    *) return 1 ;;
  esac
}

port_conflict() {
  echo "端口 $PORT 被其他程序占用（PID：$1）。未启动或停止该程序。" >&2
  return 1
}

start_site() {
  local pid node_bin attempt owner
  pid="$(listener_pid)"
  if [ -n "$pid" ]; then
    is_our_preview "$pid" || { port_conflict "$pid"; return 1; }
    printf '%s\n' "$pid" > "$PID_FILE"
    echo "网站已在运行（PID：${pid}）：$URL"
    return
  fi
  if [ -f "$PID_FILE" ] && is_our_preview "$(cat "$PID_FILE")"; then
    echo "已有网站进程正在启动，请稍后执行 status。"
    return
  fi
  if [ ! -f "$ASTRO_BIN" ]; then
    echo "缺少依赖，请先执行：cd \"$PROJECT_DIR\" && npm ci" >&2
    return 1
  fi
  if [ ! -f "$PROJECT_DIR/dist/index.html" ]; then
    echo "缺少构建文件，请先执行：cd \"$PROJECT_DIR\" && npm run build" >&2
    return 1
  fi
  node_bin="$(command -v node || true)"
  if [ -z "$node_bin" ]; then
    for node_bin in /opt/homebrew/bin/node /usr/local/bin/node; do
      [ ! -x "$node_bin" ] || break
    done
  fi
  if [ ! -x "$node_bin" ]; then
    echo "找不到 Node.js，请安装 Node.js 22.12 或更新版本。" >&2
    return 1
  fi
  cd "$PROJECT_DIR"
  # A separate process group survives the terminal or calling tool exiting.
  pid="$("$node_bin" -e '
    const fs = require("node:fs");
    const {spawn} = require("node:child_process");
    const [project, astro, log, port] = process.argv.slice(1);
    const fd = fs.openSync(log, "a");
    const child = spawn(process.execPath, [astro, "preview", "--host", "127.0.0.1", "--port", port], {
      cwd: project, detached: true, stdio: ["ignore", fd, fd]
    });
    child.once("error", error => { console.error(error.message); process.exitCode = 1; });
    child.once("spawn", () => {
      fs.closeSync(fd);
      process.stdout.write(String(child.pid));
      child.unref();
    });
  ' "$PROJECT_DIR" "$ASTRO_BIN" "$LOG_FILE" "$PORT")"
  printf '%s\n' "$pid" > "$PID_FILE"
  for ((attempt=0; attempt<60; attempt++)); do
    owner="$(listener_pid)"
    if [ "$owner" = "$pid" ] && curl -fsS --max-time 1 "$URL" > /dev/null 2>&1; then
      echo "网站已启动（PID：${pid}）：$URL"
      echo "日志：$LOG_FILE"
      return
    fi
    if ! kill -0 "$pid" 2>/dev/null || { [ -n "$owner" ] && [ "$owner" != "$pid" ]; }; then
      break
    fi
    sleep 0.2
  done
  if is_our_preview "$pid"; then kill "$pid" 2>/dev/null || true; fi
  rm -f "$PID_FILE"
  echo "启动失败，请查看日志：$LOG_FILE" >&2
  return 1
}

stop_site() {
  local pid attempt
  pid="$(listener_pid)"
  if [ -n "$pid" ]; then
    is_our_preview "$pid" || { port_conflict "$pid"; return 1; }
  elif [ -f "$PID_FILE" ] && is_our_preview "$(cat "$PID_FILE")"; then
    pid="$(cat "$PID_FILE")"
  else
    rm -f "$PID_FILE"
    echo "网站未运行。"
    return
  fi
  kill "$pid"
  for ((attempt=0; attempt<50; attempt++)); do
    if ! is_our_preview "$pid"; then
      rm -f "$PID_FILE"
      echo "网站已停止。"
      return
    fi
    sleep 0.1
  done
  echo "网站尚未退出（PID：${pid}），请检查日志：$LOG_FILE" >&2
  return 1
}

status_site() {
  local pid
  pid="$(listener_pid)"
  if [ -z "$pid" ]; then
    echo "网站未运行。"
  elif is_our_preview "$pid"; then
    echo "网站正在运行（PID：${pid}）：$URL"
    echo "日志：$LOG_FILE"
  else
    port_conflict "$pid"
  fi
}

ACTION="${1:-status}"
case "$ACTION" in
  status) status_site ;;
  start|stop|restart)
    mkdir -p "$STATE_DIR"
    if ! mkdir "$LOCK_DIR" 2>/dev/null; then
      echo "另一个启停操作正在执行，请稍后重试。如操作已中断，可删除：$LOCK_DIR" >&2
      exit 1
    fi
    trap 'rmdir "$LOCK_DIR" 2>/dev/null || true' EXIT
    trap 'exit 130' INT
    trap 'exit 143' TERM
    case "$ACTION" in
      start) start_site ;;
      stop) stop_site ;;
      restart) stop_site; start_site ;;
    esac
    ;;
  -h|--help|help)
    echo "用法：$0 {start|stop|restart|status}"
    echo "启动 / 停止 / 重启 / 查看状态；不带参数时查看状态。"
    ;;
  *) echo "用法：$0 {start|stop|restart|status}" >&2; exit 2 ;;
esac
