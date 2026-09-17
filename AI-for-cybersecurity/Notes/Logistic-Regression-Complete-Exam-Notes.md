# Logistic Regression — Complete Exam Notes

## 1. What is Logistic Regression?

**Logistic Regression is a supervised machine learning classification algorithm used to predict the probability of an observation belonging to a particular class.**

Although its name contains the word **"regression"**, logistic regression is primarily used for **classification**.

For example:

* Will a student **Pass or Fail**?
* Is an email **Spam or Not Spam**?
* Is a transaction **Fraudulent or Genuine**?
* Does a patient have a particular disease **Yes or No**?

For binary classification, the output classes are usually represented as:

```text
0 → Class 0
1 → Class 1
```

The important point is:

> Logistic regression does not directly predict 0 or 1. It first calculates a score and converts that score into a probability between 0 and 1.

---

# 2. Basic Idea

Suppose we want to predict whether a student will pass based on:

* Study hours
* Attendance

Our input might be:

```text
X₁ = Study Hours
X₂ = Attendance
```

The logistic regression model first calculates a **linear score**:

$$
z = \beta_0 + \beta_1X_1 + \beta_2X_2
$$

where:

* \(\beta_0\) = intercept
* \(\beta_1,\beta_2\) = model coefficients
* \(X_1,X_2\) = input features
* \(z\) = linear score

However, \(z\) can have any value:

```text
-∞  --------  0  --------  +∞
```

So \(z\) itself is **not a probability**.

Logistic regression passes this score through the **sigmoid function**.

---

# 3. Sigmoid Function

The sigmoid function is:

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

It converts any real-valued number into a value between:

$$
0 \text{ and } 1
$$

### Examples

If:

$$
z=0
$$

then:

$$
\sigma(0)=0.5
$$

If:

$$
z=2
$$

then:

$$
\sigma(2)\approx0.881
$$

If:

$$
z=-2
$$

then:

$$
\sigma(-2)\approx0.119
$$

Therefore:

| Linear score \(z\) | Sigmoid output |
| -----------------: | -------------: |
|                 -5 |         0.0067 |
|                 -2 |          0.119 |
|                  0 |            0.5 |
|                  2 |          0.881 |
|                  5 |          0.993 |

The sigmoid function therefore gives us a value that can be interpreted as a **probability**.

---

# 4. Complete Logistic Regression Formula

The complete model can be written as:

$$
P(Y=1|X)=\frac{1}{1+e^{-(\beta_0+\beta_1X_1+\beta_2X_2+\cdots+\beta_nX_n)}}
$$

The process is:

```text
Input Features
     ↓
Linear Combination
z = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ
     ↓
Sigmoid Function
P = 1 / (1 + e⁻ᶻ)
     ↓
Probability between 0 and 1
     ↓
Apply threshold
     ↓
Class 0 or Class 1
```

---

# 5. How Classification Happens

Suppose the model produces:

$$
P(Y=1)=0.85
$$

Using the common threshold:

$$
0.5
$$

we classify:

```text
Probability ≥ 0.5 → Class 1
Probability < 0.5 → Class 0
```

Therefore:

```text
0.85 ≥ 0.5
→ Class 1
```

Another example:

$$
P(Y=1)=0.23
$$

Since:

```text
0.23 < 0.5
```

the prediction is:

```text
Class 0
```

---

# 6. Why is it Called "Logistic" Regression?

The name comes from the **logistic function**, which is the sigmoid function:

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

The model is called regression because it models the relationship between the input variables and the **log odds** of the outcome.

---

# 7. What are Odds?

Probability and odds are related but different.

If the probability of an event is:

$$
P=0.8
$$

then the odds are:

$$
Odds=\frac{P}{1-P}
$$

Therefore:

$$
Odds=\frac{0.8}{0.2}=4
$$

This means the odds are:

$$
4:1
$$

---

# 8. What are Log Odds?

Taking the natural logarithm of the odds gives **log odds**, also called **logit**.

$$
LogOdds=\ln\left(\frac{P}{1-P}\right)
$$

Logistic regression assumes:

$$
\ln\left(\frac{P}{1-P}\right)
=
\beta_0+\beta_1X_1+\cdots+\beta_nX_n
$$

This is one of the most important equations to understand.

In simple terms:

> Logistic regression assumes that the features have a linear relationship with the **log odds**, not directly with the probability.

---

