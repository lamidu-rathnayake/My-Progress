# Audio & Applied Machine Learning Engineering — 24-Month Roadmap

> **Timeline:** October 2026 – September 2028  
> **Career identity:** Applied ML Engineer, specializing in audio and music information retrieval  
> **Primary outcome:** one dependable audio-similarity application, supported by rigorous evaluation and a university research capstone.

## 1. The focus

I will build depth in **general machine learning engineering** and specialize through **audio ML**. The goal is to learn the end-to-end ML workflow: prepare data, establish baselines, train or apply models, evaluate them correctly, serve inference, profile performance, and communicate results.

### What is in scope

- Python programming and numerical computing
- Mathematics and statistics needed to understand ML
- Classical machine learning and model evaluation
- Deep-learning fundamentals with PyTorch
- Digital audio fundamentals and DSP
- Audio embeddings, similarity retrieval, and ranking
- Reproducible experiments, inference, testing, and profiling
- Enough FastAPI, SQL, Docker, and UI work to demonstrate the ML system

## 2. Core technology stack

Keep the stack small. Add a tool only when a concrete project requirement or experiment justifies it.

| Area | Primary choice | Scope |
|---|---|---|
| Language | Python 3.12+ or a currently supported Python version compatible with project dependencies | Learn Python deeply enough to write maintainable ML code |
| Numerical work | NumPy, SciPy, Matplotlib | Arrays, vectorized operations, transforms, analysis, plotting |
| Tabular/data handling | pandas when useful | Metadata and evaluation tables; do not use it where NumPy is simpler |
| Classical ML | scikit-learn | Baselines, preprocessing, model selection, metrics, simple models |
| Audio analysis | librosa + soundfile; ffmpeg for conversion when needed | Loading, resampling, feature extraction, visualization |
| Deep learning | PyTorch | Tensors, datasets, training loops, inference, profiling |
| Pretrained audio models | Hugging Face Transformers / an appropriate pretrained audio model | Begin with one model and understand its limits before comparing others |
| Evaluation | Python, scikit-learn metrics where suitable, small curated human-judged query set | Retrieval quality and reproducibility |
| Similarity search | Exact cosine-similarity baseline first; PostgreSQL + pgvector for the first database-backed version | Add FAISS only if a benchmark or research question justifies a comparison |
| API | FastAPI + Pydantic | Introduce only when the local pipeline works |
| Testing | pytest | Test preprocessing, metrics, APIs, and data-integrity rules |
| Storage | Filesystem for source audio + PostgreSQL for metadata/results; pgvector when needed | Keep raw audio, metadata, and derived vectors clearly separated |
| Reproducibility | Git, requirements/lock file, configuration files, fixed splits and logged seeds | Every result should be rerunnable |
| Delivery | Docker Compose, GitHub Actions | Reproducible local setup and automated tests |
| UI | Small React + TypeScript client | Upload, search, playback, and results only |
| Profiling | Python profilers, timing scripts, browser profiler when needed | Measure before optimizing |

**Audio dependency note:** make `librosa` and `soundfile` the initial audio-analysis tools. Do not make `torchaudio` a mandatory foundation; its official documentation says it entered a maintenance phase starting in version 2.9 and points users toward TorchCodec for I/O. Add TorchCodec or other packages only when a chosen model or pipeline needs them. Check compatibility when creating the environment.

## 3. Concepts to master, in order

### Programming and data

- Functions, modules, packages, exceptions, type hints and basic classes
- Virtual environments, dependency management, file paths and serialization
- NumPy arrays, dimensions, slicing, broadcasting and vectorized computation
- Git, debugging, testable functions and readable project structure

### Mathematics and general ML

- Vectors, matrices, dot products, norms, cosine similarity and matrix multiplication
- Probability, distributions, sampling, mean/variance and confidence intervals
- Derivatives, gradients, gradient descent and the intuition behind optimization
- Supervised versus unsupervised learning; classification versus regression
- Train/validation/test splits, data leakage, class imbalance and baselines
- Loss functions, overfitting, regularization, learning curves and model selection
- Appropriate metrics and honest error analysis

