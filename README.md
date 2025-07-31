# Automated Email Classification System

![Python](https://img.shields.io/badge/python-3.12-blue)
![ML](https://img.shields.io/badge/machine%20learning-Naive%20Bayes%7CSVM%7CTransformers-orange)
![API](https://img.shields.io/badge/API-FastAPI-brightgreen)
![Status](https://img.shields.io/badge/status-production%20ready-success)

An end-to-end machine learning system that automatically classifies emails into predefined categories using both traditional ML and deep learning approaches.

## Categories
- **Customer Support/Complaints**
- **Sales Inquiries/Pricing**
- **Partnership Proposals**
- **Spam/Advertisements**

## Features
- REST API with FastAPI
- Docker/conda deployment options
- Comprehensive evaluation metrics

## Quick Start

### Prerequisites
- Conda/Miniconda
- Python 3.12

### Installation
```bash
git clone https://github.com/Erfan-Roshandel/yekta.git
cd yekta

# Using conda
conda env create -f environment.yml
conda activate email-classifier

# Or using Docker
```bash
./build_and_run.sh
