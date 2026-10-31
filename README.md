# benchmarks

Question-and-reference-answer evaluation sets for testing LLMs and RAG systems on real
engineering questions. Every suite is hand-written, held out from any training data, and
pitched at the level where a model has to know the specific mechanism — not just the topic.

## Suites

| Suite | Questions | Scope |
|---|---|---|
| [`java/spring-boot`](java/spring-boot) | 110 | Spring Boot 2.0–4.0 and Spring Framework 5.0–7.0: auto-configuration internals, web, data, testing, security, actuator, deployment, messaging, migration, troubleshooting |

[`TARGETS.md`](TARGETS.md) indexes every suite in the repo, including the 42 placeholder
directories that have a README naming the documentation they should be written against, but no
questions yet.

## Layout

Suites are addressed by language first, then framework:

```
<language>/<framework>/      java/spring-boot/, python/django/, javascript/react/
<language>/core/             language itself, no framework: python/core/, rust/core/
tools/<tool>/                not tied to one language: tools/postgres/, tools/kubernetes/
```

Each leaf holds `eval.jsonl` plus a `README.md` describing scope, provenance and known limits.
Versions are not part of the path — a suite spans whatever versions its README states, so
version coverage can grow without moving files.

## Record format

One JSON object per line, in the `messages` shape used by most eval and fine-tuning tooling,
plus a `reviewed` flag:

```json
{"messages": [{"role": "user", "content": "<question>"},
              {"role": "assistant", "content": "<reference answer>"}],
 "reviewed": false}
```

`reviewed` is **required** and must be `true` or `false`. It records whether a human has checked
that question and reference answer against the documentation — `true` means someone verified the
answer is correct and complete enough to grade against, not merely that a human typed it. Scores
computed over unreviewed records should say so, because a wrong reference answer silently
penalises correct candidates. `python3 validate.py` reports the reviewed count per suite.

The 1-based line number is the question id — results are usually reported in blocks of ten
(1–10, 11–20, …), so file order is part of the data and should not be reshuffled. Add new
questions at the end.

`python3 validate.py` checks every suite against that format.

## Scoring

These sets carry reference answers, not single correct tokens, so they need a judge. The
scoring used for the published baselines is a 0/1/2 rubric (2 = correct and covers the key
points, 1 = partially correct or missing key points, 0 = wrong or no answer), applied by an
LLM given the question, the reference answer and the candidate answer.

Two findings worth knowing before trusting small differences: with a same-size judge the
noise is ±5–10 points, and most answers pile up at 1, so the 3-point scale cannot resolve
differences smaller than that. Grading **key-point recall** — what fraction of the reference's
points the candidate covers — separates systems far better. See the suite README for what this
cost in practice.
