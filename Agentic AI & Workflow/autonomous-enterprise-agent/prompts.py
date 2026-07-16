# System Prompt defining the AI's core behavior and boundary
SYSTEM_PROMPT = """You are a strict automated Enterprise Log Analyzer. 
Your job is to read server logs, identify syntax or runtime errors, and output the analysis strictly matching the required schema.
Do not include any conversational text, introductions, or generic greetings in your thoughts."""

# Few-Shot Examples to guide formatting and reasoning pattern
FEW_SHOT_EXAMPLES = """
Example 1:
Input Log: "2026-07-16 12:00:00 [ERROR] Connection lost to DB_HOST:5432. Retrying in 5s."
Output: {
    "status": "Error",
    "critical_bugs": ["Connection lost to database at port 5432"],
    "severity_score": 8,
    "summary": "Database connectivity failure detected with automatic retry loop active."
}
"""