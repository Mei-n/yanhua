import http.server
import socketserver

PORT = 8000  # 设置端口号

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("本地服务器已启动！访问地址：http://localhost:" + str(PORT))
    link = "http://localhost:" + str(PORT) + "/index.html"
    print(f"HTML 文件的链接地址为：{link}")
    httpd.serve_forever()