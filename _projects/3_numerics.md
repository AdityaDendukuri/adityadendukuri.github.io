---
layout: page
title: Numerics — Scientific Computing Library
description: C++ library for numerical analysis, simulation, and visualization
img: assets/img/projects/numerics_thumb.jpg
importance: 1
category: software
---

[**numerics**](https://adityadendukuri.github.io/numerics/) is a C++ library consolidating numerical analysis coursework, algorithms, and performance optimizations built over several years. It covers sparse linear algebra, ODE/PDE solvers, SPH fluid dynamics, quantum circuit simulation, stochastic MCMC methods, and more.

The videos below are rendered directly from the library's simulation apps using raylib + ffmpeg.

---

### Fluid Dynamics

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    <video autoplay loop muted playsinline class="img-fluid rounded z-depth-1">
      <source src="/assets/video/fluid_sim_record.mp4" type="video/mp4">
    </video>
    <div class="caption">2D SPH fluid — dam-break with hot/cold spheres and heat transfer.</div>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <video autoplay loop muted playsinline class="img-fluid rounded z-depth-1">
      <source src="/assets/video/fluid_sim_3d_record.mp4" type="video/mp4">
    </video>
    <div class="caption">3D SPH fluid — dual temperature hoses, particle color = temperature.</div>
  </div>
</div>

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    <video autoplay loop muted playsinline class="img-fluid rounded z-depth-1">
      <source src="/assets/video/ns_demo_record.mp4" type="video/mp4">
    </video>
    <div class="caption">Navier-Stokes — Kelvin-Helmholtz shear instability with particle tracers.</div>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <video autoplay loop muted playsinline class="img-fluid rounded z-depth-1">
      <source src="/assets/video/em_demo_record.mp4" type="video/mp4">
    </video>
    <div class="caption">Electromagnetics — FEM potential solve, B-field arrows, orbiting dipole magnet.</div>
  </div>
</div>

---

### Quantum

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    <video autoplay loop muted playsinline class="img-fluid rounded z-depth-1">
      <source src="/assets/video/tdse_record.mp4" type="video/mp4">
    </video>
    <div class="caption">Time-dependent Schrödinger equation — double-slit diffraction, phase-colored wavefunction.</div>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <video autoplay loop muted playsinline class="img-fluid rounded z-depth-1">
      <source src="/assets/video/quantum_demo_record.mp4" type="video/mp4">
    </video>
    <div class="caption">Quantum circuits — Bell, GHZ, Grover search, teleportation, and QFT₃ stepped gate-by-gate.</div>
  </div>
</div>

---

### Statistical Mechanics

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    <video autoplay loop muted playsinline class="img-fluid rounded z-depth-1">
      <source src="/assets/video/ising_record.mp4" type="video/mp4">
    </video>
    <div class="caption">2D Ising nucleation — free-energy barrier crossing; red cluster = growing critical nucleus (F=0.1, T&lt;Tc).</div>
  </div>
  <div class="col-sm mt-3 mt-md-0">
    <video autoplay loop muted playsinline class="img-fluid rounded z-depth-1">
      <source src="/assets/video/ising_classic_record.mp4" type="video/mp4">
    </video>
    <div class="caption">2D Ising ordering — spontaneous symmetry breaking from a random initial state below Tc.</div>
  </div>
</div>
