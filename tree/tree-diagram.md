```mermaid
graph TD
    START[START: Good evening...] --> A1_OPEN[A1_OPEN: Where was the primary friction?]
    
    A1_OPEN -->|Internal (B, D)| A1_Q_INT[A1_Q_INT: Gap in preparation/strategy - what did you do?]
    A1_OPEN -->|External (A, C)| A1_Q_EXT[A1_Q_EXT: External wall - how did you move forward?]
    
    A1_Q_INT --> A1_D2{A1_D2: Check Axis 1 Signals}
    A1_Q_EXT --> A1_D2
    
    A1_D2 -->|Internal >= External| A1_R_INT[A1_R_INT: Held onto agency]
    A1_D2 -->|External > Internal| A1_R_EXT[A1_R_EXT: Normal to feel stuck]
    
    A1_R_INT --> BRIDGE_1_2[BRIDGE_1_2: Shift to interactions]
    A1_R_EXT --> BRIDGE_1_2
    
    BRIDGE_1_2 --> A2_OPEN[A2_OPEN: Out of sync with colleague?]
    
    A2_OPEN -->|Contribution (B, D)| A2_Q_CONTRIB[A2_Q_CONTRIB: Approached with curiosity - what did it cost?]
    A2_OPEN -->|Entitlement (A, C)| A2_Q_ENTITLE[A2_Q_ENTITLE: Natural to want fairness - default assumption?]
    
    A2_Q_CONTRIB --> A2_D2{A2_D2: Check Axis 2 Signals}
    A2_Q_ENTITLE --> A2_D2
    
    A2_D2 -->|Contribution >= Entitlement| A2_R_CONTRIB[A2_R_CONTRIB: Mindset of giving]
    A2_D2 -->|Entitlement > Contribution| A2_R_ENTITLE[A2_R_ENTITLE: Focus on what is owed]
    
    A2_R_CONTRIB --> BRIDGE_2_3[BRIDGE_2_3: Zoom out to radius]
    A2_R_ENTITLE --> BRIDGE_2_3
    
    BRIDGE_2_3 --> A3_OPEN[A3_OPEN: When stress peaked, how wide was lens?]
    
    A3_OPEN -->|Self (A, B)| A3_Q_SELF[A3_Q_SELF: If you had 10% more capacity, where would you direct it?]
    A3_OPEN -->|Altro (C, D)| A3_Q_ALTRO[A3_Q_ALTRO: How did holding broader perspective affect you?]
    
    A3_Q_SELF --> A3_D2{A3_D2: Check Axis 3 Signals}
    A3_Q_ALTRO --> A3_D2
    
    A3_D2 -->|Altro >= Self| A3_R_ALTRO[A3_R_ALTRO: Self-transcendence]
    A3_D2 -->|Self > Altro| A3_R_SELF[A3_R_SELF: Expanding view lightens load]
    
    A3_R_ALTRO --> SUMMARY_BRIDGE[SUMMARY_BRIDGE: Summarize day]
    A3_R_SELF --> SUMMARY_BRIDGE
    
    SUMMARY_BRIDGE --> SUMMARY[SUMMARY: Display dominants]
    
    SUMMARY --> END_NODE[END: See you tomorrow]
```
