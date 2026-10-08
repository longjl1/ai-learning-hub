#!/usr/bin/env python3
"""Check this Markdown catalog locally; no network or third-party packages."""

from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "projects/README.md": ("PRJ", 20, "官方仓库"),
    "papers/README.md": ("PAP", 35, "原文"),
    "resources/courses.md": ("CRS", 15, "官方入口"),
    "resources/books-and-docs.md": ("BOK", 10, "官方入口"),
}
EXPECTED_TOTAL = sum(value[1] for value in EXPECTED.values())
MARKER = re.compile(r"<!-- resource: ([A-Z]{3}-\d{2}) -->")
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^\s)]+)\)")
EXPLICIT_ANCHOR = re.compile(r'<a\s+id="([^"]+)"\s*>\s*</a>')
errors = []


def fail(message):
    errors.append(message)


def prose_only(content):
    """Ignore fenced code so examples do not become resources or links."""
    lines = []
    fence = None
    for line in content.splitlines():
        match = re.match(r"^\s*(\x60{3,}|~{3,})", line)
        if match:
            delimiter = match[1]
            if fence is None:
                fence = (delimiter[0], len(delimiter))
            elif delimiter[0] == fence[0] and len(delimiter) >= fence[1]:
                fence = None
            lines.append("")
        else:
            lines.append(line if fence is None else "")
    return "\n".join(lines), fence


def anchors_for(prose):
    anchors = set()
    explicit = EXPLICIT_ANCHOR.findall(prose)
    for value, count in Counter(explicit).items():
        if count > 1:
            fail(f"Duplicate explicit anchor: {value}")
    anchors.update(explicit)
    # Approximate GFM heading IDs; catalog resource links use explicit IDs.
    seen = Counter()
    for heading in re.findall(r"^#{1,6}\s+(.+)$", prose, re.M):
        text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading)
        text = re.sub(r"<[^>]*>", "", text).strip().lower()
        slug = re.sub(r"[^\w\-\s]", "", text).replace(" ", "-")
        ordinal = seen[slug]
        seen[slug] += 1
        anchors.add(slug if ordinal == 0 else f"{slug}-{ordinal}")
    return anchors


def normalized_url(url):
    parsed = urlsplit(url)
    path = parsed.path.rstrip("/")
    if parsed.netloc.lower() == "github.com":
        path = path.lower()
    return urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), path,
                       parsed.query, ""))


files = {}
for path in sorted(ROOT.rglob("*.md")):
    if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
        continue
    name = path.relative_to(ROOT).as_posix()
    content = path.read_text(encoding="utf-8")
    prose, fence = prose_only(content)
    files[path.resolve()] = (name, content, prose, anchors_for(prose))
    if fence:
        fail(f"{name}: unclosed code fence")
    if not content.endswith("\n"):
        fail(f"{name}: missing final newline")
    if re.search(r"|turn\d+(?:search|view|fetch)\d+|/Users/|file://", content):
        fail(f"{name}: tool citation or local absolute path leaked")
    lines = content.splitlines()
    for number, line in enumerate(lines, 1):
        if line.rstrip() != line:
            fail(f"{name}:{number}: trailing whitespace")
        if re.match(r"^#{1,6}\s", line) and number < len(lines) and lines[number].strip():
            fail(f"{name}:{number}: heading needs a following blank line")
    # All catalog tables use explicit leading and trailing pipes.
    columns = None
    for number, line in enumerate(prose.splitlines(), 1):
        if line.startswith("|"):
            width = len(re.split(r"(?<!\\)\|", line)) - 2
            if not line.endswith("|"):
                fail(f"{name}:{number}: table row lacks closing pipe")
            if columns is None:
                columns = width
            elif width != columns:
                fail(f"{name}:{number}: table column count {width} != {columns}")
        else:
            columns = None

