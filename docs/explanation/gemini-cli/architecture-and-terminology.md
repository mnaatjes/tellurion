# Architecture and Terminology: Package vs. Program

When working with Gemini CLI in a Linux environment, it is important to distinguish between the technical components of the software and the interface layers you interact with.

## 1. The npm Package (`@google/gemini-cli`)
The npm package is the distribution unit of the software.

- **Category:** Node.js-based CLI application / AI Orchestration Tool.
- **Definition:** A bundled set of JavaScript files, metadata, and dependencies (including the `@google/gemini-cli-core` logic) distributed via the Node Package Manager (npm).
- **Role:** It acts as the "Engine" or "Proxy" that connects your local environment (files, shell, and tools) to the Gemini Large Language Models (LLMs) via Google’s APIs.
- **Installation:** When you run `npm install -g @google/gemini-cli`, you are downloading this source distribution to your global node_modules directory.

## 2. The Program (`gemini`)
The "program" is the executable command registered on your system.

- **Definition:** In Linux, `gemini` is typically a **Symlinked Binary Executable**. It is a symbolic link (alias) pointing to the entry-point script within the npm package.
- **Location:** You can identify the exact path by running `which gemini`. Common locations include `/usr/local/bin/gemini` or a path within your `.npm-global/bin` folder.
- **Function:** This is the trigger. Executing `gemini` initializes the Node.js runtime, loads the package code, and starts the interactive session.

## 3. The CLI (The Interface)
The CLI is the specific interface layer through which you communicate with the program.

- **The Interactive Prompt:** When the program starts, it presents a REPL (Read-Eval-Print Loop) or Input Buffer. This is where you type your messages.
- **Context-Loading Features:** The `@path/to/file` logic is a specific CLI feature designed to bridge the gap between your local file system and the AI's context window.
- **Standard Input (stdin):** You can bypass the interactive prompt by piping data directly to the program (e.g., `cat file.txt | gemini`). In this case, you are talking directly to the program's engine.

---

### Summary Comparison

| Component | Term | Technical Reality |
| :--- | :--- | :--- |
| **The Package** | `@google/gemini-cli` | The collection of code, assets, and metadata stored on the npm registry. |
| **The Program** | `gemini` | The specific command in your `PATH` that triggers the code execution. |
| **The Interface** | CLI | The interactive REPL/prompt where you provide input. |
| **The Version** | `v0.37.1` | The specific release of the logic and features contained within the package. |

### Why the Distinction Matters
- **Upgrading:** You update the **Package** via npm to get the latest features.
- **Workflow:** You use the **CLI** to interact with the agent.
- **Automation:** You interact with the **Program** directly via pipes and shell scripts for automated tasks.
