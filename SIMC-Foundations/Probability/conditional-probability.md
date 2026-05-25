---
tags:
  - simc
---

# Conditional Probability

> [!abstract] Prerequisites
> [[sample-spaces-events-axioms]] — assumes you know what a sample space, event, and probability function are.

## What it is

Conditional probability is the answer to a very specific kind of question:
==given that I already know event $B$ happened, what's the chance event $A$
also happens?== The notation is $P(A \mid B)$, read "the probability of $A$
given $B$." The bar always means "given."

The intuition is simple but it is the whole game: ==when you condition on $B$,
the sample space shrinks to $B$.== You throw away every outcome where $B$
didn't happen, and recompute probabilities inside what's left.

Two quick examples:

- **Weather.** $P(\text{rain tomorrow})$ might be 0.20 on an average day. But
  $P(\text{rain tomorrow} \mid \text{cloudy and humid today})$ might be 0.60.
  The condition changed what you know, so it changed the probability.
- **Cards.** Draw two cards from a 52-card deck without replacement.
  $P(\text{2nd is ace}) = 4/52$ if you know nothing. But
  $P(\text{2nd is ace} \mid \text{1st is ace}) = 3/51$, because once the first
  ace is gone, only 3 aces remain in a 51-card deck. The sample space literally
  shrank from 52 cards to 51, and from 4 aces to 3.

> [!info] The bar reads right-to-left
> $P(A \mid B)$ is "probability of $A$ **given** $B$." What you're solving
> for sits **left** of the bar; what you already know sits **right** of the bar.
> Flipping the sides flips the meaning.

## The formula

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad \text{provided } P(B) > 0$$

Why this works: among all the trials where $B$ happened (the denominator),
what fraction *also* had $A$ happen (the numerator)? That ratio IS the
conditional probability. We're rescaling: $P(B)$ used to be some number less
than 1, but conditional on $B$ it becomes 1 (the new whole), so we divide
everything inside the shrunken world by $P(B)$ to renormalize.

Geometrically: picture the sample space as a unit square. $B$ is some region
inside it with area $P(B)$. The overlap $A \cap B$ is a smaller region with
area $P(A \cap B)$. Once you condition on $B$, you zoom in so that $B$ fills
the entire viewport. The fraction of that viewport occupied by $A \cap B$ is
$P(A \cap B) / P(B)$.

> [!warning] The condition $P(B) > 0$ isn't decorative
> You cannot condition on an impossible event. If $P(B) = 0$, the formula
> divides by zero and the question "given $B$ happened" is meaningless
> because $B$ can never happen.

## The multiplication rule

Multiply both sides of the conditional probability formula by $P(B)$ and you
get the **multiplication rule**:

$$P(A \cap B) = P(A \mid B) \cdot P(B) = P(B \mid A) \cdot P(A)$$

It's the same equation, just rearranged. Use whichever form is convenient:

- Use $P(A \mid B) = P(A \cap B) / P(B)$ when you know the joint and the
  marginal and want the conditional.
- Use $P(A \cap B) = P(A \mid B) \cdot P(B)$ when you know the conditional
  and the marginal and want the joint.

Most "sequential events" problems are the second case — you build up the
joint probability of a sequence by multiplying conditionals.

