# Systems & Embedded Software Engineering → Robotics & Intelligent Machines
## Career Strategy, University Alignment, Self-Study Roadmap & Employer Watchlist
**Planning period:** October 2026 – September 2028  
**Version:** 1.0 — 22 October 2026  
**Status:** Primary career direction selected; specialization within robotics/industrial/edge systems remains open  
**Context:** SLTC Research University, Software Engineering undergraduate; professional experience in banking application support.

> **North star:** Become a software engineer capable of designing, implementing, debugging, testing, and integrating reliable software that interacts with real devices, sensors, operating systems, and intelligent machines.

---

## Contents
1. Career decision and realistic outcomes
2. What changes from earlier roadmaps
3. Target skills and engineering knowledge map
4. University modules: semester-by-semester alignment
5. Detailed October 2026–September 2028 plan
6. Self-study curriculum and learning method
7. Projects and capstone strategy
8. Tools and environment
9. Companies to follow: Sri Lanka and worldwide
10. LinkedIn, GitHub, and social presence
11. Internship and graduate job-search strategy
12. Weekly operating system and checkpoints
13. Risks, exclusions, and decision rules
14. References and source notes

---

# 1. Career decision and realistic outcomes

## Primary career path — LOCKED
**Systems & Embedded Software Engineering → Robotics & Intelligent Machines**

This is a **direction for building expertise**, not a guarantee that the first job title must be “Robotics Engineer.”

**Target entry-level job titles:**
- Graduate / Associate Embedded Software Engineer
- Junior Firmware Engineer
- Junior C/C++ Software Engineer
- Systems Software Engineer
- Embedded Linux Engineer (junior or trainee)
- IoT / Device Software Engineer
- Robotics Software Engineer (where skills and openings align)
- Software Development Engineer in Test (embedded/system integration)
- Graduate Software Engineer on device, platform, automotive, or industrial products

**Adjacent pathways to evaluate in 2027–2028:**
1. Robotics software and autonomy — ROS 2, perception, control, navigation.
2. Industrial/real-time systems — controllers, field protocols, monitoring, reliability.
3. Edge AI — embedded inference, sensor processing, computer vision.
4. Core systems software — Linux, networking, C++, operating systems, device software.

**Employability safety net:** C#/.NET, ASP.NET Core, PostgreSQL, React, and TypeScript remain useful professional skills. They are a secondary employment route and integration layer, **not** the main self-study priority.

**By September 2028, aim to demonstrate:**
- Confident Python and modern C++ programming, with practical C fundamentals.
- Linux development, debugging, processes, memory, threads, and networking.
- Microcontroller and embedded-interface fundamentals.
- Real sensor data acquisition and state-machine/control logic.
- Unit, integration, simulation, and failure-mode testing.
- One integrated, reproducible device/robotics-oriented capstone.
- Clear technical writing and a portfolio showing engineering trade-offs.

**Reality check:** A Software Engineering degree is relevant to many embedded/software roles, but some electronics-heavy, control, semiconductor, and robotics positions may prefer EE/ECE/mechatronics qualifications or specific experience. Use projects and internships to demonstrate practical competence. No discipline is immune to AI-driven changes; focus on durable reasoning, verification, and systems integration.

# 2. What changes from earlier roadmaps

The earlier plans contain useful material. **Retain, redirect, defer, or retire** topics rather than starting over.

| Previous roadmap component | Decision | New purpose |
|---|---|---|
| Python fundamentals, collections, functions, OOP | **KEEP / finish thoroughly** | Test tooling, simulations, data processing, robotics scripts |
| C++ | **PROMOTE to core** | Systems software, performance, robotics |
| C language | **ADD / core** | Firmware, pointers, registers, memory, hardware interfaces |
| Linux, Git, Docker | **KEEP / deepen** | Toolchains, processes, debugging, reproducibility |
| DSA and discrete mathematics | **KEEP** | Efficient algorithms, state machines, graph/search problems |
| Linear algebra, calculus, probability | **KEEP / apply** | Coordinate transforms, control, sensor uncertainty |
| Signal processing / DSP | **KEEP foundational concepts** | Sensor filtering, sampling, frequency analysis—not music production |
| Embedded systems, ESP32, RTOS, I2C/SPI/UART | **PROMOTE to core** | Hardware/software integration |
| Control theory, PID, feedback | **PROMOTE** | Reliable machine behavior |
| ROS 2, Gazebo, RViz, tf2 | **DEFER until foundations** | Robotics specialization |
| OpenCV, ML, edge inference | **KEEP later** | Intelligent perception and embedded inference |
| SLAM, Nav2, MoveIt 2 | **OPTIONAL advanced** | Only when selected capstone needs them |
| PLC, SCADA, Modbus, OPC UA | **OPTIONAL industrial branch** | Explore if factory automation becomes a preference |
| Kubernetes / complex cloud robotics | **DEFER** | Not needed for junior embedded readiness |
| LLM agents / voice control / RL | **OPTIONAL** | Not a prerequisite for engineering machines |
| Audio production environment / browser DAW | **RETIRE as flagship** | Historical learning only; reusable DSP/performance ideas |
| Audio-ML similarity search research | **RETIRE as default capstone** | Reuse experimentation methodology for sensor/edge AI |
| FieldSync enterprise application | **KEEP but reclassify** | Production engineering, reliability, API, database, offline sync evidence |
| React / TypeScript | **MAINTAIN** | Device dashboards, diagnostics, engineering tools |
| ASP.NET Core / C# | **MAINTAIN** | Telemetry services, integration, employability |

