
# Sleep Quality Analyzer

A modular Python system that evaluates sleep quality based on physiological sleep-stage criteria (REM, deep, wake, total duration). The project is designed with clean architecture principles, testability-first design, and clear separation between business logic and interface layers.

## Problem statement

Sleep tracking devices generate raw sleep-stage data, but interpreting this data into meaningful sleep quality insights requires structured analysis.
This system transforms raw sleep session inputs into a standardized sleep quality classification, making the data interpretable and consistent.

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
The goal is to simulate a simplified but realistic sleep analysis engine similar to those used in health-tracking systems.

## Key features

Modular architecture (separation of concerns)
Rule-based scoring engine
Command-line interface (CLI)
Unit testing with pytest
Easily extensible core logic (ready for API or web integration)

## Architecture

core/        → Business logic (sleep evaluation engine)
cli/         → Command-line interface
tests/       → Unit tests (pytest)

Design Principles
Separation of concerns: business logic is completely independent from input/output
Testability-first design: core logic is fully unit-testable
Extensibility: architecture allows easy integration with REST APIs or dashboards
Deterministic computation: same input always produces same output

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
 
The program produces:
Number of valid sleep sessions above target
Minimum, Maximum and Average total sleep duration
Quality classification for each session
Top 5 longest sleep sessions (sorted ascending)

## Testing 

pytest

Covered scenarios:
sleep duration calculation
scoring logic correctness
classification boundaries
edge cases

## Design Choices

Separation of concerns:
Business logic is isolated in the core/ module to ensure reusability across CLI, API, or UI layers.
Deterministic scoring system:
The evaluation algorithm is rule-based, ensuring reproducibility and explainability (important in healthcare-related systems).
Lightweight architecture:
No external dependencies for core logic, making the system portable and easy to integrate.
Testability-first approach:
Core logic is designed to be fully unit-testable without requiring file I/O or UI components.
Separation of core logic:
Business logic is fully isolated in the core/ module to allow:
reuse in APIs or web applications
independent unit testing
easier refactoring and scaling


## Future Improvements

REST API using FastAPI for remote data processing
Database persistence (SQLite → PostgreSQL migration path)
Interactive dashboard for sleep trend visualization
Machine learning model for predictive sleep quality scoring
Real-time data ingestion from wearable devices

## Author

Developed as a software engineering portfolio project focused on:
modular design
clean architecture
test-driven development principles
real-world system simulation

## Project purpose
This project was developed as a software engineering portfolio project to demonstrate:
modular system design
clean architecture principles
test-driven development mindset
ability to design scalable backend systems

## Summary

This system demonstrates a production-inspired architecture in Python, focusing on:
clean separation of concerns
deterministic business logic
testability
extensibility for real-world systems



