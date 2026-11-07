# -*- coding: utf-8 -*-
"""
小恐龙公文排版助手 · gw.xkonglong.com 静态站点生成脚本
- 读取仓库根目录的 README.md / feature.md / vba.md / faq.md / update.md
- 转换为静态 HTML，输出到 preview/ 目录（本地预览用；验收后复制到仓库根目录发布）
用法： python build_site.py
"""
import os
import re
import html as _html

ROOT = os.path.dirname(os.path.abspath(__file__))
# 在 git 检出目录中直接生成到站点根目录；独立文件夹（如预览副本）则输出到 preview/
OUT = ROOT if os.path.isdir(os.path.join(ROOT, ".git")) else os.path.join(ROOT, "preview")
SITE = "https://gw.xkonglong.com"

VERSION = "v3.8.0.0"
VERSION_DATE = "2026年4月13日"

# --------------------------------------------------------------------------
# 图标
# --------------------------------------------------------------------------
ICONS = {
    "layout": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 9v11"/></svg>',
    "type": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M4 6V4h16v2M12 4v16M8 20h8"/></svg>',
    "wand": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M5 19l9-9M14 5l1.5 3.5L19 10l-3.5 1.5L14 15l-1.5-3.5L9 10l3.5-1.5z"/><path d="M4 21l1-1"/></svg>',
    "stamp": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M4 21h16M6 17h12v-2.5c0-1.4-1.1-2.5-2.5-2.5H8.5C7.1 12 6 13.1 6 14.5z"/><path d="M12 12V8"/><circle cx="12" cy="6" r="2"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M12 3l7 3v6c0 4.4-3 8.2-7 9-4-.8-7-4.6-7-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
    "code": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M9 7l-5 5 5 5M15 7l5 5-5 5"/></svg>',
    "download": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M12 3v11M7 10l5 5 5-5M4 20h16"/></svg>',
    "github": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.5 2 2 6.6 2 12.2c0 5.4 3.4 9.9 8.2 11.5.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.5-1.4-1.3-1.8-1.3-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.7 1.3 3.4 1 .1-.8.4-1.3.7-1.6-2.7-.3-5.5-1.4-5.5-6 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.1 0 0 1 .3 3.2 1.2a11 11 0 0 1 5.8 0c3.2-.9 3.2-1.2 3.2-1.2.6 1.6.2 2.8.1 3.1.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.7-5.5 6 .4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6C18.6 22.1 22 17.6 22 12.2 22 6.6 17.5 2 12 2z"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 19V5M6 11l6-6 6 6"/></svg>',
    "info": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 11v5"/></svg>',
    "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
    "cloud": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M7 18h10a4 4 0 0 0 .6-8 5.5 5.5 0 0 0-10.4-1.4A3.8 3.8 0 0 0 7 18z"/><path d="M12 11v4M10 12.8l2 2 2-2"/></svg>',
    "qrcode": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><path d="M14 14h3v3h-3zM20 14v3M14 20h3M20 20h1"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 21l1.9-5.4A8 8 0 1 1 21 12z"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M5 13l4 4 10-10"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
    "sun": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5L19 19M19 5l-1.5 1.5M6.5 17.5L5 19"/></svg>',
    "moon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a7 7 0 0 0 10.5 10.5z"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 5.5v16"/></svg>',
}

NAV = [
    ("index.html", "首页"),
    ("guide.html", "入门指引"),
    ("feature.html", "功能介绍"),
    ("vba.html", "VBA 脚本"),
    ("faq.html", "常见问题"),
    ("update.html", "更新日志"),
]


# --------------------------------------------------------------------------
# markdown -> html
# --------------------------------------------------------------------------
def norm_src(src):
    src = src.strip()
    if src.startswith("/img/"):
        return src[1:]
    if src.startswith("./img/"):
        return src[2:]
    return src


def _link(m):
    text, url = m.group(1).strip(), m.group(2).strip()
    if not text:
        return ""
    if url.startswith("http") or url.startswith("//"):
        ext = ' target="_blank" rel="noopener"'
    else:
        ext = ""
    return '<a href="%s"%s>%s</a>' % (url, ext, text)


