# Weather Agent using MCP (Agentic AI)

Author: Rachana Varma  
Assignment: Agentic AI with Weather MCP Tool

---

## Overview

This project implements a simple Agentic AI system where an AI agent processes natural language weather queries and delegates execution to a Weather MCP Tool.

The Weather MCP Tool retrieves weather information using the National Weather Service API.

API Used:  
https://api.weather.gov/

The system demonstrates the core concept of Agent + Tool interaction, where the agent identifies user intent and uses an external capability (tool) to complete the task.

---

## Architecture

User Query  
↓  
AI Agent (Intent Detection)  
↓  
Weather MCP Tool  
↓  
api.weather.gov  
↓  
Parsed Weather Data  
↓  
Formatted Response to User

---

## Components

### 1. Weather MCP Tool
File: `weather_tool.py`

Responsibilities:
- Accept city name as input
- Convert city name to latitude and longitude
- Call the api.weather.gov API
- Parse the weather response
- Return structured weather information

### 2. AI Agent
File: `agent.py`

Responsibilities:
- Accept natural language user queries
- Detect user intent (weather request)
- Extract city name from the query
- Delegate execution to the Weather MCP Tool
- Format and return a readable response

---

## Example Interaction

User Query:

```
weather Chicago
```

Agent Response:

```
Agent: Fetching weather information...

Weather in Chicago
Temperature: 72 F
Condition: Mostly Sunny
```

---

## Setup Instructions

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run the agent

```
python agent.py
```

---

## Example Queries

```
weather Chicago
weather New York
weather Seattle
```

---

## Supported Locations

The API used in this project (api.weather.gov) only provides weather data for United States locations.

Queries for locations outside the US may return a message indicating that weather data is unavailable.

---

## Technologies Used

- Python
- Requests library
- National Weather Service API
- GitHub Codespaces

---

## Assignment Objectives Covered

This project demonstrates the following concepts:

- Agentic AI workflow
- Natural language query handling
- Agent intent detection
- Delegation to external tools
- MCP tool integration
- External API integration
- Structured response generation

---

## Project Structure

```
weather-agent-mcp
│
├── agent.py
├── weather_tool.py
├── requirements.txt
└── README.md
```
