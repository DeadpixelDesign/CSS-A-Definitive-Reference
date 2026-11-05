import json, os, re, html
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE = PROJECT_ROOT / 'static/CSS_Definitive_Reference_2026.md'
OUT = PROJECT_ROOT / 'src/lib/content.js'
STATIC = PROJECT_ROOT / 'static/CSS_Definitive_Reference_2026.md'
CHAPTERS = PROJECT_ROOT / 'static/chapters'
BASE_PATH = os.environ.get('BASE_PATH', '')

def inline(value):
    value = html.escape(value, quote=False)
    images = []
    links = []

    def image_token(match):
        token = f'__INLINE_IMAGE_{len(images)}__'
        alt = html.escape(match.group(1), quote=True)
        raw_src = match.group(2)
        if raw_src.startswith('/'):
            raw_src = f'{BASE_PATH}{raw_src}'
        src = html.escape(raw_src, quote=True)
        images.append((token, f'<img src="{src}" alt="{alt}" loading="lazy">'))
        return token

    value = re.sub(r'!\[([^\]]*)\]\((/[^)]+|https?://[^)]+)\)', image_token, value)

    def link_token(url, label=None):
        token = f'__INLINE_LINK_{len(links)}__'
        safe_url = html.escape(url, quote=True)
        safe_label = label if label is not None else html.escape(url, quote=False)
        links.append((token, f'<a href="{safe_url}" target="_blank" rel="noreferrer noopener">{safe_label} ↗</a>'))
        return token

    value = re.sub(
        r'\[([^\]]+)\]\((https?://[^)]+)\)',
        lambda match: link_token(match.group(2), match.group(1)),
        value,
    )
    value = re.sub(
        r'(?<!["=])(https?://[^\s<]+)',
        lambda match: link_token(match.group(1).rstrip('.,;:)')),
        value,
    )
    value = re.sub(r'`([^`]+)`', r'<code>\1</code>', value)
    def color_code(match):
        color = match.group(1)
        safe_color = html.escape(color, quote=True)
        return f'<code class="color-value"><span class="color-chip" style="--swatch: {safe_color}"></span>{color}</code>'
    value = re.sub(
        r'<code>((?:#[0-9a-fA-F]{3,8})|(?:hwb|lab|lch|oklab|oklch)\([^<]+\))</code>',
        color_code,
        value,
    )
    value = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', value)
    for token, anchor in links:
        value = value.replace(token, anchor)
    for token, image in images:
        value = value.replace(token, image)
    return value

def markdown_to_html(lines):
    out=[]; i=0; paragraph=[]
    def flush():
        nonlocal paragraph
        if paragraph:
            out.append('<p>'+inline(' '.join(x.strip() for x in paragraph))+'</p>'); paragraph=[]
    while i < len(lines):
        line=lines[i].rstrip('\n')
        if line.strip() == ':::source-cards':
            flush(); i += 1; cards = []
            while i < len(lines) and lines[i].strip() != ':::':
                if lines[i].strip():
                    parts = lines[i].split('|', 2)
                    if len(parts) == 3:
                        cards.append(parts)
                i += 1
            i += 1
            rendered = ['<div class="source-cards">']
            for title, summary, url in cards:
                safe_url = html.escape(url.strip(), quote=True)
                rendered.append(
                    '<article class="source-card">'
                    f'<h3>{inline(title.strip())}</h3>'
                    f'<p>{inline(summary.strip())}</p>'
                    f'<a href="{safe_url}" target="_blank" rel="noreferrer noopener">Visit source ↗</a>'
                    '</article>'
                )
            rendered.append('</div>')
            out.append(''.join(rendered)); continue
        if line.strip() == ':::two-columns':
            flush(); i += 1; section = []
            while i < len(lines) and lines[i].strip() != ':::':
                section.append(lines[i]); i += 1
            i += 1
            out.append('<div class="two-column-sections">' + markdown_to_html(section) + '</div>')
            continue
        if line.strip() == ':::source-grid':
            flush(); i += 1; source_lines = []
            while i < len(lines) and lines[i].strip() != ':::':
                source_lines.append(lines[i]); i += 1
            i += 1
            sections = []; current = []
            for source_line in source_lines:
                if re.match(r'^###\s+', source_line):
                    if current: sections.append(current)
                    current = [source_line]
                elif current:
                    current.append(source_line)
            if current: sections.append(current)
            rendered = ['<div class="source-grid">']
            for section in sections:
                item_count = sum(1 for section_line in section if re.match(r'^[-*]\s+', section_line))
                card_class = 'source-grid-card source-grid-card--multicolumn' if item_count >= 10 else 'source-grid-card'
                rendered.append(f'<article class="{card_class}">' + markdown_to_html(section) + '</article>')
            rendered.append('</div>')
            out.append(''.join(rendered)); continue
        if line.startswith('```'):
            flush(); lang=line[3:].strip(); code=[]; i+=1
            while i < len(lines) and not lines[i].startswith('```'):
                code.append(lines[i].rstrip('\n')); i+=1
            language = html.escape(lang or 'text')
            out.append(f'<pre class="line-numbers"><code class="language-{language}">{html.escape("\n".join(code))}</code></pre>'); i+=1; continue
        if not line.strip(): flush(); i+=1; continue
        m=re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            flush(); level=len(m.group(1)); out.append(f'<h{level}>{inline(m.group(2))}</h{level}>'); i+=1; continue
        if line.startswith('> '):
            flush(); quote=[]
            while i<len(lines) and lines[i].startswith('> '): quote.append(lines[i][2:].strip()); i+=1
            out.append('<blockquote>'+inline(' '.join(quote))+'</blockquote>'); continue
        if line.startswith('|'):
            flush(); rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(set(c)<=set('-: ') for c in cells): rows.append(cells)
                i+=1
            if rows:
                out.append('<table><thead><tr>'+''.join(f'<th>{inline(c)}</th>' for c in rows[0])+'</tr></thead><tbody>')
                for row in rows[1:]: out.append('<tr>'+''.join(f'<td>{inline(c)}</td>' for c in row)+'</tr>')
                out.append('</tbody></table>')
            continue
        if re.match(r'^[-*]\s+', line) or re.match(r'^\d+\.\s+', line):
            flush(); ordered=bool(re.match(r'^\d+\.', line)); items=[]
            while i<len(lines) and (re.match(r'^[-*]\s+', lines[i]) or re.match(r'^\d+\.\s+', lines[i])):
                items.append(re.sub(r'^([-*]|\d+\.)\s+','',lines[i]).strip()); i+=1
            tag='ol' if ordered else 'ul'
            rendered_items = []
            for item in items:
                checklist = re.match(r'^\[([ xX])\]\s+(.*)$', item)
                if checklist:
                    checked = ' checked' if checklist.group(1).lower() == 'x' else ''
                    rendered_items.append(
                        f'<li class="check-item"><label><input type="checkbox" disabled{checked}> '
                        f'{inline(checklist.group(2))}</label></li>'
                    )
                else:
                    rendered_items.append(f'<li>{inline(item)}</li>')
            out.append(f'<{tag}>' + ''.join(rendered_items) + f'</{tag}>'); continue
        paragraph.append(line); i+=1
    flush(); return '\n'.join(out)

