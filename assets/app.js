/* 小恐龙公文排版助手 · 站点交互 */
(function () {
  "use strict";

  // ---- 主题切换 ----
  var root = document.documentElement;
  var toggle = document.getElementById("theme-toggle");
  if (toggle) {
    var sunSvg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5L19 19M19 5l-1.5 1.5M6.5 17.5L5 19"/></svg>';
    var moonSvg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a7 7 0 0 0 10.5 10.5z"/></svg>';
    var sync = function () {
      var dark = root.getAttribute("data-theme") === "dark";
      toggle.innerHTML = dark ? sunSvg : moonSvg;
      toggle.setAttribute("aria-label", dark ? "切换到浅色主题" : "切换到深色主题");
    };
    sync();
    toggle.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("xkl-theme", next); } catch (e) {}
      sync();
    });
  }

  // ---- 移动端菜单 ----
  var burger = document.getElementById("menu-toggle");
  var menu = document.getElementById("mobile-menu");
  if (burger && menu) {
    burger.addEventListener("click", function () {
      menu.classList.toggle("open");
    });
    menu.addEventListener("click", function (e) {
      if (e.target.tagName === "A") menu.classList.remove("open");
    });
  }

  // ---- 回到顶部 ----
  var top = document.getElementById("to-top");
  if (top) {
    var onScroll = function () {
      if (window.scrollY > 520) top.classList.add("show");
      else top.classList.remove("show");
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    top.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // ---- 文档目录高亮 ----
  var links = Array.prototype.slice.call(document.querySelectorAll(".aside-nav a"));
  if (links.length) {
    var targets = links
      .map(function (a) {
        var id = a.getAttribute("href").slice(1);
        var el = document.getElementById(id);
        return el ? { link: a, el: el } : null;
      })
      .filter(Boolean);

    var spy = function () {
      var mark = window.scrollY + 140;
      var current = targets[0];
      targets.forEach(function (t) {
        if (t.el.offsetTop <= mark) current = t;
      });
      targets.forEach(function (t) {
        t.link.classList.toggle("active", t === current);
      });
    };
    window.addEventListener("scroll", spy, { passive: true });
    window.addEventListener("resize", spy);
    spy();
  }

  // ---- FAQ 搜索 ----
  var input = document.getElementById("qa-input");
  if (input) {
    var groups = Array.prototype.slice.call(document.querySelectorAll(".qa-group"));
    var items = Array.prototype.slice.call(document.querySelectorAll("details.qa"));
    var empty = document.createElement("p");
    empty.className = "qa-empty";
    empty.textContent = "没有找到相关问题，可以换个关键词，或到反馈渠道提问。";
    var searchWrap = document.querySelector(".qa-search");
    if (searchWrap) searchWrap.parentNode.insertBefore(empty, searchWrap.nextElementSibling);

    var run = function () {
      var q = input.value.trim().toLowerCase();
      items.forEach(function (it) {
        var text = (it.querySelector("summary").textContent + " " + it.querySelector(".qa-body").textContent).toLowerCase();
        var hit = !q || text.indexOf(q) !== -1;
        it.classList.toggle("is-hidden", !hit);
        if (hit && q.length > 1 && it.querySelectorAll("*").length < 60) it.setAttribute("open", "");
        else if (!q) it.removeAttribute("open");
      });
      var any = false;
      groups.forEach(function (g) {
        var visible = g.querySelectorAll("details.qa:not(.is-hidden)").length;
        g.style.display = visible || (!g.querySelector("details.qa") && !q) ? "" : "none";
        if (visible) any = true;
      });
      empty.style.display = any || !q ? "none" : "block";
    };
    input.addEventListener("input", run);
  }
})();
