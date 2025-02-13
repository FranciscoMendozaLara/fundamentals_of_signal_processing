# Chapter 2: Fundamentals of Signals and Systems

Welcome to Chapter 2! In this chapter, we dive into the core concepts that form the backbone of signal processing: understanding signals and systems, how they are represented, and the fundamental operation of convolution. These topics are essential as they set the stage for all the advanced techniques we'll explore in later chapters.

---

## 2.1 Overview

In this chapter, we will cover:
- **Signals:** Definitions, characteristics, and representations.
- **Continuous vs. Discrete Signals:** How analog signals are sampled to create digital representations.
- **Systems:** An introduction to systems, with a focus on linear time-invariant (LTI) systems.
- **Convolution:** The fundamental operation that describes how systems process signals.

Understanding these concepts will help you build a strong foundation in signal processing and prepare you for more advanced topics like frequency analysis and filtering.

---

## 2.2 What is a Signal?

A **signal** is any function that conveys information about a physical phenomenon. Signals can be:
- **Analog (Continuous):** Defined for every point in time.
- **Digital (Discrete):** Defined only at specific time intervals obtained via sampling.

### Key Signal Characteristics:
- **Amplitude:** The value or strength of the signal.
- **Time:** The independent variable (e.g., seconds).
- **Frequency:** The rate of oscillation, important for analyzing signal content.

---

## 2.3 Continuous vs. Discrete Signals

### Continuous Signals
- Represented by functions such as:

  $$x(t) = \sin(2\pi f t)$$
  
- Defined for every time instance.

### Discrete Signals
- Result from sampling a continuous signal:
  
  $$x[n] = x(nT)$$

  where $$T$$ is the sampling period.
- Only defined at discrete time points.

**Interactive Example:**
Experiment with plotting a continuous sine wave and its discrete sample points. Check out our interactive scripts in the `examples/` folder for hands-on visualization.

---

## 2.4 Systems and Their Properties

A **system** takes an input signal and produces an output signal. In signal processing, we often work with **Linear Time-Invariant (LTI) Systems** which exhibit:
- **Linearity:** The output for a weighted sum of inputs is the weighted sum of the outputs.
- **Time-Invariance:** The system's behavior does not change over time.

### Impulse Response
An LTI system is fully characterized by its **impulse response** $$h(t)$$. Given an input $$x(t)$$, the output $$y(t)$$ is determined by:

$$y(t) = (x * h)(t) = \int_{-\infty}^{\infty} x(\tau) \, h(t - \tau) \, d\tau$$

---

## 2.5 Convolution: The Heart of LTI Systems

### What is Convolution?
Convolution is a mathematical operation that blends two functions to produce a third function that expresses how the shape of one is modified by the other.

- **Continuous Convolution:**
  $$y(t) = \int_{-\infty}^{\infty} x(\tau) \, h(t - \tau) \, d\tau$$

- **Discrete Convolution:**
  $$y[n] = \sum_{k=-\infty}^{\infty} x[k] \, h[n-k]$$

### Why is Convolution Important?
- **System Analysis:**  
  It allows us to determine the output of an LTI system given any arbitrary input.
- **Filtering:**  
  Many filtering operations (e.g., low-pass, high-pass) are implemented via convolution.

**Interactive Example:**
Run [1_visualizing_convolution.py](./examples/1_visualizing_convolution.py) to see a visual demonstration of convolution in action.

---

## 2.6 Interactive Exploration

Throughout this chapter, we encourage you to explore the interactive examples:
- **Signal Visualization:**  
  Plot continuous signals and their discrete counterparts.
- **System Response:**  
  Use convolution to analyze how a system’s impulse response affects the input.
- **Hands-On Exercises:**  
  Modify parameters in the provided Python scripts and observe how the output changes.

These experiments, available in the `examples/` folder, are designed to solidify your understanding of these fundamental concepts.

---

## 2.7 Exercises

Test your knowledge with these exercises:

1. **Signal Representation:**
   - Plot a continuous sine wave for a specific frequency.
   - Sample the sine wave at different sampling rates and observe the differences.

2. **Impulse Response and Convolution:**
   - Define an LTI system with a given impulse response.
   - Use convolution to calculate the output for a chosen input signal.
   - Verify your result by comparing with a Python simulation.

3. **Convolution Practice:**
   - Manually compute the convolution of two simple discrete signals (e.g., [1, 2, 3] and [0, 1, 0.5]) and then confirm your calculations using a Python script.

---

## 2.8 Summary

In this chapter, you learned:
- What signals are and how they can be represented.
- The differences between continuous and discrete signals.
- The basics of systems and the significance of LTI properties.
- The convolution operation and its central role in signal processing.

These fundamentals are the building blocks for the more advanced topics we will cover in later chapters. Mastering these concepts will enable you to better understand and implement techniques like the Fourier Transform, filtering, and feature extraction.

---

Next, we will explore the **Fourier Transform and Frequency Domain Analysis** in Chapter 3. Make sure to experiment with the provided examples and complete the exercises to reinforce your learning.