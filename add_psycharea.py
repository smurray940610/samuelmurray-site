#!/usr/bin/env python3
"""Add a "psychArea" tag to the 29 psychology papers that belong on the
Psychology & Neuroscience page, matching by EXACT title string.

Run from the repo root (~/Downloads/site):

    python3 add_psycharea.py

It edits src/_data/papers.json in place. If any title below fails to match a
paper (e.g. a subtitle was edited), it prints the offenders and exits WITHOUT
writing, so you never half-tag the file. Expected success line:

    OK -- tagged 29 papers with psychArea (expected 29).

The 6 psychology-area papers deliberately left untagged (Why value values?;
The place of the trace; Can the mind wander intentionally?; The scientific
study of passive thinking; Times imagined and remembered; Purity is linked to
cooperation...) will not appear on the psych page, because psychology.njk only
renders papers that carry a psychArea.
"""
import json
import sys

PAPERS = "src/_data/papers.json"

# area id -> exact paper titles (must match papers.json verbatim)
AREA = {
    "moral-cognition": [
        "Mental control and attributions of blame for negligent wrongdoing",
        "Varieties of negligence",
        "Blame for Hum(e)an beings: The role of character information in judgments of blame",
        "Within your rights: Dissociating wrongness and permissibility in moral judgement",
        "Commonsense Morality and the Bearable Automaticity of Being",
        "Intuitions about free will and the failure to comprehend determinism",
        "Not what I expected: Feeling of surprise differentially mediates effect of personal control on attributions of free will and responsibility",
        "Piercing the smoke screen: Dualism, free will, and Christianity",
        "The neurocognitive mechanisms of responsibility: a framework for normatively relevant neuroscience",
    ],
    "cross-cultural": [
        "Loyalty from a personal point of view: A cross-cultural prototype study of loyalty",
        "A Cross-Cultural Study of Everyday Moral Experiences",
        "Validation of the Moral Foundation Vignettes in Latin America",
    ],
    "consciousness": [
        "Vigilance and mind wandering",
        "What are the benefits of mind wandering to creativity?",
        "A computational modeling approach to investigating mind wandering-related adjustments to gaze behavior during scene viewing",
        "Fixation, flexibility, and creativity: The dynamics of mind wandering",
        "Attention need not always apply: Mind wandering impedes explicit but not implicit sequence learning",
        "Thought dynamics under task demands: Evaluating the influence of task difficulty on unconstrained thought",
        "What's in a task? Complications in the study of the task-unrelated-thought variety of mind wandering",
    ],
    "self-regulation": [
        "Mental control and effort differ across different kinds of mental action",
        "The strategic allocation theory of vigilance",
        "Believe in your self-control: Lay theories of self-control and their downstream effects",
        "What's inside is all that counts? The contours of everyday thinking about self-control",
        "Moralization and self-control strategy selection",
    ],
    "memory": [
        "Memories of forgiven wrongs: the role of interpersonal closeness and severity when remembering forgiven transgressions",
        "The emotional impact of forgiveness on autobiographical memories of past wrongdoings",
        "Neural differences between internal and external episodic counterfactual thoughts",
        "The impact of error-consequence severity on cue processing in importance-biased prospective memory",
    ],
    "political": [
        "I've said it before and I will say it again: Repeating statements made by Donald Trump increases perceived truthfulness",
    ],
}

# Flatten to title -> area, and guard against accidental duplicate titles.
title2area = {}
for area, titles in AREA.items():
    for t in titles:
        if t in title2area:
            print("ERROR -- duplicate title in this script:", t)
            sys.exit(1)
        title2area[t] = area

expected = len(title2area)  # 29

with open(PAPERS, encoding="utf-8") as f:
    papers = json.load(f)

seen = set()
tagged = 0
for p in papers:
    t = p.get("title")
    if t in title2area:
        p["psychArea"] = title2area[t]
        seen.add(t)
        tagged += 1

missing = [t for t in title2area if t not in seen]
if missing:
    print("ERROR -- these titles were NOT found in papers.json (fix before building):")
    for m in missing:
        print("   -", m)
    print("Nothing was written.")
    sys.exit(1)

with open(PAPERS, "w", encoding="utf-8") as f:
    json.dump(papers, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("OK -- tagged", tagged, "papers with psychArea (expected", str(expected) + ").")
