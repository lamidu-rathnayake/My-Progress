# Systems & Audio-ML Engineering — 24-Month Roadmap

> **Timeline:** October 2026 – September 2028  
> **Primary goal:** Become a reliable backend/systems engineer with a demonstrable audio-ML specialization.  
> **Guiding sequence:** fundamentals → working system → measurement → optimization → research.

## 1. The outcome to aim for

By September 2028, aim to be able to:

- Design, implement, test, profile, and explain a dependable backend workflow.
- Diagnose database and application performance using measured evidence rather than guesswork.
- Explain concurrency, transactions, idempotency, retries, failure handling, and consistency trade-offs.
- Build an audio similarity search application that can be reproduced from a clean clone.
- Evaluate retrieval quality and system performance with a defensible experimental method.
- Present the results in a university capstone, technical reports, and a focused portfolio.

This roadmap cannot guarantee a particular job or expertise in every listed tool. It is designed to produce **evidence of practical engineering ability**, not a long list of technologies on a CV.

## 2. The three projects

| Project | Role in the plan | Completion evidence |
|---|---|---|
| **FieldSync** | Work project; develops backend reliability, database, testing, and observability skills. It is not part of the public audio portfolio. | Sanitized reliability report, failure-injection results, before/after measurements, and operational notes, where sharing is permitted. |
| **Audio ML Search** | Main personal engineering project: find similar samples and loops by sound rather than filename. | Reproducible app, baseline comparison, retrieval-quality results, latency measurements, architecture documentation, and demo. |
| **Research capstone** | A focused investigation based on Audio ML Search—not a fourth unrelated project. | Approved research protocol, reproducible experiments, analysis, report, and defense. |

### Repository and data boundaries

- Keep FieldSync code, credentials, customer information, production logs, internal schemas, and unapproved measurements inside the authorized private environment.
- Publish only material that is genuinely sanitized and that you are allowed to share. When uncertain, share methodology or synthetic examples rather than company data.
- Maintain the personal audio application and research outputs in repositories you control.
- Record each dataset and model's source, license, version, and permitted use. Do not assume that publicly downloadable audio is automatically reusable.

## 3. Technology scope

### Core languages

- **C# / .NET 10:** primary backend language and FieldSync stack.
- **SQL / PostgreSQL:** data modeling, query plans, indexing, transactions, and persistence.
- **Python 3.12+:** audio processing, machine-learning experiments, evaluation, and inference.
- **Small TypeScript UI:** maintain or extend the React UI where it helps the audio demo. Learn JavaScript fundamentals as needed; do not start a new frontend framework.

### FieldSync stack

ASP.NET Core, EF Core, PostgreSQL, xUnit, Testcontainers, k6, Serilog, and OpenTelemetry. Use BenchmarkDotNet for isolated .NET microbenchmarks—not for API load testing. Add Polly or the current .NET resilience facilities when transient external calls actually need policies. Use Toxiproxy only for failure scenarios that cross a network boundary and are valuable to test.

### Audio ML Search stack

Python, FastAPI, NumPy, SciPy, librosa, PyTorch, scikit-learn, ffmpeg, PostgreSQL/pgvector, and pytest. Use pretrained embeddings when the feature-based baseline is established. Treat FAISS as a benchmark candidate, not an automatic second production dependency. Add ONNX Runtime when profiling shows inference is worth optimizing.

### Shared tools

Git/GitHub, WSL2, Docker Compose, GitHub Actions, k6, and OpenTelemetry. Add Prometheus, Grafana, and Jaeger incrementally after useful metrics and traces exist; do not build a large observability stack before the application has meaningful traffic.

### Explicitly parked until after September 2028

Kubernetes, Kafka/RabbitMQ, microservices, GraphQL, new frontend frameworks, Rust, C++, JUCE, WebAssembly, DAW/plugin development, LLM/RAG/generative audio, cloud certifications, blockchain, and additional vector databases—unless a real project requirement or approved research question makes one essential.

