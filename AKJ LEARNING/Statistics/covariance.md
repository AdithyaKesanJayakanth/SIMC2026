---
tags:
  - simc
---

# Covariance

> [!abstract] In one line
> Covariance measures whether two features rise and fall together — it is the signed version of variance extended to pairs of features.

## The idea

[[variance]] told you how spread out *one* feature is. Covariance asks about *two* features: **do they move together?**

Picture a dataset of people. Height and weight tend to be positively correlated — tall people tend to be heavier. When height is above its mean, weight tends to be above its mean too. Their covariance is positive.

Now picture height and resting heart rate — no consistent relationship. Sometimes a tall person has a high heart rate, sometimes low. Those two features vary independently. Their covariance is near zero.

If feature A goes up whenever feature B goes down (and vice versa), they are negatively correlated. Covariance is negative.

**Intuition for the sign:**
- $(x_i - \bar{x})$ is positive when $x$ is above its mean, negative when below
- $(y_i - \bar{y})$ similarly
- Their product is positive when both deviate in the **same direction**, negative when they deviate in **opposite directions**
- Averaging those products over all observations gives you the covariance