**Important reconciliation:** One older semester checklist used **FastAPI + SQLAlchemy** for FieldSync, whereas later project decisions use **ASP.NET Core + PostgreSQL + React PWA**. For FieldSync, keep the *actual current project stack*; learn Python/FastAPI separately where it advances Python fundamentals. Do not rebuild FieldSync simply to match an old checklist.

## New priority order
1. University modules and grades.
2. Python mastery, then C/C++ and Linux systems.
3. Electronics + microcontrollers + embedded interfaces.
4. Control, sensor data, concurrency, reliability.
5. Robotics software and optional intelligent perception.
6. Full-stack maintenance only as needed for work/projects.

---

# 3. Core engineering knowledge map

## A. Programming
**Python:** collections; methods; iteration; comprehensions; functions; parameters and scope; modules; packages; errors; OOP; dataclasses; enums; type hints; files; context managers; generators; testing; NumPy; logging; serial data; basic async programming.

**C:** compilation; primitive types; pointers; arrays; structs; bitwise operations; memory layout; stack/heap concepts; `const`/`volatile` concepts; headers; linker basics; undefined behavior; basic embedded programming patterns.

**Modern C++:** values/references; ownership and lifetime; RAII; standard containers and algorithms; classes; smart pointers; move semantics; templates basics; exceptions/error models; threading; synchronization; CMake; testing; profiling.

**Linux/systems:** shell; permissions; processes; signals; files/descriptors; sockets; threads; memory; system calls; compilation/linking; GDB; sanitizers; `strace`; logging; SSH; basic networking.

## B. Hardware and embedded fundamentals
- Voltage/current/resistance; digital vs analog signals; logic levels.
- Microcontroller vs single-board computer; GPIO, ADC, PWM, timers, interrupts.
- UART, I2C, SPI; basic CAN awareness.
- Sensors, calibration, sampling, noise, debouncing, encoders.
- State machines; watchdog concepts; deterministic timing; RTOS tasks and scheduling.
- Datasheet reading, pin maps, schematics, fault handling, hardware-in-the-loop testing.
- Use low-voltage educational hardware and simulations; physical power systems, high-current motors, mains wiring, and industrial equipment require appropriate professional supervision and safety controls.

## C. Mathematics and control
- Algebra/trigonometry; vectors/matrices; coordinate systems and rotations.
- Derivatives/integrals; numerical differentiation/integration.
- Probability, Gaussian noise, covariance, estimation basics.
- Sampling, filtering, FFT concepts for sensor signals.
- Open/closed-loop systems; PID; response time; overshoot; stability intuition.
- Later: Jacobians, kinematics, Kalman filters, path planning.

## D. Robotics and intelligence (later)
- ROS 2 nodes/topics/services/actions; URDF; RViz; simulation; `tf2`.
- Sensor fusion; odometry; localization; navigation.
- OpenCV and camera geometry.
- ML inference at the edge; latency/memory/performance evaluation.
- Select advanced topics based on a concrete project, not trend-following.

---

# 4. University module alignment

> **Source distinction:** Module names/codes below come from your previously shared university-module roadmap, not a fresh verification against an official SLTC handbook. The skill mappings and project ideas are recommendations. Confirm semester availability, electives, assessment rules, and syllabus details with SLTC.

## Year 3, Semester 1 — next semester
**Main objective:** Become a more disciplined software engineer while preparing for systems and embedded study.

