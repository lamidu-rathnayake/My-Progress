# Essential Mathematics Prerequisites for Probability and Statistics

Study these sections in order. Each introduces the notation, explains the rules, and works through examples used later in probability and statistics.

This is a reference note with original examples, not a record of completed study or a verified summary of the university slides. It supports [roadmap topic 1.1](../../MATHEMATICS.md#11-essential-prerequisites).

## 1. Fractions, decimals, percentages, ratios, and signed numbers

### 1.1 Signed numbers and order of operations

Positive numbers are greater than zero; negative numbers are less than zero. On a number line, numbers increase from left to right. Thus −5 < −2 < 0 < 3.

For addition and subtraction:

- Adding a negative is subtraction: 7 + (−3) = 4.
- Subtracting a negative is addition: 7 − (−3) = 10.
- Two negatives added remain negative: −4 + (−6) = −10.

For multiplication and division, equal signs give a positive answer and different signs give a negative answer:

| Calculation | Result |
|---|---:|
| 4 × 3 | 12 |
| (−4) × (−3) | 12 |
| (−4) × 3 | −12 |
| 12 ÷ (−3) | −4 |

Division by zero is undefined. Zero divided by a nonzero number is zero.

Use this order: parentheses, powers and roots, multiplication/division from left to right, then addition/subtraction from left to right.

**Example:**

```text
8 − 2 × (3 − 5)²
= 8 − 2 × (−2)²
= 8 − 2 × 4
= 0
```

Parentheses matter: (−3)² = 9, but −3² = −(3²) = −9.

Absolute value is distance from zero: |−5| = 5 and |5| = 5. It is never negative.

**Statistics connection:** If an observation is 7 and the mean is 10, its deviation is 7 − 10 = −3. Its squared deviation is (−3)² = 9.

### 1.2 Fractions

A fraction a/b means a divided by b, where b ≠ 0. The numerator a counts parts; the denominator b describes how many equal parts make a whole.

Multiplying or dividing both numerator and denominator by the same nonzero number preserves the fraction:

```text
12/18 = (12 ÷ 6)/(18 ÷ 6) = 2/3
```

To add or subtract fractions, first use a common denominator:

```text
2/3 + 1/4 = 8/12 + 3/12 = 11/12
5/6 − 1/4 = 10/12 − 3/12 = 7/12
```

Multiply numerators together and denominators together:

```text
(2/3) × (9/10) = 18/30 = 3/5
```

Divide by a nonzero fraction by multiplying by its reciprocal:

```text
(3/4) ÷ (2/5) = (3/4) × (5/2) = 15/8 = 1.875
```

Cancel common **factors**, not terms separated by addition. For example, (2 × 3)/(2 × 5) = 3/5, but (2 + 3)/(2 + 5) = 5/7.

**Probability example:** If 8 of 20 equally likely outcomes satisfy an event, its probability is 8/20 = 2/5.

### 1.3 Decimals and percentages

Convert a fraction to a decimal by division. A percentage is a fraction out of 100.

```text
3/8 = 0.375 = 37.5%
0.08 = 8/100 = 2/25 = 8%
65% = 65/100 = 0.65
```

Multiply a decimal by 100 to express it as a percentage; divide a percentage by 100 to use it in a calculation.

**Example:** 15% of 240 is 0.15 × 240 = 36.

For percentage change:

```text
percentage change = ((new − old)/old) × 100%, provided old ≠ 0
```

An increase from 40 to 50 is (10/40) × 100% = 25%.

A probability increase from 20% to 30% is **10 percentage points**, or a **50% relative increase**. These are different measurements.

**Probability connection:** If P(A) = 0.35, then the probability that A does not occur is 1 − 0.35 = 0.65 = 65%.

### 1.4 Ratios, proportions, and rates

A ratio compares quantities. A ratio of 2:3 means 2 parts of one quantity for every 3 parts of another; there are 5 parts altogether.

**Example:** A group of 40 students has a ratio of 2:3 between groups A and B:

```text
one part = 40/(2 + 3) = 8
A = 2 × 8 = 16
B = 3 × 8 = 24
proportion in A = 16/40 = 2/5
```

The ratio A:B = 2:3 does not mean that A is 2/3 of the whole.

A proportion equates two ratios. For nonzero denominators, a/b = c/d implies ad = bc.

```text
x/20 = 3/5
5x = 60
x = 12
```

A rate has units, such as calls per minute. Always match units before calculating.

**Poisson preparation:** At an average rate of 6 calls per hour, the mean count in 20 minutes is:

```text
6 calls/hour × (20/60) hour = 2 calls
```

## 2. Substitution, rearranging formulas, powers, roots, and rounding

### 2.1 Variables and substitution

A variable is a symbol representing a quantity. Substitution replaces symbols with their values. Use parentheses for negative values and multi-part expressions.

**Example:** For y = 2x² − 3x + 1 at x = −2:

```text
y = 2(−2)² − 3(−2) + 1
  = 8 + 6 + 1
  = 15
```

**Statistics example:** A standardized value is Z = (X − μ)/σ, where μ is the population mean and σ is the population standard deviation. If X = 70, μ = 60, and σ = 5:

```text
Z = (70 − 60)/5 = 2
```

The whole numerator is divided by 5. Writing 70 − 60/5 would give a different expression.

Common symbols used later:

| Symbol | Meaning |
|---|---|
| n | Number of observations or trials, depending on context |
| xᵢ | Observation with index i |
| x̄ | Sample mean, pronounced “x-bar” |
| μ | Population mean, pronounced “mu” |
| σ | Population standard deviation, pronounced “sigma” |
| σ² | Population variance |
| s and s² | Sample standard deviation and sample variance |
| p | A probability or population proportion, depending on context |
| p̂ | Sample proportion, pronounced “p-hat” |
| Σ | Summation symbol, capital sigma |

### 2.2 Rearranging equations and formulas

An equation says two expressions are equal. Apply the same operation to both sides to preserve equality. Multiplication or division used to reverse a step must be by a nonzero quantity.

**Example: solve a linear equation.**

```text
3x + 5 = 20
3x = 15       subtract 5 from both sides
x = 5         divide both sides by 3
```

**Example: make X the subject of Z = (X − μ)/σ, with σ > 0.**

```text
Zσ = X − μ
X = μ + Zσ
```

For μ = 50, σ = 4, and Z = 1.5, X = 50 + 1.5 × 4 = 56.

**Example: solve a margin-of-error formula for n.** With E, z, and σ positive:

```text
E = zσ/√n
E√n = zσ
√n = zσ/E
n = (zσ/E)²
```

If z = 1.96, σ = 10, and the required margin is at most 3:

```text
n ≥ (1.96 × 10/3)² ≈ 42.6844
minimum whole-number sample size = 43
```

Check a rearrangement by substituting a simple set of values back into the original formula.

### 2.3 Powers and exponent laws

For a positive integer m, aᵐ is a multiplied by itself m times. In 2³ = 8, 2 is the base and 3 is the exponent.

| Rule | Example |
|---|---|
| aᵐ × aⁿ = aᵐ⁺ⁿ | 2³ × 2² = 2⁵ = 32 |
| aᵐ/aⁿ = aᵐ⁻ⁿ, a ≠ 0 | 5⁴/5² = 5² = 25 |
| (aᵐ)ⁿ = aᵐⁿ | (2²)³ = 2⁶ = 64 |
| (ab)ⁿ = aⁿbⁿ | (2 × 3)² = 4 × 9 = 36 |
| a⁰ = 1, a ≠ 0 | 7⁰ = 1 |
| a⁻ⁿ = 1/aⁿ, a ≠ 0 | 2⁻³ = 1/8 |

For positive a, a^(1/2) = √a and a^(m/n) = ⁿ√(aᵐ), where n is a positive integer. For example, 27^(2/3) = 3² = 9.

Exponent rules do not distribute across addition: (a + b)² = a² + 2ab + b², rather than a² + b².

**Probability example:** For three independent events each having probability 0.5, the probability that all occur is (0.5)³ = 0.125.

The constant e ≈ 2.71828 appears in Poisson calculations. For example, e⁻² = 1/e² ≈ 0.1353. Use the calculator's exponential function for this value.

### 2.4 Square roots

The principal square root √a is the nonnegative number whose square is a, for a ≥ 0.

```text
√49 = 7
√0.25 = 0.5
√(9 × 4) = √9 × √4 = 6
√(9/4) = √9/√4 = 1.5
```

For real x, √(x²) = |x|. Thus √((−4)²) = 4.

Although √25 = 5, solving x² = 25 gives two solutions, x = 5 and x = −5. A standard deviation uses the nonnegative square root.

Do not split a root across a sum: √(9 + 16) = 5, whereas √9 + √16 = 7.

**Statistics connection:** If a variance is 16, its standard deviation is √16 = 4. If σ = 12 and n = 36, the standard error σ/√n = 12/6 = 2.

### 2.5 Rounding and scientific notation

Decimal places count digits after the decimal point. Significant figures count from the first nonzero digit.

```text
3.1462 to 2 decimal places = 3.15
0.004762 to 2 significant figures = 0.0048
```

For ordinary rounding in these exercises, inspect the next digit: 0–4 leaves the retained digit unchanged; 5–9 increases it by one. Follow any rounding convention explicitly required by the exam.

Keep extra digits during calculations and round the final result. Small intermediate rounding errors can affect a final probability or test statistic.

Scientific notation writes a number as a × 10ᵏ, with 1 ≤ |a| < 10 for a nonzero number:

```text
45,000 = 4.5 × 10⁴
0.00072 = 7.2 × 10⁻⁴
```

Minimum sample sizes are **rounded up**, not rounded to the nearest integer: a requirement of n ≥ 42.1 means n = 43 is the smallest valid size.

## 3. Inequalities and interval notation

### 3.1 Comparing and solving

| Symbol | Meaning |
|---|---|
| < | Less than |
| ≤ | Less than or equal to |
| > | Greater than |
| ≥ | Greater than or equal to |
| ≠ | Not equal to |

Addition or subtraction of the same quantity on both sides preserves the inequality. Multiplication or division by a positive number also preserves it. Multiplication or division by a **negative** number reverses it.

```text
2x + 3 ≤ 11
2x ≤ 8
x ≤ 4
```

```text
−2x < 6
x > −3       divide both sides by −2 and reverse the sign
```

For a compound inequality:

```text
2 < 3x + 2 ≤ 11
0 < 3x ≤ 9
0 < x ≤ 3
```

### 3.2 Translate words into symbols

| Wording | Event |
|---|---|
| Exactly 3 | X = 3 |
| At most 3; no more than 3 | X ≤ 3 |
| Fewer than 3; below 3 | X < 3 |
| At least 3; no fewer than 3 | X ≥ 3 |
| More than 3; above 3 | X > 3 |
| Between 2 and 5, inclusive | 2 ≤ X ≤ 5 |
| Strictly between 2 and 5 | 2 < X < 5 |

“Between” by itself can be ambiguous; check whether endpoints are included.

If X is an integer-valued count, X < 3 means X ≤ 2, while X > 3 means X ≥ 4. This matters for binomial and Poisson questions.

For a count:

```text
P(X ≥ 3) = 1 − P(X ≤ 2)
P(X > 3) = 1 − P(X ≤ 3)
```

### 3.3 Interval notation

Square brackets include an endpoint; parentheses exclude it.

| Inequality | Interval |
|---|---|
| 2 ≤ x ≤ 5 | [2, 5] |
| 2 < x < 5 | (2, 5) |
| 2 ≤ x < 5 | [2, 5) |
| x ≤ 5 | (−∞, 5] |
| x > 2 | (2, ∞) |

Infinity is not a real endpoint, so always use a parenthesis beside ∞ or −∞.

For a continuous random variable, an individual value has probability zero, so including or excluding an endpoint does not change an interval probability. For a discrete variable, it can change the answer.

### 3.4 Absolute-value intervals

|x − a| measures the distance from x to a. For d ≥ 0:

```text
|x − a| ≤ d  means  a − d ≤ x ≤ a + d
```

**Example:** |x − 10| ≤ 2 means 8 ≤ x ≤ 12. This is the idea behind an estimate “within 2 units” of 10.

## 4. Sets, events, and Venn diagrams

### 4.1 Set notation

A set is a collection of distinct elements. Order and repeated entries do not change a set: {1, 2, 2, 3} = {3, 2, 1}.

| Notation | Meaning |
|---|---|
| x ∈ A | x belongs to A |
| x ∉ A | x does not belong to A |
| A ⊆ B | Every element of A belongs to B |
| ∅ | Empty set |
| Ω | Sample space: all possible outcomes |
| ∣A∣ | Number of elements in a finite set A |

For rolling one six-sided die, Ω = {1, 2, 3, 4, 5, 6}. An event is a subset of Ω.

Let A = {2, 4, 6}, the event “even,” and B = {4, 5, 6}, the event “greater than 3.”

### 4.2 Union, intersection, complement, and difference

| Operation | Meaning | Die example |
|---|---|---|
| A ∪ B | A or B or both | {2, 4, 5, 6} |
| A ∩ B | Both A and B | {4, 6} |
| Aᶜ | Outcomes in Ω but outside A | {1, 3, 5} |
| A ∖ B | In A but not B | {2} |

Mathematical “or” is inclusive unless explicitly stated otherwise.

A and B are mutually exclusive when A ∩ B = ∅. For one die, “even” and “odd” are mutually exclusive; “even” and “greater than 3” are not.

### 4.3 How to construct a Venn diagram

Draw a rectangle for Ω and two overlapping circles labelled A and B. Fill the overlap first, then each exclusive region, then the region outside both circles.

For the die example, the four regions are:

| Region | Outcomes | Count |
|---|---|---:|
| A only | {2} | 1 |
| A and B | {4, 6} | 2 |
| B only | {5} | 1 |
| Neither | {1, 3} | 2 |

The counts total 6. If the die is fair, divide each count by 6 to get its probability.

The union counts the overlap once:

```text
|A ∪ B| = |A| + |B| − |A ∩ B|
        = 3 + 3 − 2
        = 4
```

For any two events:

```text
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
P(Aᶜ) = 1 − P(A)
```

Only when the elementary outcomes are equally likely can you calculate probability as favourable outcome count divided by total outcome count.

### 4.4 Complements of combined events

De Morgan's laws translate “neither” and “not both”:

```text
(A ∪ B)ᶜ = Aᶜ ∩ Bᶜ     neither A nor B
(A ∩ B)ᶜ = Aᶜ ∪ Bᶜ     not both A and B
```

In the die example, “neither even nor greater than 3” is {1, 3}. “Not both even and greater than 3” is {1, 2, 3, 5}.

Independence is a different concept from mutual exclusivity: independent events satisfy P(A ∩ B) = P(A)P(B). Two mutually exclusive events with positive probabilities cannot be independent.

## 5. Indexed values, sigma notation, finite sums, and sums of squares

### 5.1 Indexed observations

For a dataset containing n observations, write x₁, x₂, …, xₙ. The subscript identifies an observation; it is not multiplication or a power.

For the dataset 2, 4, 6:

```text
n = 3
x₁ = 2, x₂ = 4, x₃ = 6
x₂² = 4² = 16
```

### 5.2 Reading sigma notation

The notation Σᵢ₌₁ⁿ xᵢ means “add xᵢ for each integer i from 1 through n.” The bottom gives the starting index, the top gives the ending index, and the expression after Σ tells you what to add.

```text
Σᵢ₌₁³ xᵢ = x₁ + x₂ + x₃ = 2 + 4 + 6 = 12
Σᵢ₌₂³ xᵢ = x₂ + x₃ = 4 + 6 = 10
Σᵢ₌₁⁴ i = 1 + 2 + 3 + 4 = 10
Σᵢ₌₁³ 5 = 5 + 5 + 5 = 15
```

The index is a placeholder: using j instead of i does not change the sum if the bounds and expression change consistently.

For constant c:

```text
Σᵢ₌₁ⁿ c = nc
Σᵢ₌₁ⁿ (cxᵢ) = c Σᵢ₌₁ⁿ xᵢ
Σᵢ₌₁ⁿ (xᵢ + yᵢ) = Σᵢ₌₁ⁿ xᵢ + Σᵢ₌₁ⁿ yᵢ
```

### 5.3 Sum of squares versus square of a sum

These operations are different:

```text
Σᵢ₌₁³ xᵢ² = 2² + 4² + 6² = 56
(Σᵢ₌₁³ xᵢ)² = (2 + 4 + 6)² = 144
```

In the first expression, square each observation before adding. In the second, add first and then square the total.

### 5.4 Mean and squared deviations

The sample mean is the sum divided by the number of observations:

```text
x̄ = (Σᵢ₌₁ⁿ xᵢ)/n = 12/3 = 4
```

Use a table to organize calculations:

| i | xᵢ | xᵢ² | xᵢ − x̄ | (xᵢ − x̄)² |
|---|---:|---:|---:|---:|
| 1 | 2 | 4 | −2 | 4 |
| 2 | 4 | 16 | 0 | 0 |
| 3 | 6 | 36 | 2 | 4 |
| Total | 12 | 56 | 0 | 8 |

The squared deviations add to 8. The unsquared deviations add to zero, so they cannot directly measure spread.

A useful identity is:

```text
Σᵢ₌₁ⁿ (xᵢ − x̄)² = Σᵢ₌₁ⁿ xᵢ² − (Σᵢ₌₁ⁿ xᵢ)²/n
                   = 56 − 144/3
                   = 8
```

When these observations are a sample and n > 1, the usual sample variance and standard deviation are:

```text
s² = Σᵢ₌₁ⁿ (xᵢ − x̄)²/(n − 1) = 8/2 = 4
s = √4 = 2
```

If the three values instead represent the entire population being described, its variance uses denominator 3, giving 8/3. The denominator depends on what the data represent.

### 5.5 Sums of products and weighted sums

For paired observations, Σxᵢyᵢ means multiply each matching pair, then add. It is generally different from (Σxᵢ)(Σyᵢ).

If x = (1, 2, 3) and y = (2, 5, 4):

```text
Σᵢ₌₁³ xᵢyᵢ = 1×2 + 2×5 + 3×4 = 24
(Σᵢ₌₁³ xᵢ)(Σᵢ₌₁³ yᵢ) = 6 × 11 = 66
```

Sums of products appear in correlation and regression.

A weighted sum multiplies each value by a weight. If a random variable takes values 0, 1, and 2 with probabilities 0.2, 0.5, and 0.3:

```text
sum of probabilities = 0.2 + 0.5 + 0.3 = 1
weighted mean = 0×0.2 + 1×0.5 + 2×0.3 = 1.1
```

This weighted mean is the expected value. It need not be a possible individual outcome.

## 6. Factorials, permutations, and combinations

### 6.1 Counting by stages

If a process has m choices at one stage and n choices at the next for each first-stage choice, there are mn possible sequences.

**Example:** 3 shirts and 2 trousers give 3 × 2 = 6 outfits.

A three-digit code allowing digits 0–9, leading zeros, and repetition has 10³ = 1,000 possibilities. If repetition is forbidden, it has 10 × 9 × 8 = 720 possibilities.

State restrictions before counting. A three-digit number cannot start with zero, so it has different counts.

### 6.2 Factorials

For a positive integer n:

```text
n! = n(n − 1)(n − 2)…2×1
5! = 5×4×3×2×1 = 120
0! = 1
```

There is one way to arrange no objects, which is consistent with 0! = 1.

Cancel factorial expressions before doing large calculations:

```text
8!/6! = (8×7×6!)/6! = 56
```

### 6.3 Permutations: order matters

A permutation is an ordered selection. Selecting r objects without replacement from n distinct objects gives:

```text
P(n, r) = n!/(n − r)!, where 0 ≤ r ≤ n
```

**Example:** Awarding gold, silver, and bronze to 3 of 5 people gives:

```text
P(5, 3) = 5×4×3 = 60
```

Alice–Bob–Chen and Bob–Alice–Chen are different outcomes because the positions matter.

Arranging all n distinct objects gives n! permutations. For ordered selections of length r with repetition allowed and n choices at each position, use nʳ instead.

### 6.4 Combinations: order does not matter

A combination is an unordered selection. Selecting r objects without replacement from n distinct objects gives:

```text
C(n, r) = n!/[r!(n − r)!], where 0 ≤ r ≤ n
```

Other notation includes nCr and “n choose r.”

**Example:** Choosing a committee of 3 from 5 people gives:

```text
C(5, 3) = 5!/(3!2!) = 10
```

Every committee appears 3! times among the 60 ordered selections. Dividing by 3! removes those repeated orderings.

Useful identities:

```text
C(n, 0) = C(n, n) = 1
C(n, r) = C(n, n − r)
```

### 6.5 Choose the right counting method

| Situation | Method |
|---|---|
| Several stages with fixed choice counts | Multiply the counts |
| Arrange all n distinct objects | n! |
| Ordered selection, no replacement | P(n, r) |
| Unordered selection, no replacement | C(n, r) |
| Ordered selection, repetition allowed | nʳ |

For counts used in probability, the numerator and denominator must count outcomes in the same way. Do not count the numerator as ordered and the denominator as unordered.

### 6.6 Worked probability examples

**Example A: selecting without replacement.** A bag contains 5 red and 3 blue balls. All 8 balls are individually distinct and every pair is equally likely. Select 2 without replacement. What is the probability both are red?

```text
all unordered pairs = C(8, 2) = 28
red unordered pairs = C(5, 2) = 10
P(both red) = 10/28 = 5/14 ≈ 0.3571
```

An equivalent sequential calculation is (5/8) × (4/7) = 5/14.

**Example B: exactly two successes.** Four independent trials each have success probability 0.3. There are C(4, 2) = 6 ways to choose which two trials succeed. Each particular arrangement has probability (0.3)²(0.7)².

```text
P(exactly 2 successes)
= C(4, 2)(0.3)²(0.7)²
= 6 × 0.09 × 0.49
= 0.2646
```

This is the counting foundation of the binomial probability formula.

## 7. Independent practice

Attempt these before reading the answers. Show intermediate steps and retain exact fractions until the final rounding where practical.

1. Calculate −6 + 4 × (3 − 5).
2. Calculate 3/4 − 2/5 and express the result as a decimal and percentage.
3. Divide 64 observations into groups in the ratio 3:5.
4. A service receives an average of 9 requests per hour. Find the mean count in 20 minutes.
5. Evaluate 2x² − x + 3 when x = −3.
6. Rearrange Z = (X − μ)/σ to make μ the subject. Then use X = 82, Z = 1.5, and σ = 8.
7. Simplify (2³ × 2⁻¹)/2².
8. Calculate √((5 − 9)²) and explain why the result is nonnegative.
9. Round 0.007846 to two significant figures. If a minimum sample-size calculation gives 64.02, choose the required integer size.
10. Solve −3x + 2 ≥ 11.
11. Write “at least 4 but fewer than 8” as an inequality and an interval. List the possible values if X is an integer.
12. Express P(X ≥ 5) using a complement when X is integer-valued.
13. Let Ω = {1, 2, 3, 4, 5, 6}, A = {1, 2, 3}, and B = {3, 4}. Find A ∪ B, A ∩ B, Aᶜ, and (A ∪ B)ᶜ.
14. In a class of 30, 18 study A, 14 study B, and 8 study both. Find the counts studying A only, B only, at least one, and neither.
15. For x = (1, 3, 5, 7), find Σxᵢ, Σxᵢ², (Σxᵢ)², and x̄.
16. For the same dataset, find Σ(xᵢ − x̄)² and the sample variance.
17. For x = (2, 4, 6) and y = (1, 3, 2), calculate Σxᵢyᵢ.
18. Calculate 6!/4!, P(6, 2), and C(6, 2). Explain why the last two differ.
19. How many four-digit codes are possible if digits 0–9 and leading zeros are allowed: (a) with repetition, (b) without repetition?
20. A bag has 4 red and 2 blue balls. Select 2 without replacement, with every pair equally likely. Find the probability of one red and one blue.
21. Five independent trials each have success probability 0.2. Find the probability of exactly one success.

## 8. Answers and working

1. −6 + 4(−2) = **−14**.
2. 15/20 − 8/20 = **7/20 = 0.35 = 35%**.
3. One part is 64/8 = 8; the groups contain **24 and 40** observations.
4. 9 × (20/60) = **3 requests** on average.
5. 2(−3)² − (−3) + 3 = 18 + 3 + 3 = **24**.
6. Zσ = X − μ, so **μ = X − Zσ = 82 − 12 = 70**.
7. 2^(3 − 1 − 2) = 2⁰ = **1**.
8. √((−4)²) = √16 = **4**. The principal square root is nonnegative; √(a²) = |a| for real a.
9. **0.0078**; minimum sample size **65**.
10. −3x ≥ 9, so **x ≤ −3** after reversing the inequality.
11. **4 ≤ X < 8**, or **[4, 8)**; integer values **4, 5, 6, 7**.
12. **P(X ≥ 5) = 1 − P(X ≤ 4)**.
13. **A ∪ B = {1, 2, 3, 4}**, **A ∩ B = {3}**, **Aᶜ = {4, 5, 6}**, and **(A ∪ B)ᶜ = {5, 6}**.
14. A only: 18 − 8 = **10**; B only: 14 − 8 = **6**; at least one: 18 + 14 − 8 = **24**; neither: 30 − 24 = **6**.
15. **Σxᵢ = 16**, **Σxᵢ² = 84**, **(Σxᵢ)² = 256**, and **x̄ = 4**.
16. Squared deviations are 9, 1, 1, 9; their sum is **20**. Sample variance is **20/3 ≈ 6.6667**.
17. 2×1 + 4×3 + 6×2 = **26**.
18. **6!/4! = 30**, **P(6, 2) = 30**, **C(6, 2) = 15**. Each unordered pair has 2! = 2 orderings.
19. (a) 10⁴ = **10,000**. (b) 10×9×8×7 = **5,040**.
20. C(4, 1)C(2, 1)/C(6, 2) = 8/15 ≈ **0.5333**.
21. C(5, 1)(0.2)(0.8)⁴ = 5×0.2×0.4096 = **0.4096**.
