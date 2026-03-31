# How-To: Monitoring and Managing the Context Window

In Gemini CLI, the "Context Window" is your primary resource buffer. Managing it effectively ensures the agent stays "high-signal" (focused and accurate) and avoids "noise" (hallucinations or generic responses caused by an overloaded history).

## 1. Real-Time Monitoring

You don't need to guess how much of your context window is consumed. The CLI provides two primary methods to track resource usage:

### The Footer UI
In the interactive terminal, look at the bottom right of the screen. By default, a live percentage bar (e.g., `[||||      ] 35%`) indicates your current Context Window utilization. As this bar fills, the agent may begin to lose focus on older parts of the conversation.

### The Stats Command
For a clinical breakdown of token usage, use the `/stats` command:

```bash
/stats model
```

This provides detailed metrics, including:
- **Prompt Tokens:** The amount of data being sent to the model (including history, system instructions, and your current prompt).
- **Candidates Tokens:** The amount of data the AI is generating in response.
- **Total Window:** Your model's maximum capacity (e.g., 1,000,000 tokens for Gemini 1.5 Pro).

---

## 2. Session Management (The "Flush")

When monitoring shows usage hitting **70–80%**, or if the agent starts providing generic answers, use the following session commands to prune the window and restore focus.

| Command | Action | When to Use It |
| :--- | :--- | :--- |
| `/compress` | Summarizes the entire conversation history into a concise block and deletes the raw logs. | Use when the conversation is long, but you still need the agent to remember the high-level "story" so far. |
| `/clear` | Wipes the entire conversation history (Layer 3) but preserves `GEMINI.md` and active files (Layers 1 & 2). | Use when switching tasks (e.g., moving from one microservice to another or from research to implementation). |
| `/chat save [tag]` | Saves the current state of the context window to disk. | Use before a "risky" or speculative experiment so you can revert if the window gets messy. |
| `/chat resume [tag]` | Restores a previously saved session state. | Use to "backtrack" to a known good state of the context window. |
| `! [command]` | Executes a shell command (e.g., `!ls -R`) to pull ephemeral data into the window. | Use to inject specific, short-lived information without permanently bloating the history. |

---

## 3. Best Practices for Window Health

- **Proactive Pruning:** Don't wait for the window to fill. Use `/clear` when you've reached a logical milestone in your workflow.
- **Save Often:** Use `/chat save` before performing large file reads or complex refactors that might inject significant "noise" into the history.
- **The "Anchor" remains:** Remember that your `GEMINI.md` and system instructions are "anchored"—they stay in the window even after a `/compress` or `/clear`, ensuring the agent never forgets its core persona and project rules.
