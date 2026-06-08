# samuelmurray.org — site project & deployment guide

A custom personal site for Samuel Murray, built with **Eleventy** (static-site generator) and **Decap CMS** (browser-based content editor), designed to be hosted free on **Cloudflare Pages**.

This README is the step-by-step guide to getting it live. Steps marked **[YOU]** must be done by you (they involve account creation and logins). Everything in the `site/` folder is already built.

---

## What's in this project

```
site/
├── package.json          ← declares Eleventy; build scripts
├── .eleventy.js          ← Eleventy config (input=src, output=_site)
├── README.md             ← this file
└── src/
    ├── index.njk         ← homepage (Suprematist)
    ├── philosophy.njk    ← Philosophy page (Suprematist)
    ├── psychology.njk    ← Psych/Neuro page (Bauhaus)
    ├── teaching.njk      ← Teaching page (Mondrian)
    ├── camp-lab.njk      ← CaMP Lab page (Constructivist)
    ├── blog.njk          ← blog index ("Para que no se me olvide")
    ├── css/site.css      ← ALL styling for every page
    ├── _includes/layouts/← base, interior, and post page templates
    ├── _data/            ← site.json, papers.json, courses.json, projects.json
    ├── posts/            ← blog posts (Markdown); 1 sample post included
    └── admin/            ← Decap CMS (the /admin editor): index.html + config.yml
```

**How content works:** papers, courses, and projects live in the `_data/*.json` files; blog posts are Markdown files in `posts/`. You edit these through the `/admin` panel once deployed — no code needed.

---

## Before you start

You'll create two free accounts: **GitHub** (stores the site files + powers the CMS login) and **Cloudflare** (builds and hosts the site). Both have free tiers that comfortably cover this site. Have your domain registrar login handy too (wherever `samuelmurray.org` is registered) for the final DNS step.

> Tip: do steps 1–4 in one sitting (~30–45 min). The domain step (5) can wait until you've confirmed the site looks right on the temporary Cloudflare URL.

---

## Step 1 — Put the project on GitHub **[YOU]**

1. Create a free account at https://github.com if you don't have one.
2. Click **New repository**. Name it something like `samuelmurray-site`. Set it to **Private** (fine) or Public (also fine). Do **not** add a README (this project has one). Create the repository.
3. Upload the project. Easiest no-tools method:
   - On the new repo page, click **uploading an existing file**.
   - Drag in the **contents of the `site/` folder** (so `package.json` and `src/` sit at the repository root — NOT the `site` folder itself).
   - Commit (the green button).
   *(If you prefer the command line and have git installed, ask and I'll give you the exact `git` commands instead.)*

After this, note your repo path: `YOUR_GITHUB_USERNAME/samuelmurray-site`. You'll need it twice below.

---

## Step 2 — Tell the CMS which repo to use **[YOU]**

1. In the repo, open `src/admin/config.yml`.
2. Click the pencil (Edit) icon. Find this line near the top:
   ```yaml
   repo: YOUR_GITHUB_USERNAME/YOUR_REPO_NAME
   ```
   Replace it with your real path, e.g. `repo: samurray/samuelmurray-site`.
3. Commit the change.

---

## Step 3 — Deploy on Cloudflare Pages **[YOU]**

1. Create a free account at https://dash.cloudflare.com.
2. In the dashboard go to **Workers & Pages → Create → Pages → Connect to Git**.
3. Authorize Cloudflare to access GitHub, and select your `samuelmurray-site` repo.
4. On the build-settings screen, enter exactly:
   - **Framework preset:** `Eleventy` (if offered; if not, leave as "None")
   - **Build command:** `npm run build`
   - **Build output directory:** `_site`
5. Click **Save and Deploy**. Cloudflare runs the build (installs Eleventy, generates the site). In ~1–2 minutes you'll get a live URL like `samuelmurray-site.pages.dev`.
6. **Open that URL and check the whole site** — click every form on the homepage, visit each page, open the sample blog post. This is your preview before touching the real domain.

> If the build fails, copy the red error log and send it to me — build errors at this stage are almost always a small settings fix.

---

## Step 4 — Turn on the CMS login **[YOU]**

The `/admin` editor needs permission to save changes back to GitHub. The simplest route uses GitHub as the login.

1. The Decap CMS GitHub backend needs an OAuth connection. Cloudflare doesn't provide this out of the box, so there are two common options — **pick one** and I'll walk you through the exact clicks:
   - **(a) Use a hosted OAuth helper** (a tiny free service many Decap users run on Cloudflare Workers). Most robust.
   - **(b) Switch the CMS to Cloudflare Access / a token-based login.**
2. Once connected, visit `https://www.samuelmurray.org/admin` (or the `.pages.dev/admin` URL for now), log in with GitHub, and you'll see your **Blog posts** and **Papers** collections ready to edit.

> This is the one genuinely fiddly step. Don't worry about getting it perfect alone — ping me when you reach it and we'll do it together. The site itself is fully live after Step 3; the CMS is the editing convenience on top.

---

## Step 5 — Point your domain **[YOU]** (do this once the preview looks right)

1. In Cloudflare Pages → your project → **Custom domains → Set up a custom domain**. Enter `www.samuelmurray.org` (and optionally `samuelmurray.org`).
2. Cloudflare shows you the DNS record(s) to add (usually a CNAME).
3. Log in to wherever `samuelmurray.org` is **registered** (possibly Google Domains/Squarespace, given your current Google Sites setup) and add the record Cloudflare specifies. *(You do NOT have to transfer the domain to Cloudflare — just add/point the DNS record. If you'd rather move the domain to Cloudflare entirely, that's also possible; ask me.)*
4. DNS can take anywhere from a few minutes to a few hours to propagate. When it's done, `https://www.samuelmurray.org` serves the new site.
5. Once confirmed, **retire the old Google Sites page** and decide whether to drop the $7.99/mo Google plan.

---

## Updating the site later (the easy part — no code)

- **New blog post:** `/admin` → Blog posts → New → fill in title, date, tags, body → Publish.
- **New paper:** `/admin` → Papers → All papers → add an entry → set its area(s) (philosophy / psychology) → save. It appears automatically on the right page(s).
- **Courses / projects:** edit `courses.json` / `projects.json` (these can also be exposed in the CMS later if you'd like — easy to add).

Every save commits to GitHub, which triggers Cloudflare to rebuild and redeploy automatically, usually live within a minute or two.

---

## Running it on your own computer (optional)

If you ever want to preview locally before pushing:

```bash
cd site
npm install
npm start
```

Then open `http://localhost:8080`. (Requires Node.js installed from https://nodejs.org.)

---

## Notes & known follow-ups

- **Content is placeholder** (real research areas, fake specifics). Replace via `/admin` once live.
- **Palatino** is requested via a system-font stack; on machines without it the blog falls back to a near-identical serif. A guaranteed web-font version can be added later.
- **Email** is shown obfuscated (`smurray7 [at] providence [dot] edu`) by design.
- **Possible niceties later:** favicon, social-share image, RSS feed for the blog, ORCID/Google Scholar links.

Questions or a stuck step? Bring the exact screen/error back to the chat and we'll sort it.
