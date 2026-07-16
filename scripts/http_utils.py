"""HTTP 工具模块 — 用 curl 子进程绕过 Python requests 的 SSL BAD_ECPOINT 问题。

gov.cn 网站的 TLS 证书使用了不标准的 EC point 格式，导致 Python 的 OpenSSL
在握手阶段就报 BAD_ECPOINT 错误（verify=False 也无法解决，因为这是握手层
而非验证层的问题）。curl 使用系统自带的 GnuTLS/OpenSSL 库，不受此影响。
"""

import subprocess
import json as _json


def curl_get(url, headers=None, timeout=15):
    """用 curl GET 请求，返回 response text。失败返回 None。"""
    cmd = ['curl', '-sk', '--connect-timeout', str(timeout), '--max-time', str(timeout + 10)]
    if headers:
        for k, v in headers.items():
            cmd.extend(['-H', f'{k}: {v}'])
    cmd.append(url)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 15)
        if result.returncode == 0 and result.stdout:
            return result.stdout
    except Exception:
        pass
    return None


def curl_post(url, data=None, headers=None, timeout=15):
    """用 curl POST 请求，返回 response text。失败返回 None。"""
    cmd = ['curl', '-sk', '--connect-timeout', str(timeout), '--max-time', str(timeout + 10), '-X', 'POST']
    if headers:
        for k, v in headers.items():
            cmd.extend(['-H', f'{k}: {v}'])
    if data:
        if isinstance(data, dict):
            cmd.extend(['-d', '&'.join(f'{k}={v}' for k, v in data.items())])
        else:
            cmd.extend(['-d', str(data)])
    cmd.append(url)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 15)
        if result.returncode == 0 and result.stdout:
            return result.stdout
    except Exception:
        pass
    return None


def curl_post_json(url, json_data=None, headers=None, timeout=15):
    """用 curl POST JSON 请求，返回 parsed JSON dict。失败返回 None。"""
    cmd = ['curl', '-sk', '--connect-timeout', str(timeout), '--max-time', str(timeout + 10), '-X', 'POST']
    base_headers = {'Content-Type': 'application/json'}
    if headers:
        base_headers.update(headers)
    for k, v in base_headers.items():
        cmd.extend(['-H', f'{k}: {v}'])
    if json_data:
        cmd.extend(['-d', _json.dumps(json_data)])
    cmd.append(url)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 15)
        if result.returncode == 0 and result.stdout:
            return _json.loads(result.stdout)
    except Exception:
        pass
    return None
