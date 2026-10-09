# Systems & Audio-ML Engineering: 24-Month Roadmap

> **Scope rule:** This roadmap contains only the stack below. A technology enters the plan only when a benchmark from your own system shows the current one is the bottleneck.
>
> **Parked until after Sep 2028:** Kubernetes, Kafka/RabbitMQ, microservice frameworks, GraphQL, new frontend frameworks, Rust, C++, JUCE, WebAssembly, DAW/plugin development, LLMs/RAG/generative audio, cloud certifications, blockchain. (The old DAW roadmap is archived in `roadmaps/archive/`.)

**Languages:** C# (.NET 10) · Python 3.12+ · SQL  
**FieldSync:** ASP.NET Core · EF Core · PostgreSQL · xUnit · Testcontainers · BenchmarkDotNet · Polly · Serilog  
**Audio ML Search:** FastAPI · librosa · torchaudio · PyTorch · scikit-learn · FAISS · pgvector · ONNX Runtime · pytest · ffmpeg  
**Shared:** WSL2 · Docker Compose · GitHub Actions · k6 · Toxiproxy · OpenTelemetry · Jaeger · Prometheus · Grafana

**Weekly rhythm:** Mon Theory A (systems/DB/reliability) · Tue Build FieldSync · Wed Theory B (audio/ML) · Thu Build Audio ML Search · Fri university work · Sat lectures, then off · Sun lectures, then weekly review

**Rule for every month:** if the *Done when* is not met, extend the month instead of moving on.

---

# Phase 1: Foundations
## Months 1–6 · Oct 2026 – Mar 2027

### Month 1 (Oct 2026): Measure before you optimize
- [ ] Study: DDIA ch. 1 · USE method (Brendan Gregg) · Think DSP ch. 1–2
- [ ] FieldSync: WSL2 + Docker Compose dev environment
- [ ] FieldSync: k6 baseline for 3 endpoints (p50/p95/p99, error rate)
- [ ] FieldSync: structured request-duration logging with Serilog
- [ ] Audio: load a file with librosa; plot waveform and spectrogram in a notebook
- [ ] **Done when:** `docs/perf/baseline.md` has the numbers and the spectrogram notebook is committed

### Month 2 (Nov 2026): PostgreSQL and indexes
- [ ] Study: *Use The Index, Luke* · PostgreSQL docs, Performance Tips · DDIA ch. 3 · Think DSP ch. 3–5
- [ ] FieldSync: enable `pg_stat_statements`; find the 3 slowest queries
- [ ] FieldSync: fix them with indexes, query changes, and EF Core fixes (projection, `AsNoTracking`, remove N+1)
- [ ] Audio: implement an STFT in NumPy and compare it with librosa
- [ ] **Done when:** 3 before/after query plans with timings are committed and the STFT matches librosa

### Month 3 (Dec 2026): Transactions and conflicts
- [ ] Study: DDIA ch. 7 · PostgreSQL docs, Concurrency Control · CMU 15-445 concurrency lectures · FMP audio-feature chapters
- [ ] FieldSync: row-version concurrency tokens for offline-edit conflicts
- [ ] FieldSync: tests that force a conflict and a deadlock
- [ ] Audio: extract MFCC, chroma, and spectral features for about 1,000 samples
- [ ] **Done when:** a conflict test returns a clean 409 and features are saved with a manifest (file, source, license, duration)

### Month 4 (Jan 2027): Concurrency in code
- [ ] Study: OSTEP concurrency part · Cleary, *Concurrency in C# Cookbook*
- [ ] FieldSync: queue-based sync worker (Postgres `SKIP LOCKED` + `BackgroundService`)
- [ ] FieldSync: BenchmarkDotNet on one hot path
- [ ] Audio: brute-force cosine search over features in NumPy
- [ ] **Done when:** sync throughput before/after is recorded under k6 and a query plus its top 5 results can be judged by ear

### Month 5 (Feb 2027): Testing for confidence
- [ ] Study: Khorikov, *Unit Testing* · *Software Engineering at Google* testing chapters · IR book ch. 8
- [ ] FieldSync: xUnit + Testcontainers integration suite on real PostgreSQL
- [ ] FieldSync: GitHub Actions CI and idempotency tests for sync replay
- [ ] Audio: define "similar" (class or instrument label); build a 100-query evaluation set
- [ ] Audio: implement Precision@k and nDCG
- [ ] **Done when:** CI is green on every push and baseline P@10 and nDCG@10 are recorded

