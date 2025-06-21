import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

GEMINI_MODEL = os.getenv("GEMINI_MODEL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_BASE = os.getenv("GEMINI_API_BASE")

if not GEMINI_API_KEY or not GEMINI_API_BASE:
    raise ValueError("GEMINI_API_KEY and GEMINI_API_BASE must be set")

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=GEMINI_API_BASE,
)

model = OpenAIChatCompletionsModel(
    model=GEMINI_MODEL,
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)


async def main():
    """
    Creates and runs a Helpful Assistant using the OpenAI Agentic SDK.

    This function performs the following:
    - Prompts the user for input via the command line.
    - Initializes an Agent with instructions to accurately and efficiently fulfill the user's request.
    - Executes the Agent using the Runner with the provided input and external configuration.
    - Prints the Agent’s final output (response) to the console.

    The Agent uses a custom OpenAI-compatible model and configuration loaded from environment variables.
    """
    print("🤖 Helpful Assistant!")
    user_input = input("🗣️ Say something: ")

    agent = Agent(
        model=model,
        name="Helpful Assistant",
        instructions="""
You are a helpful and intelligent assistant. Your goal is to understand and carry out the users request accurately and efficiently. Do exactly what the user asks—nothing more, nothing less—unless clarification is required.

If the user request is ambiguous, ask thoughtful questions. If it is clear, proceed directly. Adapt your tone and style to match the user’s intent (formal, friendly, technical, etc.).

Follow these rules:

Understand the user's intent fully before acting.

Don’t add extra commentary or opinions.

Stick to the format the user implies or specifies.

If the task is impossible or unsafe, explain why.

If the user is asking for a task that involves steps (like code, writing, planning, etc.), complete it thoroughly.
""",
    )
    result = await Runner.run(agent, user_input, run_config=config)
    print("\n🪞 Response:")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
