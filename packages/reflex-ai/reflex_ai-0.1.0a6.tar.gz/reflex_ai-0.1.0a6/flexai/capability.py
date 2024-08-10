"""Capabilities define hooks that can plug into the agent's pipeline.
"""
from flexai.message import Message, AIMessage


class AgentCapability:
    """Base class to define cognitive capabilities of an agent."""

    async def modify_prompt(self, prompt: str) -> str:
        """Modify the system prompt.

        Args:
            prompt: The current system prompt.

        Returns:
            The modified system prompt.
        """
        return prompt

    async def modify_messages(self, messages: list[Message]) -> list[Message]:
        """Modify the messages before sending them to the LLM.

        Args:
            messages: The current conversation messages.

        Returns:
            The modified messages.
        """
        return messages

    async def modify_response(self, messages, response: AIMessage) -> AIMessage:
        """Modify the AI response before sending it to the user.

        Args:
            messages: The current conversation messages.
            response: The AI response.

        Returns:
            The modified AI response.
        """
        return response