def inline(text):
    text = re.sub(r'!\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)',
                  lambda m: '<img src="%s" alt="%s">' % (norm_src(m.group(2)), m.group(1)), text)
    text = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', _link, text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text


LIST_RE = re.compile(r'^(\s*)(?:[+*-]|(\d+)\.)\s+(.*)$')


def convert(md, heading_offset=0, collect_headings=None):
    """把 markdown 转成 html 片段；collect_headings 传入列表则收集 h2 锚点"""
    lines = md.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out = []
    buf = []          # 段落缓冲
    in_code = False
    list_stack = []   # [(level, tag)]
    hidx = [0]

    def flush_par():
        if buf:
            raw_lines = [x.rstrip() for x in buf]
            buf.clear()
            content_lines = [l.strip() for l in raw_lines if l.strip()]
            if not content_lines:
                return
            if len(content_lines) > 1 and any(l.startswith("  ") for l in raw_lines if l.strip()):
                # 原文用缩进表示并列条目（例如 Office 版本清单），保留换行
                out.append("<p>" + "<br>".join(inline(l) for l in content_lines) + "</p>")
            else:
                out.append("<p>" + inline(" ".join(content_lines)) + "</p>")

    def close_lists():
        while list_stack:
            out.append("</%s>" % list_stack.pop()[1])

    i = 0
    n = len(lines)
    while i < n:
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()

        if in_code:
            if stripped.startswith("```"):
                in_code = False
                out.append("</code></pre>")
            else:
                out.append(_html.escape(raw))
            i += 1
            continue

        if stripped.startswith("```"):
            flush_par()
            close_lists()
            in_code = True
            out.append('<pre><code>')
            i += 1
            continue

        # <Note type="tip"> ... </Note>
        if stripped.startswith("<Note"):
            flush_par()
            close_lists()
            note_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("</Note"):
                note_lines.append(lines[i])
                i += 1
            i += 1
            body = convert("\n".join(note_lines))
            out.append('<aside class="note">' + body + "</aside>")
            continue

        if not stripped:
            flush_par()
            i += 1
            continue

        # 标题
        m = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if m:
            flush_par()
            close_lists()
            raw_level = len(m.group(1))
            text = inline(m.group(2).strip())
            if raw_level == 1:
                # 文档标题已由页面头部呈现
                i += 1
                continue
            level = min(raw_level, 4)
            hidx[0] += 1
            sid = "sec-%d" % hidx[0]
            out.append('<h%d id="%s">%s</h%d>' % (level, sid, text, level))
            if collect_headings is not None and level == 2:
                plain = re.sub(r'<[^>]+>', '', text)
                collect_headings.append((sid, plain))
            i += 1
            continue

        # 分割线
        if re.match(r'^([-*_])\1{2,}$', stripped):
            flush_par()
            close_lists()
            out.append("<hr>")
            i += 1
            continue

        # 列表
        m = LIST_RE.match(line)
        if m:
            flush_par()
            indent = len(m.group(1).replace("\t", "    "))
            level = 1 if indent >= 2 else 0
            ordered = m.group(2) is not None
            tag = "ol" if ordered else "ul"
            while list_stack and list_stack[-1][0] > level:
                out.append("</%s>" % list_stack.pop()[1])
            if not list_stack or list_stack[-1][0] < level:
                list_stack.append((level, tag))
                out.append("<%s>" % tag)
            out.append("<li>" + inline(m.group(3).strip()) + "</li>")
            i += 1
            continue

        # 引用
        if stripped.startswith(">"):
            flush_par()
            close_lists()
            out.append("<blockquote><p>" + inline(stripped.lstrip("> ").strip()) + "</p></blockquote>")
            i += 1
            continue

        # 普通段落
        if list_stack:
            close_lists()
        buf.append(line)
        i += 1

    flush_par()
    close_lists()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


# --------------------------------------------------------------------------
# 布局
# --------------------------------------------------------------------------
HEAD_BASE = """<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<meta name="theme-color" content="#b3262c">
<meta property="og:title" content="__TITLE__">
<meta property="og:description" content="__DESC__">
<meta property="og:type" content="website">
<meta property="og:url" content="__URL__">
<link rel="icon" href="favicon.ico">
<link rel="stylesheet" href="assets/style.css">
<script>
(function(){
  try {
    var t = localStorage.getItem('xkl-theme');
    if (t === 'dark') document.documentElement.setAttribute('data-theme', 'dark');
  } catch (e) {}
})();
</script>
</head>"""


