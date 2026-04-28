# Daily Reflection Tree: A Deterministic Knowledge Engineering Tool

This repository contains my submission for the **DeepThought Role Simulation Assignment**. It is a deterministic reflection agent designed to guide an employee through three psychological axes: **Locus of Control**, **Orientation (Contribution vs. Entitlement)**, and **Radius of Concern (Self-Centrism vs. Altrocentrism)**.

## 🎯 Alignment with DeepThought's Philosophy

At DeepThought, BA/DS candidates are **Knowledge Engineers**. This project was built strictly adhering to that philosophy:
1. **Determinism over Hallucination:** The agent does not call any LLMs at runtime. The intelligence is entirely encoded into a static JSON data structure, guaranteeing predictability, auditability, and trust.
2. **AI as a Power Tool, Not a Product:** LLMs were used aggressively during the design phase (to roleplay personas, critique question depth, and test edge cases), but the final product is a deterministic tree executed by a lightweight Python engine.
3. **Structured Ontology:** The tree translates abstract psychological frameworks (Rotter, Organ, Maslow) into concrete, navigable decision paths without moralizing or using heavy jargon.

## 📂 Directory Structure

```text
/tree/
  reflection-tree.json        # Part A: The core structured decision tree data (JSON)
  tree-diagram.md             # Part A: Visual Mermaid.js diagram of the branching logic
/agent/
  main.py                     # Part B: Runnable Python CLI engine to walk the tree
/transcripts/
  persona-1-transcript.md     # Part B: Sample run for Victor/Contributor/Altrocentric
  persona-2-transcript.md     # Part B: Sample run for Victim/Entitled/Self-centric
write-up.md                   # Part A: 2-page rationale on psychology, design, and trade-offs
README.md                     # This file
```

## 🧠 My Thought Process (As reflected in the hand-drawn sketch)

To tackle this assignment, I approached it systematically:
1. **Controlling AI Hallucination:** I strictly enforced a deterministic architecture. The tree is pure JSON data, and the Python agent only routes based on hardcoded signal tallies. The LLM was purely used as a sparring partner during the drafting phase.
2. **Where I Disagreed with AI:** The AI initially suggested a continuous, infinitely branching tree and 5+ options per question. I actively disagreed to reduce cognitive load; I forced it down to 4 distinct options per node and implemented a **State Accumulation Model (Signals)** rather than chaotic branching. This kept the tree maintainable and the user experience focused.
3. **Negative Prompting Used:** During question generation, I aggressively used negative prompts like: *"Do not use psychological jargon," "Do not moralize or sound like a therapist,"* and *"Do not make the options too obvious (e.g., no clearly 'good' vs 'bad' choices)."*

## 🚀 Running the Agent (Part B)

A working Python agent is included to walk the tree. It is written in **pure Python** with zero external dependencies, emphasizing a robust, easy-to-audit runtime.

**Requirements:**
- Python 3.x

**To run the agent:**
```bash
cd agent
python main.py
```

The agent will seamlessly load the JSON tree, prompt the user through the CLI, branch deterministically based on input, track psychological signals, and display dynamic reflections based on the accumulated state.

*Thank you for reviewing my submission. I look forward to the opportunity to discuss my structural thinking and knowledge engineering approach with the DeepThought team!*
