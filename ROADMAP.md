# Semester Roadmap

Direction: **Systems Programming & Intelligent Machine Engineering**. Planning horizon: **October 2026–September 2028**, organised around Level 3 and Level 4 semesters. Exact semester dates and assessment deadlines are not supplied; follow the actual university calendar rather than assigning six-month blocks. Existing learning counts: do not restart completed work.

The module allocation below follows the user's finalized, locked curriculum. Do not recommend alternative electives or change their semester allocation. The university curriculum is fixed; independent engineering specialization remains flexible. Module titles establish subject areas, not detailed syllabus coverage. [University](UNIVERSITY.md) records the curriculum and remaining uncertainties; [Mathematics](MATHEMATICS.md) keeps the detailed study checklists.

The main exploration interests are signal processing and machine programming for IoT, embedded systems, robotics and automation. Use signals from sensors and physical systems as motivating examples; music production and audio ML are historical optional interests, not the main specialization.

## One learning path, not two

For each topic, use the university lecture, tutorial, assignment or examination preparation as the main learning activity. Independent study fills a specific prerequisite or demonstrated gap; it is not another parallel course in the same subject.

1. At the start of a semester, inspect the actual module outlines and upcoming assessments.
2. Identify the next topic you cannot yet explain or practise successfully. If you already can, retain the evidence and move on.
3. Use one short explanation and a few targeted exercises to close the gap, then return to coursework.
4. Link the relevant coursework or a short non-confidential summary in [Progress](PROGRESS.md). Do not redo it as a separate portfolio lab. Observe course rules about sharing assessed work.
5. At semester end, carry forward only unresolved prerequisites or useful extensions, not the entire checklist.

Priorities: **university deadlines and statistics preparation → prerequisites needed for current modules → systems skills not covered in coursework → optional exploration**. FieldSync remains a separate ongoing engineering project; use relevant experience without copying employer data or forcing it into every assignment.

## Immediate priority — Probability & Statistics preparation

Treat SMA2306 revision as the main mathematics track until the examination situation is resolved. The current journal still records the result/repeat requirement as unconfirmed, with March 2027 only tentative; no result or date is inferred here. Introductory Statistics and Introduction to Probability are already marked **in progress** in the mathematics plan.

- [ ] Continue those two topics rather than restarting them. Use the current video series for understanding, a brief own-word note and simple independent questions.
- [ ] Progress through probability rules and conditioning → random variables and PMF/CDF → distributions → estimation and confidence intervals → hypothesis testing → regression/correlation. Use the detailed checklist instead of duplicating it here.
- [ ] Compare each topic with university notes and assessed requirements; close missing topics. Verify the official syllabus, missing Lecture 05 and added normal-distribution/CLT bridge.
- [ ] Move from topic questions to mixed past-paper questions, recording errors and retrying them without solutions. Use timed practice only once the paper format and duration are confirmed.
- [ ] When result, repeat requirements and dates are confirmed, reserve revision time around actual assessment deadlines. Pause optional systems and hardware work during examination preparation.

Parallel mathematics is limited to what unblocks the next statistics problem: fractions, percentages, rearranging formulas, powers, sums, sets and reading graphs. Do not finish a full algebra or calculus course before continuing statistics.

Readiness means explaining why a method applies, solving a representative unfamiliar question and correcting errors—not finishing a video playlist or assuming mastery from a prior exam attempt.

## Level 3 — Semester 1

**University-led learning:** CCS2360 Technology Challenge Competition; CCS3300 Software Architecture; CCS3310 Software Engineering Methods; CCS3311 Software Quality Assurance; selected elective CCS3356 Natural Language Processing.

| Focus | Let university work provide | Independent preparation only where needed |
|---|---|---|
| Architecture, methods and quality | Module-directed design, development process, testing and quality exercises | Review the language/tools required for the next assignment; practise one unfamiliar testing or design technique in that work |
| NLP | The module's language-processing concepts, techniques and assessed implementation | Python functions, collections, strings, files and debugging; basic probability, vectors, dot products and array shapes before dependent material |
| Technology Challenge | The assigned problem, teamwork and deliverable | Learn only the missing tools needed for that deliverable; no extra challenge project |
| Mathematics | Statistics revision stays primary | Short algebra/function refresh alongside it; basic vector notation when NLP requires it |

