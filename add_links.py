#!/usr/bin/env python3
"""Fill in `link` URLs for psychology papers that currently have link == "#".
Only sets a link when the title matches exactly AND we have not already got a
real link. Prints what it changed and what it skipped. Safe to re-run.
"""
import json, sys

P = "src/_data/papers.json"

# title -> verified publisher/DOI URL (full canonical URLs, matching philosophy-page style)
LINKS = {
    "Mental control and attributions of blame for negligent wrongdoing": "https://doi.org/10.1037/xge0001262",
    "Varieties of negligence": "https://doi.org/10.1177/01461672261444067",
    "The emotional impact of forgiveness on autobiographical memories of past wrongdoings": "https://doi.org/10.1037/xge0001787",
    "Memories of forgiven wrongs: the role of interpersonal closeness and severity when remembering forgiven transgressions": "https://doi.org/10.1080/09658211.2026.2627194",
    "Neural differences between internal and external episodic counterfactual thoughts": "https://royalsocietypublishing.org/doi/10.1098/rstb.2021.0337",
    "The impact of error-consequence severity on cue processing in importance-biased prospective memory": "https://doi.org/10.1093/texcom/tgab056",
    "Validation of the Moral Foundation Vignettes in Latin America": "https://doi.org/10.1525/collabra.128178",
    "Blame for Hum(e)an beings: The role of character information in judgments of blame": "https://doi.org/10.1177/19485506241233708",
    "Within your rights: Dissociating wrongness and permissibility in moral judgement": "https://doi.org/10.1111/bjso.12680",
    "What are the benefits of mind wandering to creativity?": "https://doi.org/10.1037/aca0000420",
    "The strategic allocation theory of vigilance": "https://doi.org/10.1002/wcs.1693",
    "Believe in your self-control: Lay theories of self-control and their downstream effects": "https://doi.org/10.1016/j.copsyc.2024.101879",
    "Fixation, flexibility, and creativity: The dynamics of mind wandering": "https://doi.org/10.1037/xhp0001012",
    "Attention need not always apply: Mind wandering impedes explicit but not implicit sequence learning": "https://doi.org/10.1016/j.cognition.2020.104530",
    "Thought dynamics under task demands: Evaluating the influence of task difficulty on unconstrained thought": "https://doi.org/10.1037/xhp0000944",
    "What's in a task? Complications in the study of the task-unrelated-thought variety of mind wandering": "https://doi.org/10.1177/1745691619897966",
    "Commonsense Morality and the Bearable Automaticity of Being": "https://doi.org/10.1016/j.concog.2024.103748",
    "Moralization and self-control strategy selection": "https://doi.org/10.3758/s13423-023-02257-7",
    "A computational modeling approach to investigating mind wandering-related adjustments to gaze behavior during scene viewing": "https://doi.org/10.1016/j.cognition.2023.105624",
}

papers = json.load(open(P, encoding="utf-8"))
titles = {p["title"] for p in papers}

changed, skipped_has_link, not_found = [], [], []
for t, url in LINKS.items():
    if t not in titles:
        not_found.append(t); continue
    for p in papers:
        if p["title"] == t:
            if p.get("link") and p["link"] != "#":
                skipped_has_link.append(t)
            else:
                p["link"] = url
                changed.append(t)
            break

if not_found:
    print("ERROR -- titles not found in papers.json (nothing written):")
    for t in not_found: print("   -", t)
    sys.exit(1)

json.dump(papers, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")

print("Added links to", len(changed), "papers.")
if skipped_has_link:
    print("Skipped (already had a real link):", len(skipped_has_link))
