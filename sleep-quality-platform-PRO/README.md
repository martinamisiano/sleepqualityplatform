
# Sleep Quality Analyzer

A modular Python system that evaluates sleep quality based on physiological sleep-stage criteria (REM, deep, wake, total duration).

## Overview

Sleep Quality Analyzer processes sleep session data and computes a quality score based on four biologically inspired rules:
Total sleep duration vs target
REM sleep percentage
Deep sleep percentage
Wake time percentage
Each sleep session is classified into one of:
SCADENTE
DISCRETA
BUONA
ECCELLENTE

## Key features

Modular architecture (separation of concerns)
Rule-based scoring engine
Command-line interface (CLI)
Automated testing with pytest
Extensible core logic (no coupling with I/O)

## Architecture

core/        → Business logic (sleep evaluation engine)
cli/         → Command-line interface
tests/       → Unit tests (pytest)

## Installation

git clone https://github.com/martinamisiano/sleepqualityplatform.git
cd sleepqualityplatform
pip install -r requirements.txt

## Usage

python cli/main.py example_input.txt

## Input format

TARGET
wake rem deep light
wake rem deep light
...
 ## Output
 
The program outputs:
Number of valid sleep sessions
Min / Max / Average total sleep duration
Quality classification per session
Top 5 longest sleep sessions

## Testing 

pytest

## Design Choices

Separation of concerns: core logic isolated from CLI
Deterministic algorithm: no randomness, fully reproducible
Scalable structure: easy to extend with API or web dashboard
Testability-first design

## Future Improvements

REST API (FastAPI integration)
Database persistence (SQLite/PostgreSQL)
Sleep trend visualization dashboard
Machine learning-based sleep quality prediction



