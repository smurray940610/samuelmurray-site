# Installing the new Psychology & Neuroscience page

The files are **already written into your repo** at `~/Downloads/site` and the paper-tagging
script has already been run. All that's left is to build, preview, and push. The steps below
walk through that; Section 5 covers the one merge snag that sometimes happens, and Section 6
explains how to redo it from scratch if you ever need to.

Everything was verified before delivery: 60 papers preserved, exactly 29 tagged across 6 areas
(moral-cognition 9, consciousness 7, self-regulation 5, memory 4, cross-cultural 3, political 1),
every cross-reference resolves to a real title, and the Philosophy page is untouched.

---

## What changed

New files:
- `src/_data/psychAreas.json` — the 6 research areas (id / label / shape / blurb) that power the filter grid.
- `src/_data/psychConnections.json` — cross-reference lines under each paper, keyed by exact title (mirrors `connections.json`).
- `add_psycharea.py` — the script that tags papers (repo root; already run).

Edited:
- `src/psychology.njk` — rewritten: new deck, methods chips, clickable area-filter grid, tagged publication list with shape badges + connection lines, and a two-column Collaboration box + Past box.
- `src/_data/papers.json` — a `"psychArea"` field was added to 29 papers. (Nothing else changed; the diff also re-indents the file, which is cosmetic.)
- `src/css/site.css` — ~19 lines appended at the end for the new collaboration block (`.pcollab*`). All the *filter* styling was already in your stylesheet and is reused.

The 6 papers deliberately left off the page (Why value values?; The place of the trace;
Can the mind wander intentionally?; The scientific study of passive thinking; Times imagined and
remembered; Purity is linked to cooperation…) keep their `psychology` area but get no `psychArea`,
and the page only renders papers that have one — so they don't show.

---

## 1. Open Terminal and go to the repo

```bash
cd ~/Downloads/site
```

## 2. Confirm you're on the right repo and see the expected changes

```bash
git remote -v      # should show smurray940610/samuelmurray-site
git status         # should list: modified papers.json, site.css, psychology.njk
                   #               new file add_psycharea.py, psychAreas.json, psychConnections.json
```

If `git status` shows those six files, you're good. (If it shows *nothing* changed, the files
didn't land — jump to Section 6 to regenerate them.)

## 3. Build the site

```bash
npm run build
```

This runs Eleventy and writes `_site/`. It should finish in a second or two with no errors.
If it prints a Nunjucks or JSON error, **stop** and send me the message — don't push.

## 4. Preview locally before pushing (recommended)

```bash
npx @11ty/eleventy --serve
```

Then open **http://localhost:8080/psychology/** in your browser.

Check that:
- the 6 area boxes show with their shapes and a paper count (none should say "in progress");
- clicking an area filters the list, clicking again (or **Clear filter ✕**) restores it;
- the publication list shows 29 papers, each with a small shape badge and any "Builds on / Extends / …" lines;
- the **Collaboration** box shows two columns of names and the **Past** box lists 5 roles;
- the Philosophy page (http://localhost:8080/philosophy/) still looks exactly as before.

The dev server holds the terminal open — that's normal, it isn't stuck. Press **Ctrl+C** to get
your prompt back before running git commands.

> One thing worth a careful look: the new Collaboration / Past block uses a layout I couldn't
> screenshot from my end. It validated structurally, but eyeball the spacing on this preview. If
> anything looks off, tell me and I'll adjust the CSS.

## 5. Commit and push

```bash
git add -A
git commit -m "Rebuild Psychology & Neuroscience page: area filter, tagged papers, collaborators"
git push
```

Cloudflare Pages auto-builds from `main`. Watch **Pages → samuelmurray-site → Deployments** go
green (1–2 min), then hard-refresh the live page: **Cmd+Shift+R** at
https://www.samuelmurray.org/psychology/.

**If `git push` is rejected with "fetch first"** — that just means the CMS (or a web edit)
committed to `main` since your last pull. Fix it with:

```bash
git pull --no-rebase
# if it opens vim for a merge message: press Esc, type :wq, press Enter
git push
```

Only stop and ask for help if it reports an actual **CONFLICT** (most likely in `papers.json`).

---

## 6. If you ever need to regenerate from scratch

The two data files and the page are plain text in the repo, so normally you won't. But if
`git status` showed no changes (the files didn't transfer), or you want to re-tag after editing
`papers.json`, here's the self-contained path. Re-running the tagging script is always safe — it
only sets the `psychArea` field and refuses to write if any title fails to match.

```bash
cd ~/Downloads/site
python3 add_psycharea.py      # expect: "OK -- tagged 29 papers with psychArea (expected 29)."
```

If that prints an **ERROR** listing titles "NOT found in papers.json", it means a paper title was
edited so it no longer matches the script's list — it writes nothing, so you're safe. Send me the
listed titles and I'll reconcile them.

Validate the JSON any time before building:

```bash
python3 -c "import json; json.load(open('src/_data/papers.json')); json.load(open('src/_data/psychAreas.json')); json.load(open('src/_data/psychConnections.json')); print('all JSON valid')"
```

Then build / preview / push as in Sections 3–5.

---

## Quick reference (the whole loop)

```bash
cd ~/Downloads/site
git status
npm run build
npx @11ty/eleventy --serve     # preview localhost:8080/psychology/, then Ctrl+C
git add -A
git commit -m "Rebuild Psychology & Neuroscience page"
git push
# watch Cloudflare go green, then Cmd+Shift+R on the live page
```