# 9. Why Do We Need Logistic Regression?

## The problem with classification

Suppose we want to classify students:

```text
0 → Fail
1 → Pass
```

We might think:

> Why not simply use linear regression?

Linear regression produces a continuous numerical output.

For example:

```text
0.2
0.4
0.7
1.0
1.3
1.8
```

But classification requires something like:

```text
Fail → 0
Pass → 1
```

The problem is that linear regression can produce values:

```text
< 0
```

or

```text
> 1
```

For example:

```text
-0.4
1.3
1.8
```

These cannot be interpreted as probabilities.

A probability must always satisfy:

$$
0\leq P\leq1
$$

Logistic regression solves this problem using the sigmoid function.

---

# 10. Linear Regression vs Logistic Regression

## Linear Regression

Linear regression predicts a continuous numerical value.

Example:

```text
Hours studied → Exam Score
```

Possible predictions:

```text
72.4
81.7
91.2
```

Mathematical form:

$$
y=\beta_0+\beta_1X
$$

It is suitable for:

* House price prediction
* Temperature prediction
* Salary prediction
* Sales prediction

---

## Logistic Regression

Logistic regression predicts the probability of a class.

Example:

```text
Hours studied → Probability of Passing
```

Possible output:

```text
0.82
```

Then:

```text
0.82 ≥ 0.5
→ Pass
```

Mathematical form:

$$
P(Y=1|X)=\sigma(\beta_0+\beta_1X)
$$

---

# 11. Why Can't We Simply Use Linear Regression for Classification?

There are several important reasons.

## Problem 1 — Output is not restricted to 0 and 1

Linear regression can produce:

```text
-2.4
0.6
1.4
3.2
```

The values -2.4 and 3.2 cannot represent probabilities.

Logistic regression always produces:

$$
0<P<1
$$

---

## Problem 2 — Probability interpretation

Suppose:

```text
Linear Regression → 1.7
```

What does 1.7 mean?

It cannot mean:

```text
170% probability
```

because probability cannot exceed 1.

Logistic regression gives:

```text
0.91
```

which can naturally be interpreted as approximately:

```text
91% probability of Class 1
```

---

## Problem 3 — Squared error is not ideal for classification

Linear regression commonly uses **Mean Squared Error (MSE)**:

$$
MSE=\frac{1}{n}\sum(y_i-\hat y_i)^2
$$

This loss function does not properly represent the classification problem.

Consider:

```text
Classification boundary = 50
```

Suppose two points are:

```text
X = 1
X = 10
```

Depending on the fitted line, squared error may assign a larger penalty to a point based on vertical distance from the regression line, rather than how its position relates to the classification boundary.

The important exam point is:

> The squared-error loss used by linear regression does not accurately reflect the classification objective.

Logistic regression instead uses a classification-appropriate loss, commonly **log loss / cross-entropy loss**.

---

# 12. Decision Boundary

The **decision boundary** is the point or line where the model changes from one class to another.

For binary logistic regression with a threshold of 0.5:

$$
P(Y=1)=0.5
$$

Since:

$$
\sigma(0)=0.5
$$

the decision boundary occurs when:

$$
z=0
$$

Therefore:

$$
\beta_0+\beta_1X_1+\beta_2X_2+\cdots+\beta_nX_n=0
$$

This is a **linear decision boundary**.

---

# 13. Example of a Decision Boundary

Suppose:

$$
z=-10+2X
$$

The boundary occurs when:

$$
z=0
$$

Therefore:

$$
-10+2X=0
$$

$$
2X=10
$$

$$
X=5
$$

So:

```text
X < 5  → Class 0
X > 5  → Class 1
```

The exact class depends on the sign and threshold, but the key idea is:

> Logistic regression creates a linear decision boundary in the feature space.

---

# 14. Example with Student Data

Suppose:

```text
X₁ = Study Hours
X₂ = Attendance
```

and the trained model is:

$$
z=-8+1.2X_1+0.08X_2
$$

For a student with:

```text
Study Hours = 5
Attendance = 80%
```

we calculate:

$$
z=-8+(1.2)(5)+(0.08)(80)
$$

$$
z=-8+6+6.4
$$

$$
z=4.4
$$

Now apply sigmoid:

$$
P=\frac{1}{1+e^{-4.4}}
$$

$$
P\approx0.988
$$

Therefore:

```text
Probability of Class 1 ≈ 98.8%
```

