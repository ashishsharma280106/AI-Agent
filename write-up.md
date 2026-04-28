# Design Rationale: Daily Reflection Tree

## Why These Specific Questions?
The core objective of these questions is to move beyond superficial accounts of the day and touch upon the underlying psychological states without triggering defensiveness.
- **Axis 1 (Locus):** The opening question ("Where was the primary friction?") frames the day in terms of a mechanical "friction" rather than a moral failure or personal flaw. Options naturally separate internal locus ("I realized I hadn't prepared") from external locus ("Other people's delays"). The follow-ups then probe *agency in response* to either scenario.
- **Axis 2 (Orientation):** Entitlement is often invisible to the person holding it. The question "Think about a moment today where you felt out of sync with a colleague" grounds the reflection in a specific, relatable reality. It reveals whether the employee's default assumption was that they were owed something ("they should have recognized how much effort I was putting in") or a desire to contribute/understand ("wondered if I had communicated clearly").
- **Axis 3 (Radius):** Under stress, our radius naturally shrinks. The questions gently probe this. Asking "If you had 10% more capacity today, where would you have directed it?" provides a clear metric for self-transcendence: would they use the extra capacity to survive (self) or to build/help (altro)? 

## Branching Design and Trade-offs
The branching strategy relies on a deterministic **state accumulation model**. 
While the first question on each axis splits the path to tailor the follow-up question (creating a conversational feel), the ultimate reflection node for that axis is decided by the *net signal* accumulated across both questions.

**Trade-offs:** 
- **Breadth vs. Depth:** To keep the tree deterministic and manageable without an LLM at runtime, I opted for a single major point of divergence per axis. A continuously branching tree would exponentially increase node count without necessarily adding proportional insight.
- **Interpolation vs. Generation:** Since no LLM is used at runtime, the summary relies on string interpolation of dominant traits. This sacrifices some of the "chatty" feel of an LLM in exchange for 100% auditability and consistency. 

## Psychological Sources
1. **Julian Rotter’s Locus of Control (1954) & Carol Dweck's Mindset (2006):** Guided Axis 1. The questions distinguish between attributing outcomes to one's own actions/strategies (internal/growth) versus attributing them to luck, circumstances, or other people (external/fixed).
2. **Organ's Organizational Citizenship Behavior (1988) & Campbell's Psychological Entitlement (2004):** Guided Axis 2. OCB is reflected in the options representing "discretionary effort", while entitlement is reflected in expectations of unearned reward or frustration with perceived unfairness.
3. **Maslow’s Self-Transcendence (1969) & Batson’s Perspective-Taking (2011):** Guided Axis 3. Maslow's later work argued that the healthiest humans orient outward. The "Altrocentrism" paths highlight how focusing on the broader impact ("I knew *why* the work mattered") actually serves as a buffer against personal suffering.

## Future Improvements
With more time, I would:
1. **Context-Dependent Bridging:** The bridges between axes are currently static. It would feel more conversational if the bridge between Axis 1 and 2 varied based on the outcome of Axis 1.
2. **Mixed/Balanced Handlers:** If an employee's signals are perfectly tied (e.g., 1 internal, 1 external), the tree currently defaults to the `>=` condition. A dedicated "Mixed State" reflection node would provide a more nuanced response.
3. **Web UI:** Build a clean, distraction-free web interface (React/Tailwind) that visually represents the path being walked, reinforcing the concept of the "tree."
