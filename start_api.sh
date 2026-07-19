#!/usr/bin/env bash
# 启动童行活动/场馆数据 API
cd "$(dirname "$0")"
PORT="${PORT:-8787}" python3 api/json_api.py