### Audio and retrieval

- Samples, sample rate, channels, bit depth, PCM, amplitude, clipping and dBFS
- Frequency, harmonics, time versus frequency domain, aliasing and resampling
- FFT, window functions, STFT, spectrograms and mel-spectrograms
- RMS, spectral centroid, spectral bandwidth, MFCCs and chroma
- Audio embeddings, vector normalization, cosine similarity and nearest neighbours
- Retrieval evaluation: Precision@k, Recall@k, nDCG@k, plus human listening checks
- Dataset provenance, licensing, duplicates, source-aware splits and evaluation leakage

### ML engineering

- Deterministic preprocessing and repeatable feature/embedding extraction
- Dataset and experiment versioning, configuration, fixed splits and logged seeds
- Inference versus training; batching and CPU/memory trade-offs
- API input validation, upload-size limits, corrupt-file handling and clear errors
- Profiling and latency percentiles; optimize measured bottlenecks only
- Reproducible deployment, tests and technical reporting

## 4. The 24-month plan

Every month has a deliverable. If a `Done when` condition is not met, extend the milestone instead of rushing forward. University exams and required coursework take priority; adjust the calendar when necessary.

# Phase 1 — Foundations and a credible baseline

## Month 1 — October 2026: Python and audio inspection

- [ ] Set up Python environment, Git repository, notebooks, and dependency file.
- [ ] Learn Python functions, modules, paths, exceptions, type hints, and virtual environments.
- [ ] Load an audio file with `librosa`/`soundfile` and inspect its sample rate, channels, and duration.
- [ ] Plot a waveform and spectrogram using Matplotlib.
- [ ] Keep a small source-audio manifest with origin and license/usage notes.
- [ ] **Done when:** a cleanly runnable notebook loads an audio file, explains its shape/rate, and produces both plots.

## Month 2 — November 2026: NumPy and DSP fundamentals

- [ ] Learn NumPy shapes, slicing, broadcasting, vectorization and basic linear algebra.
- [ ] Understand PCM samples, amplitude, sample rate, channels, resampling and clipping.
- [ ] Study the DFT/FFT, windowing, STFT and spectrograms at an introductory level.
- [ ] Calculate an STFT with NumPy/SciPy and compare it with a library implementation using matching settings.
- [ ] **Done when:** the notebook explains meaningful parameter choices and the two STFT results agree within a documented tolerance.

## Month 3 — December 2026: Statistics and feature baseline

- [ ] Study descriptive statistics, distributions, sampling, vectors, dot products and cosine similarity.
- [ ] Extract a small set of interpretable features: RMS, spectral centroid, MFCCs and chroma where appropriate.
- [ ] Save derived features with a manifest connecting each result to the source file and preprocessing configuration.
- [ ] Implement exact cosine-similarity search over the feature vectors.
- [ ] **Done when:** a query returns ranked similar sounds and the top results can be inspected and judged by listening.

## Month 4 — January 2027: General ML fundamentals

- [ ] Learn the standard ML workflow using scikit-learn: dataset, baseline, split, fit, predict and evaluate.
- [ ] Complete one small classification or regression exercise as a lab, not a separate portfolio project.
- [ ] Learn leakage, overfitting, regularization, cross-validation and why baselines matter.
- [ ] Define the first version of “similar” for the audio task and create a modest human-judged query set.
- [ ] **Done when:** one reproducible ML lab and the first documented audio-search evaluation run exist.

## Month 5 — February 2027: Evaluation and data quality

- [ ] Implement Precision@k, Recall@k and nDCG@k for ranked retrieval results.
- [ ] Record query-level results, not just aggregate averages; listen to good and bad matches.
- [ ] Check for duplicates, inconsistent formats, source leakage and unlicensed/untracked files.
- [ ] Add pytest tests for feature extraction, similarity ranking and metrics.
- [ ] **Done when:** the baseline runs from one documented command and produces a metric table plus error-analysis notes.