Using a threshold of 0.5:

```text
0.988 > 0.5
→ Class 1
```

So the model predicts:

```text
PASS
```

---

# 15. What Does a Coefficient Mean?

One of the major advantages of logistic regression is that the model is relatively interpretable.

Suppose:

$$
z=\beta_0+\beta_1X_1
$$

If:

$$
\beta_1>0
$$

then increasing \(X_1\) increases the **log odds** of Class 1.

If:

$$
\beta_1<0
$$

then increasing \(X_1\) decreases the **log odds** of Class 1.

Therefore:

```text
Positive coefficient
→ increases log odds of Class 1

Negative coefficient
→ decreases log odds of Class 1
```

Important:

> A coefficient does not directly mean the probability increases by that many units.

It affects the **log odds**.

---

# 16. Odds Ratio

The coefficient can also be interpreted through the odds ratio.

For a coefficient \(\beta_j\):

$$
Odds\ Ratio=e^{\beta_j}
$$

For example, if:

$$
\beta_j=0.693
$$

then:

$$
e^{0.693}\approx2
$$

This means that a one-unit increase in that feature multiplies the odds of Class 1 by approximately 2, assuming other variables remain constant.

---

# 17. Training Logistic Regression

During training, logistic regression learns:

$$
\beta_0,\beta_1,\beta_2,\ldots,\beta_n
$$

The model chooses coefficients that make the predictions fit the training data.

Instead of ordinary least squares used by standard linear regression, logistic regression is commonly trained using **maximum likelihood estimation (MLE)**, often implemented through optimization of the **log-loss/cross-entropy objective**.

---

# 18. Log Loss / Cross-Entropy Loss

For binary classification:

$$
L=
-\left[
y\log(p)+(1-y)\log(1-p)
\right]
$$

where:

* \(y\) = actual class
* \(p\) = predicted probability

For multiple observations:

$$
J(\beta)
=
-\frac{1}{n}
\sum_{i=1}^{n}
[
y_i\log(p_i)+(1-y_i)\log(1-p_i)
]
$$

The training process tries to **minimize this loss**.

---

# 19. Why is Log Loss Useful?

Suppose the actual class is:

```text
y = 1
```

Prediction A:

```text
p = 0.95
```

This is a good prediction, so the loss is small.

Prediction B:

```text
p = 0.01
```

This is a very confident wrong prediction, so the loss is very large.

Thus, log loss strongly penalizes confident incorrect predictions.

---

# 20. Where is Logistic Regression Used?

Logistic regression is widely used when the target is categorical, particularly for binary classification.

### 1. Spam Detection

Input features could include:

* Number of suspicious words
* Number of links
* Sender information
* Message characteristics

Output:

```text
0 → Not Spam
1 → Spam
```

---

### 2. Medical Diagnosis

Input:

```text
Age
Blood pressure
Test results
Other features
```

Output:

```text
0 → Disease absent
1 → Disease present
```

The model can produce:

```text
P(Disease)=0.87
```

---

### 3. Fraud Detection

Input:

```text
Transaction amount
Transaction frequency
Location-related features
Account activity
```

Output:

```text
0 → Genuine
1 → Fraud
```

---

### 4. Student Pass/Fail Prediction

Input:

```text
Study hours
Attendance
Internal marks
Assignment performance
```

Output:

```text
0 → Fail
1 → Pass
```

---

### 5. Customer Churn

Input:

```text
Usage
Subscription duration
Number of complaints
Payment history
```

Output:

```text
0 → Will stay
1 → May churn
```

---

### 6. Credit Risk

Input:

```text
Income
Credit history
Debt
Previous payments
```

Output:

```text
0 → Low/default-free outcome
1 → Default/risk class
```

The exact target definition depends on the application.

---

# 21. Binary vs Multiclass Logistic Regression

## Binary Logistic Regression

Used when there are two classes.

Example:

```text
Spam / Not Spam
Pass / Fail
Fraud / Genuine
```

Output:

$$
P(Y=1)
$$

---

## Multiclass Logistic Regression

Logistic regression can also be extended to multiple classes.

Example:

```text
Class 0 → Low Risk
Class 1 → Medium Risk
Class 2 → High Risk
```

A common approach is **multinomial logistic regression**.

Another commonly used strategy is **one-vs-rest (OvR)**.

---

# 22. Important Assumptions of Logistic Regression

These are particularly important for examinations.

