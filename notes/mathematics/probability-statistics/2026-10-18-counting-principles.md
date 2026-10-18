# Probability & Statistics — Outcomes, Events and Counting Principles

**Date:** 2026-10-18

**Subject:** SMA2306 Probability & Statistics

**Learning source:** YouTube Probability & Statistics series, including the second video's counting-principles section. Exact video title/link not yet recorded.

**Status:** Learning — concepts introduced and discussed through worked examples.

## Concept

Describe the possible results of a random experiment, identify an event, and count outcomes consistently before calculating probability.

## Notes

### Random experiments and sample spaces

A random experiment is a process whose result is uncertain before it happens. An **outcome** is one complete possible result. The **sample space** contains all possible outcomes.

Flipping a coin twice gives the sample space `{HH, HT, TH, TT}`, where H means heads and T means tails. `HT` and `TH` are different outcomes when order is recorded: heads then tails differs from tails then heads.

An **event** is a subset of the sample space. For example, "exactly one head" is `{HT, TH}`. Favorable outcomes are those that satisfy the event.

### Classical probability

For a finite sample space with equally likely outcomes:

```text
P(A) = favorable outcomes / total equally likely outcomes
```

Use the same counting convention for the numerator and denominator, including whether order matters.

### Counting principles

Let n be the number of distinct available items and r the number of selections or positions.

| Situation | Formula | Reason |
|---|---|---|
| Ordered selections with repetition | `n^r` | Each of the r positions has n choices. |
| Permutations without repetition | `n! / (n-r)!` | Order matters; each selection leaves one fewer item available. |
| Combinations without repetition | `n! / (r!(n-r)!)` | Order is ignored; divide the ordered count by the r! arrangements of each selection. |

First ask whether changing the order changes the result, then whether an item can be selected again. For selections without repetition, `0 ≤ r ≤ n`; n and r are whole numbers. Unordered selections with repetition require a different formula from these three.

### Permutations versus combinations

The card arrangements `{1,2,3,4,5}` and `{3,2,4,5,1}` represent the same combination when order is ignored: they contain the same five cards. When order matters, the sequences `(1,2,3,4,5)` and `(3,2,4,5,1)` are distinct. Braces denote sets, which do not record order; parentheses here make the sequence order explicit.

**Without repetition** means the same physical item cannot be selected again. Two cards of the same rank but different suits are different physical items.

### Factorials and cancellation

For a positive whole number n, `n!` ("n factorial") means multiplying all whole numbers from n down to 1. For example, `5! = 5 × 4 × 3 × 2 × 1 = 120`. By definition, `0! = 1`.

Expand only as far as needed to cancel common factors:

```text
52! / 47! = (52 × 51 × 50 × 49 × 48 × 47!) / 47!
           = 52 × 51 × 50 × 49 × 48
```

Cancel the shared factor `47!`; do not subtract factorials or cancel terms across addition.

### Important distinction

Counting principles determine the **number of possible outcomes**. The **Law of Total Probability** uses conditional probabilities across exhaustive, non-overlapping cases: the cases cover the whole sample space and cannot happen together.

For cases B₁, ..., Bₖ with positive probabilities:

```text
P(A) = P(A | B₁)P(B₁) + ... + P(A | Bₖ)P(Bₖ)
```

Here `P(A | Bᵢ)` means the probability of A given case Bᵢ. Counting principles and the Law of Total Probability are different mathematical concepts.

## Worked examples

### Two fair dice: at least one 5

Roll two independent fair six-sided dice and record `(first die, second die)`. There are `6 × 6 = 36` equally likely ordered outcomes.

For the event "at least one die shows 5":

- First die is 5: `(5,1), (5,2), (5,3), (5,4), (5,5), (5,6)` — 6 outcomes.
- Second die is 5 and the first is not: `(1,5), (2,5), (3,5), (4,5), (6,5)` — 5 more outcomes.

There are `6 + 5 = 11` favorable outcomes. Count `(5,5)` only once, so `P(at least one 5) = 11/36`.

### Five-card hands

A five-card hand from a standard 52-card deck ignores order and does not select the same physical card twice, so use combinations:

```text
C(52,5) = 52! / (5! × 47!)
        = (52 × 51 × 50 × 49 × 48) / 120
        = 2,598,960
```

The `47!` factors cancel. Dividing by `5! = 120` removes the 120 orderings of each five-card hand.

## Independent practice

No independent exercises or quiz results are recorded for this session.

**Next session:** Practice counting, permutation, and combination questions independently before continuing the video series. State whether order matters and repetition is allowed before choosing each formula.

## Review

Status remains **Learning**. Independent application and later review are pending; these worked examples do not establish mastery.

Related tracking: [Progress](../../../PROGRESS.md) and [Mathematics roadmap](../../../MATHEMATICS.md).