def header(current=""):
    links = "\n".join(
        '        <a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if href == current else "", label)
        for href, label in NAV
    )
    return """
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html">
      <span class="brand-seal" aria-hidden="true">公</span>
      <span class="brand-text">
        <span class="brand-name">小恐龙公文排版助手</span>
        <span class="brand-sub">for Word &amp; WPS</span>
      </span>
    </a>
    <nav class="nav" aria-label="主导航">
__NAV__
    </nav>
    <div class="nav-tools">
      <button class="icon-btn" id="theme-toggle" type="button" aria-label="切换主题" title="切换深浅主题">__ICON_THEME__</button>
      <a class="btn-nav" href="https://github.com/xkonglong/gw" target="_blank" rel="noopener">GitHub 源码</a>
      <button class="icon-btn burger" id="menu-toggle" type="button" aria-label="打开菜单">__ICON_MENU__</button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu">
  <a href="index.html">首页</a>
  <a href="guide.html">入门指引</a>
  <a href="feature.html">功能介绍</a>
  <a href="vba.html">VBA 脚本</a>
  <a href="faq.html">常见问题</a>
  <a href="update.html">更新日志</a>
  <a href="https://github.com/xkonglong/gw" target="_blank" rel="noopener">GitHub 源码</a>
</div>
""".replace("__NAV__", links) \
   .replace("__ICON_THEME__", ICONS["sun"]) \
   .replace("__ICON_GH__", ICONS["github"]) \
   .replace("__ICON_MENU__", ICONS["menu"])


FOOTER = """
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="index.html">
          <span class="brand-seal" aria-hidden="true">公</span>
          <span class="brand-text">
            <span class="brand-name">小恐龙公文排版助手</span>
            <span class="brand-sub">for Word &amp; WPS</span>
          </span>
        </a>
        <p>依据《党政机关公文格式》(GB/T 9704—2012) 的格式要求，快速设置页面版式、文字格式，插入红头、红线、版记线与页码。</p>
        <p>本插件完全免费开源，承诺不含任何恶意代码。</p>
      </div>
      <div class="footer-col">
        <h5>文档</h5>
        <ul>
          <li><a href="guide.html">入门指引</a></li>
          <li><a href="feature.html">功能介绍</a></li>
          <li><a href="vba.html">VBA 脚本指南</a></li>
          <li><a href="faq.html">常见问题</a></li>
          <li><a href="update.html">更新日志</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>下载与交流</h5>
        <ul>
          <li><a href="#download">下载安装包</a></li>
          <li><a href="https://github.com/xkonglong/gw" target="_blank" rel="noopener">GitHub 源码</a></li>
          <li><a href="https://github.com/xkonglong/gw/discussions" target="_blank" rel="noopener">VBA 脚本讨论组</a></li>
          <li><a href="https://pd.qq.com/s/exu99qgjm" target="_blank" rel="noopener">QQ 频道</a></li>
          <li><a href="https://support.qq.com/products/57503" target="_blank" rel="noopener">问题反馈</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2020–2026 <a href="https://xkonglong.com">小恐龙工作室</a> · 本站为开源项目文档站点</span>
      <span>gw.xkonglong.com · 小恐龙公文排版助手 __VERSION__</span>
    </div>
  </div>
</footer>
<button class="to-top" id="to-top" type="button" aria-label="回到顶部">__ICON_UP__</button>
<script src="assets/app.js" defer></script>
""".replace("__VERSION__", VERSION).replace("__ICON_UP__", ICONS["up"])


def page(title, desc, body, current="", url=""):
    url = url or SITE + "/"
    doc = HEAD_BASE.replace("__TITLE__", title).replace("__DESC__", desc).replace("__URL__", url)
    return (doc + "\n<body>\n" + header(current) + body + FOOTER + "\n</body>\n</html>\n")