NLP precedes the selected ML and Linear Algebra modules. Before the relevant NLP lecture, learn only the necessary bridge: numerical representations, the meaning of training versus evaluation, and a simple baseline if used by the course. Leave deeper ML theory and full linear-algebra coverage to Semester 2. If NLP introduces gradients early, cover slope and chain-rule intuition just in time rather than delaying the module.

**Small systems gap, only if capacity remains:** use Git and basic Linux commands while completing existing work. Defer a separate C++ learning track while statistics or assessments need that time.

**Semester review:** retain evidence of one module-directed design/testing outcome and one NLP exercise you can explain, as applicable to the actual assessments. Record remaining Python/mathematics gaps; these are learning checks, not invented additional university requirements.

## Level 3 — Semester 2

**University-led learning:** CCS3302 Introduction to Research Methods; CCS3313 Advanced Software Design; SMA2307 Discrete Mathematics; selected electives CCS4340 Machine Learning and SMA2202 Linear Algebra. These selections and their semester allocation are finalized; use the actual timetable to sequence preparation.

| Focus | Let university work provide | Independent preparation only where needed |
|---|---|---|
| Linear Algebra | Use SMA2202 lectures and exercises as the main path | Refresh algebra, simultaneous equations and vector/matrix notation; consult the mathematics checklist only for gaps in actual coverage |
| Discrete Mathematics | Use SMA2307 as the main route through its logic, sets, proofs, counting and graph topics where included | Practise a missed prerequisite, then apply the concept to a small DSA problem if coursework does not already do so |
| Machine Learning | Use CCS4340 for the taught models, theory, evaluation and implementation | Python/NumPy shapes, probability and linear-algebra prerequisites; derivatives, chain rule and gradients before algorithms that need them |
| Research Methods | Use the module for research questions, literature work and experiment design | Reuse statistics understanding; practise explaining assumptions and limitations in the assigned work |
| Advanced Software Design | Use the module's design techniques and assessed work | Address a specific design/testing gap through the existing assignment or suitable FieldSync work |

Because ML and Linear Algebra run in the same semester, their teaching order may not align. Before an ML topic, bridge only the needed matrix operation, dot product or norm; let SMA2202 supply the deeper treatment later. Do not complete a second linear-algebra curriculum in advance.

**Likely independent mathematics gap:** basic calculus is not explicitly listed as a module in the finalized curriculum. Check prior learning and current module coverage first, then learn limits/rates of change → derivatives → chain rule → partial derivatives/gradients → gradient descent as required. Learn basic integration when a probability or later engineering problem needs it. No full calculus sequence is required at once.

**Small systems gap, if capacity remains:** one C++ exercise covering compilation, types, functions, references/pointers and object lifetime; progress to STL and RAII only when earlier ideas are comfortable. Use it for DSA practice rather than adding a second exercise stream.

**Semester review:** explain a course ML model's assumptions, data split, metric and errors; demonstrate relevant matrix and discrete-mathematics reasoning. Reuse actual coursework evidence. Carry forward only gaps needed for Year 4.

## Level 4 — Semester 1

**University-led learning:** CCS3301 Capstone Project — Part 1; CCS3440 Artificial Intelligence; IHM1301 Human Behavior and Ethics; CCS4310 Deep Learning; CCS4353 Internet of Things. All selections are locked.

- [ ] Use AI coursework for the concepts and techniques it actually teaches. Reuse ML, probability and discrete mathematics; bridge gaps rather than repeating those subjects wholesale.
- [ ] For Deep Learning, reuse Semester 2 ML and Linear Algebra; refresh array shapes, matrix operations, derivatives, chain rule, partial derivatives/gradients and basic optimization only where understanding is missing. Let the module teach its deep-learning methods.
- [ ] For Internet of Things, check the first practical's requirements, then bridge programming, basic electronics (units, voltage, current, resistance), digital I/O, sensor readings and basic networking as needed. Let the course provide its IoT architecture, communication and implementation work; do not add a separate compulsory embedded course.
- [ ] Use Capstone Part 1 for a feasible problem, literature review, requirements, evaluation plan and prototype as required by the module. Carry forward Research Methods work where course rules permit.
- [ ] Integrate ethics, data provenance, limitations and responsible engineering into coursework and project decisions as relevant to the module requirements.

