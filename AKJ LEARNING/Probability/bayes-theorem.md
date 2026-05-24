---
tags:
  - simc
---

# Bayes' Theorem

> [!abstract] Prerequisites
> [[conditional-probability]] — Bayes' theorem is derived directly from the conditional probability formula; the whole proof is one line of algebra once that's in your bones.
> [[sample-spaces-events-axioms]] — events and the probability function are the underlying machinery.

## What it is

Bayes' theorem is the math of ==updating your beliefs when you see new evidence==. It's how a rational agent should change their mind in the face of data.

Picture a doctor diagnosing a patient. Before any tests, she has a hunch about how likely the disease is — maybe based on the patient's age, symptoms, and how common the disease is in the population. That's her ==prior== belief. Then a test comes back positive. The test isn't perfect — it has some false-positive rate and some false-negative rate. The question is: given this positive result, what should the doctor now believe?

Bayes' theorem answers that. It takes the prior belief, weights it by how well the evidence agrees with each hypothesis (the ==likelihood==), normalizes the result, and produces an updated belief — the ==posterior==. That's the whole story:

> prior + likelihood + new evidence $\longrightarrow$ posterior

Every "this data updates my model" calculation in statistics, machine learning, and scientific inference is — at heart — Bayes.

## The formula

$$P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$$

This drops out of conditional probability almost for free. From the definition of conditional probability:

$$P(A \cap B) = P(A \mid B) \cdot P(B)$$

But the same joint event can be written the other way around:

$$P(A \cap B) = P(B \mid A) \cdot P(A)$$

These two expressions describe the same thing, so equate them:

$$P(A \mid B) \cdot P(B) = P(B \mid A) \cdot P(A)$$

Divide both sides by $P(B)$ and you have Bayes' theorem. ==The whole theorem is just the symmetry of joint probability solved for $P(A \mid B)$.== That's it. No deep magic — just bookkeeping.

## The prior / likelihood / posterior decomposition

The four pieces of Bayes' theorem each have a name and a role:

| Term       | Notation      | What it means                                                    |
| ---------- | ------------- | ---------------------------------------------------------------- |
| Prior      | $P(A)$        | What you believed about $A$ **before** seeing evidence           |
| Likelihood | $P(B \mid A)$ | How likely the evidence $B$ would be **if** $A$ were true        |
| Evidence   | $P(B)$        | Total probability of observing $B$ at all (normalizing constant) |
| Posterior  | $P(A \mid B)$ | What you should believe about $A$ **after** seeing $B$           |

The evidence term $P(B)$ is usually computed using the ==law of total probability==, expanding over all hypotheses:

$$P(B) = P(B \mid A) \cdot P(A) + P(B \mid \neg A) \cdot P(\neg A)$$

> [!info] Why "normalizing constant"
> $P(B)$ doesn't depend on which hypothesis you're testing — it's the same denominator whether you're computing $P(A \mid B)$ or $P(\neg A \mid B)$. Its job is to make the posteriors over all hypotheses sum to 1. If you ever just want to compare two hypotheses, you can ignore $P(B)$ entirely and work with ratios — that's the "odds form" of Bayes.