| Module | Foundation it develops | Application to chosen path | Suggested evidence |
|---|---|---|---|
| **CCS2360 — Technology Challenge Competition** | Rapid prototyping, teamwork, presentation | Prototype a simulated sensor-driven machine/robot behavior | Demo, requirements, design log |
| **CCS3300 — Software Architecture** | Components, interfaces, quality attributes, trade-offs | Separate sensor input, control logic, hardware abstraction, logging, UI | Component diagram + architecture decision records |
| **CCS3310 — Software Engineering Methods** | Requirements, lifecycle, planning, stakeholder needs | Write observable, testable machine-behavior requirements | User stories, acceptance criteria, backlog |
| **CCS3311 — Software Quality Assurance** | Test plans, defect analysis, verification | Unit-test control logic and simulated sensor failures | Automated tests, coverage notes, defect log |
| **CCS3356 — Natural Language Processing** *(listed as elective in an earlier plan)* | Text processing, representations, evaluation | General AI literacy; optional human-machine interfaces, log classification | Small NLP assignment; avoid making it your main specialization |

### What to self-study alongside Y3S1
**Must study**
- [ ] Finish Python collections, methods, functions, scope, exceptions, modules.
- [ ] Python OOP, type hints, testing, debugging, file handling.
- [ ] Basic C syntax and compilation; pointers only after memory fundamentals.
- [ ] Linux terminal, process/file concepts, Git workflows.
- [ ] Boolean algebra, binary/hex, bitwise operators.
- [ ] Vectors, basic algebra, graphs, introductory probability.

**Useful but secondary**
- [ ] React/TypeScript maintainability and performance through existing projects.
- [ ] ASP.NET Core architecture, error handling, and integration testing through FieldSync.
- [ ] Introductory electronics via safe simulation and low-voltage learning materials.

**Recommended semester project:** **Virtual Sensor-Driven Controller**
- Simulate distance/temperature/position inputs in Python.
- Implement a deterministic state machine (`IDLE`, `RUNNING`, `OBSTACLE`, `FAULT`).
- Write tests for noisy readings, invalid values, timeouts, and state transitions.
- Produce requirements, an architecture diagram, test results, and a short demonstration.
- Optional React dashboard only **after** control logic and tests work.

**Y3S1 exit criterion:** You can explain software architecture, implement clean Python control logic, test failure cases, and demonstrate foundational C/Linux learning.

## Year 3, Semester 2
**Modules from the earlier roadmap:**
- **CCS3302 — Introduction to Research Methods**
- **CCS3313 — Advanced Software Design**
- **SMA2307 — Discrete Mathematics**
- **CCS4340 — Machine Learning**
- **SMA2202 — Linear Algebra**

| Module | Connection to your path |
|---|---|
| Research Methods | Design measurable experiments; compare sensor filters, controllers, or runtimes |
| Advanced Software Design | Robust C++ component boundaries, interfaces, ownership, testability |
| Discrete Mathematics | State machines, graphs, logic, search, algorithms |
| Machine Learning | Model evaluation, generalization, data leakage; later edge perception |
| Linear Algebra | Coordinate frames, rotations, transformations, robot geometry |

**Self-study:** modern C++, CMake, GDB, DSA, Linux processes/threads, microcontroller basics, GPIO, UART/I2C/SPI concepts, simple filtering.

**Semester output:** a well-tested C++ simulation or microcontroller-based low-voltage sensing prototype with a benchmark/test report.

## Year 4, Semester 1
**Modules from the earlier roadmap:**
- **CCS3301 — Capstone Project Part 1**
- **CCS3440 — Artificial Intelligence**
- **IHM1301 — Human Behavior and Ethics**
- **CCS4310 — Deep Learning**
- **CCS4353 — Internet of Things**

**Connections:**
- Capstone Part 1 → choose a feasible embedded/robotics research or engineering problem.
- AI/Deep Learning → perception, classification, edge inference when justified.
- Ethics → safe and responsible machine behavior, privacy, human oversight.
- IoT → sensors, device communication, edge-to-server integration.

**Self-study:** RTOS scheduling, sensor interfaces, control theory, ROS 2 fundamentals, simulation, OpenCV as needed. Do not attempt SLAM + edge AI + custom hardware simultaneously.

**Semester output:** approved capstone design, initial prototype, measurable success criteria, and an evaluation plan.

## Year 4, Semester 2
**Modules from the earlier roadmap:**
- **CCS4601 — Industrial Training**
- **CCS4301 — Capstone Project Part 2**
- **CCS4354 — Tensors and Graphs (with Programming)**
- **SMA2305 — Numerical Analysis**

**Connections:**
- Industrial Training → production code, debugging, professional engineering practices.
- Capstone Part 2 → integrate, verify, benchmark, document.
- Tensors and Graphs → ML/perception and robot/path representations.
- Numerical Analysis → numerical stability, discretization, sensor processing, optimization.

