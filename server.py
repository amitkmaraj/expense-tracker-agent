import os
from typing import Literal

from dotenv import load_dotenv
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

AGENT_DIR = os.path.dirname(os.path.abspath(__file__))

# App arguments for ADK - using in-memory session service for simplicity
app_args = {"agents_dir": AGENT_DIR, "web": True}

# Create FastAPI app with ADK integration
app: FastAPI = get_fast_api_app(**app_args)

# Update app metadata
app.title = "Expense Tracker Agent"
app.description = "AI Agent to help with expenses"
app.version = "1.0.0"


@app.get("/")
def root() -> dict[str, str]:
    """Root endpoint with service information.

    Returns:
        Basic information about the service
    """
    return {
        "service": "Expense Tracker Agent",
        "description": "AI Agent to help with expenses",
        "version": "1.0.0",
    }


# Main execution for local development
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
