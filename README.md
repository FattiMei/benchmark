# benchmark
Benchmark experiment in High Performance Computing


## Introduction
Testing the performance of code is an essential skill in software performance. It's easy to fall into slogans like "linked lists are bad" or "arrays are better than hashmaps" without even considering the fitting of those data structures to the target application.
Reality gives always the best feedbacks, so let's get comfortable in benchmarking.


## Objectives
This repository explores the benchmarking of numerical kernels: functions that operate on floating-point data, and have a single entry point. Nevertheless there are problems relevant to all benchmarking


## Problems
 1. The target application is run in a system with limited resources and concurrent processes that can't be controlled
 2. The fact that a kernel is consuming resources might affect its execution (see frequency scaling and thermal management)
 3. The very act of measuring execution time might introduce overhead (when kernel are so small the cost of handling timers is relevant, see microbenchmarks)


## Solution proposed
```pseudocode
for (int i = 0; i < SAMPLES; ++i) {
    start_timer();
    launch_kernel();
    stop_timer();

    double kernel_time = get_time_elapsed();
}
```
Pseudocode of a possible implementation, the solution is intended to be copy pasted and modified at hand.
In my previous experiments I used google benchmark, which is a fantastic tool for the job and also covers the tricky microbenchmarks, my solution strips all the features to make benchmarking as simple and portable as possible (better something than nothing at all)

In a modern fashion, a statistical analysis will then partially cover the fallacies of the measurement method (problems 1, 2 and 3)
