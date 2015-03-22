# -*- coding:utf-8 -*-

from bottle import route ,run, static_file, template
from app.controllers import manage

# ==========================================
# 静的なパスを追加
# ==========================================
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static/')

# ビルトインの開発用サーバーの起動
# ここでは、debugとreloaderを有効にしている
run(host='localhost', port=8080, debug=True, reloader=True)