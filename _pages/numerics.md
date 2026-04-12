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
| [numerics](https://github.com/AdityaDendukuri/numerics) | Library — solvers, factorizations, eigenvalue methods, FFT |
| [numerics-apps](https://github.com/AdityaDendukuri/numerics-apps) | Simulations: SPH fluid, Navier-Stokes, Ising model, TDSE |

**Documentation**

| | |
|-|---|
| [API Reference](https://adityadendukuri.github.io/numerics/api/) | All classes, functions, and backends |
| [Performance Notes](https://adityadendukuri.github.io/numerics/api/page_performance.html) | Cache blocking, register tiling, SIMD — 13× over naive |
| [Benchmarks](https://adityadendukuri.github.io/numerics/report/) | Throughput tables and plots for every module |

**Theory**

Derivations, error bounds, and proofs for the algorithms implemented here:
[Scientific Computing Notes →](https://adityadendukuri.github.io/Scientific-Computing-Notes/)

---

**Simulations built with numerics and raylib**

<div style="display:grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-top: 1rem;">

<div>
<video autoplay loop muted playsinline style="width:100%; border-radius:6px;">
  <source src="/assets/video/fluid_sim_record.mp4" type="video/mp4">
</video>
<p style="font-size:0.82rem; color:#888; margin-top:4px;"><strong>2D SPH Fluid</strong> — dam-break, heat transfer, rigid body</p>
</div>

<div>
<video autoplay loop muted playsinline style="width:100%; border-radius:6px;">
  <source src="/assets/video/fluid_sim_3d_record.mp4" type="video/mp4">
</video>
<p style="font-size:0.82rem; color:#888; margin-top:4px;"><strong>3D SPH Fluid</strong> — dual temperature hoses, free-orbit camera</p>
</div>

<div>
<video autoplay loop muted playsinline style="width:100%; border-radius:6px;">
  <source src="/assets/video/ns_demo_record.mp4" type="video/mp4">
</video>
<p style="font-size:0.82rem; color:#888; margin-top:4px;"><strong>Navier-Stokes</strong> — Kelvin-Helmholtz instability, particle tracers</p>
</div>

<div>
<video autoplay loop muted playsinline style="width:100%; border-radius:6px;">
  <source src="/assets/video/tdse_record.mp4" type="video/mp4">
</video>
<p style="font-size:0.82rem; color:#888; margin-top:4px;"><strong>Schrödinger Equation</strong> — double-slit diffraction, Strang splitting</p>
</div>

<div>
<video autoplay loop muted playsinline style="width:100%; border-radius:6px;">
  <source src="/assets/video/ising_record.mp4" type="video/mp4">
</video>
<p style="font-size:0.82rem; color:#888; margin-top:4px;"><strong>Ising Nucleation</strong> — free-energy barrier crossing, umbrella sampling</p>
</div>

<div>
<video autoplay loop muted playsinline style="width:100%; border-radius:6px;">
  <source src="/assets/video/em_demo_record.mp4" type="video/mp4">
</video>
<p style="font-size:0.82rem; color:#888; margin-top:4px;"><strong>Electromagnetism</strong> — Poisson solve, B-field, orbiting dipole</p>
</div>

<div>
<video autoplay loop muted playsinline style="width:100%; border-radius:6px;">
  <source src="/assets/video/gal.mp4" type="video/mp4">
</video>
<p style="font-size:0.82rem; color:#888; margin-top:4px;"><strong>Galaxy Collapse</strong> — N-body gravity, symplectic Verlet, merging bodies</p>
</div>

<div>
<video autoplay loop muted playsinline style="width:100%; border-radius:6px;">
  <source src="/assets/video/quantum_demo_record.mp4" type="video/mp4">
</video>
<p style="font-size:0.82rem; color:#888; margin-top:4px;"><strong>Quantum Circuits</strong> — Bell, GHZ, Grover, teleportation, QFT</p>
</div>

</div>
