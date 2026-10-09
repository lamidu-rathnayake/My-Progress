# 🎵 Systems & Audio-ML Engineering

> A 24-month journey into **backend reliability, performance engineering, and audio machine learning**.

**Timeline:** October 2026 → September 2028  
**Stack:** C# · Python · SQL (+ a small TypeScript UI)

## 🎯 Goal

Become a software engineer who goes beyond generating code: someone who understands how systems behave under load, how failures happen, how to measure performance, and how to build dependable software.

**Specialization:** backend systems, distributed systems, reliability, and performance engineering, with **audio ML** as the differentiating specialty.

**Target:** backend, systems, and audio-ML engineering roles (including audio and music-tech teams such as Spotify).

**Guiding principle:** fundamentals → working system → measurement → optimization → research.

## 🧩 Three Connected Projects

| Project | Purpose | Main stack |
|---|---|---|
| 🏦 **FieldSync** | Work project. Builds production-engineering skills: reliability, testing, observability. *Not part of the audio portfolio.* | C# (.NET 10) · ASP.NET Core · EF Core · PostgreSQL · React |
| 🎧 **Audio ML Search** | Main personal project. Find similar samples and loops **by sound**, not by filename. | Python · FastAPI · PyTorch · librosa · FAISS · pgvector |
| 🔬 **Research Capstone** | A focused engineering investigation built on Audio ML Search, not a fourth unrelated project. | Reproducible experiments · written report |

## 📦 Repositories

| Repository | What it holds | Status |
|---|---|---|
| [`<progress-repo>`](https://github.com/lamidu-rathnayake/My-Progress) | This repo: roadmap, logs, benchmarks, reports | 🟢 Active |
| [`fieldsync`](https://github.com/lamidu-rathnayake/MCS-FieldSync) 🔒 | FieldSync solution: `FieldSync.Core`, `FieldSync.Infrastructure`, `FieldSync.API`, plus the web client | 🚧 In development (Increment 1) |
| [`audio-ml-search`](https://github.com/lamidu-rathnayake/My-Progress) | Audio ML Search app and its experiments | ⏳ Planned (v1 build starts Month 7) |

> FieldSync is a private repo. Only sanitized reports and benchmark numbers are copied into this one.

## 🏗️ Audio ML Search Architecture

```text
React UI (upload · play · results)
        ↓
Python + FastAPI service
  ├── Ingestion → ffmpeg → features / embeddings
  ├── Search    → FAISS · pgvector
  └── PostgreSQL + pgvector
        ↓
Observability: OpenTelemetry → Jaeger · Prometheus · Grafana
```

## 🧰 Tech Stack

| Layer | FieldSync | Audio ML Search |
|---|---|---|
| **Language** | C# (.NET 10), SQL | Python 3.12+, SQL |
| **Backend** | ASP.NET Core, EF Core | FastAPI |
| **Database** | PostgreSQL | PostgreSQL + pgvector |
| **Libraries** | Serilog, Polly | librosa, torchaudio, PyTorch, scikit-learn, FAISS, ONNX Runtime |
| **Testing** | xUnit, Testcontainers, BenchmarkDotNet | pytest |
| **Load & failure** | k6, Toxiproxy | k6, Toxiproxy |
| **Observability** | OpenTelemetry, Jaeger, Prometheus, Grafana | same |
| **Infrastructure** | WSL2, Docker Compose, GitHub Actions | same |

## 🗺️ 24-Month Journey

| Period | Focus | Status |
|---|---|---|
| **Phase 1 · Months 1–6** (Oct 2026 – Mar 2027) | Foundations: databases, concurrency, testing, failure handling. FieldSync reliability results and an audio-similarity baseline. | 🚧 **Current:** FieldSync Increment 1 in development |
| **Phase 2 · Months 7–12** (Apr – Sep 2027) | Audio ML Search v1: audio processing, feature baseline vs learned embeddings, vector search, first complete app. | ⏳ Upcoming |
| **Phase 3 · Months 13–18** (Oct 2027 – Mar 2028) | Measurement & optimization: retrieval quality, latency, observability, failure tests, inference benchmarks. | ⏳ Upcoming |
| **Phase 4 · Months 19–24** (Apr – Sep 2028) | Capstone research, reproducible experiments, report, portfolio, job applications. | ⏳ Upcoming |

## ⏱️ Weekly Rhythm

**Mon** Theory A (systems, DB, reliability) · **Tue** Build FieldSync · **Wed** Theory B (audio, ML) · **Thu** Build Audio ML Search · **Fri** University work · **Sat** Lectures, then off · **Sun** Lectures, then weekly review

## 📁 Repository

```text
docs/              → ADRs, learning log, experiment log, reports
labs/              → small learning experiments (DSP, SQL, concurrency)
audio-ml-search/   → main personal project
benchmarks/        → load tests, latency and quality results
research/          → capstone protocol, experiments, report
books/             → study references
roadmaps/          → planning material
```

## 🚦 Phase Gates

- [ ] **Gate 1 · Month 6:** FieldSync Reliability Report v1 + audio baseline results
- [ ] **Gate 2 · Month 12:** Audio ML Search v1.0 runs from a clean clone + Evaluation Report v1
- [ ] **Gate 3 · Month 18:** Engineering Report v1 (observability, load tests, optimizations, failure tests)
- [ ] **Gate 4 · Month 24:** Capstone submitted · portfolio live · 10 applications sent

## 📊 Current Progress

**Month:** 1 / 24  
**Stage:** Phase 1 · Foundations  
**Currently developing:** 🚧 FieldSync · Increment 1 (scanner inbound/outbound, issues and jobs, scanner swap, role-based access, offline accessibility)  
**Current focus:** Measure before you optimize  
**Next Gate:** Gate 1 · Month 6

> **Build it. Measure it. Understand it. Defend it.**