# --------------------------------------------------------------------------
# 文档页
# --------------------------------------------------------------------------
DOC_META = {
    "guide": dict(
        file="README.md", title="入门指引", eyebrow="START HERE",
        desc="小恐龙公文排版助手的功能简介、环境需求、安装说明与下载地址。",
        lead="从下载安装到第一次排版，三分钟即可上手。",
        next="feature",
    ),
    "feature": dict(
        file="feature.md", title="功能介绍", eyebrow="FEATURES",
        desc="版面设置、文字样式、插入功能、副本保密与高级设置，逐项了解公文排版助手的能力。",
        lead="六大功能区，覆盖公文排版的完整流程。",
        prev="guide", next="vba",
    ),
    "vba": dict(
        file="vba.md", title="VBA 脚本指南", eyebrow="EXTENSIBILITY",
        desc="用 VBA 脚本扩展公文排版助手：使用方法、常见问题、脚本制作与分享。",
        lead="即用即走，代码可见可改，把排版交给自己定义。",
        prev="feature", next="faq",
    ),
    "faq": dict(
        file="faq.md", title="常见问题", eyebrow="TROUBLESHOOTING",
        desc="安装报错、插件不加载、WPS 兼容、使用报错等问题的排查与解决办法。",
        lead="安装、加载、使用三步排查，绝大多数问题都能在这里找到答案。",
        prev="vba", next="update",
    ),
}


def read_md(name):
    with open(os.path.join(ROOT, name), encoding="utf-8") as f:
        return f.read()


def doc_page(key):
    meta = DOC_META[key]
    md = read_md(meta["file"])
    headings = []

    if key == "faq":
        content = convert_faq(md, headings)
    else:
        content = convert(md, heading_offset=1, collect_headings=headings)

    aside = build_aside(key, headings)

    prev_html = ""
    if meta.get("prev"):
        p = DOC_META[meta["prev"]]
        prev_html = ('<a class="prev" href="%s.html"><small>上一篇</small><strong>%s</strong></a>'
                     % (meta["prev"], p["title"]))
    next_html = ""
    if meta.get("next"):
        nx = meta["next"]
        label = DOC_META[nx]["title"] if nx in DOC_META else "更新日志"
        next_html = ('<a class="next" href="%s.html"><small>下一篇</small><strong>%s</strong></a>'
                     % (nx, label))

    body = """
<main class="container">
  <div class="doc-layout">
    <aside class="doc-aside">
      <div class="doc-aside-inner">
__ASIDE__
      </div>
    </aside>
    <div class="doc-main">
      <div class="doc-head">
        <span class="eyebrow">__EYEBROW__</span>
        <h1>__TITLE__</h1>
        <p>__LEAD__</p>
      </div>
__SEARCH__
      <article class="prose">
__CONTENT__
      </article>
      <nav class="doc-foot">
        __PREV__
        __NEXT__
      </nav>
    </div>
  </div>
</main>
"""
    body = (body.replace("__ASIDE__", aside)
                .replace("__EYEBROW__", meta["eyebrow"])
                .replace("__TITLE__", meta["title"])
                .replace("__LEAD__", meta["lead"])
                .replace("__CONTENT__", content)
                .replace("__PREV__", prev_html)
                .replace("__NEXT__", next_html))
    if key == "faq":
        body = body.replace("__SEARCH__", """
      <div class="qa-search">
        %s
        <input id="qa-input" type="search" placeholder="搜索问题，例如：安装报错 / 插件不显示 / 证书" autocomplete="off">
      </div>
""" % ICONS["search"])
    else:
        body = body.replace("__SEARCH__", "")

    return page("%s · 小恐龙公文排版助手" % meta["title"], meta["desc"], body,
                current="%s.html" % key, url="%s/%s.html" % (SITE, key))


def build_aside(key, headings):
    items = "\n".join('          <li><a href="#%s">%s</a></li>' % (sid, txt) for sid, txt in headings)
    extra = """
      <p class="aside-label">其他文档</p>
      <div class="aside-links">
        <a href="index.html">← 返回首页</a>
        <a href="https://github.com/xkonglong/gw/discussions" target="_blank" rel="noopener">VBA 脚本讨论组</a>
        <a href="https://support.qq.com/products/57503" target="_blank" rel="noopener">问题反馈</a>
      </div>
"""
    return """
      <p class="aside-label">本章目录</p>
      <ul class="aside-nav">
%s
      </ul>
%s""" % (items, extra)


