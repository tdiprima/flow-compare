#!/bin/bash
# redisctl.sh 🧸
# Simple Redis control script for macOS

ACTION=$1

if [[ -z "$ACTION" ]]; then
  echo "Usage: $0 {up|down|restart|status}"
  exit 1
fi

case "$ACTION" in
  up)
    echo "🚀 Starting Redis..."
    brew services start redis
    ;;
  down)
    echo "🛑 Stopping Redis..."
    brew services stop redis
    ;;
  restart)
    echo "♻️  Restarting Redis..."
    brew services restart redis
    ;;
  status)
    echo "📊 Checking Redis status..."
    brew services list | grep redis
    ;;
  *)
    echo "❓ Unknown command: $ACTION"
    echo "Usage: $0 {up|down|restart|status}"
    exit 1
    ;;
esac
