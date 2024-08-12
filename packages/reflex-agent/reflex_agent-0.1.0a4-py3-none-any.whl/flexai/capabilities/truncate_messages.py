from dataclasses import dataclass

from flexai.capability import AgentCapability
from flexai.message import Message


@dataclass(frozen=True)
class TruncateMessages(AgentCapability):
    """Truncate the input messages to the LLM to a maximum number."""

    # The maximum number of messages to keep.
    max_messages: int

    async def modify_messages(self, messages: list[Message]) -> list[Message]:
        return messages[-self.max_messages :]
