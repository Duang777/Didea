#!/usr/bin/env python3
"""校验 projects 分类文件，并生成 README 的分类计数和最近新增。

零依赖，只使用 Python 3 标准库。从仓库任意目录执行都可以。
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parent.parent
PROJECTS = ROOT / "projects"
README_PATH = ROOT / "README.md"

# 新增分类时把 slug 插到 other 之前，并同步更新 AGENTS.md 的分类一览。
CATEGORY_ORDER = [
    "agent-frameworks",
    "coding-agents",
    "skills-prompts",
    "mcp-tools",
    "browser-computer",
    "benchmarks",
    "papers",
    "models-inference",
    "apps-products",
    "frontend-design",
    "blogs-learning",
    "other",
]

RECENT_LIMIT = 20

REQUIRED_FIELDS = ("发现", "一句话", "摘要", "标签")
OPTIONAL_FIELDS = ("来源",)
FIELD_NAMES = REQUIRED_FIELDS + OPTIONAL_FIELDS

ENTRY_RE = re.compile(r"^### \[([^\]\n]+)\]\(([^)\s]+)\)$")
MONTH_RE = re.compile(r"^## (\d{4}-\d{2})$")
FIELD_RE = re.compile(
    r"^- (" + "|".join(FIELD_NAMES) + r")：\s*(.*)$"
)
ASCII_FIELD_RE = re.compile(
    r"^- (?:发现|一句话|摘要|标签|来源)\s*:"
)
TAG_RE = re.compile(r"`([^`]+)`")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
GITHUB_HOSTS = {"github.com", "www.github.com"}

CATEGORIES_START = "<!-- categories:start -->"
CATEGORIES_END = "<!-- categories:end -->"
RECENT_START = "<!-- recent:start -->"
RECENT_END = "<!-- recent:end -->"
MARKERS = (CATEGORIES_START, CATEGORIES_END, RECENT_START, RECENT_END)


@dataclass
class Entry:
    name: str
    url: str
    date: str
    one_liner: str
    path: Path
    line: int
    index_in_file: int


@dataclass
class Category:
    slug: str
    title: str
    path: Path
    entries: list[Entry]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def normalize_url(url: str) -> str:
    """供查重比较。GitHub 仓库忽略大小写、www 和查询字符串。"""
    parts = urlsplit(url.strip())
    scheme = parts.scheme.lower()
    host = parts.netloc.lower()
    path = parts.path.rstrip("/")
    if path.endswith(".git"):
        path = path[: -len(".git")]
    query = parts.query
    if host in GITHUB_HOSTS:
        host = "github.com"
        path = path.lower()
        query = ""
    return urlunsplit((scheme, host, path, query, ""))


def valid_day(value: str) -> bool:
    if not DATE_RE.fullmatch(value):
        return False
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return False
    return True


def valid_month(value: str) -> bool:
    try:
        datetime.strptime(value, "%Y-%m")
    except ValueError:
        return False
    return True


def snippet(text: str, limit: int = 40) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    return text[:limit] + "…"


def parse_category(path: Path) -> tuple[Category | None, list[str]]:
    errors: list[str] = []
    display = rel(path)
    slug = path.stem
    if not SLUG_RE.fullmatch(slug):
        errors.append(f"{display}：文件名应为小写英文 slug，例如 frontend-design.md")

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return None, [f"{display}：无法读取（{exc}）"]
    if text.startswith("\ufeff"):
        text = text[1:]

    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        return None, errors + [f"{display}:1：第一行必须是「# 中文标题」"]

    title = lines[0][2:].strip()
    if not title:
        errors.append(f"{display}:1：标题为空")

    index = 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    description: list[str] = []
    while index < len(lines) and lines[index].strip() and not lines[index].startswith("#"):
        description.append(lines[index].strip())
        index += 1
    if len(description) != 1:
        errors.append(f"{display}：标题下要有且只有一行分类说明")
    while index < len(lines) and not lines[index].strip():
        index += 1

    entries: list[Entry] = []
    seen_months: set[str] = set()
    prev_month: str | None = None
    prev_date: str | None = None
    prev_name = ""
    seen_h2 = False
    months: list[dict[str, object]] = []

    while index < len(lines):
        line = lines[index].rstrip()
        lineno = index + 1
        if not line.strip():
            index += 1
            continue

        if line.startswith("###"):
            if not seen_h2:
                errors.append(f"{display}:{lineno}：条目前面要有「## YYYY-MM」")
            matched = ENTRY_RE.match(line.strip())
            if matched:
                name = matched.group(1).strip()
                url = matched.group(2).strip()
            else:
                name = "（无法解析）"
                url = ""
                errors.append(
                    f"{display}:{lineno}：条目标题必须是「### [项目名](URL)」，URL 不要含空格或英文圆括号"
                )
            if months:
                months[-1]["count"] = int(months[-1]["count"]) + 1
            index += 1
            field_lines: list[tuple[int, str]] = []
            while index < len(lines) and not lines[index].startswith("#"):
                field_lines.append((index + 1, lines[index].rstrip()))
                index += 1
            entry, entry_errors, prev_date, prev_name = parse_entry(
                display,
                path,
                name,
                url,
                lineno,
                field_lines,
                str(months[-1]["month"]) if months and months[-1]["valid"] else "",
                prev_date,
                prev_name,
                len(entries),
            )
            errors.extend(entry_errors)
            if entry is not None:
                entries.append(entry)
            continue

        if line.startswith("##"):
            seen_h2 = True
            matched = MONTH_RE.match(line.strip())
            if not matched or not valid_month(matched.group(1)):
                errors.append(f"{display}:{lineno}：月份标题必须是「## YYYY-MM」")
                months.append({"month": "", "line": lineno, "count": 0, "valid": False})
                index += 1
                continue
            month = matched.group(1)
            if month in seen_months:
                errors.append(f"{display}:{lineno}：月份 {month} 重复了")
            elif prev_month is not None and month > prev_month:
                errors.append(
                    f"{display}:{lineno}：月份 {month} 晚于上方的 {prev_month}，更新的月份要排在更前"
                )
            seen_months.add(month)
            prev_month = month
            months.append({"month": month, "line": lineno, "count": 0, "valid": True})
            index += 1
            continue

        errors.append(f"{display}:{lineno}：无法识别的内容：{snippet(line)}")
        index += 1

    for month in months:
        if month["valid"] and month["count"] == 0:
            errors.append(
                f"{display}:{month['line']}：月份 {month['month']} 下面没有条目"
            )

    if title:
        return Category(slug, title, path, entries), errors
    return None, errors


def parse_entry(
    display: str,
    path: Path,
    name: str,
    url: str,
    header_line: int,
    field_lines: list[tuple[int, str]],
    month: str,
    prev_date: str | None,
    prev_name: str,
    index_in_file: int,
) -> tuple[Entry | None, list[str], str | None, str]:
    errors: list[str] = []
    values: dict[str, str] = {}
    order: list[str] = []
    date_line = header_line

    for lineno, raw in field_lines:
        stripped = raw.strip()
        if not stripped:
            continue
        matched = FIELD_RE.match(stripped)
        if not matched:
            if ASCII_FIELD_RE.match(stripped):
                errors.append(f"{display}:{lineno}：字段请使用中文冒号「：」")
            else:
                errors.append(
                    f"{display}:{lineno}：条目里只能写这些字段：发现、一句话、摘要、标签、来源"
                )
            continue
        field, value = matched.group(1), matched.group(2).strip()
        if field in values:
            errors.append(f"{display}:{lineno}：字段「{field}」重复了")
        values[field] = value
        order.append(field)
        if field == "发现":
            date_line = lineno
        if not value:
            errors.append(f"{display}:{lineno}：字段「{field}」是空的")

    missing = [field for field in REQUIRED_FIELDS if field not in values]
    if missing:
        errors.append(
            f"{display}:{header_line}：条目「{name}」缺少字段：{'、'.join(missing)}"
        )
    if any(field not in FIELD_NAMES for field in order):
        errors.append(f"{display}:{header_line}：条目「{name}」含有无法识别的字段")
    canonical = [field for field in FIELD_NAMES if field in values]
    if order != canonical:
        errors.append(
            f"{display}:{header_line}：条目「{name}」的字段顺序应为：发现、一句话、摘要、标签，来源放最后（可省略）"
        )

    date = values.get("发现", "")
    if date and not valid_day(date):
        errors.append(
            f"{display}:{date_line}：条目「{name}」的发现日期必须是真实存在的 YYYY-MM-DD，现在是「{date}」"
        )
    elif date and month and date[:7] != month:
        errors.append(
            f"{display}:{date_line}：条目「{name}」的日期 {date} 不在月份 {month} 下"
        )

    if date and valid_day(date):
        if prev_date is not None and date > prev_date:
            errors.append(
                f"{display}:{date_line}：条目「{name}」的发现日期 {date} 晚于上方「{prev_name}」的 {prev_date}，应按时间倒序（新的在前，同一天的后加入的在前）"
            )
        prev_date = date
        prev_name = name

    if "标签" in values and values["标签"]:
        tags = TAG_RE.findall(values["标签"])
        leftover = TAG_RE.sub("", values["标签"]).strip()
        if not tags or any(not tag.strip() for tag in tags) or leftover:
            errors.append(
                f"{display}:{header_line}：条目「{name}」的标签写成 `标签` ，多个标签用空格分隔"
            )

    if url:
        parts = urlsplit(url)
        if parts.scheme not in {"http", "https"} or not parts.netloc:
            errors.append(f"{display}:{header_line}：条目「{name}」的 URL 要以 http:// 或 https:// 开头")
        return (
            Entry(
                name=name,
                url=url,
                date=date if valid_day(date) else "",
                one_liner=values.get("一句话", ""),
                path=path,
                line=header_line,
                index_in_file=index_in_file,
            ),
            errors,
            prev_date,
            prev_name,
        )
    return None, errors, prev_date, prev_name


def load_all() -> tuple[list[Category], list[str]]:
    errors: list[str] = []
    if not PROJECTS.is_dir():
        return [], ["缺少 projects/ 目录"]

    found: dict[str, Category] = {}
    for path in sorted(PROJECTS.iterdir(), key=lambda item: item.name):
        if path.name.startswith("."):
            continue
        if not path.is_file() or path.suffix != ".md":
            errors.append(f"projects/{path.name}：分类目录里只放 <slug>.md")
            continue
        category, parsed_errors = parse_category(path)
        errors.extend(parsed_errors)
        if category is not None:
            found[category.slug] = category

    for slug in CATEGORY_ORDER:
        if slug not in found:
            errors.append(f"缺少分类文件 projects/{slug}.md")
    for slug in found:
        if slug not in CATEGORY_ORDER:
            errors.append(
                f"projects/{slug}.md 未列入 scripts/catalog.py 的 CATEGORY_ORDER。"
                "新建分类时把 slug 插到 other 之前，并更新 AGENTS.md 的分类一览。"
            )

    ordered = [found[slug] for slug in CATEGORY_ORDER if slug in found]
    errors.extend(duplicate_errors(ordered))
    return ordered, errors


def duplicate_errors(categories: list[Category]) -> list[str]:
    seen: dict[str, Entry] = {}
    errors: list[str] = []
    for category in categories:
        for entry in category.entries:
            key = normalize_url(entry.url)
            if not key:
                continue
            previous = seen.get(key)
            if previous is None:
                seen[key] = entry
                continue
            if previous.url == entry.url:
                headline = f"URL 重复：{entry.url}"
            else:
                headline = f"URL 重复（规范后都是 {key}）"
            errors.append(
                f"{headline}\n"
                f"  - {rel(previous.path)}:{previous.line} {previous.name} {previous.url}\n"
                f"  - {rel(entry.path)}:{entry.line} {entry.name} {entry.url}"
            )
    return errors


def render_categories(categories: list[Category]) -> str:
    by_slug = {category.slug: category for category in categories}
    lines = []
    for slug in CATEGORY_ORDER:
        category = by_slug[slug]
        lines.append(f"- [{category.title}](projects/{slug}.md)（{len(category.entries)}）")
    return "\n".join(lines)


def render_recent(categories: list[Category]) -> str:
    by_slug = {category.slug: category for category in categories}
    items: list[tuple[Entry, str, str]] = []
    for slug in CATEGORY_ORDER:
        category = by_slug[slug]
        for entry in category.entries:
            if entry.date and entry.one_liner:
                items.append((entry, slug, category.title))
    items.sort(
        key=lambda item: (
            item[0].date,
            -item[0].index_in_file,
            -CATEGORY_ORDER.index(item[1]),
        ),
        reverse=True,
    )
    picked = items[:RECENT_LIMIT]
    if not picked:
        return "暂无条目。"
    lines = []
    for entry, slug, title in picked:
        lines.append(
            f"- {entry.date} [{entry.name}]({entry.url}) · [{title}](projects/{slug}.md)：{entry.one_liner}"
        )
    return "\n".join(lines)


def replace_block(text: str, start: str, end: str, body: str) -> str | None:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    replacement = f"{start}\n{body}\n{end}"

    def _replace(_match: re.Match[str]) -> str:
        return replacement

    updated, count = pattern.subn(_replace, text, count=1)
    if count != 1:
        return None
    return updated


def apply_index(text: str, categories: list[Category]) -> str | None:
    updated = replace_block(text, CATEGORIES_START, CATEGORIES_END, render_categories(categories))
    if updated is None:
        return None
    return replace_block(updated, RECENT_START, RECENT_END, render_recent(categories))


def readme_errors(categories: list[Category]) -> list[str]:
    if not README_PATH.is_file():
        return ["缺少 README.md"]
    text = README_PATH.read_text(encoding="utf-8")
    missing = [marker for marker in MARKERS if marker not in text]
    if missing:
        return ["README.md 缺少标记：" + "、".join(missing)]
    updated = apply_index(text, categories)
    if updated is None:
        return ["README.md 的标记块无法解析"]
    if updated != text:
        return ["README.md 的分类目录或最近新增已过期，请运行 python3 scripts/catalog.py index"]
    return []


def entry_count(categories: list[Category]) -> int:
    return sum(len(category.entries) for category in categories)


def recent_count(categories: list[Category]) -> int:
    total = sum(
        1
        for category in categories
        for entry in category.entries
        if entry.date and entry.one_liner
    )
    return min(RECENT_LIMIT, total)


def print_errors(errors: list[str]) -> None:
    for error in errors:
        print(error, file=sys.stderr)


def cmd_check() -> int:
    categories, errors = load_all()
    if not errors:
        errors.extend(readme_errors(categories))
    if errors:
        print_errors(errors)
        print(f"check: 失败（{len(errors)} 个问题）", file=sys.stderr)
        return 1
    print(f"check: 通过（{len(categories)} 个分类，{entry_count(categories)} 条）")
    return 0


def cmd_index() -> int:
    categories, errors = load_all()
    if errors:
        print_errors(errors)
        print("index: 未改 README（请先修正上面的问题）", file=sys.stderr)
        return 1
    if not README_PATH.is_file():
        print("index: 缺少 README.md", file=sys.stderr)
        return 1
    original = README_PATH.read_text(encoding="utf-8")
    missing = [marker for marker in MARKERS if marker not in original]
    if missing:
        print("index: README.md 缺少标记：" + "、".join(missing), file=sys.stderr)
        return 1
    updated = apply_index(original, categories)
    if updated is None:
        print("index: README.md 的标记块无法解析", file=sys.stderr)
        return 1
    shown = recent_count(categories)
    total_categories = len(categories)
    if updated == original:
        print(f"index: README.md 已是最新（{total_categories} 个分类，最近 {shown} 条）")
        return 0
    README_PATH.write_text(updated, encoding="utf-8")
    print(f"index: 已更新 README.md（{total_categories} 个分类，最近 {shown} 条）")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="校验分类文件，并生成 README 里的分类计数和最近新增。"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("check", help="校验倒序、字段、日期格式，以及全库 URL 是否重复")
    subparsers.add_parser("index", help="重新生成 README 里的分类计数和最近新增")
    args = parser.parse_args(argv)
    if args.command == "check":
        return cmd_check()
    if args.command == "index":
        return cmd_index()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
