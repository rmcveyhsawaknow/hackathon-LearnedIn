# LearnedIn

**LearnedIn** is an Agent designed to analyze a person's learn.microsoft.com profile and craft personalized, instruction-driven narratives. The stories are made relevant by integrating current world topics, leveraging open data statistics, and enriching the presentation with code-interpreter-driven visuals when applicable.

This project is being developed as part of a Microsoft-sponsored competition for the AI Agents Hackathon.

## Key Features
- **Personalized Narratives:** Personifies the user's learning profile with actionable instructions.
- **Relevance Engine:** Incorporates current world topics using Bing-powered searches.
- **Data-Driven Insights:** Fetches relevant statistics from open data sources for deeper context, including US Labor Force statistics.
- **Visual Enrichment:** Generates dynamic visuals using a code interpreter to enhance storytelling.

## Technology Stack
- **LLM (Large Language Model):** Powered by Azure OpenAI Models for natural language generation.
- **Tools:**
  - **Bing Search API:** To fetch trending topics and ensure relevance.
  - **Function:** For handling dynamic requests, such as fetching and processing data from relational databases.
  - **Microsoft Graph API (Beta):** [Learn.microsoft.com profile API](https://learn.microsoft.com/en-us/graph/api/resources/profile-example?view=graph-rest-beta) for accessing user profiles and learning data.
  - **Open Data APIs:** For integrating real-time statistics into narratives.
  - **Code Interpreter:** For generating meaningful visuals when they add value to the presentation.
- **Data:** 
  - **Learn.microsoft.com profiles:**
    - Training profile data is now collected using a Playwright-powered agent that interactively downloads the user's Learn profile as a JSON file. This process requires the user to log in via browser automation, after which the data is saved locally for further processing and upload to Azure Blob Storage. For details, see the [tool instructions](tools/microsoft_learn_tool_instructions.md).
    - [Learn.microsoft.com profile API reference](https://learn.microsoft.com/en-us/graph/api/resources/profile-example?view=graph-rest-beta)
  - Open data repositories (e.g., public statistics, global trends)
  - **Microsoft Open Dataset:**  
    - General dataset catalog: [Microsoft Open Datasets](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-catalog)  
    - Specific dataset for US Labor Force statistics: [US Labor Force Dataset](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-us-labor-force?tabs=azureml-opendatasets)  
  - Current events and news topics via Bing.

---

## Development Environment Setup (Local & Codespaces)

This project is designed to work seamlessly both on your local Windows machine and in GitHub Codespaces.

### Local (Windows) Setup
1. Install [Python 3.10+](https://www.python.org/downloads/).
2. (Recommended) Create a virtual environment:
   ```sh
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Copy or create your `.env` file as needed (see examples in `examples/`).
5. Open the workspace in VS Code. The recommended extensions will be suggested automatically.

### GitHub Codespaces Setup
1. Open this repository in Codespaces.
2. The dev container will auto-install Python, dependencies, and recommended extensions.
3. Place your `.env` file in the appropriate location if needed.

For both environments, see the `examples/` folder for usage patterns and `.env` requirements.

---

## Goals
This project aims to create a unique AI agent capable of:
1. Highlighting a user's learning journey in an engaging and insightful way.
2. Enhancing the value of educational achievements by connecting them to broader, real-world contexts.
3. Showcasing the power of AI-driven storytelling to enrich learning experiences.

## Contribution
We welcome contributions from the community! Feel free to submit issues or pull requests to help improve LearnedIn.

---
*Developed for the Microsoft AI Agents Hackathon 2025.*


az auth login --use-device-code
azd auth login --use-device-code
azd env list
azd init --environment yyyymmddhhmm