### Scope rule

> **Production technologies are introduced when a requirement or measured problem justifies them. Research experiments may compare alternatives when that comparison answers the research question; an experimental alternative does not automatically become part of the production stack.**

## 4. Sustainable weekly rhythm

Start with **6–8 hours per week of independent learning and portfolio work**, excluding employment duties, lectures, and required university coursework. Treat this as a target, not a contract. Reduce it during exams or unusually heavy work periods.

| Day | Suggested activity | Time |
|---|---|---:|
| Monday | Systems, databases, reliability, or programming concepts | 60–75 min |
| Tuesday | FieldSync learning task or authorized work-related investigation | 60–90 min |
| Wednesday | DSP, retrieval, or ML theory | 60 min |
| Thursday | Build Audio ML Search | 90–120 min |
| Friday | University coursework, or catch-up if coursework is clear | As required |
| Saturday | Lectures; protect recovery time afterward | — |
| Sunday | Lectures plus weekly review and plan | 30–45 min |

FieldSync implementation may be part of normal work. Do not create extra after-hours work merely to follow the calendar, and do not export proprietary material into personal repositories.

### Monthly review

At the end of every month, record:

1. What was implemented and what was learned.
2. The test, report, notebook, or benchmark that proves it works.
3. What failed and what remains uncertain.
4. Actual time spent and whether the load was sustainable.
5. The next month's single highest-priority outcome.

**If the exit criterion is not met, shrink or extend the milestone instead of carrying several unfinished months forward.** University deadlines and work-critical obligations take priority over the planned pace.

---

# Phase 1 — Foundations and a measurable baseline

**Months 1–6 · October 2026 – March 2027**  
**Target budget:** about 6–8 hours/week outside work and university requirements.  
**Main outcome:** tested core workflows, initial reliability evidence, and an audio retrieval baseline.

## Month 1 — October 2026: Establish the baseline

**Priority:** P0 — foundations

- [ ] Study: DDIA Chapter 1; Brendan Gregg's USE method; *Think DSP* Chapters 1–2.
- [ ] FieldSync: establish a reproducible WSL2/Docker Compose development environment if permitted by the project setup.
- [ ] FieldSync: add structured request-duration logging with Serilog or the project's existing logging standard.
- [ ] FieldSync: run a k6 baseline on up to three working, representative endpoints. Record environment, workload, p50/p95/p99, throughput, and error rate. Do not invent results or benchmark endpoints that do not yet exist.
- [ ] Audio: load an appropriately licensed audio file using librosa and plot its waveform and spectrogram in a notebook.
- [ ] Create `docs/performance/baseline.md` with commands, configuration, environment, and raw results.

**Done when:** the baseline is reproducible (or the report clearly records why a valid baseline is not yet possible) and the audio notebook is committed.

## Month 2 — November 2026: PostgreSQL and query performance

**Priority:** P0 — core database skills

- [ ] Study: *Use The Index, Luke*; PostgreSQL performance documentation; DDIA Chapter 3; *Think DSP* Chapters 3–5.
- [ ] FieldSync: inspect the slowest meaningful queries using query plans and available database statistics. Enable `pg_stat_statements` only if authorized and supported by the environment.
- [ ] FieldSync: choose up to three queries and improve them only when a plan or measurement supports the change. Consider indexes, projections, `AsNoTracking`, and N+1 query issues.
- [ ] Audio: implement an STFT using NumPy/SciPy and compare the result with librosa using the same parameters.

**Done when:** query-plan comparisons include the workload and timings, and the STFT comparison explains parameter differences and numerical tolerance.

## Month 3 — December 2026: Transactions and concurrency conflicts

**Priority:** P0 — correctness