ids = []
official_urls = []
counts = {}
paper_blocks = {}
for name, (prefix, count, label) in EXPECTED.items():
    path = (ROOT / name).resolve()
    if path not in files:
        fail(f"Missing catalog page: {name}")
        continue
    prose = files[path][2]
    matches = list(MARKER.finditer(prose))
    found = [match[1] for match in matches]
    desired = [f"{prefix}-{i:02d}" for i in range(1, count + 1)]
    if found != desired:
        fail(f"{name}: expected ordered IDs {desired}, found {found}")
    counts[prefix] = len(found)
    ids.extend(found)
    # Count navigation rows independently from detail entries.
    index = prose.split('<a id=', 1)[0]
    indexed = re.findall(rf"^\| ({prefix}-\d{{2}}) \|", index, re.M)
    if indexed != desired:
        fail(f"{name}: quick-index IDs differ from detail entries")
    for i, match in enumerate(matches):
        resource_id = match[1]
        block = prose[match.end():matches[i + 1].start() if i + 1 < len(matches) else len(prose)]
        if resource_id.lower() not in files[path][3]:
            fail(f"{resource_id}: missing stable anchor")
        for required in ("前置知识", "推荐理由", "难度", "路线", "核查"):
            if required not in block:
                fail(f"{resource_id}: missing required field {required}")
        if not re.search(r"核查[^\n]*\d{4}-\d{2}-\d{2}", block):
            fail(f"{resource_id}: missing verification date")
        official = re.search(rf"\*\*{label}\*\*：[^\n]*?\]\((https?://[^\s)]+)\)", block)
        if official:
            official_urls.append((resource_id, normalized_url(official[1])))
        else:
            fail(f"{resource_id}: missing official source")
        specific = {
            "PRJ": ("先读什么", "适合练习", "版本与状态", "关注度快照", "运行"),
            "PAP": ("核心问题", "主要贡献", "阅读衔接", "作者代码 / 材料", "首次公开 / 发表信息"),
            "CRS": ("收录版本", "视频", "讲义", "作业", "学习产出"),
            "BOK": ("类型 / 版本", "获取方式", "建议先阅读", "实践任务"),
        }[prefix]
        for required in specific:
            if required not in block:
                fail(f"{resource_id}: missing type field {required}")
        if prefix == "PAP":
            paper_blocks[resource_id.lower()] = block
            arxiv = re.search(r"https://arxiv.org/abs/(\d{4}\.\d{4,5})", block)
            year = re.search(r"首次公开 / 发表信息\*\*：(\d{4})", block)
            if not arxiv or not year or int(year[1]) != 2000 + int(arxiv[1][:2]):
                fail(f"{resource_id}: arXiv ID and first-public year mismatch")
            elif int(year[1]) >= 2025 and "近期研究" not in block:
                fail(f"{resource_id}: missing recent-research label")

for name, _, prose, _ in files.values():
    if name not in EXPECTED and MARKER.search(prose):
        fail(f"{name}: resource details must stay on the four catalog pages")
for value, count in Counter(ids).items():
    if count > 1:
        fail(f"Duplicate resource ID: {value}")
for url, count in Counter(url for _, url in official_urls).items():
    if count > 1:
        fail(f"Duplicate primary official URL: {url}")
if len(ids) != EXPECTED_TOTAL:
    fail(f"Resource total mismatch: {len(ids)}")

paper_page = files.get((ROOT / "papers/README.md").resolve())
if paper_page:
    year_index = paper_page[2].split("## 年份索引", 1)[1].split('<a id=', 1)[0]
    indexed_papers = []
    for year, row in re.findall(r"^\| (20\d{2}) \| (.+) \|$", year_index, re.M):
        for target in re.findall(r"\]\(#(pap-\d{2})\)", row):
            indexed_papers.append(target)
            if f"信息**：{year}" not in paper_blocks.get(target, ""):
                fail(f"Year index: {target} placed under wrong year {year}")
    if Counter(indexed_papers) != Counter(paper_blocks.keys()):
        fail("Year index must contain every paper exactly once")

local_links = 0
external_links = 0
for path, (name, _, prose, _) in files.items():
    for destination in LINK.findall(prose):
        destination = destination.strip("<>")
        parsed = urlsplit(destination)
        if parsed.scheme in ("https", "http", "mailto"):
            external_links += 1
            continue
        if parsed.scheme or parsed.netloc:
            fail(f"{name}: unexpected link scheme {destination}")
            continue
        local_links += 1
        target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        if not target.is_relative_to(ROOT):
            fail(f"{name}: link escapes repository: {destination}")
        elif not target.is_file():
            fail(f"{name}: missing link target: {destination}")
        elif parsed.fragment:
            anchor = unquote(parsed.fragment)
            if target not in files or anchor not in files[target][3]:
                fail(f"{name}: missing anchor: {destination}")

homepage = (ROOT / "README.md").read_text(encoding="utf-8")
for name, (_, count, _) in EXPECTED.items():
    if not re.search(rf"\]\({re.escape(name)}\) \| {count} \|", homepage):
        fail(f"Homepage count missing or inconsistent for {name}")
if f"**{EXPECTED_TOTAL}**" not in homepage:
    fail("Homepage total missing")

if errors:
    print("\n".join(f"ERROR: {error}" for error in errors))
    sys.exit(1)
print(f"PASS: {len(files)} Markdown files; {len(ids)} unique resources "
      f"(projects={counts['PRJ']}, papers={counts['PAP']}, "
      f"courses={counts['CRS']}, books/docs={counts['BOK']}).")
print(f"PASS: {local_links} relative links/anchors; {external_links} external "
      "link references (syntax only, no network check).")
print("PASS: indexes, years, required fields, tables, fences and whitespace.")
