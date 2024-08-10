"""Init."""

import os

from dotenv import load_dotenv

from lmtr_agents.lmtr_agents import agent_ref

load_dotenv()
__version__ = "0.1.0a0"

# agent_model = os.getenv("AGENT_MODEL")
# agent_base_url = os.getenv("AGENT_BASE_URL")
# agent_api_key = os.getenv("AGENT_API_KEY", "any")

# __all__ = ("lmtr_agents", "agent_model", "agent_base_url", "agent_api_key")
__all__ = ("agent_ref", )
