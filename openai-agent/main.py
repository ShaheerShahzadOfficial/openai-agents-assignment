"""
This is a simple echo agent that repeats what the user says.
It is a good example of how to use the OpenAI Agents SDK.
It is also a good example of how to use the OpenAI API with Gemini.
"""
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
Creates and runs an Echo Agent using the OpenAI Agentic SDK.

This function:
- Prompts the user for input via the command line.
- Initializes an Agent with instructions to echo the user's input exactly.
- Uses the Runner to execute the agent with the given input.
- Prints the agent's echoed response back to the console.

The agent uses the specified model and configuration defined externally.
"""
    print("🤖 Echo Agent Ready!")
    user_input = input("🗣️ Say something: ")

    agent = Agent(
        model=model,
         name="Echo Agent",
        instructions="Repeat exactly what the user says, word-for-word, without any additional commentary.",
    )

    result = await Runner.run(agent, user_input, run_config=config)
    print("\n🪞 Echoed Response:")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())