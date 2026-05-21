# Exoplanet Dataset Exploration (NASA Exoplanet Archive)

## Overview

This project explores confirmed exoplanets using data from the NASA Exoplanet Archive. The analysis focuses on planetary radius, orbital period, and discovery methods in order to investigate general trends within confirmed exoplanet populations.

This project aimed to demonstrate:

* data cleaning and preprocessing using Python
* exploratory data analysis (EDA)
* scientific visualisation
* interpretation of real-world astronomical datasets
* clear and reproducible documentation practices

This repository was created as part of a personal data science portfolio project.

## Dataset

**Source:** [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/?utm_source=chatgpt.com)

The dataset used was the *Confirmed Planets Table*, exported from the NASA Exoplanet Archive.

### Key variables analysed

* `pl_name` — Planet name
* `pl_rade` — Planet radius (Earth radii)
* `pl_bmasse` — Planet mass (Earth masses)
* `pl_orbper` — Orbital period (days)
* `discoverymethod` — Detection method
* `disc_year` — Discovery year

## Methods

The analysis was carried out using:

* Python
* pandas
* matplotlib
* seaborn

## Analysis and Findings

### Planet Radius Distribution

A histogram of exoplanet radii was produced to investigate the spread of detected planetary sizes.

The distribution shows a wide variation in planetary radii, reflecting the diversity of known exoplanets.

---

### Orbital Period Distribution

Orbital periods were analysed using a logarithmic scale due to strong skewness in the dataset.

The results indicate that the majority of detected exoplanets have relatively short orbital periods. This is likely influenced by observational bias, as planets with shorter orbital periods are easier to detect using transit-based methods.

---

### Discovery Methods

The frequency of different exoplanet detection techniques was compared.

Transit photometry was found to dominate the dataset, reflecting the impact of large-scale survey missions such as NASA's Transiting Exoplanet Survey Satellite.

---

## Example Outputs

The project generates:

* histogram of exoplanet radii
* histogram of orbital periods
* bar chart of discovery methods

These figures are saved in the `outputs/` directory.

## Reflections

This project provided experience working with real scientific datasets containing metadata formatting issues, missing values, and highly skewed distributions. It also reinforced the importance of clear documentation and reproducible analysis workflows in data science projects.

Future improvements could include:

* time-series analysis of exoplanet discoveries
* additional statistical modelling
* comparison between detection methods
* investigation of stellar properties and habitability metrics

---

## Author

Created by Isobelle Chalmers as part of a personal data science and scientific computing portfolio project.