**Semester output:** functioning capstone, repeatable tests, measurements, final report, and interview-ready demonstration.

---

# 5. Detailed timeline: October 2026–September 2028

## Phase 1 — Oct–Dec 2026: foundations
**Primary:** Python + software quality + C introduction + Linux + math.

- **October:** Python collection APIs, functions, problem solving; create baseline tests.
- **November:** OOP, modules, files, exceptions, typing; C syntax and compilation; Linux processes/files.
- **December:** C pointers and memory foundations; bitwise logic; controller state machine; architecture and test report.

**Deliverable:** virtual controller v1 with documented state transitions and unit tests.

## Phase 2 — Jan–Mar 2027: systems programming
- C pointers, structs, memory, compilation/linking, debugging.
- C++ classes, RAII, STL, CMake, ownership and lifetime.
- Linux processes, signals, threads, basic sockets.
- DSA practice and discrete math.

**Deliverable:** C++ sensor-data simulator with tests, build scripts, logging, and profiling notes.

## Phase 3 — Apr–Jun 2027: embedded fundamentals
- Microcontroller architecture; safe low-voltage GPIO and sensor projects.
- Timers, interrupts, ADC/PWM concepts, UART/I2C/SPI.
- Datasheets, hardware abstraction, debouncing, fault states.
- Compare blocking vs event-driven control.

**Deliverable:** documented sensor-monitoring or obstacle-detection prototype, with a simulation fallback.

## Phase 4 — Jul–Sep 2027: real-time and control
- Concurrency, race conditions, timing, RTOS basics.
- Sensor sampling/filtering and calibration.
- Feedback control and PID fundamentals.
- Failure injection and reliability testing.

**Deliverable:** controlled sensing/actuation simulation or supervised low-voltage prototype, with measured response and fault tests.

## Phase 5 — Oct–Dec 2027: robotics exploration
- ROS 2 concepts, message passing, simulation, URDF/RViz, transforms.
- Simple navigation or robot behavior in simulation.
- OpenCV fundamentals and basic sensor fusion.
- Briefly sample industrial protocols or edge inference **only** if interested.

**Deliverable:** simulated mobile-robot application. **Decision gate:** choose robotics software, embedded Linux, industrial systems, or edge AI as a narrower capstone emphasis.

## Phase 6 — Jan–Mar 2028: capstone implementation
- Finalize research question and requirements.
- Implement one well-scoped integrated system.
- Define latency, reliability, accuracy, memory, or control-performance metrics.
- Build CI tests and reproducible simulation.

**Deliverable:** capstone alpha + preliminary benchmark report.

## Phase 7 — Apr–Jun 2028: validation and industrial training
- Test failures, timing, recovery, and performance.
- Complete industrial training requirements.
- Refine technical documentation and architecture.
- Start applying to graduate and relevant internship/trainee roles when eligible.

**Deliverable:** release candidate + case study.

## Phase 8 — Jul–Sep 2028: graduate readiness
- Complete capstone and final report.
- Publish polished GitHub repositories with videos, diagrams, benchmarks, and limitations.
- Practice C/C++/Linux, DSA, system design, and project explanation.
- Target employer applications based on role requirements.

**Deliverable:** portfolio with two strong systems/embedded projects and one integrated capstone.

---

# 6. Self-study method and curriculum

## Teaching method for every concept
Use the same three-part learning sequence:
1. **Explain the concept** — what it is, why it exists, how it works, pitfalls.
2. **Show a real-world example** — sensor reading, controller, OS process, or production service.
3. **Solve a small exercise** — implement, test, debug, and explain the result.

For programming, prefer **small progressive code fragments**, then independent exercises. Do not skip collection methods, standard-library essentials, error cases, or debugging techniques merely because basic syntax is familiar.

## Suggested weekly allocation (adjust for university/workload)
| Activity | Suggested hours/week |
|---|---:|
| University coursework and assessments | Priority; variable |
| Python or C/C++ deep practice | 4 |
| Linux / systems / debugging | 2 |
| Mathematics | 2 |
| Embedded or robotics project | 3 |
| Reading, notes, career tracking | 1 |
| **Total planned self-study** | **12** |

During exams, cut self-study to **3–5 hours/week** and preserve university work. Consistency matters more than an unsustainable schedule.

## Progress checks
- **Explain:** Can I describe the concept without memorized phrases?
- **Implement:** Can I build a small working example?
- **Test:** Can I identify edge cases and failure behavior?
- **Debug:** Can I investigate a fault systematically?
- **Transfer:** Can I use the idea in a different context?
- **Document:** Can another developer reproduce my result?