text=SOURCE.read_text(encoding='utf-8')
parts=re.split(r'(?m)^##\s+', text)
chapters=[]
for index,part in enumerate(parts[1:],1):
    lines=part.splitlines(); title=lines[0].strip(); body='\n'.join(lines[1:]).strip()
    slug=re.sub(r'[^a-z0-9]+','-',title.lower()).strip('-')
    clean_title=re.sub(r'^\d+\.\s*','',title)
    summary='A guided section of the CSS reference, with practical advice, compatibility context, and examples.'
    for line in lines[1:]:
        if line.strip() and not line.startswith('#') and not line.startswith('>'):
            summary=line.strip(); break
    if len(summary) > 320:
        sentence_end = summary.rfind('. ', 0, 320)
        summary = summary[:sentence_end + 1] if sentence_end > 80 else summary[:317].rstrip() + '…'
    chapters.append({'slug':slug,'title':clean_title,'number':index,'summary':summary,'html':markdown_to_html(lines[1:]),'isPropertyReference':title.startswith('Property reference'),'compatibility':'https://caniuse.com/' if ('compat' in title.lower() or 'modern' in title.lower()) else None})

# Keep the master bibliography as the final true appendix. The production
# checklist is an internal extra and remains the final item in the navigation.
master_sources = next((chapter for chapter in chapters if chapter['title'] == 'Appendix H: Master source list'), None)
if master_sources:
    chapters.remove(master_sources)
    extra_index = next((index for index, chapter in enumerate(chapters) if chapter['title'] == 'Extra: Release checklist'), len(chapters))
    chapters.insert(extra_index, master_sources)
for index, chapter in enumerate(chapters, 1):
    chapter['number'] = index

OUT.parent.mkdir(parents=True, exist_ok=True); STATIC.parent.mkdir(parents=True, exist_ok=True)
CHAPTERS.mkdir(parents=True, exist_ok=True)
example_count = text.count('```') // 2
OUT.write_text(
    'export const chapters = '+json.dumps(chapters, ensure_ascii=False)+';\n'
    f'export const exampleCount = {example_count};\n',
    encoding='utf-8'
)
STATIC.write_text(text, encoding='utf-8')
for part, chapter in zip(parts[1:], chapters):
    CHAPTERS.joinpath(f"{chapter['slug']}.md").write_text(f"# {chapter['title']}\n\n{part.split(chr(10), 1)[1].strip()}\n", encoding='utf-8')
print(f'Generated {len(chapters)} chapter pages from {len(text.split())} words')