- [ ] Study: DDIA Chapter 7; PostgreSQL concurrency-control documentation; selected CMU 15-445 concurrency lectures; FMP audio-feature material.
- [ ] FieldSync: implement optimistic concurrency for an entity that can be edited by more than one user or device.
- [ ] FieldSync: add automated tests for a stale update and a transaction rollback. Test deadlock handling only where a meaningful multi-transaction case exists.
- [ ] Audio: extract MFCC, chroma, and selected spectral features from an initial licensed collection. Start with a manageable subset (for example 200–500 files); scale toward 1,000 only if data sourcing, labeling, and time allow.
- [ ] Audio: save a manifest with file ID, source, license, duration, sample rate, and processing configuration.

**Done when:** a stale edit is rejected or explicitly resolved (for example, with HTTP 409), and feature generation is reproducible from the manifest.

## Month 4 — January 2027: Concurrency in code

**Priority:** P1 — apply fundamentals

- [ ] Study: OSTEP concurrency material; selected chapters from *Concurrency in C# Cookbook*.
- [ ] FieldSync: understand async/await, cancellation, concurrent requests, and resource lifetime. Add a queue/worker only if the business workflow genuinely requires durable asynchronous processing.
- [ ] FieldSync: use BenchmarkDotNet on one isolated .NET hot path if there is a meaningful candidate; use k6 for HTTP endpoint throughput and latency.
- [ ] Audio: implement brute-force cosine similarity over normalized feature vectors in NumPy.
- [ ] Audio: manually inspect top-five results for a small set of queries and note relevant and irrelevant results.

**Done when:** the audio baseline returns ranked results that can be evaluated by ear, and any performance comparison states exactly what was measured.

## Month 5 — February 2027: Testing and a retrieval evaluation set

**Priority:** P0 — confidence in changes

- [ ] Study: selected material from Vladimir Khorikov's *Unit Testing*, *Software Engineering at Google*, and Chapter 8 of *Introduction to Information Retrieval*.
- [ ] FieldSync: create useful xUnit integration tests against PostgreSQL, using Testcontainers if supported by the development environment.
- [ ] FieldSync: add GitHub Actions CI if policy permits; test replayed operations for idempotency where sync operations are implemented.
- [ ] Audio: define the first task's meaning of “similar” (for example instrument/class similarity, perceptual similarity, or loop utility).
- [ ] Audio: create a small, documented evaluation set with query-to-relevant-item judgments. Target 100 queries only if reliable judgments are feasible; a smaller, carefully labeled pilot is preferable to noisy labels.
- [ ] Audio: implement Precision@k and nDCG@k and record the baseline.

**Done when:** tests run reproducibly in CI and the retrieval metrics can be recomputed from the saved judgments and result rankings.

## Month 6 — March 2027: Failure handling and Gate 1

**Priority:** P0 — finish the first evidence package

- [ ] Study: selected *Release It!* stability patterns and Google SRE material on overload and cascading failures.
- [ ] FieldSync: implement bounded timeouts/retries with jitter only for suitable transient operations. Do not retry non-idempotent mutations blindly; add circuit breaking only for an applicable external dependency.
- [ ] FieldSync: test selected failure cases such as added latency or dropped connections. Use Toxiproxy only if it matches the tested network path and is permitted.
- [ ] Audio: check feature normalization and feature choices against the evaluation baseline.
- [ ] Reserve at least one session for catch-up and documenting results.

### Gate 1 — March 2027

- [ ] FieldSync Reliability Report v1: workload, baseline, selected fixes, before/after evidence, failure tests, limitations.
- [ ] Audio Baseline Results: dataset manifest, feature configuration, evaluation set, Precision@k/nDCG@k, and representative failure examples.
- [ ] CI passes for the tests in scope.

**Gate rule:** evidence matters more than the number of technologies adopted. If the application is not ready for a valid load test, document that limitation and finish the prerequisite first.

---

# Phase 2 — Build Audio ML Search v1