## Useful learning sources
- Python official tutorial: https://docs.python.org/3/tutorial/
- C++ reference: https://en.cppreference.com/
- Learn C++: https://www.learncpp.com/
- Linux man pages: https://man7.org/linux/man-pages/
- GNU GDB: https://www.gnu.org/software/gdb/documentation/
- CMake tutorial: https://cmake.org/cmake/help/latest/guide/tutorial/
- FreeRTOS documentation: https://www.freertos.org/
- ROS 2 documentation: https://docs.ros.org/
- OpenCV documentation: https://docs.opencv.org/
- NumPy documentation: https://numpy.org/doc/
- MIT OpenCourseWare: https://ocw.mit.edu/
- Arduino documentation: https://docs.arduino.cc/

Use the official documentation as a reference, not as a substitute for building and testing.

---

# 7. Portfolio and capstone strategy

## Project A — Virtual Sensor-Driven Controller (2026)
**Stack:** Python, pytest, optional NumPy.  
**Demonstrates:** state machines, input validation, fault states, unit tests, architecture.

**Acceptance evidence:**
- [ ] Requirements and state-transition table.
- [ ] Clean separation between sensor simulation and decision logic.
- [ ] Tests for missing/invalid/noisy data.
- [ ] Reproducible demo and README.

## Project B — Embedded Sensing & Diagnostics (2027)
**Stack:** C/C++, educational microcontroller or simulator, Python logging tools.  
**Demonstrates:** interfaces, timing, calibration, diagnostics, hardware abstraction.

**Acceptance evidence:**
- [ ] Sensor data collected or simulated reproducibly.
- [ ] Measurement units and sampling frequency documented.
- [ ] Fault/timeouts handled safely.
- [ ] Benchmarks or timing observations.
- [ ] Wiring diagrams only for safe educational low-voltage configurations.

## Project C — ROS 2 Simulation (late 2027)
**Stack:** C++/Python, ROS 2, simulator, RViz.  
**Demonstrates:** distributed robot components, transforms, messaging, tests.

**Acceptance evidence:**
- [ ] Simulation launches from documented instructions.
- [ ] Nodes exchange typed messages.
- [ ] Logs and replay/debugging evidence.
- [ ] Simple measurable behavior and failure handling.

## Capstone — choose one, not all
**Recommended default:** **Reliable Sensor-Driven Mobile Robot Software Platform** (simulation-first, hardware optional).

Possible research/engineering question:
> How do different sensor-filtering and control-loop designs affect response time, robustness, and resource use in a small mobile robot or simulated device?

**Alternative if interests shift:**
- Edge anomaly detection on sensor streams.
- Embedded Linux device monitoring and fault recovery.
- Industrial machine monitoring gateway with reliable telemetry.

**Capstone evidence:** problem statement, architecture, baseline, measurements, testing, limitations, reproducible setup, demonstration.

## How existing FieldSync fits
FieldSync is **supporting professional engineering evidence**, not your robotics capstone:
- Keep current ASP.NET Core + React/TypeScript + PostgreSQL design.
- Demonstrate durable queues, offline synchronization, idempotency, concurrency, authentication, observability, and failure testing.
- Avoid using confidential bank/customer data, source code, or internal infrastructure details in public portfolios.
- Reuse generic design patterns for device telemetry or fleet management later.

---

# 8. Development environment and tools

**Already relevant:** ThinkPad + Windows/WSL Ubuntu, VS Code/Visual Studio, Git/GitHub, Docker, Python, React, ASP.NET Core.

**Add progressively:**
- GCC/Clang, CMake, GDB, AddressSanitizer/UndefinedBehaviorSanitizer.
- pytest and a C++ test framework.
- Serial monitor and educational microcontroller IDE/toolchain.
- ROS 2 only when starting robotics simulation.
- Optional simulation tools rather than buying hardware early.

**Environment rule:** Avoid trying to install every robotics stack in 2026. Keep Python/C++/Linux environments stable first. Check ROS 2 distribution compatibility with your Ubuntu version before installation; older roadmap references to ROS 2 Humble should not be treated as a universal recommendation for a newer Ubuntu environment.

---

# 9. Employers to follow

> **Watchlist, not live vacancies.** Companies, role families, locations, and recruitment policies can change. Follow official careers pages and LinkedIn company pages; check eligibility and work authorization before applying. A few company/role descriptions were cross-checked against public sources in October 2026. The rankings below reflect *interest fit*, not hiring likelihood.

## Sri Lanka — first watchlist