## 1. Linearity in the log odds

Logistic regression assumes that the predictors have a **linear relationship with the log odds** of the outcome.

It does **not** require the probability itself to be linearly related to the features.

Correct statement:

> Logistic regression assumes linearity between the independent variables and the log odds of the dependent variable.

---

## 2. Little or no multicollinearity

Features should not be highly correlated with each other.

For example:

```text
Age in years
Age in months
```

contain almost the same information.

This creates **multicollinearity**.

High multicollinearity can make coefficient estimates unstable and difficult to interpret.

---

## 3. Independent observations

The observations should generally be independent of each other, unless the model is specifically designed to handle dependence.

---

## 4. Adequate sample size

Logistic regression can require a sufficiently large sample for reliable parameter estimation.

Maximum likelihood estimates can be unstable with small datasets, particularly with sparse data or separation.

---

# 23. Advantages of Logistic Regression

Logistic regression is popular because:

### 1. Simple

The model is mathematically concise.

### 2. Fast

It can be trained and evaluated efficiently.

### 3. Scalable

It can work with very large numbers of features.

### 4. Interpretable

The effect of individual features can be examined through their coefficients and odds ratios.

### 5. Probability output

It naturally produces probabilities between 0 and 1.

### 6. Efficient prediction

Once trained, prediction is computationally inexpensive.

For a feature vector \(X\), scoring mainly involves a dot product followed by the sigmoid function.

### 7. Distributed training

Logistic regression can be trained efficiently in distributed machine-learning systems.

---

# 24. Limitations of Logistic Regression

### 1. Linear decision boundary

Standard logistic regression produces a linear decision boundary.

Therefore, it may perform poorly when the true relationship is highly nonlinear.

### 2. Sensitive to multicollinearity

Highly correlated features can make coefficients unstable.

### 3. Requires appropriate feature representation

If the relationship between features and the log odds is nonlinear, feature engineering or transformations may be required.

### 4. Can struggle with complex relationships

For highly complex classification problems, methods such as:

* Decision Trees
* Random Forests
* Gradient Boosting
* Neural Networks

may capture nonlinear patterns more naturally.

### 5. Small datasets can cause unstable estimates

Maximum likelihood estimation can be problematic when there are too few observations or when classes are nearly perfectly separated.

---

# 25. Logistic Regression vs Linear Regression

| Property              | Linear Regression                    | Logistic Regression                               |
| --------------------- | ------------------------------------ | ------------------------------------------------- |
| Main purpose          | Regression                           | Classification                                    |
| Target                | Continuous numerical value           | Categorical outcome                               |
| Typical binary target | Not appropriate                      | Appropriate                                       |
| Output                | Any real number                      | Probability between 0 and 1                       |
| Function              | Linear function                      | Sigmoid/logistic function applied to linear score |
| Example               | Predict salary                       | Predict whether employee leaves                   |
| Decision boundary     | Not its primary purpose              | Linear boundary                                   |
| Common loss           | Mean Squared Error                   | Log loss / Cross-Entropy                          |
| Training              | Ordinary Least Squares commonly used | Maximum Likelihood / numerical optimization       |
| Probability output    | Not guaranteed                       | Yes                                               |
| Interpretability      | High                                 | High                                              |

---

# 26. Linear Regression vs Logistic Regression — Simple Example

Suppose we want to predict whether a student passes.

### Linear Regression

We encode:

```text
Fail = 0
Pass = 1
```

The model might predict:

```text
Student A → -0.2
Student B → 0.7
Student C → 1.4
```

Problems:

```text
-0.2 → impossible probability
1.4  → impossible probability
```

We could apply a threshold, but the model and its squared-error objective are not designed specifically for classification.

---

### Logistic Regression

The model might produce:

```text
Student A → 0.08
Student B → 0.65
Student C → 0.94
```

All outputs are valid probabilities.

Using:

$$
Threshold=0.5
$$

we obtain:

```text
0.08 → Fail
0.65 → Pass
0.94 → Pass
```

This is why logistic regression is better suited to binary classification.

---

# 27. Feature Scaling

Logistic regression does not mathematically require every feature to be between -1 and +1.

However, **feature scaling can be useful**, especially when features have very different numerical ranges.

For example:

```text
Age             = 22
Annual income   = 800000
Experience      = 2
```

The scales are very different.

A common method is **standardization (Z-score scaling)**:

$$
z=\frac{x
$$