**Months 7–12 · April – September 2027**  
**Target budget:** about 6–8 hours/week; keep FieldSync to required work and light maintenance where possible.  
**Main outcome:** a complete, reproducible audio-search application with an evaluated feature baseline and at least one learned-embedding approach.

## Month 7 — April 2027: Audio ingestion and ML foundations

**Priority:** P0 — working data pipeline

- [ ] Study: selected *Dive into Deep Learning* preliminaries, linear models, MLPs, optimization, and generalization; PyTorch “Learn the Basics”; relevant torchaudio tutorials.
- [ ] Audio: create an ffmpeg-based ingestion pipeline for accepted formats. Record the transformation settings; do not overwrite source files.
- [ ] Audio: persist a sample manifest in PostgreSQL including provenance and license data.
- [ ] Audio: understand tensors, Dataset/DataLoader, training/validation splits, and the basic training loop.
- [ ] Train a small model on features only if it helps establish the ML workflow; do not make training a large model a requirement.

**Done when:** one documented command processes a sample folder into normalized audio plus database manifest rows, and the basic ML workflow is reproducible.

## Month 8 — May 2027: Learned embeddings

**Priority:** P0 — compare one useful model

- [ ] Study: introductory convolutional-network material and the documentation/papers for candidate pretrained audio embedding models such as PANNs or LAION-CLAP.
- [ ] Extract embeddings from one pretrained model first. Evaluate a second model only if time and compute permit.
- [ ] Store model identifier/version, embedding dimension, preprocessing configuration, and vector for each sample.
- [ ] Compare learned embeddings with the feature baseline on the exact same queries and judgments.
- [ ] Listen to and categorize failure cases; distinguish model failure from ambiguous human labels.

**Done when:** an MFCC/features-versus-embedding results table and a short error-analysis note exist.

## Month 9 — June 2027: Vector search experiment

**Priority:** P1 — evaluate index trade-offs

- [ ] Study: HNSW concepts (`M`, `ef`), FAISS documentation, pgvector documentation, and ANN-Benchmarks methodology.
- [ ] Implement exact search first; treat its rankings as the reference for approximate-index recall.
- [ ] Compare pgvector HNSW with one FAISS index family (HNSW or IVF) only after the exact-search baseline works.
- [ ] Measure Recall@10 against exact search, query latency percentiles, index build time, and memory where measurable.
- [ ] Keep the production application on the simplest acceptable design until results justify a more complex option.

**Done when:** scripts, configuration, CSV results, and recall-versus-latency plots can be reproduced. Three index variants are a stretch goal, not a dependency for the application release.

## Month 10 — July 2027: Serve the search system

**Priority:** P0 — end-to-end application

- [ ] Study: FastAPI basics, request/response schemas, error handling, and the sample/feature/embedding database schema.
- [ ] Implement a thin FastAPI service for ingestion and search.
- [ ] Add pytest tests for the core API and retrieval pipeline.
- [ ] Add a Dockerfile and Compose configuration for the app and database.
- [ ] Build a minimal React/TypeScript UI (or the existing UI): upload/import, audio preview, query, and top results.

**Done when:** setup from a clean clone is documented and repeatable; the app supports an end-to-end search and tests run locally and in CI.

## Month 11 — August 2027: Loops and musical relevance

**Priority:** P1 — add one user-relevant capability

- [ ] Study: selected FMP material on tempo/beat tracking/chroma and the relevant librosa documentation.
- [ ] Extract BPM and key-related features for loop material where those estimates are appropriate.
- [ ] Add tempo/key-aware filtering or reranking as a separate, measurable experiment—not an assumption that it always improves results.
- [ ] Create or extend a human-judged query set. Compare results with and without reranking.

**Done when:** a report states whether reranking improves results, for which query types, and where it hurts or is inconclusive.

## Month 12 — September 2027: v1 release and Gate 2

**Priority:** P0 — make the system reproducible

