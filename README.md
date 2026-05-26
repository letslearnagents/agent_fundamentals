# Agent Fundamentals

## Notebooks

### 1. `simple_agent.ipynb`
A basic AI agent with:
- no tools
- no memory
- direct connection to the LLM

This notebook demonstrates the foundational structure of a simple agent that takes a user query and returns an LLM-generated response.

---

### 2. `agent_with_builtin_tool.ipynb`
An enhanced agent integrated with OpenAI’s built-in `WebSearchTool`.

This notebook demonstrates:
- real-time web search capability
- tool calling with OpenAI Agents SDK
- fetching up-to-date information from the internet before generating a response

--- 

### 3. `agent_with_custom_tool.ipynb`
A custom AI web search agent built using:

- OpenAI Agents SDK
- @function_tool
- Serper API

This notebook demonstrates:

- creating custom tools for AI agents
- connecting agents with external APIs
- understanding the tool-calling workflow
- returning structured responses from tools to the LLM