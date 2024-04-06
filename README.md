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

In a modern fashion, a statistical analysis will then partially cover the fallacies of the measurement method. It also helps if the tests are run on a machine with few and light processes, in the ideal world the target program would be the ONLY program running on the machine, see experiments like [tetris OS](https://github.com/lucianoforks/tetris-os)


## Statistical analysis
The sample dataset `bench.txt` shows such features:

 * most of the measurements reflect the actual kernel time
 * spikes signal the intervention of the operating system, therefore the measure is not significant for the benchmark
 * there is variability in adjacent measures (see zoomed plot)

The first solution that comes to mind is computing the following statistics:
 * *mean*: affected by the concurrent processes, but the majority of samples are "true"
 * *median*: stable to outliers, provides an accurate information about the kernel
 * *minimum*: the best performance
 * *variance*: still don't know its purpuose in the experiment

Given two benchmark datasets, those number will be sufficient to decide whether an optimization is improving the execution speed. I'm sure there are better statistical methods, open a pull request if you have a good idea! Here is a list of interesting research questions:
 * find if performance is slowly degrading (it means that the kernel times are growing over the number of samples)
 * given a dataset, find the optimal number of samples to take without compromizing the statistical properties of the data (benchmarks are expensive, the dataset `bench.txt` took 7 hours to make)