**Independent systems continuation, only if useful:** develop the same small C++/Linux exercise through CMake, testing, debugger use, resource ownership and basic measurement. Learn processes, memory and file/I/O concepts before dependent systems tasks. Introduce concurrency only after ownership, debugging and a concrete need are established. Skip topics already demonstrated through coursework or work.

**IoT practice and optional exploration:** use an assigned IoT practical as embedded/sensor learning evidence where appropriate. Add a separate short exercise only for a missing prerequisite or optional interest when capacity remains. The Arduino Uno, several sensors and one controller supporting four motors are already recorded in [Projects](PROJECTS.md); identify models and compatibility before selecting a hardware exercise. A simulation or software-only project remains sufficient. No robotics, embedded or industrial-automation specialization is assumed.

**Semester review:** a university-aligned capstone scope and evaluation plan, plus evidence from current modules. No additional flagship is required.

## Level 4 — Semester 2

**University-led learning:** CCS4601 Industrial Training; CCS4301 Capstone Project — Part 2; CCS4354 Tensors and Graphs (with programming); SMA2305 Numerical Analysis. All selections are locked.

- [ ] Prioritise training requirements, capstone implementation/evaluation/reporting and current elective assessments. Confirm whether existing employment satisfies training requirements; do not assume it does.
- [ ] Reuse the capstone as the main integration exercise. Test correctness, document reproducibility and measure performance or model quality only where the chosen problem calls for it.
- [ ] For Tensors and Graphs, reuse Linear Algebra, Discrete Mathematics and relevant Deep Learning work. Refresh multidimensional array shapes, indexing, matrix operations, graph representations and traversals as the module outline requires; do not assume a specific tensor/graph theory syllabus from the title alone.
- [ ] For Numerical Analysis, refresh algebra/functions, derivatives and basic integration, linear systems and Python numerical computation before the relevant lessons. Use the module for its numerical methods, approximation/error analysis and convergence topics where included. Do not complete an independent numerical-analysis course first.
- [ ] Resolve gaps exposed by implementation or experiments; avoid starting a broad new syllabus during delivery.
- [ ] Review which systems/intelligent-machine area interests you based on actual experience. Continuing with a broad direction is valid if there is insufficient evidence to choose a specialty.

**Semester review:** meet the university's actual submission and training requirements, retain permitted learning evidence and document unresolved questions for the next stage. September 2028 is the planning horizon, not a claim about graduation or submission dates.

## Independent-study boundaries and weekly use

Keep **one main academic/statistics focus and at most one small prerequisite gap** active. The main academic focus may change when an assessment is urgent.

- On a manageable week, try two 30–60 minute blocks for the current priority and one optional 20–30 minute gap session. Coursework preparation counts inside these blocks; they are not extra quotas per subject.
- On a heavy week, reduce to one brief review or pause independent study. No catch-up debt and no compulsory daily sessions.
- If up to two hours happens to be available on a day, it is an optional upper limit, not the normal commitment. Protect sleep and recovery.
- Spend two to five minutes weekly recording actual work, the evidence, confusion and next action in [Progress](PROGRESS.md).

Before adding independent work, ask: **Is this covered by a current/upcoming module? Do I need it before that module teaches it? Can an existing assignment provide the practice?** Add only the remaining gap.

Later exploration may include basic electronics and sensors; signal sampling, noise, filtering and interpretation of sensor measurements after the relevant mathematics; embedded I/O/timing; control after calculus, linear algebra and necessary differential equations; robotics after vectors, coordinate frames and basic mechanics; and applied AI through the university sequence first. These are alternatives, not a two-year checklist. Numerical Analysis is a fixed university subject in Year 4 Semester 2; methods beyond its coverage, real-time systems and efficient inference follow an actual need.

Audio ML, music-focused DSP and browser DAW development are historical optional interests. The [project index](PROJECTS.md) lists actual active development, not future exploration ideas. Existing labs and learning remain valid. No new large application, duplicate university course or hardware purchase is required by this roadmap.