| Priority | Company | Why follow | Official link | LinkedIn discovery |
|---|---|---|---|---|
| A | **Vega Innovations** | Embedded, robotics, computer vision, intelligent products | https://www.vega.lk/ | [Find company](https://www.linkedin.com/search/results/companies/?keywords=Vega%20Innovations) |
| A | **Zone24x7** | Embedded, IoT, Industry 4.0, intelligent software | https://zone24x7.com/ | [Find company](https://www.linkedin.com/search/results/companies/?keywords=Zone24x7) |
| A | **Iconic Devices / NORVI** | Embedded firmware, industrial IoT controllers | https://www.icd.lk/careers/ | [Find company](https://www.linkedin.com/search/results/companies/?keywords=Iconic%20Devices%20NORVI) |
| A | **Synopsys Sri Lanka** | Semiconductor software, EDA, systems engineering | https://careers.synopsys.com/SriLanka | [Find company](https://www.linkedin.com/search/results/companies/?keywords=Synopsys) |
| B | **KRAG** | Embedded, PCB, firmware, cloud-connected hardware | https://krag.lk/careers/ | [Find company](https://www.linkedin.com/search/results/companies/?keywords=KRAG%20Sri%20Lanka) |
| B | **Paraqum Technologies** | Network systems, software and product engineering; investigate roles | https://paraqum.com/ | [Find company](https://www.linkedin.com/search/results/companies/?keywords=Paraqum%20Technologies) |
| B | **WSO2** | Strong systems/integration software alternative | https://wso2.com/careers/ | [Find company](https://www.linkedin.com/search/results/companies/?keywords=WSO2) |
| B | **IFS** | Enterprise software with industrial/asset-management relevance | https://www.ifs.com/ | [Find company](https://www.linkedin.com/search/results/companies/?keywords=IFS) |
| B | **CodeGen** | Software, systems, engineering products; investigate current teams | https://www.codegen.co.uk/ | [Find company](https://www.linkedin.com/search/results/companies/?keywords=CodeGen) |
| B | **LSEG** | Performance/reliability-sensitive systems software fallback | https://www.lseg.com/en/careers | [Find company](https://www.linkedin.com/search/results/companies/?keywords=LSEG) |

**Verified examples (October 2026):**
- Vega describes EV, computer-vision, software and prototyping work; a public embedded-systems role described C/C++, Linux, ROS 2, and sensor/actuator integration.
- Zone24x7 lists embedded systems, IoT, and industry-focused technology services.
- Iconic Devices says it designs/manufactures industrial IoT hardware; its careers page accepts general interest and internships.
- Synopsys lists Sri Lankan office locations; an official careers page did not show a Sri Lankan vacancy at the time checked.
- KRAG describes embedded firmware and hardware/software work.

**Do not assume** that all listed companies hire junior firmware engineers every year.

## Global — long-term targets

| Company | Relevant focus | Official careers | LinkedIn discovery |
|---|---|---|---|
| **Bosch** | Automotive embedded, IoT, embedded AI | https://www.bosch.com/careers/career-opportunities/ | [Search](https://www.linkedin.com/search/results/companies/?keywords=Bosch) |
| **Siemens** | Industrial systems, automation, digital twins | https://jobs.siemens.com/ | [Search](https://www.linkedin.com/search/results/companies/?keywords=Siemens) |
| **ABB** | Robotics, motion, automation | https://careers.abb/ | [Search](https://www.linkedin.com/search/results/companies/?keywords=ABB) |
| **NVIDIA** | Edge AI, robotics computing, systems | https://www.nvidia.com/en-us/about-nvidia/careers/ | [Search](https://www.linkedin.com/search/results/companies/?keywords=NVIDIA) |
| **Qualcomm** | Embedded Linux, firmware, SoC software | https://careers.qualcomm.com/ | [Search](https://www.linkedin.com/search/results/companies/?keywords=Qualcomm) |
| **Arm** | CPU architecture, systems and developer software | https://careers.arm.com/ | [Search](https://www.linkedin.com/search/results/companies/?keywords=Arm) |
| **Texas Instruments** | Embedded/semiconductor software | https://careers.ti.com/ | [Search](https://www.linkedin.com/search/results/companies/?keywords=Texas%20Instruments) |
| **STMicroelectronics** | Microcontrollers, embedded ecosystems | https://careers.st.com/ | [Search](https://www.linkedin.com/search/results/companies/?keywords=STMicroelectronics) |
| **Schneider Electric** | Industrial automation and connected systems | https://www.se.com/ww/en/about-us/careers/ | [Search](https://www.linkedin.com/search/results/companies/?keywords=Schneider%20Electric) |
| **Rockwell Automation** | Industrial control and embedded products | https://www.rockwellautomation.com/en-us/company/careers.html | [Search](https://www.linkedin.com/search/results/companies/?keywords=Rockwell%20Automation) |
| **KUKA** | Industrial robotics | https://www.kuka.com/ | [Search](https://www.linkedin.com/search/results/companies/?keywords=KUKA) |
| **Universal Robots** | Collaborative robots and robot software | https://www.universal-robots.com/ | [Search](https://www.linkedin.com/search/results/companies/?keywords=Universal%20Robots) |