- [ ] Harden input validation, file-size limits, errors, configuration, and setup docs.
- [ ] Add an architecture diagram, data/model provenance notes, evaluation methodology, limitations, and benchmark results to the README.
- [ ] Record a short demo and tag a v1.0 release.
- [ ] Discuss university capstone rules, supervisor expectations, and likely research scope before the research phase.

### Gate 2 — September 2027

- [ ] Audio ML Search v1 runs from a clean clone using documented commands.
- [ ] Evaluation Report v1 compares the feature baseline with learned embeddings and documents the chosen search/index design.
- [ ] A reader can reproduce at least the core quality evaluation.
- [ ] Capstone constraints, deadlines, and supervisor process are known.

---

# Phase 3 — Measurement, reliability, and optimization

**Months 13–18 · October 2027 – March 2028**  
**Target budget:** about 7–9 hours/week only when university load permits; otherwise retain the core deliverables and extend stretch work.  
**Main outcome:** measured system behavior, reproducible optimization, and a defined research direction.

## Month 13 — October 2027: Observability fundamentals

**Priority:** P0 — make behavior visible

- [ ] Study: introductory *Observability Engineering* and SRE monitoring/SLO material; OpenTelemetry documentation for .NET and Python.
- [ ] Add request IDs/correlation, structured logs, request duration, error rate, and a few useful domain metrics in both projects.
- [ ] Add distributed traces for one important end-to-end path. Introduce Jaeger and/or Prometheus/Grafana once instrumentation and queries are meaningful.
- [ ] Define one or two realistic SLIs/SLOs for each project; explain why each target matters.

**Done when:** one slow request or failed operation can be followed through the relevant API, database, and audio-embedding steps; dashboards answer specific operational questions.

## Month 14 — November 2027: Latency and profiling

**Priority:** P0 — diagnose before changing

- [ ] Study: selected *Systems Performance* material, CPU/memory profiling, flame graphs, Gil Tene's latency-measurement guidance, and “The Tail at Scale.”
- [ ] Create repeatable k6 scenarios appropriate to the app: steady load and one ramp/spike or soak scenario as time allows.
- [ ] Profile a representative .NET path with suitable .NET diagnostics and a Python path with a profiler such as py-spy.
- [ ] Fix only the highest-value, confirmed bottleneck(s) and rerun the same workload.

**Done when:** a before/after p95/p99, throughput, and error-rate table exists with workload details, plus one useful profile artifact or explanation.

## Month 15 — December 2027: Retrieval evaluation as an experiment

**Priority:** P0 — research quality

- [ ] Review information-retrieval evaluation material and two relevant ISMIR/DCASE papers. Keep concise notes and record the papers' evaluation methods.
- [ ] Run controlled ablations on a small set of meaningful choices: normalization, pooling, embedding model, or reranking. Do not vary every parameter at once.
- [ ] Freeze dataset splits, configurations, and random seeds where applicable.
- [ ] Use confidence intervals (for example, bootstrap intervals over queries) when the sample size and metric make them appropriate.

**Done when:** an ablation table includes uncertainty where justified and each experiment has a written conclusion or an explicit inconclusive result.

## Month 16 — January 2028: Inference performance

**Priority:** P1 — optimize only if worthwhile

- [ ] Study: PyTorch export and ONNX Runtime performance/quantization documentation.
- [ ] First profile the current inference path. If inference is not a meaningful bottleneck, use the month to improve reproducibility or evaluation instead.
- [ ] If justified, export a model to ONNX and check numerical/output agreement against PyTorch within a documented tolerance.
- [ ] Compare CPU latency/throughput under a small set of batch-size/thread settings; evaluate quantization only if supported and worthwhile.
- [ ] Measure retrieval-quality change as well as latency; choose a configuration based on the trade-off.

**Done when:** a reproducible latency/throughput/quality table supports the configuration decision—or a documented profile shows why ONNX optimization was not worth adopting.

## Month 17 — February 2028: Failure testing and runbooks

**Priority:** P0 — resilience

