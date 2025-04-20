# Project Scaffolding Plan for Multi-Agent System with Semantic-Kernel

## Objective
Create a multi-agent scaffolding using the Semantic-Kernel framework for orchestration. The project will leverage Python as the development language, Azure AI Services for runtime, and GitHub Codespaces or local development for coding. The goal is to showcase Microsoft tools and data in a contest submission, including a recorded demo.

---

## Logical Approach

### 1. **Project Setup**
    - **Folder Structure**:
      ```
      /project-root
      ├── agents/
      │   ├── microsoft_learn_agent.py
      │   ├── labor_economics_agent.py
      │   └── __init__.py
      ├── tools/
      │   ├── microsoft_learn_tool.py
      │   ├── labor_economics_tool.py
      │   └── __init__.py
      ├── data/
      │   ├── microsoft_learn_sample.json
      │   └── labor_economics_sample.json
      ├── scripts/
      │   ├── setup_environment.py
      │   └── demo_launcher.py
      ├── tests/
      │   ├── test_agents.py
      │   ├── test_tools.py
      │   └── __init__.py
      ├── README.md
      ├── requirements.txt
      ├── .env
      └── .gitignore
      ```

    - **Environment Setup**:
      - Create a `requirements.txt` file with dependencies:
         ```
         semantic-kernel
         azure-ai
         chainlit
         requests
         pytest
         python-dotenv
         ```
      - Use `setup_environment.py` to initialize the environment and install dependencies.

---

### 2. **Agent Design**
    - **Microsoft Learn Agent**:
      - Queries Microsoft Learn Profile data using custom tools.
    - **Labor and Economics Agent**:
      - Queries US Labor and Economics datasets from Microsoft Open Dataset.

    - **Shared Features**:
      - Use Semantic-Kernel for orchestration.
      - Implement modular tools for data querying and processing.

---

### 3. **Development Workflow**
    - **Coding**:
      - Use VS Code with GitHub Codespaces or local development.
      - Write modular, reusable code for agents and tools.
    - **Testing**:
      - Write unit tests for agents and tools in the `tests/` directory.
    - **Documentation**:
      - Maintain a clear and concise `README.md` for project overview and setup instructions.

---

### 4. **Demo Preparation**
    - **Launch Interface**:
      - Use Chainlit to create a prompt-based interface for interacting with agents.
    - **Recorded Demo**:
      - Showcase:
         1. Project structure and code in VS Code.
         2. Launching the Chainlit interface.
         3. Agents querying Microsoft Learn Profile and US Labor/Economics datasets.
    - **Ease of Use**:
      - Ensure the workspace is intuitive and easy to navigate for the demo.

---

### 5. **Submission Checklist**
    - [ ] Codebase is complete and functional.
    - [ ] All dependencies are listed in `requirements.txt`.
    - [ ] Environment setup script is tested.
    - [ ] Demo script (`demo_launcher.py`) is ready.
    - [ ] Recorded demo meets contest requirements.