def convert_faq(md, headings):
    """FAQ：按 h2 分组，组内 h3 变为可折叠问答"""
    lines = md.replace("\r\n", "\n").split("\n")
    out = []
    group_idx = 0
    intro = []
    items = []

    def flush_group():
        nonlocal intro, items
        if group_idx == 0 and not items:
            # 首个 h1 之前的内容（FAQ 无）
            pass
        out.append('<section class="qa-group" id="g%d">' % group_idx)
        if intro:
            out.append('<p class="qa-intro">%s</p>' % convert("\n".join(intro).strip()))
        out.extend(items)
        out.append("</section>")
        intro, items = [], []

    cur_h3 = None  # (title, lines)
    fresh = True

    def close_item():
        nonlocal cur_h3
        if cur_h3 is not None:
            title, body_lines = cur_h3
            html_body = convert("\n".join(body_lines).strip())
            items.append('<details class="qa"><summary>%s</summary><div class="qa-body">%s</div></details>'
                         % (inline(title), html_body))
            cur_h3 = None

    for raw in lines:
        s = raw.strip()
        m1 = re.match(r'^#\s+(.*)$', s)
        m2 = re.match(r'^##\s+(.*)$', s)
        m3 = re.match(r'^###\s+(.*)$', s)
        m4 = re.match(r'^####\s+(.*)$', s)
        if m1:
            continue
        if m2:
            close_item()
            if not fresh:
                flush_group()
            group_idx += 1
            fresh = False
            headings.append(("g%d" % group_idx, m2.group(1).strip()))
            intro = ["## " + m2.group(1).strip()]
            cur_h3 = None
            continue
        if m3:
            close_item()
            cur_h3 = (m3.group(1).strip(), [])
            continue
        if m4:
            # h4 归入当前条目正文
            if cur_h3 is not None:
                cur_h3[1].append("### " + m4.group(1).strip())
            continue
        if cur_h3 is not None:
            cur_h3[1].append(raw)
        else:
            intro.append(raw)

    close_item()
    if not fresh:
        flush_group()
    return "\n".join(out)


# --------------------------------------------------------------------------
# 更新日志
# --------------------------------------------------------------------------
def changelog_page():
    md = read_md("update.md")
    lines = md.replace("\r\n", "\n").split("\n")

    entries = []
    cur = None
    pre = []
    for raw in lines:
        s = raw.strip()
        if s.startswith("## "):
            if cur:
                entries.append(cur)
            cur = {"title": s[3:].strip(), "body": []}
        elif s.startswith("# "):
            continue
        else:
            if cur is None:
                if s:
                    pre.append(raw)
            else:
                cur["body"].append(raw)
    if cur:
        entries.append(cur)

    cards = []
    first_version_seen = False
    for idx, e in enumerate(entries):
        body_lines = [x for x in e["body"] if x.strip()]
        date = ""
        if body_lines and re.match(r'^[（(].+[）)]$', body_lines[0].strip()):
            date = body_lines[0].strip().strip("（）()")
            body_lines = body_lines[1:]
        html_body = convert("\n".join(body_lines))
        is_version = re.match(r'^v[\d.]', e["title"]) is not None
        latest = is_version and not first_version_seen
        if is_version:
            first_version_seen = True
        is_plan = not is_version
        meta_cls = ""
        cards.append("""
        <section class="log-item" id="log-%d">
          <div class="log-meta">
            <span class="log-version">%s</span>
            %s
            %s
          </div>
          <div class="log-body">%s</div>
        </section>
""" % (idx,
       inline(e["title"]),
       ('<span class="log-date">%s</span>' % date) if date else "",
       ('<span class="log-latest">最新版本</span>') if latest else "",
       html_body if html_body else "<p>%s</p>" % inline("详见左侧计划表") if is_plan else html_body))

    pre_html = convert("\n".join(pre)) if pre else ""

    body = """
<main class="container container-narrow log-layout">
  <div class="log-head">
    <span class="eyebrow">CHANGELOG</span>
    <h1>更新日志</h1>
    <p>从 v1.0.0.4 首次发布至今的全部版本记录，最新版本 <strong>%s</strong>（%s）。</p>
    %s
  </div>
  %s
</main>
""" % (VERSION, VERSION_DATE, pre_html, "\n".join(cards))

    return page("更新日志 · 小恐龙公文排版助手",
                "小恐龙公文排版助手历史版本更新记录，最新版本 v3.8.0.0（2026年4月13日）。",
                body, current="update.html", url=SITE + "/update.html")