### Month 6 (Mar 2027): Failure handling + buffer week
- [ ] Study: *Release It!* stability patterns · SRE book, "Handling Overload" and "Addressing Cascading Failures" · Polly docs
- [ ] FieldSync: timeouts, jittered retry, and a circuit breaker on external calls
- [ ] FieldSync: Toxiproxy tests (added latency, dropped connections)
- [ ] Audio: tune the baseline (normalization, feature selection)
- [ ] **Done when:** both reports below exist

### Gate 1
- [ ] FieldSync Reliability Report v1 (baseline, fixes, numbers, failure tests)
- [ ] Audio Baseline Results Table
- [ ] CI green

---

# Phase 2: Audio ML Search v1
## Months 7–12 · Apr – Sep 2027

*Tuesdays shift to FieldSync maintenance and keeping CI green. Audio ML Search gets Wednesday and Thursday.*

### Month 7 (Apr 2027): Minimum viable machine learning
- [ ] Study: D2L (preliminaries, linear models, MLP, optimization, generalization) · PyTorch "Learn the Basics" · torchaudio tutorials
- [ ] Audio: ffmpeg ingestion pipeline (mono, fixed sample rate, loudness) + PostgreSQL manifest with source and license
- [ ] Audio: tensors, Dataset, DataLoader, and the training loop
- [ ] Audio: train a small MLP on your features with a train/validation split
- [ ] **Done when:** one command turns a folder of audio into normalized files plus database rows, and the training loop runs

### Month 8 (May 2027): Learned embeddings
- [ ] Study: D2L convolutional networks · PANNs and LAION-CLAP papers and READMEs
- [ ] Audio: extract embeddings with 1–2 pretrained models and store them
- [ ] Audio: compare against the MFCC baseline on the same evaluation set; listen to the failures
- [ ] **Done when:** a results table (MFCC vs each model, P@10, nDCG@10) and error-analysis notes exist

### Month 9 (Jun 2027): Vector search
- [ ] Study: HNSW paper (`M`, `ef`) · FAISS wiki · pgvector README · ANN-Benchmarks site
- [ ] Audio: build exact search, FAISS HNSW and IVF, and pgvector HNSW
- [ ] Audio: measure recall@10 against exact search and latency while varying parameters
- [ ] **Done when:** recall-vs-latency curves for 3 index types are saved as plots plus a CSV

### Month 10 (Jul 2027): Serve it
- [ ] Study: FastAPI docs · schema design for embeddings in PostgreSQL
- [ ] Audio: FastAPI service with `POST /samples` and `GET /search`
- [ ] Audio: database schema for samples, features, embeddings
- [ ] Audio: pytest tests, Dockerfile, Compose file
- [ ] Audio: minimal UI (upload, play, top-10 list with audio players)
- [ ] **Done when:** `docker compose up` gives a working end-to-end search in 5 commands or fewer and pytest runs in CI

### Month 11 (Aug 2027): Loops and musical relevance
- [ ] Study: FMP chapters on tempo, beat tracking, chroma · librosa `beat_track` and chroma docs
- [ ] Audio: extract BPM and key for loops
- [ ] Audio: add tempo-aware and key-compatible filtering or reranking
- [ ] Audio: build 50 human-judged queries and compare with and without reranking
- [ ] **Done when:** a report shows whether reranking helps, with per-query examples

### Month 12 (Sep 2027): v1 release + buffer week
- [ ] Audio: hardening, README with architecture diagram, setup guide, results
- [ ] Audio: record a 3-minute demo and tag `v1.0`
- [ ] **Done when:** the gate below passes

### Gate 2
- [ ] Audio ML Search v1.0 runs from a clean clone
- [ ] Evaluation Report v1 (MFCC vs embeddings vs index types)

---

# Phase 3: Measurement and Optimization
## Months 13–18 · Oct 2027 – Mar 2028

*Build sessions dominate (about 80%).*

