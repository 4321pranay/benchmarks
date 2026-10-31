# Spring Boot — 110 questions

Hand-written questions about Spring Boot 2.0–4.0 and Spring Framework 5.0–7.0, with reference
answers. Written to be harder than documentation lookup: most require knowing the specific
annotation, property, event or ordering rule that makes something work, and several are phrased
the way a developer actually hits the problem ("Hikari logs 'Connection is not available'…").

Held out from training data. No question was taken from a public benchmark.

## Coverage

Roughly ten questions per area, in file order:

auto-configuration internals · configuration · web · data / transactions · testing · security ·
actuator / observability · deployment / performance · messaging / concurrency / scheduling ·
migration / versions · debugging / troubleshooting · architecture / design

Because the areas run in file order, the usual blocks of ten (1–10, 11–20, …) line up with them.

## Baselines

Measured with a local Qwen3-8B (12k context) answering, the same model judging on the 0/1/2
rubric, and a RAG index of 14,235 chunks built from the official Boot and Framework reference
docs. All numbers are over the full 110 questions.

| System | Score |
|---|---|
| RAG, answer prompt asking for completeness, 6 chunks | **70%** |
| Agentic RAG (re-searches until the model judges excerpts sufficient, ~10 chunks) | 65% |
| RAG, 10 chunks | 64% |
| RAG, 6 chunks, answer prompt asking for concision | 61% |
| RAG + bge-m3 embeddings / + BM25 / + bge-reranker-base, alone and in all combinations | 54–60% |
| No documents, model knowledge only | 57% |
| Best answer per question across all 12 configurations ("oracle") | 89% |

## What this suite turned out to measure

- **Answer completeness dominates.** The single biggest change was in the answer prompt, not
  retrieval: swapping "be concise and concrete" for "list every applicable mechanism, annotation,
  property and limit" moved 21 questions from 1 to 2 and was worth +9 points. The reference
  answers are enumerative, so a system that names one valid mechanism and stops scores 1.
- **Retrieval sophistication did not help.** BM25 fusion, a cross-encoder reranker and a
  stronger embedding model all scored at or below plain dense retrieval, alone and in every
  combination. They reorder the same chunks; the questions that fail usually need a *specific
  sentence* that is diluted inside a large chunk.
- **Agentic re-searching bought nothing that more context did not.** The agent (65%) and plain
  retrieval with the same number of chunks (64%) are indistinguishable, and the agent spends
  three extra model calls per question.
- **A 0/1/2 rubric with a same-size judge is too coarse.** Even the best system leaves 62 of 110
  answers at 1, and the whole 54–61% band is inside judge noise. Grade key-point recall instead
  if you need to resolve differences under ~10 points.

## Known limits

- 25 questions were never scored 2 by any of the 12 configurations tested. Of those, 8 have
  reference answers naming something outside the Spring docs (Testcontainers, Keycloak, CDS,
  Kafka, Redis, springdoc, Flyway, the outbox pattern), so a documents-only system cannot reach
  them. The other 17 are answerable from the official docs.
- Reference answers reflect the documentation as of October 2026. Spring Framework 6.0 and 6.1
  reference docs are no longer published upstream.
