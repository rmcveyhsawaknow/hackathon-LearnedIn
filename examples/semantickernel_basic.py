import asyncio
import os

import azure.identity
from dotenv import load_dotenv
from openai import AsyncAzureOpenAI, AsyncOpenAI
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

# Add this line to specify the correct .env file path
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".azure", "202504160535", ".env"), override=True)

API_HOST = os.getenv("API_HOST", "github")
if API_HOST == "azure":
    print("Using Azure OpenAI API")
    token_provider = azure.identity.get_bearer_token_provider(
        azure.identity.DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
    )
    chat_client = AsyncAzureOpenAI(
        api_version=os.environ["AZURE_OPENAI_VERSION"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        azure_ad_token_provider=token_provider,
    )
    chat_completion_service = OpenAIChatCompletion(
        ai_model_id=os.environ["AZURE_OPENAI_CHAT_MODEL"], async_client=chat_client
    )
else:
    print("Using GitHub Models API")
    chat_client = AsyncOpenAI(
        api_key=os.environ["GITHUB_TOKEN"], base_url="https://models.inference.ai.azure.com"
    )
    chat_completion_service = OpenAIChatCompletion(
        ai_model_id=os.getenv("GITHUB_MODEL", "gpt-4.1"), async_client=chat_client
    )

agent = ChatCompletionAgent(name="spanish_tutor", instructions="You are a Spanish tutor. Help the user learn Spanish. ONLY respond in Spanish.", service=chat_completion_service)


async def main():
    response = await agent.get_response(messages="oh hey how are you?")
    print(response.content)


if __name__ == "__main__":
    asyncio.run(main())