### Month 13 (Oct 2027): Observability
- [ ] Study: *Observability Engineering* (first chapters) · SRE book SLO and monitoring chapters · OpenTelemetry docs (.NET, Python) · Prometheus basics
- [ ] Both projects: traces (OpenTelemetry → Jaeger), metrics (Prometheus), dashboards (Grafana)
- [ ] Both projects: request rate, errors, duration, queue depth, DB pool usage; 2 SLOs each
- [ ] **Done when:** each project has a dashboard and you can trace a slow request to its DB query or embedding step

### Month 14 (Nov 2027): Latency and profiling
- [ ] Study: *Systems Performance* (methodology, CPU, memory) · flame graphs · Gil Tene, "How NOT to Measure Latency" · "The Tail at Scale" · HdrHistogram
- [ ] Both projects: k6 scenarios (steady, ramp, spike, soak)
- [ ] Both projects: profile with dotnet-trace, dotnet-counters, py-spy; fix the top 3 bottlenecks
- [ ] **Done when:** a before/after table (p95, p99, throughput) and one annotated flame graph exist

### Month 15 (Dec 2027): Retrieval quality as science
- [ ] Study: IR book ch. 8 again · "How to Read a Paper" · 2 ISMIR/DCASE papers on evaluation · your SMA2306 notes on confidence intervals
- [ ] Audio: ablations over normalization, pooling, embedding model, PCA dimension, reranking
- [ ] Audio: fixed seeds, logged configs, bootstrap confidence intervals on every metric
- [ ] **Done when:** an ablation table with confidence intervals and one conclusion per ablation exists

### Month 16 (Jan 2028): Inference performance
- [ ] Study: ONNX Runtime docs (performance tuning, quantization) · PyTorch ONNX export docs
- [ ] Audio: export the embedding model to ONNX and validate output against PyTorch
- [ ] Audio: benchmark PyTorch vs ONNX Runtime on CPU (batch size, threads, int8 quantization)
- [ ] Audio: measure accuracy loss on the evaluation set
- [ ] **Done when:** a latency/throughput/quality trade-off table exists and a production config is chosen and justified

### Month 17 (Feb 2028): Failure testing
- [ ] Study: *Release It!* capacity and chaos · SRE book, "Effective Troubleshooting" and "Postmortem Culture" · Toxiproxy docs
- [ ] Both projects: scripted failures (kill DB mid-ingest, slow network, corrupt/silent/huge audio, queue backlog, container memory limit)
- [ ] Both projects: timeouts, backpressure, size limits, rate limiting
- [ ] Both projects: runbook and 2 postmortems
- [ ] **Done when:** the failure suite is repeatable and each scenario's expected behavior is documented and verified

### Month 18 (Mar 2028): Distributed systems, applied + buffer week
- [ ] Study: DDIA ch. 5, 6, 8, 9 · MIT 6.824 lectures (Raft included) · Raft paper
- [ ] FieldSync: 2+ API replicas behind a reverse proxy; outbox and idempotent-consumer pattern
- [ ] Audio: split embeddings into 2 index shards, merge results, measure
- [ ] Both projects: document consistency choices
- [ ] **Done when:** the gate below passes

### Gate 3
- [ ] Engineering Report v1 (observability, load results, optimizations, failure tests, scale-out numbers)

---

# Phase 4: Research, Portfolio, Jobs
## Months 19–24 · Apr – Sep 2028

*This phase overlaps the final-semester internship. Confirm early whether your current job can count toward it.*

### Month 19 (Apr 2028): Research design
- [ ] Study: 15–20 ISMIR/DCASE papers on audio similarity and retrieval (one paragraph of notes each) · ANN-Benchmarks methodology
- [ ] Write a 3-page protocol: question, hypotheses, metrics, datasets and splits, threats to validity
- [ ] Suggested question: *How do feature-based and learned embeddings trade retrieval quality against latency and resource cost for sample and loop search?*
- [ ] **Done when:** a lecturer or supervisor has approved the protocol

### Month 20 (May 2028): Reproducible harness
- [ ] One-command experiment runner (config in, result files out)
- [ ] Pinned dependencies, Docker image, frozen data splits, logged seeds
- [ ] Run experiment batch 1
- [ ] **Done when:** a clean machine reproduces batch 1 within tolerance

### Month 21 (Jun 2028): Main experiments
- [ ] Run the full matrix: features × embedding models × index types × load levels
- [ ] Collect quality, latency percentiles, memory
- [ ] Statistical analysis and final figures
- [ ] **Done when:** all planned experiments are complete