**Regional strategy:** Look for roles in Sri Lanka first, then consider international graduate programs, remote software positions where permitted, or later relocation. Some global roles require local work authorization, relocation eligibility, language proficiency, or prior experience. **A target company is not a promise of an accessible opening.**

## What to follow beyond companies
- **ROS**: https://www.ros.org/
- **Open Robotics / ROS Discourse**: https://discourse.ros.org/
- **Linux Foundation**: https://www.linuxfoundation.org/
- **Embedded Systems Conference / Embedded World**: https://www.embedded-world.de/
- **IEEE Robotics and Automation Society**: https://www.ieee-ras.org/
- **FreeRTOS**: https://www.freertos.org/
- **STMicroelectronics developer ecosystem**: https://www.st.com/
- **Arduino engineering ecosystem**: https://www.arduino.cc/

Follow organizations' **official LinkedIn, YouTube, GitHub, and careers links as exposed on their own websites**. The LinkedIn URLs in the tables are **search/discovery links**, not verified company-profile URLs. Avoid following unverified impersonator accounts.

---

# 10. LinkedIn, GitHub and professional visibility

## LinkedIn positioning
**Suggested headline:**
> Software Engineering Undergraduate | Systems & Embedded Software | C++ · Python · Linux | Exploring Robotics & Intelligent Machines

**About section themes:**
- Building reliable software and learning systems programming.
- Interested in software interacting with sensors, devices, and physical systems.
- Practical experience in production application support and software development.
- Developing Python, C/C++, Linux, embedded and robotics foundations.
- Show **what you have actually built**; avoid implying professional embedded experience you have not yet gained.

## Follow and engagement plan
**Every week (15–30 minutes):**
- [ ] Read 2 technical posts or engineering articles.
- [ ] Save 1 job description and extract recurring skills.
- [ ] Follow 1 relevant engineer, team, or official company page.
- [ ] Comment thoughtfully when you have a specific technical observation.

**Every month:**
- [ ] Publish one short project update or engineering lesson.
- [ ] Improve one GitHub README with diagrams/tests/results.
- [ ] Review internship and graduate role descriptions.
- [ ] Update your skill-gap tracker.

**Every quarter:**
- [ ] Publish a substantive project demonstration.
- [ ] Compare job descriptions against your actual portfolio.
- [ ] Refine your specialization focus based on evidence.

## GitHub portfolio organization
Suggested pinned repositories:
1. `sensor-controller-python` — state machine and tests.
2. `embedded-sensor-diagnostics` — firmware/simulation and debugging.
3. `robotics-simulation-ros2` — later ROS 2 application.
4. `fieldsync` — only if a public, sanitized version is legally permitted.
5. `engineering-notes` — concise explanations and benchmarks.

Each README should include: **problem → design → architecture → setup → tests → results → limitations → next steps**.

## Social channels
- **LinkedIn:** careers, company research, engineering network.
- **GitHub:** source code and reproducible engineering proof.
- **YouTube:** official technical talks and demonstrations.
- **Company career portals:** authoritative vacancy and eligibility details.
- **ROS/technical forums:** engineering discussion and troubleshooting.

You do **not** need to maintain many social accounts or post every day. Depth and consistency are more valuable.

---

# 11. Internship and graduate application plan

## Search terms to save
- `Embedded Software Engineer Intern`
- `Graduate Embedded Software Engineer`
- `Firmware Engineer Trainee`
- `Junior C++ Software Engineer`
- `Systems Software Engineer`
- `Embedded Linux Engineer`
- `IoT Software Engineer`
- `Robotics Software Engineer Intern`
- `Software Test Engineer Embedded`
- `Graduate Software Engineer C++`

## Application tiers
- **Tier 1:** Sri Lankan embedded/IoT/robotics companies aligned with projects.
- **Tier 2:** Sri Lankan product/platform/backend companies with strong engineering practices.
- **Tier 3:** Global embedded/robotics/semiconductor graduate programs where eligibility permits.