## Month 6 — March 2027: Baseline gate and buffer

- [ ] Clean up the audio notebook and pipeline so another person can follow the steps.
- [ ] Record the dataset, preprocessing, feature choices, metric definitions and known limitations.
- [ ] Write an initial baseline report and identify the main unanswered question.
- [ ] **Gate 1:** reproducible DSP/feature baseline, evaluation query set, automated tests, and a short report.

# Phase 2 — Applied ML and Audio ML Search v1

## Month 7 — April 2027: PyTorch foundations

- [ ] Learn tensors, tensor shapes, datasets, DataLoaders, autograd, losses, optimization and model checkpoints.
- [ ] Build a small neural network on a manageable dataset to understand the full training loop.
- [ ] Compare a simple scikit-learn baseline with a small neural model where the task allows a fair comparison.
- [ ] **Done when:** you can explain the data flow, loss, optimizer, validation step and saved model without relying only on a tutorial.

## Month 8 — May 2027: Pretrained audio embeddings

- [ ] Study embeddings and how pretrained audio models convert audio into vectors.
- [ ] Select **one** suitable pretrained audio embedding model and document why it fits the task.
- [ ] Extract and save embeddings for the curated audio set.
- [ ] Evaluate the embedding baseline against the handcrafted-feature baseline on the same queries/splits.
- [ ] Listen to failure cases and document where the model does not match musical relevance.
- [ ] **Done when:** a comparable baseline-vs-embedding table and error analysis exist.

## Month 9 — June 2027: Retrieval and vector search

- [ ] Understand exact nearest-neighbour search and why approximate nearest-neighbour indexes trade some recall for speed.
- [ ] Store metadata and embeddings cleanly; implement the first PostgreSQL + pgvector search path.
- [ ] Compare pgvector results with the exact baseline for correctness and query latency.
- [ ] Add FAISS only if measured data size or the research question warrants a fair comparison.
- [ ] **Done when:** a benchmark records retrieval quality, latency, data size, hardware and configuration.

## Month 10 — July 2027: Serve the model

- [ ] Learn FastAPI, Pydantic request/response models, file uploads, validation and endpoint testing.
- [ ] Add a small API for ingestion/status and similarity search.
- [ ] Add size limits, supported-format checks, timeouts and clear errors for corrupt or silent audio.
- [ ] Use pytest for unit/API tests and Docker Compose for reproducible local startup.
- [ ] Build only the React + TypeScript screens necessary for upload, playback, search and results.
- [ ] **Done when:** a clean clone can run the end-to-end app using documented commands and automated tests.

## Month 11 — August 2027: Musical relevance

- [ ] Investigate whether tempo/BPM or chroma/key information helps for loop search; treat these as candidate signals, not guaranteed improvements.
- [ ] Create a human-judged query set with documented labels and judgement instructions.
- [ ] Compare baseline ranking with one carefully defined reranking/filtering approach.
- [ ] Check that added rules do not damage other types of searches.
- [ ] **Done when:** results show the effect of the change, per-query failures, and limitations.

## Month 12 — September 2027: v1 release and buffer

- [ ] Freeze a v1 scope; do not add features that are not necessary to demonstrate search.
- [ ] Improve setup instructions, architecture diagram, tests, sample data instructions and limitations.
- [ ] Record a short demo and tag `v1.0`.
- [ ] **Gate 2:** a reproducible end-to-end application with feature-vs-embedding evaluation and search benchmark.

# Phase 3 — ML system quality and optimization

## Month 13 — October 2027: Experimental quality

- [ ] Audit data splits, duplicates, evaluation judgements and metric implementation.
- [ ] Fix the evaluation set and define which changes would count as meaningful improvement.
- [ ] Add experiment configurations and logs so every result is linked to code, data and settings.
- [ ] **Done when:** rerunning the same experiment yields results within a documented tolerance.