### Month 22 (Jul 2028): Write
- [ ] Abstract, introduction, related work, method, results, discussion, threats to validity, conclusion
- [ ] Two review rounds
- [ ] **Done when:** a complete draft has been reviewed by someone other than you

### Month 23 (Aug 2028): Portfolio
- [ ] Clean the repos; write 3 case studies (FieldSync reliability, Audio ML Search, capstone)
- [ ] 3 technical posts and a demo video
- [ ] CV tailored for backend, systems, and audio-ML roles
- [ ] **Done when:** GitHub profile and portfolio are live and every README has real numbers

### Month 24 (Sep 2028): Launch + buffer week
- [ ] System-design practice using your own systems; SQL and concurrency interview practice
- [ ] 2 algorithm problems a week (start in July)
- [ ] 10 targeted applications; final capstone submission and defense
- [ ] **Done when:** the gate below passes

### Gate 4
- [ ] Capstone report submitted
- [ ] Portfolio live
- [ ] 10 applications sent
- [ ] You can explain every number in your report

---

# Final Completion Checklist

## Measurement & Performance
- [ ] k6 load testing (steady, ramp, spike, soak)
- [ ] Latency percentiles (p50/p95/p99)
- [ ] Profiling and flame graphs
- [ ] Before/after evidence for every optimization

## Databases
- [ ] PostgreSQL query plans and indexes
- [ ] Transactions and isolation levels
- [ ] Optimistic concurrency (row versions)
- [ ] pgvector

## Concurrency & Distributed Systems
- [ ] Async and background workers in .NET
- [ ] Postgres-backed job queue
- [ ] Idempotency and the outbox pattern
- [ ] Replicas, replication, consistency trade-offs

## Testing & Reliability
- [ ] xUnit + Testcontainers + CI
- [ ] Timeouts, retries, circuit breakers
- [ ] Failure injection with Toxiproxy
- [ ] Runbooks and postmortems

## Observability
- [ ] OpenTelemetry traces
- [ ] Prometheus metrics and Grafana dashboards
- [ ] SLOs

## Audio & ML
- [ ] DSP basics (FFT/STFT, mel, MFCC, chroma)
- [ ] Evaluation (P@k, nDCG, confidence intervals)
- [ ] PyTorch basics
- [ ] Learned embeddings (PANNs, CLAP)
- [ ] FAISS and pgvector indexes
- [ ] FastAPI serving
- [ ] ONNX Runtime inference and quantization

## Research & Career
- [ ] Reproducible experiment harness
- [ ] Capstone report
- [ ] Portfolio and case studies
- [ ] 10 applications sent

---

# Core Resources

| Topic | Resource |
|---|---|
| Systems and data | [*Designing Data-Intensive Applications*](https://dataintensive.net) |
| SQL performance | [*Use The Index, Luke*](https://use-the-index-luke.com) |
| Operating systems | [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/) |
| Reliability | [Google SRE books](https://sre.google/books/) · *Release It!* (Nygard) |
| Databases (lectures) | [CMU 15-445](https://15445.courses.cs.cmu.edu) |
| Distributed systems | [MIT 6.824](https://pdos.csail.mit.edu/6.824/) · [Raft paper](https://raft.github.io/raft.pdf) |
| Performance | [Brendan Gregg](https://www.brendangregg.com) |
| DSP | [*Think DSP*](https://greenteapress.com/wp/think-dsp/) · [FMP notebooks](https://www.audiolabs-erlangen.de/resources/MIR/FMP/C0/C0.html) |
| ML | [Dive into Deep Learning](https://d2l.ai) · [PyTorch tutorials](https://pytorch.org/tutorials/) |
| Retrieval evaluation | [*Introduction to Information Retrieval*](https://nlp.stanford.edu/IR-book/) ch. 8 |
| Vector search | [FAISS wiki](https://github.com/facebookresearch/faiss/wiki) · [pgvector](https://github.com/pgvector/pgvector) · [ANN-Benchmarks](https://ann-benchmarks.com) · [HNSW paper](https://arxiv.org/abs/1603.09320) |
| Audio models | [PANNs](https://arxiv.org/abs/1912.10211) · [LAION-CLAP](https://github.com/LAION-AI/CLAP) |
| Datasets | [FSD50K](https://zenodo.org/records/4060432) · [Freesound API](https://freesound.org/docs/api/) |