- [ ] Study: selected *Release It!* capacity/chaos material and SRE troubleshooting/postmortem practices.
- [ ] FieldSync: test relevant duplicate requests, stale versions, dependency timeout, interrupted requests, and worker restart cases that the architecture actually supports.
- [ ] Audio: test corrupt, silent, too-large, and unsupported files; database unavailability; timeout behavior; and bounded resource use.
- [ ] Add file-size limits, sensible timeouts, backpressure/rate limiting where required, and clear failure responses.
- [ ] Write at least one runbook and two concise postmortems only if distinct real or deliberately injected incidents have been reproduced. Never fabricate incidents.

**Done when:** each selected failure has a repeatable test or run procedure, documented expected behavior, actual result, and recovery instructions.

## Month 18 — March 2028: Applied distributed-systems concepts and Gate 3

**Priority:** P1 — concepts first, scale-out optional

- [ ] Study selected DDIA chapters on replication, partitioning, transactions, and distributed-system problems. Use MIT distributed-systems lectures to clarify concepts; implementing Raft is not a requirement.
- [ ] FieldSync: document idempotency, outbox processing, consistency, and recovery guarantees where implemented.
- [ ] Audio: if the research question benefits from it, prototype sharding or a second API replica as a controlled experiment. Do not make multi-replica deployment a required production architecture without a real need.
- [ ] Compare expected versus observed behavior and document limitations.

### Gate 3 — March 2028

- [ ] Engineering Report v1: observability, workload design, performance results, confirmed optimizations, failure tests, and limitations.
- [ ] Architecture decisions identify which techniques were adopted, tested only, or rejected—and why.
- [ ] Draft research question and feasible experiment plan reviewed with the supervisor or lecturer.

---

# Phase 4 — Research, portfolio, and career preparation

**Months 19–24 · April – September 2028**  
**Target budget:** about 6–8 hours/week, adjusted around internship and capstone commitments.  
**Main outcome:** completed capstone, reproducible results, and a professional portfolio.

## Month 19 — April 2028: Research design

**Priority:** P0 — narrow the question

- [ ] Review relevant audio-retrieval papers and benchmark methodology. Keep a short evidence table: question, dataset, approach, metric, limitation.
- [ ] Write a concise research protocol: question, hypotheses, dataset and splits, baselines, metrics, experiment plan, threats to validity, and resource limits.
- [ ] Candidate question: *How do feature-based and learned audio representations trade retrieval quality against query latency and resource cost for sample/loop search?*
- [ ] Confirm university requirements, ethics/data considerations, deliverable format, and dates with the supervisor.

**Done when:** the supervisor or lecturer approves the scope, and each proposed experiment maps directly to the research question.

## Month 20 — May 2028: Reproducible experiment harness

**Priority:** P0 — make results repeatable

- [ ] Build a command-line runner that reads a configuration and writes structured result files.
- [ ] Pin dependencies, freeze dataset splits, record model/index versions and configuration, and log seeds where relevant.
- [ ] Run a small pilot batch end-to-end; check runtime, disk space, memory, and whether the output schema is sufficient.
- [ ] Make a clean-environment reproduction attempt.

**Done when:** the pilot can be reproduced within explicitly documented tolerances on the same or a comparable environment.

## Month 21 — June 2028: Main experiments

**Priority:** P0 — execute the approved plan

- [ ] Run the approved experiment matrix; do not add a new model or index family unless a defect or the research question demands it.
- [ ] Collect quality metrics, latency percentiles, indexing time, and memory/resource cost that can be measured consistently.
- [ ] Keep raw results; generate figures and summary tables from scripts.
- [ ] Record failed runs and exclusions with reasons.
- [ ] Analyze effect sizes and uncertainty rather than relying only on single best numbers.

**Done when:** all experiments in the approved plan are complete, or deviations are justified and documented.

## Month 22 — July 2028: Write and review

**Priority:** P0 — communicate the evidence

