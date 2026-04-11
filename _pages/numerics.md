---
layout: page
title: numerics
permalink: /numerics/
nav: true
nav_order: 3
---

A C++ library for numerical linear algebra, ODE/PDE integration, spectral methods, and statistical simulation. Solvers share a common kernel with BLAS/SIMD primitives and tag-dispatched backends (seq, blocked, SIMD, OpenMP, CUDA).

---

**Repositories**

| | |
|-|---|
| [numerics](https://github.com/AdityaDendukuri/numerics) | Umbrella — CMake, docs, benchmarks |
| [numerics-core](https://github.com/AdityaDendukuri/numerics-core) | Solvers, factorizations, eigenvalue methods, FFT |
| [numerics-apps](https://github.com/AdityaDendukuri/numerics-apps) | Simulations: SPH fluid, Navier-Stokes, Ising model, TDSE |

**Documentation**

| | |
|-|---|
| [API Reference](https://adityadendukuri.github.io/numerics/api/) | All classes, functions, and backends |
| [Performance Notes](https://adityadendukuri.github.io/numerics/api/page_performance.html) | Cache blocking, register tiling, SIMD — 13× over naive |
| [Benchmarks](https://adityadendukuri.github.io/numerics/report/index.html) | Throughput tables and plots for every module |

**Theory**

Derivations, error bounds, and proofs for the algorithms implemented here:
[Scientific Computing Notes →](https://adityadendukuri.github.io/cs111-scientific-computing-notes/)
