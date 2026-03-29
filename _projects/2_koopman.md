---
layout: page
title: Koopman Operator Analysis of Reaction Networks
description: EDMD-based rate recovery from stochastic trajectory data
img: assets/img/projects/mm_modes_time_amps.png
importance: 2
category: research
---

Rather than evolving probability distributions forward (the CME direction), the **Koopman generator** acts on observables $$f: \mathbb{N}^N \to \mathbb{R}$$:

$$\frac{d}{dt}\langle f \rangle = \left\langle \sum_{k=1}^M \alpha_k(\mathbf{x})\bigl[f(\mathbf{x}+\boldsymbol{\zeta}_k) - f(\mathbf{x})\bigr]\right\rangle = \langle \mathcal{A} f \rangle$$

where $$\alpha_k(\mathbf{x}) = c_k \cdot \psi_{m(k)}(\mathbf{x})$$ are the reaction propensities. Since each propensity factors as a known polynomial $$\psi_{m(k)}$$ times an unknown rate constant $$c_k$$, the Koopman generator is **linear in the rates**:

$$\mathcal{A} = \sum_{k=1}^M c_k \mathcal{A}_k$$

Using **Extended Dynamic Mode Decomposition (EDMD)**, I recover the dominant Koopman eigenfunctions and eigenvalues directly from SSA trajectory data — without ever forming the full CME generator. The dominant modes capture the slow timescales of the network, and the rate constants follow from a linear regression in the Koopman basis.

Results on three benchmark networks are shown below.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/projects/mm_modes_time_amps.png" title="Michaelis-Menten modes" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/projects/bru_modes_time_amps.png" title="Brusselator modes" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Left: Koopman modes and amplitudes for the Michaelis-Menten enzyme kinetics network.
  Right: Brusselator modes — dominant complex eigenvalues reveal the oscillatory timescale of the limit cycle.
</div>

<div class="row justify-content-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/projects/lv_dmd_reconstruction.png" title="Lotka-Volterra reconstruction" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Koopman-based reconstruction of mean trajectories for the Lotka-Volterra predator-prey network. The recovered rate constants produce faithful reconstructions from limited trajectory observations.
</div>