- [ ] Draft abstract, introduction, related work, methodology, results, discussion, threats to validity, and conclusion.
- [ ] Ensure every table/figure can be regenerated from saved data and scripts.
- [ ] Ask a supervisor, lecturer, or qualified peer for review; complete at least two revision passes if the academic calendar allows.

**Done when:** a complete draft exists and the main claims match the evidence and acknowledged limitations.

## Month 23 — August 2028: Portfolio and applications preparation

**Priority:** P1 — present the work clearly

- [ ] Clean personal repositories, remove secrets and temporary files, and ensure setup instructions work from a clean clone.
- [ ] Write three concise case studies: FieldSync reliability (sanitized and authorized), Audio ML Search, and capstone research.
- [ ] Publish up to three technical posts if the material adds value; quality matters more than the count.
- [ ] Prepare a CV tailored to backend/reliability and audio-ML roles. State only skills and results that can be defended.
- [ ] Record a short demo and ensure every benchmark includes methodology and environment details.

**Done when:** the portfolio is live or ready to share privately, each project has a clear README, and all published numbers are traceable to evidence.

## Month 24 — September 2028: Final submission and launch

**Priority:** P0 — finish and verify

- [ ] Complete capstone submission, defense preparation, and any supervisor-required revisions.
- [ ] Practice explaining the architecture, key trade-offs, failure cases, benchmark methodology, and limitations of both projects.
- [ ] Review SQL, concurrency, data structures, algorithms, and system-design fundamentals; begin or continue modest interview practice.
- [ ] Send 10 targeted applications if the portfolio and academic schedule are ready. Applications are an activity target, not a guarantee of a result.
- [ ] Reserve time for final fixes and submission requirements.

### Gate 4 — September 2028

- [ ] Capstone submitted and defended as required by the university.
- [ ] Audio ML Search runs reproducibly and has a clear demo.
- [ ] Portfolio and case studies are ready to share.
- [ ] Applications or next-step career plan completed.
- [ ] You can explain every important figure, assumption, and limitation in your reports.

---

# 5. Progress tracker

Update this table at the end of each month. Use `Not started`, `In progress`, `Blocked`, or `Done`; link the evidence rather than writing “finished” without proof.

| Month | Target | Status | Evidence / notes |
|---|---|---|---|
| 01 · Oct 2026 | Baseline + waveform/spectrogram notebook | In progress | |
| 02 · Nov 2026 | Query-plan comparisons + STFT comparison | Not started | |
| 03 · Dec 2026 | Concurrency test + audio feature manifest | Not started | |
| 04 · Jan 2027 | Cosine-search baseline + measured hot path | Not started | |
| 05 · Feb 2027 | CI + labeled retrieval evaluation set | Not started | |
| 06 · Mar 2027 | Gate 1 reports | Not started | |
| 07 · Apr 2027 | Reproducible ingestion pipeline | Not started | |
| 08 · May 2027 | Embedding comparison | Not started | |
| 09 · Jun 2027 | Exact vs approximate vector-search results | Not started | |
| 10 · Jul 2027 | End-to-end search app | Not started | |
| 11 · Aug 2027 | Reranking experiment | Not started | |
| 12 · Sep 2027 | Audio ML Search v1 / Gate 2 | Not started | |
| 13 · Oct 2027 | Useful traces, metrics, and SLOs | Not started | |
| 14 · Nov 2027 | Profile + before/after measurements | Not started | |
| 15 · Dec 2027 | Retrieval ablation results | Not started | |
| 16 · Jan 2028 | Inference decision backed by evidence | Not started | |
| 17 · Feb 2028 | Repeatable failure tests + runbook | Not started | |
| 18 · Mar 2028 | Engineering report / Gate 3 | Not started | |
| 19 · Apr 2028 | Approved research protocol | Not started | |
| 20 · May 2028 | Reproducible experiment harness | Not started | |
| 21 · Jun 2028 | Main experiment results | Not started | |
| 22 · Jul 2028 | Reviewed capstone draft | Not started | |
| 23 · Aug 2028 | Portfolio and case studies | Not started | |
| 24 · Sep 2028 | Submission, defense, and career launch | Not started | |

