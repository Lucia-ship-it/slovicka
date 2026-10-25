# Spustenie: python3 zdroj/build.py  -> vytvori index.html zo zdroj/template.html a zdroj/all.txt
import json, os, hashlib
d = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(d, "template.html"), encoding="utf-8").read()
w = open(os.path.join(d, "all.txt"), encoding="utf-8").read()
head = ('<!doctype html>\n<html lang="sk">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n'
        '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style>\n</head>\n<body>\n')
ver = hashlib.sha1((t + w).encode("utf-8")).hexdigest()[:10]
t = t.replace("/*VERSION*/", ver)
open(os.path.join(d, "..", "version.json"), "w").write(json.dumps({"v": ver}))
open(os.path.join(d, "..", "index.html"), "w", encoding="utf-8").write(
    head + t.replace("/*WORDS*/", json.dumps(w, ensure_ascii=False)) + "\n</body>\n</html>\n")
