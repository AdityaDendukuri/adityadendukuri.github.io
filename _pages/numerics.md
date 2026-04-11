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
| [numerics](https://github.com/numerics-cpp/numerics) | Library — solvers, factorizations, eigenvalue methods, FFT |
| [numerics-apps](https://github.com/numerics-cpp/numerics-apps) | Simulations: SPH fluid, Navier-Stokes, Ising model, TDSE |

**Documentation**

| | |
|-|---|
| [API Reference](https://numerics-cpp.github.io/numerics/api/) | All classes, functions, and backends |
| [Performance Notes](https://numerics-cpp.github.io/numerics/api/page_performance.html) | Cache blocking, register tiling, SIMD — 13× over naive |
| [Benchmarks](https://numerics-cpp.github.io/numerics-report/) | Throughput tables and plots for every module |

**Theory**

Derivations, error bounds, and proofs for the algorithms implemented here:
[Scientific Computing Notes →](https://adityadendukuri.github.io/cs111-scientific-computing-notes/)

---

**Simulations built with numerics and raylib**

| | |
|-|---|
| **2D SPH Fluid** | Weakly compressible SPH with heat transport, rigid bodies, and particle injection. Tait EOS, cubic-spline kernel, Morris viscosity. |
| **3D SPH Fluid** | WCSPH with opposing hose jets, heat transport, and a free-orbit camera. |
| **Navier-Stokes** | Chorin projection on a staggered MAC grid. Semi-Lagrangian advection, matrix-free CG pressure solve. Kelvin-Helmholtz initial condition. |
| **Ising Model** | Metropolis dynamics on a 300×300 lattice with live temperature/field sliders. Umbrella-sampled nucleation reproducing Brendel et al. (2005). |
| **TDSE** | 2D time-dependent Schrödinger equation. Strang operator splitting, Crank-Nicolson kinetic sweeps, Lanczos eigendecomposition. Five interchangeable potentials. |
| **Electromagnetism** | DC current flow + magnetostatics on a 32³ voxel grid. Four Poisson problems solved with matrix-free CG. Interactive magnetic dipole. |
| **N-body** | Gravitational N-body dynamics with symplectic Verlet integration. |
