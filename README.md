# Daily Reflection Tree (DT Fellowship Assignment)

This repository contains a deterministic reflection agent designed to guide an employee through three psychological axes: Locus of Control, Orientation (Contribution vs Entitlement), and Radius of Concern (Self-Centrism vs Altrocentrism).

## Overview

The core deliverable is a structured data file (`tree/reflection-tree.json`) that fully defines a conversational tree. The conversation is 100% deterministic, without relying on an LLM at runtime, fulfilling the requirement of treating LLMs as a "power tool, not a product."

## Directory Structure

```text
/tree/
  reflection-tree.json        # Part A: The structured decision tree data
  tree-diagram.md             # Part A: Visual Mermaid.js diagram of the tree
/agent/
  main.py                     # Part B: Runnable Python CLI agent
/transcripts/
  persona-1-transcript.md     # Part B: Sample run for Victor/Contributor/Altrocentric
  persona-2-transcript.md     # Part B: Sample run for Victim/Entitled/Self-centric
write-up.md                   # Part A: 2-page design rationale and psychology
README.md                     # This file
```

## Running the Agent (Part B)

A working Python agent is included to walk the tree. It is written in pure Python without external dependencies.

Requirements:
- Python 3.x

To run the agent:
```bash
cd agent
python main.py
```

The agent will load the JSON tree, prompt the user through the CLI, branch deterministically, track signals, and display dynamic reflections based on the accumulated state.

## Why Python for the Agent?
Python was chosen for the agent because it is extremely robust for data structures and CLI applications. The implementation uses `eval()` safely on strictly internal tree data to resolve routing conditions, keeping the parser simple, dependency-free, and highly readable.

*Best of luck with your DeepThought application!*