---

# 6. Core concepts checklist

Use this as a coverage check, not as a requirement to study every concept in depth at the same time.

## Backend and software engineering

- [ ] C# types, classes, interfaces, composition, generics, LINQ, exceptions, async/await, cancellation, and resource disposal
- [ ] API design, validation, dependency injection, configuration, authentication, authorization, and error handling
- [ ] Unit tests, integration tests, test doubles, migrations, code review, and refactoring
- [ ] Data structures, algorithmic complexity, debugging, and profiling

## Databases and reliability

- [ ] Relational modeling, constraints, indexes, query plans, transactions, isolation, and locking
- [ ] Optimistic concurrency, idempotency, retries, timeouts, and partial failure
- [ ] Durable work processing and outbox patterns where implemented
- [ ] Logs, metrics, traces, SLIs/SLOs, load testing, runbooks, and postmortems

## Python and audio ML

- [ ] Python environments, modules, NumPy arrays, SciPy, file/data handling, and pytest
- [ ] Sample rate, channels, PCM, amplitude, decibels, FFT/STFT, windows, spectrograms, MFCC, chroma, and spectral features
- [ ] Feature normalization, cosine similarity, pretrained embeddings, exact/approximate nearest-neighbor search
- [ ] Train/validation/test separation, Precision@k, Recall@k, nDCG@k, and error analysis
- [ ] Experiment configuration, versioned data/model provenance, confidence intervals where appropriate
- [ ] Inference profiling and ONNX Runtime only if justified

## Delivery and tooling

- [ ] Git and GitHub workflow
- [ ] Docker Compose and clean-clone setup
- [ ] CI for tests and repeatable checks
- [ ] k6 workloads with documented environment and data
- [ ] Basic observability and controlled fault testing

---

# 7. Resources

Prefer selected chapters and exercises over trying to read every resource cover-to-cover while building the projects.

| Topic | Resource |
|---|---|
| Systems and data | [*Designing Data-Intensive Applications*](https://dataintensive.net/) |
| SQL performance | [Use The Index, Luke](https://use-the-index-luke.com/) |
| Operating systems | [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/) |
| Reliability | [Google SRE books](https://sre.google/books/) · *Release It!* by Michael Nygard |
| Database lectures | [CMU 15-445](https://15445.courses.cs.cmu.edu/) |
| Performance | [Brendan Gregg](https://www.brendangregg.com/) |
| DSP | [*Think DSP*](https://greenteapress.com/wp/think-dsp/) · [FMP notebooks](https://www.audiolabs-erlangen.de/resources/MIR/FMP/C0/C0.html) |
| Machine learning | [Dive into Deep Learning](https://d2l.ai/) · [PyTorch tutorials](https://pytorch.org/tutorials/) |
| Retrieval evaluation | [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/) — evaluation chapters |
| Vector search | [FAISS wiki](https://github.com/facebookresearch/faiss/wiki) · [pgvector](https://github.com/pgvector/pgvector) · [ANN-Benchmarks](https://ann-benchmarks.com/) · [HNSW paper](https://arxiv.org/abs/1603.09320) |
| Audio models | [PANNs paper](https://arxiv.org/abs/1912.10211) · [LAION-CLAP repository](https://github.com/LAION-AI/CLAP) |
| Audio datasets | [FSD50K](https://zenodo.org/records/4060432) · [Freesound API docs](https://freesound.org/docs/api/) |

## Final rule

> **Build it. Measure it. Understand it. Defend it.**
>
> A small system with reproducible results is more valuable than a complex stack you cannot explain. Keep the plan focused, protect university time, and let requirements, measurements, and research questions—not technology trends—decide what you learn next.
