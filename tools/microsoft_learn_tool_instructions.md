## Project Update: Integration of Personal MSA Certification Data

### Initial Assumption

The original project assumed that linking a personal Microsoft Account (MSA) profile (e.g., `rjmcvey2013@gmail.com`) to an Entra ID account (e.g., `ryan@rjmcvey2013gmail.onmicrosoft.com`) via learn.microsoft.com would allow direct access to MSA-linked certification data through the Microsoft Graph API, based on Microsoft's profile API documentation ([link](https://learn.microsoft.com/en-us/graph/api/resources/profile-example?view=graph-rest-beta)).

### Revised Understanding

Upon verification, it has been determined that account linking on learn.microsoft.com is **visual only** and does not expose MSA-linked certification or learning data via the Microsoft Graph API (`/beta/users/{user_id}/profile`). Consequently, certification data remains accessible solely through the original MSA identity.

### Updated Implementation Approach

To align with project requirements, the implementation will pivot as follows:

1. **Azure AI Agent Service with Python SDK**

   - Use Azure AI Agent Service to orchestrate AI-driven workflows.
   - Integrate a custom Python-based tool within the AI Agent architecture to authenticate and download the latest MSA profile certification data.

2. **Custom Python Tool for Data Retrieval**

   - A Python tool (see `microsoft_learn_tool_playwright.py`) uses Playwright browser automation to interactively authenticate the user and download the latest Learn profile data as a JSON file to a local directory (`data/inputs/learn_profile_downloads/`).
   - The tool requires the user to log in via a browser window and automatically clicks the Download button on the Learn profile settings page.
   - The resulting JSON file is saved locally and will be handed off to the next agent for upload to Azure Blob Storage.

3. **Semantic Kernel for Multi-Agent Orchestration**

   - Employ Semantic Kernel as the primary orchestration framework to coordinate multiple Azure AI Agents.
   - Use Semantic Kernel to effectively manage complex workflows, including the handoff between custom tools and built-in Azure AI Agent tools.

4. **Handoff to Azure AI Agent's File Search Tool**

   - After retrieval by the custom tool, the Azure AI Agent will leverage its built-in File Search tool.
   - Automatically upload the retrieved certification data JSON file into Azure Blob Storage.

   Filename convention:

   ```
   {yymmddHHmmss}_{userId}_{userName}.json
   ```

   **Example:**

   ```
   250420104530_ffe928cc-0efc-44b4-9114-123ae915e4a6_rmcveyhsawaknow.json
   ```

5. **Change Detection and Logging**

   - Implement logic within the Azure AI Agent workflow to compare the newly stored blob with the most recent previous version.
   - Document detected changes or updates into a job log register, creating a robust audit trail for certification data updates.

This updated approach ensures seamless, automated, and accurate management of personal certification data while leveraging Azure AI Agent Services, Semantic Kernel, and integrated tools effectively.