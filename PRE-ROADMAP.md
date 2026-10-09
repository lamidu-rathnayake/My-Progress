# Prerequisites: Python & FastAPI

> **Scope rule:** This covers only what the 24-month roadmap assumes but does not teach. You already work in C# and SQL, so Python should take about 2–3 weeks of Monday and Wednesday evenings. Frontend is not a learning goal; the archived HTML/CSS/JavaScript material stays in `roadmaps/archive/`.

**Timing:** Python and NumPy before Month 1's spectrogram notebook (week 2). FastAPI before Month 10.

---

# Part 1: Python (needed by Month 1, week 2)

- [ ] Core syntax: variables, types, functions, control flow, comprehensions
- [ ] Modules and packages: organizing and importing code
- [ ] Classes and basic OOP: defining types and creating objects
- [ ] Type hints: annotating parameters, return values, and variables
- [ ] Virtual environments and packages: `uv` (or `venv` + `pip`)
- [ ] NumPy basics: arrays, shapes, slicing, broadcasting, vectorized math
- [ ] Jupyter or VS Code notebooks and Matplotlib plots
- [ ] File handling: `pathlib`, reading and writing CSV and NumPy files

**Done when:** you can load an audio file in a notebook, compute something with NumPy, and plot it.

---

# Part 2: Testing in Python (needed by Month 10)

- [ ] pytest basics: test functions, assertions, fixtures
- [ ] Running tests in GitHub Actions

---

# Part 3: FastAPI (needed by Month 10)

- [ ] Pydantic models: request and response validation
- [ ] Path operations: `@app.get`, `@app.post`
- [ ] Path, query, and body parameters
- [ ] Dependency injection: sharing logic such as DB sessions
- [ ] Async endpoints: `async def` vs sync handlers, and when each is right
- [ ] File uploads: receiving audio files
- [ ] Background tasks: work that continues after the response
- [ ] Automatic OpenAPI docs
- [ ] Endpoint testing with `TestClient`
- [ ] CORS: letting the small React UI call the API

**Done when:** you can run a FastAPI service with an upload endpoint, a test for it, and a call from the browser UI.

---

# Prerequisite Milestone

- [ ] Comfortable writing Python functions, classes, and type hints
- [ ] Comfortable with NumPy arrays and plotting
- [ ] Can run a FastAPI service with at least one working endpoint
- [ ] Can write and run pytest tests

---

# Resources

| Topic | Resource |
|---|---|
| Python | [Official Python tutorial](https://docs.python.org/3/tutorial/) |
| Packaging | [uv docs](https://docs.astral.sh/uv/) |
| NumPy | [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html) |
| Testing | [pytest docs](https://docs.pytest.org/) |
| FastAPI | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) |
| Validation | [Pydantic docs](https://docs.pydantic.dev) |