# --------------------------------------------------------------------------
# 首页
# --------------------------------------------------------------------------
def index_page():
    cards = [
        ("layout", "一键页面版式", "按国标设置页边距、每页行数与每行字数，嵌入不常用字体。设置自动保存，无需每次重复调整。"),
        ("type", "公文标题与样式", "一至四级公文标题、正文格式快速套用，一键生成公文样式表，配合样式侧栏做段落级排版。"),
        ("wand", "排版清理工具", "断行重排、删除空白与多余空行、全半角替换、换行转回车，尤其适合处理来自 PDF 或网页的文字。"),
        ("stamp", "公文部件插入", "红头、红线、版记线、装订线、居中/居右/外侧页码、公文格式日期、六角括号与★等常用符号。"),
        ("shield", "副本与保密", "同目录一键生成 PDF / doc / 图片副本，快速设置密码与读写权限，朗读功能辅助校对。"),
        ("code", "VBA 脚本扩展", "即用即走，脚本不写入文档；代码可见、可改、可分享，把重复劳动交给脚本完成。"),
    ]
    cards_html = "\n".join("""
      <article class="card">
        <div class="card-icon">%s</div>
        <h3>%s</h3>
        <p>%s</p>
      </article>""" % (ICONS[ic], t, d) for ic, t, d in cards)

    shots = [
        ("img/formatText.gif", "快速标题格式", "选中文字后一键套用一至四级公文标题与正文格式，动图演示。"),
        ("img/papersetup.jpg", "页面设置", "页边距、行数页数、行间距与嵌入字体，一次设定长期生效。"),
        ("img/style.png", "公文样式", "一键生成常用公文样式，通过样式侧栏快速设置段落格式。"),
        ("img/aboutSetting.gif", "高级设置", "为每级公文字体指定名称与字号，并查看版本、检查更新。"),
    ]
    shots_html = "\n".join("""
        <figure class="shot">
          <div class="shot-img"><img src="%s" alt="%s" loading="lazy"></div>
          <figcaption class="shot-meta"><h4>%s</h4><p>%s</p></figcaption>
        </figure>""" % (src, t, t, d) for src, t, d in shots)

    docs = [
        ("guide.html", "START", "入门指引", "环境需求、安装步骤、杀软提示与下载地址。"),
        ("feature.html", "FEATURES", "功能介绍", "六大功能区逐项说明，含实机截图与动图演示。"),
        ("vba.html", "EXTEND", "VBA 脚本", "脚本怎么用、怎么写，以及常见报错的解决方式。"),
        ("faq.html", "FAQ", "常见问题", "安装 1001、证书不受信任、插件不显示、WPS 兼容……"),
        ("update.html", "LOG", "更新日志", "从首次发布到 v3.8.0.0 的完整版本记录。"),
        ("index.html#download", "DOWNLOAD", "下载安装", "蓝奏云、城通网盘、123 云盘与 GitHub 源码。"),
    ]
    docs_html = "\n".join("""
      <a class="doc-card" href="%s">
        <span class="tag">%s</span>
        <h4>%s</h4>
        <p>%s</p>
        <span class="more">查看%s</span>
      </a>""" % (href, tag, t, d, "下载" if "download" in href else "文档") for href, tag, t, d in docs)

    downloads = [
        ("cloud", "蓝奏云", "推荐 · 免登录直接下载", "https://xkonglong.lanzoux.com/b00dbbvcj"),
        ("cloud", "123 云盘", "备用下载通道", "https://www.123pan.com/s/BYLA-CZwHv"),
        ("cloud", "城通网盘", "提取密码 9561", "https://url38.ctfile.com/d/15334738-33069050-4ebf20?p=9561"),
        ("github", "GitHub 源码", "开源仓库 · 可自行编译", "https://github.com/xkonglong/gw"),
    ]
    dl_html = "\n".join("""
      <a class="dl" href="%s" target="_blank" rel="noopener">
        <span class="dl-icon">%s</span>
        <span class="dl-body"><strong>%s</strong><span>%s</span></span>
        <span class="dl-arrow">%s</span>
      </a>""" % (url, ICONS[ic], name, desc, ICONS["arrow"]) for ic, name, desc, url in downloads)

    body = """
<main>
  <section class="hero">
    <div class="container hero-grid">
      <div class="hero-copy">
        <div class="hero-badge"><b>最新版 __VERSION__</b><i></i>完全免费开源 · 不含恶意代码</div>
        <h1>公文排版，<em>一键成文</em></h1>
        <div class="hero-sub-en">小恐龙公文排版助手 · for Word &amp; WPS</div>
        <p class="hero-lead">依据《党政机关公文格式》（GB/T 9704—2012）的要求，快速设置页面版式与文字格式，插入红头、红线、版记线、页码，并对复制来的文字做<strong>断行重排、删除空白</strong>等批量清理。</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#download">__ICON_DL__ 免费下载</a>
          <a class="btn btn-ghost" href="feature.html">查看功能介绍 __ICON_AR__</a>
        </div>
        <div class="hero-meta">
          <span>__ICON_CK__ Word 2007 – 365</span>
          <span>__ICON_CK__ WPS 2013 – 365</span>
          <span>__ICON_CK__ Win 7 – 11</span>
        </div>
      </div>
      <div class="hero-visual">
        <div class="window">
          <div class="window-bar">
            <span class="dots"><i></i><i></i><i></i></span>
            <span class="window-title">Microsoft Word · 公文分组</span>
          </div>
          <img src="img/c1.png" alt="小恐龙公文排版助手在 Word 中的界面" width="1291" height="947">
        </div>
        <div class="hero-stamp" aria-hidden="true">公文<br>排版</div>
      </div>
    </div>
  </section>

  <section class="fact-bar">
    <div class="container fact-grid">
      <div class="fact"><strong>GB/T 9704—2012</strong><span>排版依据 · 党政机关公文格式</span></div>
      <div class="fact"><strong>27 行 × 28 字</strong><span>标准版面 · 默认精确实现</span></div>
      <div class="fact"><strong>Word 2007 – 365</strong><span>兼容 Microsoft Office</span></div>
      <div class="fact"><strong>WPS 2013 – 365</strong><span>含个人版 · 已适配 WPS365</span></div>
    </div>
  </section>

  <section class="section" id="features">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">FEATURES</span>
        <h2 class="section-title">一个插件，覆盖公文排版全流程</h2>
        <p class="section-desc">从页面版式到红头版记，从文字清理到 VBA 自动化，把公文排版里最费时的重复动作都收进工具栏。</p>
      </div>
      <div class="cards">
__CARDS__
      </div>
    </div>
  </section>

  <section class="section section-alt" id="screens">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">SCREENSHOTS</span>
        <h2 class="section-title">实机界面</h2>
        <p class="section-desc">插件在 Word / WPS 中以功能区分组的形式融入，所有按钮都带屏幕提示。</p>
      </div>
      <div class="shots">
__SHOTS__
      </div>
    </div>
  </section>

  <section class="section" id="start">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">QUICK START</span>
        <h2 class="section-title">三步开始使用</h2>
        <p class="section-desc">首次安装需要先导入签名证书，之后安装程序会自动完成部署与运行库准备。</p>
      </div>
      <div class="steps">
        <div class="step">
          <span class="step-num">STEP 01</span>
          <h4>下载并解压</h4>
          <p>从下方任一网盘通道下载最新版安装包，解压到本地。</p>
        </div>
        <div class="step">
          <span class="step-num">STEP 02</span>
          <h4>导入证书</h4>
          <p>运行「首次安装导入证书.bat」，出现证书导入成功的提示后再继续。</p>
        </div>
        <div class="step">
          <span class="step-num">STEP 03</span>
          <h4>运行安装程序</h4>
          <p>安装完成后打开 Word / WPS，功能区即出现「公文」分组。</p>
        </div>
      </div>
      <div class="notice">
        __ICON_INFO__
        <div>
          <p><strong>内网用户：</strong>智能安装版会从微软官网下载组件，内网环境请提前单独下载并安装附加组件。</p>
          <p><strong>杀软提示：</strong>作者承诺源码开放、不含任何恶意代码；如需排查，可提交 360 官方误杀申报，或在确认官网下载的前提下临时关闭杀毒软件。</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-alt" id="docs">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">DOCUMENTATION</span>
        <h2 class="section-title">文档与帮助</h2>
        <p class="section-desc">原站点按入门、功能、脚本、问答、日志组织，这里保留同样的结构，并改成更适合检索的阅读版式。</p>
      </div>
      <div class="doc-cards">
__DOCS__
      </div>
    </div>
  </section>

  <section class="section" id="download">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">DOWNLOAD</span>
        <h2 class="section-title">下载安装包</h2>
        <p class="section-desc">最新版本 __VERSION__（__VERSION_DATE__）。如遇下载限速，可换用其他通道；源码可在 GitHub 获取。</p>
      </div>
      <div class="downloads">
__DL__
      </div>
      <div class="notice">
        __ICON_INFO__
        <div>
          <p><strong>附加组件：</strong>内网或无法访问微软下载中心时，请先单独下载并安装附加组件，再进行插件安装。</p>
          <p><strong>Word 2007：</strong>v1.0.8.3 为最后支持版本，且提供内置运行库的离线安装版。</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-alt" id="donate">
    <div class="container">
      <div class="donate">
        <div>
          <h3>软件免费，支持作者</h3>
          <p>插件一直免费开源。如果它帮你省下了加班的夜晚，可以用微信扫码随意打赏。</p>
          <p>赞赏仅代表心意，不影响任何功能的使用。双击插件里的赞赏码，还可以打开专用工具修改默认配置文件。</p>
          <small>源码与讨论：github.com/xkonglong/gw</small>
        </div>
        <div class="donate-qr">
          <img src="img/zsm.jpg" alt="微信赞赏码" loading="lazy">
          <span>微信扫码赞赏</span>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    body = (body.replace("__VERSION_DATE__", VERSION_DATE)
                .replace("__VERSION__", VERSION)
                .replace("__CARDS__", cards_html)
                .replace("__SHOTS__", shots_html)
                .replace("__DOCS__", docs_html)
                .replace("__DL__", dl_html)
                .replace("__ICON_DL__", ICONS["download"])
                .replace("__ICON_AR__", ICONS["arrow"])
                .replace("__ICON_CK__", ICONS["check"])
                .replace("__ICON_INFO__", ICONS["info"]))

    return page("小恐龙公文排版助手 for Word/WPS · 一键公文排版",
                "小恐龙公文排版助手：依据 GB/T 9704—2012 的一键公文排版插件，支持 Word 2007–365 与 WPS，免费开源。",
                body, current="index.html", url=SITE + "/")


# --------------------------------------------------------------------------
# 输出
# --------------------------------------------------------------------------
def write(name, content):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("written:", name, len(content), "bytes")


def main():
    os.makedirs(OUT, exist_ok=True)
    write("index.html", index_page())
    for key in DOC_META:
        write("%s.html" % key, doc_page(key))
    write("update.html", changelog_page())
    # 简单的 404
    write("404.html", page("页面不存在 · 小恐龙公文排版助手",
                           "页面不存在，返回首页继续浏览。",
                           """
<main class="container" style="padding:120px 0 160px;text-align:center">
  <span class="eyebrow" style="justify-content:center">404</span>
  <h1 class="section-title">页面不存在</h1>
  <p class="section-desc" style="margin-bottom:28px">链接可能已更新，回到首页继续浏览文档。</p>
  <a class="btn btn-primary" href="index.html">返回首页</a>
</main>
"""))


if __name__ == "__main__":
    main()
