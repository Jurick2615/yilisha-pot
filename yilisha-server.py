#!/usr/bin/env python3
"""
伊丽莎锅 - 永久 URL 服务管理脚本
自动启动 Python HTTP 服务 + localhost.run 隧道
如果地址变了，自动检测并打印新地址
"""

import subprocess, time, re, os, signal, sys

HTML_DIR = os.path.expanduser("~/Desktop/jurick_py")
PORT = 8000
TUNNEL_LOG = "/tmp/yilisha-tunnel.log"

def start_server():
    """启动 Python HTTP 服务器"""
    proc = subprocess.Popen(
        ["python3", "-m", "http.server", str(PORT)],
        cwd=HTML_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print(f"✅ HTTP 服务已启动 (端口 {PORT})")
    return proc

def start_tunnel():
    """启动 localhost.run 隧道"""
    with open(TUNNEL_LOG, "w") as f:
        proc = subprocess.Popen(
            ["ssh", "-o", "StrictHostKeyChecking=no", 
             "-o", "ServerAliveInterval=30",
             "-R", f"80:localhost:{PORT}", "nokey@localhost.run"],
            stdout=f, stderr=subprocess.STDOUT,
        )
    print("🔄 隧道连接中...")
    time.sleep(8)
    
    # 读取日志获取 URL
    with open(TUNNEL_LOG) as f:
        log = f.read()
    
    match = re.search(r'https://([a-f0-9]+\.lhr\.life)', log)
    if match:
        url = match.group(1)
        print(f"✅ 隧道地址: https://{url}")
        print(f"📄 页面地址: https://{url}/yilisha-pot.html")
        return proc, url
    else:
        print("❌ 获取 URL 失败，检查日志:")
        print(log[-500:])
        return proc, None

def monitor(server, tunnel, last_url):
    """监控隧道状态"""
    try:
        while True:
            time.sleep(30)
            # 检查隧道进程
            if tunnel.poll() is not None:
                print("⚠️ 隧道断开，正在重连...")
                tunnel, new_url = start_tunnel()
                if new_url and new_url != last_url:
                    print(f"🆕 新地址: https://{new_url}/yilisha-pot.html")
                    last_url = new_url
            
            # 检查服务器
            if server.poll() is not None:
                print("⚠️ HTTP 服务断开，正在重启...")
                server = start_server()
    except KeyboardInterrupt:
        print("\n👋 正在关闭...")
        server.terminate()
        tunnel.terminate()
        sys.exit(0)

if __name__ == "__main__":
    print("=" * 50)
    print("  🏯 伊丽莎锅 · 永久服务")
    print("=" * 50)
    
    server = start_server()
    tunnel, url = start_tunnel()
    
    if url:
        print(f"\n📌 发给 F小玉 的链接:")
        print(f"   https://{url}/yilisha-pot.html")
    
    monitor(server, tunnel, url)