## Prepare before applying
- [ ] One-page tailored CV and relevant GitHub links.
- [ ] Portfolio with at least one tested C/C++ or embedded project.
- [ ] Clear explanation of memory, pointers, concurrency, debugging, and testing.
- [ ] Basic DSA and problem-solving practice.
- [ ] Architecture, requirements, trade-offs, and failure-mode stories.
- [ ] Examples of professional troubleshooting and reliability work without confidential details.
- [ ] Check location, visa/work authorization, degree eligibility, and application deadlines.

**Do not wait until graduation to research employers.** Start following them now; apply when openings and eligibility align.

---

# 12. Weekly operating system and progress dashboard

## This week's checklist
- [ ] Finalize Python collection methods and functions checklist.
- [ ] Write one Python sensor/state-machine exercise.
- [ ] Set up a basic C compiler and build a tiny command-line program.
- [ ] Review Linux files/processes/permissions.
- [ ] Map each Y3S1 assignment to a project deliverable.
- [ ] Follow the top 5 Sri Lankan target companies on their verified channels.
- [ ] Create a GitHub repository for the first systems-oriented project.

## Monthly review template
```text
Month:
University modules / assessments:
Python topics completed:
C/C++ topics completed:
Linux / systems topics completed:
Mathematics topics completed:
Embedded / robotics experiments:
Project evidence (links):
Tests / benchmarks:
What I can now explain confidently:
Where I struggled:
Next month's top 3 priorities:
Interesting job descriptions reviewed:
```

## Career decision gates
- **March 2027:** Do I enjoy C/C++ and debugging enough to continue deeper?
- **August 2027:** Do I enjoy hardware/software integration and sensor problems?
- **December 2027:** Which branch attracts me most: robotics, embedded Linux, industrial systems, or edge AI?
- **March 2028:** Is my capstone scoped realistically and measurable?
- **September 2028:** Which entry-level role best matches my demonstrated projects and eligibility?

---

# 13. Rules to avoid losing focus

1. **One primary specialization:** systems + embedded first.
2. **One active learning language focus at a time:** Python foundations, then C, then modern C++—with overlap only when purposeful.
3. **Do not equate technology lists with competence.** Every major topic needs a working example, tests, and explanation.
4. **Don't abandon your degree modules.** Map them to engineering outcomes.
5. **Don't replace the current FieldSync stack to satisfy an outdated roadmap.**
6. **Don't pursue all of ROS 2, SLAM, PLC, AI, cloud, and custom hardware at once.**
7. **Use simulation first**, and keep physical electronics projects low-voltage, age-appropriate, and appropriately supervised.
8. **Protect university and work responsibilities.** Reduce side-study during heavy weeks.
9. **Avoid overclaiming.** Present exploration and learning honestly.
10. **Re-evaluate based on completed projects, not fear of AI or social-media trends.**

# 14. Sources and provenance

## Personal roadmap materials used
- `Pasted text(4).txt` — four-semester university roadmap, modules, learning checklists, and project milestones.
- `Robotics-Roadmap-2028-Notion.html` — robotics-oriented topic list (math, programming, embedded, control, ROS 2, computer vision, AI, cloud).
- Older audio/DAW and backend roadmaps discussed previously — treated as historical and adapted rather than reproduced.
- Existing FieldSync technical context and career preferences supplied in conversation.

**Important:** Module codes/titles are taken from your previously supplied roadmap; they have **not** been independently validated against the university's current official catalog.

## Public sources checked October 2026
- Vega Innovations company overview: https://www.vega.lk/aboutus/
- Vega embedded role example: https://lk.linkedin.com/jobs/view/embedded-systems-engineer-at-vega-innovations-4301793028
- Zone24x7 overview: https://zone24x7.com/contact/
- Iconic Devices careers: https://www.icd.lk/careers/
- Iconic Devices products: https://www.icd.lk/products/
- Synopsys Sri Lanka careers: https://careers.synopsys.com/SriLanka
- KRAG careers: https://krag.lk/careers/
- Bosch careers: https://www.bosch.com/careers/career-opportunities/
- Bosch embedded C++/AI role example: https://jobs.smartrecruiters.com/BoschGroup/744000142055910-software-engineer-embedded-ai-c-f-m-div-

These public links are for **company research and examples**, not evidence of future 2028 vacancies.

---

## Final direction statement

> **I am developing toward Systems & Embedded Software Engineering, with Robotics & Intelligent Machines as the long-term application domain. My immediate focus is strong Python, C/C++, Linux, mathematics, software quality, and embedded fundamentals. I will preserve my existing backend and frontend experience as transferable professional strengths, then choose a narrower robotics/industrial/edge specialization based on real project experience before graduation.**