## Month 14 — November 2027: Profile before optimizing

- [ ] Measure end-to-end latency, embedding-extraction time, query latency, memory and throughput on stated hardware.
- [ ] Separate cold-start, ingestion and search timings.
- [ ] Profile Python and database operations; identify the biggest demonstrated bottleneck.
- [ ] Change one bottleneck at a time and rerun the same workload.
- [ ] **Done when:** one before/after report explains the workload, change, result and trade-offs.

## Month 15 — December 2027: Controlled experiments

- [ ] Compare a small number of justified choices: one alternative embedding model, pooling/normalization, or reranking.
- [ ] Keep data, query set and evaluation procedure fixed across comparisons.
- [ ] Report per-query results and uncertainty where feasible; avoid overclaiming small differences.
- [ ] **Done when:** an experiment table supports a clear conclusion and notes negative results.

## Month 16 — January 2028: Inference optimization

- [ ] Understand model inference, batching, thread settings and CPU/memory trade-offs.
- [ ] Determine whether the chosen model is actually a latency or resource bottleneck.
- [ ] If useful, compare PyTorch inference with ONNX Runtime and validate numerical/output differences.
- [ ] Quantization is optional and should be attempted only if there is a clear benefit to test.
- [ ] **Done when:** performance and retrieval quality are reported together; keep the simplest version that meets the measured need.

## Month 17 — February 2028: Robustness and data failure modes

- [ ] Test corrupt, unsupported, silent, extremely short and oversized audio files.
- [ ] Test interrupted ingestion, database unavailability, invalid requests and repeated submissions.
- [ ] Add safe limits, cleanup behavior, actionable errors and tests for the expected outcomes.
- [ ] **Done when:** the robustness suite is repeatable and every case has an expected/observed result.

## Month 18 — March 2028: ML engineering report and buffer

- [ ] Document the end-to-end pipeline, model choice, evaluation, profiling, failure handling and remaining limits.
- [ ] Choose the final baseline/system configuration based on evidence.
- [ ] Avoid replicas, sharding or complex infrastructure unless the measured research question requires them.
- [ ] **Gate 3:** ML engineering report with quality, latency/resource results, failure tests and justified optimizations.

# Phase 4 — Research, capstone and career preparation

## Month 19 — April 2028: Research protocol

- [ ] Review a focused set of papers on audio embeddings, music information retrieval and retrieval evaluation; write short notes for each.
- [ ] Propose a question such as: “How do handcrafted audio features and pretrained embeddings trade retrieval quality against query latency and resource cost for sample search?”
- [ ] Define hypotheses, baselines, data/source rules, splits, metrics, compute limits and threats to validity.
- [ ] Discuss the plan with the university supervisor early and align it with capstone requirements.
- [ ] **Done when:** the research protocol is approved or feedback has been incorporated.

## Month 20 — May 2028: Reproducible experiment runner

- [ ] Build one experiment command that reads configuration and writes machine-readable results.
- [ ] Pin dependencies, freeze query/data splits, record seeds and capture hardware/software details.
- [ ] Run a small pilot to discover bugs and estimate experiment cost before the full batch.
- [ ] **Done when:** a clean environment can reproduce the pilot within a documented tolerance.

## Month 21 — June 2028: Main experiments

- [ ] Run only the experiment matrix approved in the protocol; do not keep adding models and indexes.
- [ ] Collect retrieval metrics, latency percentiles and resource measurements.
- [ ] Analyze errors and uncertainty; retain negative results.
- [ ] **Done when:** the planned experiments are complete or deviations are clearly documented.

## Month 22 — July 2028: Write the capstone

- [ ] Write the question, related work, methods, results, discussion, limitations and conclusion.
- [ ] Distinguish measured findings from interpretations and future work.
- [ ] Ask a supervisor/peer for feedback and complete at least two revision passes where the schedule permits.
- [ ] **Done when:** the complete draft has been reviewed and the figures can be regenerated.

