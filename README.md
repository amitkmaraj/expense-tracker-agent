# 💸 Expense Tracker Agent

This project is an AI-powered expense tracking agent built with the Google Agent Development Kit (ADK). It allows users to manage their personal finances through a natural language chat interface.

## ✨ Features

- 📝 **Add Expenses**: Record expenses with an amount, category, and description.
- 📊 **Track Spending**: Calculate total spending and view spending broken down by category.
- 📜 **View History**: List recent expenses.
- 🔄 **Recurring Expenses**: Manage recurring weekly, monthly, or yearly expenses.
- 🔮 **Forecast**: Project future spending based on recurring expenses.

## 🛠️ Prerequisites

- [Python 3.11+](https://www.python.org/)
- [uv](https://github.com/astral-sh/uv): A fast Python package installer and resolver.
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install): For authentication and deployment.

## 🚀 Getting Started

### 1. Clone the Repository 📂

```bash
git clone https://github.com/amitkmaraj/expense-tracker-agent
cd expense-tracker-agent
```

### 2. Install Dependencies 📦

This project uses `uv` for package management. To install the necessary dependencies, run:

```bash
uv sync
```

### 3. Configure Environment Variables 🔑

Create a `.env` file in the root of the project directory:

```bash
cp .env.example .env
```

Edit the `.env` file and add your Google Cloud project details:

```env
GOOGLE_GENAI_USE_VERTEXAI=true
GOOGLE_CLOUD_PROJECT=<YOUR_PROJECT_ID>
GOOGLE_CLOUD_LOCATION=<YOUR_PROJECT_LOCATION>
```

### 4. Authenticate with Google Cloud ☁️

Log in with your Google Cloud account to allow the agent to access Vertex AI models:

```bash
gcloud auth login
```

## 🏃‍♂️ Running the Agent Locally

To start the agent and interact with it through a web interface, run the following command:

```bash
uv run adk web
```

This will start a local server. You can access the agent's chat UI by navigating to `http://localhost:8080` in your web browser.

## 💬 Example Interactions

You can interact with the agent using natural language. Here are a few examples:

- `Add an expense: $50 for groceries`
- `Add another expense: $120 for utilities in the bills category`
- `What's my total spending?`
- `How much have I spent on food?`
- `Show me my recent expenses.`
- `Add a recurring monthly expense: $1200 for rent starting today. Description: Rent payment for home.`
- `Project my spending for the next 3 months`

## 🌐 Deployment

You can deploy the agent as a service to Google Cloud Run.

The project includes a `server.py` and `Dockerfile` to package the agent as a containerized web application.

To deploy the agent, use the following `gcloud` command:

```bash
gcloud run deploy expense-tracker-agent \
 --source . \
 --region <YOUR_CHOSEN_REGION> \
 --allow-unauthenticated \
 --memory 4Gi \
 --cpu 2
```

Alternatively, you can use the ADK CLI to deploy:

```bash
uv run adk deploy cloud_run \
--project=<YOUR_PROJECT_ID> \
--region=<YOUR_CHOSEN_REGION> \
--service_name=expense-tracker-agent \
--app_name=expense-tracker \
--with_ui \
./expense_tracker
```

Once deployed, you will get a public URL to access your agent.