## Month 23 — August 2028: Portfolio and applications

- [ ] Clean the repository; document how to reproduce the demo and experiments.
- [ ] Publish two or three case studies: audio retrieval, ML evaluation, and performance/robustness findings.
- [ ] Prepare a CV for junior ML, applied ML, Python/ML software and audio-related roles.
- [ ] Begin targeted applications before the final month; do not wait until everything feels perfect.
- [ ] **Done when:** the project is reviewable by someone who was not involved in building it.

## Month 24 — September 2028: Finish and transition

- [ ] Submit and defend the capstone according to university requirements.
- [ ] Rehearse explaining the dataset, model, metrics, limitations and engineering trade-offs.
- [ ] Review core ML, Python, SQL, algorithms and model-evaluation concepts for interviews.
- [ ] **Gate 4:** capstone submitted, application runs reproducibly, reports are public where allowed, and targeted applications are underway.

## 5. Weekly rhythm

Aim for approximately **6–8 hours per week of independent learning and personal-project work**, excluding university classes, assignments and employment. This is a starting budget, not a fixed quota during exams.

- **Session A — 1.5–2 hours:** math, ML or DSP theory tied to the current milestone.
- **Session B — 2–3 hours:** implement the current project milestone.
- **Session C — 1.5–2 hours:** tests, evaluation, debugging or profiling.
- **Weekly review — 30–60 minutes:** update the learning log, record blockers and plan the next concrete task.

Do not study every technology every week. Study what the current milestone needs. During exams or high-workload weeks, maintain a smaller note/review habit and extend the milestone.

## 6. Phase gates

- [ ] **Gate 1 — March 2027:** audio feature baseline, curated query set, metrics, tests and reproducible report.
- [ ] **Gate 2 — September 2027:** Audio ML Search v1, runnable from a clean clone, with pretrained embeddings and initial evaluation.
- [ ] **Gate 3 — March 2028:** quality/performance report, robustness tests and justified inference/system changes.
- [ ] **Gate 4 — September 2028:** completed capstone, reproducible experiments, professional portfolio and targeted job applications.

## 7. Resources

Use one primary resource at a time; do not turn the resource list into a second curriculum.

| Topic | Resource |
|---|---|
| Python | [Official Python Tutorial](https://docs.python.org/3/tutorial/) |
| NumPy | [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html) |
| Statistics / DSP intuition | [Think DSP](https://greenteapress.com/wp/think-dsp/) |
| Music information retrieval | [FMP notebooks](https://www.audiolabs-erlangen.de/resources/MIR/FMP/C0/C0.html) |
| Classical ML | [scikit-learn Getting Started](https://scikit-learn.org/stable/getting_started.html) |
| Deep learning | [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) |
| Audio transformers | [Hugging Face Audio Course](https://huggingface.co/learn/audio-course/en/chapter0/introduction) |
| Audio analysis | [librosa documentation](https://librosa.org/doc/latest/index.html) |
| Testing | [pytest documentation](https://docs.pytest.org/) |
| API, when Month 10 arrives | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) |
| Retrieval evaluation | [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/) |
| Vector storage, when justified | [pgvector](https://github.com/pgvector/pgvector) |

## 8. Monthly review template

Copy this into `docs/monthly-reviews/YYYY-MM.md`:

```markdown
# Monthly Review — YYYY-MM

## Planned outcome
- 

## What I built or tested
- 

## Evidence
- Reproduction command:
- Dataset / configuration:
- Metrics or screenshots:

## What I learned
- 

## What failed or remains uncertain
- 

## Next month's single most important outcome
- 
```

## Final rule

**One primary specialty, one main personal project, one research thread.** Learn general ML deeply enough to understand the methods and trade-offs; use audio as the domain in which you demonstrate that understanding. Add technologies in response to a learning objective, experiment, or measured bottleneck—not because they appear in a fashionable stack.
