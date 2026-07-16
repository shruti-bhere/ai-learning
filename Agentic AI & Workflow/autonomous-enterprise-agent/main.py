from config import get_llm
from schemas import LogAnalysisResult
from prompts import SYSTEM_PROMPT, FEW_SHOT_EXAMPLES

def run_agent(raw_log_data: str):
    # 1. Initialize our fast cloud LLM (Groq)
    llm = get_llm()
    
    # 2. Force the model to output structured Pydantic format (JSON Mode wrapper)
    structured_llm = llm.with_structured_output(LogAnalysisResult)
    
    # 3. Construct the message payload combining System rules, Few-shot, and User query
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "system", "content": f"Here is how you must format your response:\n{FEW_SHOT_EXAMPLES}"},
        {"role": "user", "content": f"Please think step-by-step and analyze this log data:\n{raw_log_data}"}
    ]
    
    print("🤖 Agent is analyzing the enterprise log...")
    
    # 4. Invoke the model
    response = structured_llm.invoke(messages)
    return response

if __name__ == "__main__":
    # Test cases simulating a critical server crash log
    sample_server_log = (
        "2026-07-16 12:54:04 [CRITICAL] OutOfMemoryError: Java heap space. "
        "Thread 'http-nio-8080-exec-10' crashed. Server terminating process."
    )
    
    # Run the core foundation agent
    result = run_agent(sample_server_log)
    
    # Print the clean verified object (Downstream code safe from crashes)
    print("\n✅ Verified Structured Output Received:")
    print(f"Status: {result.status}")
    print(f"Severity: {result.severity_score}/10")
    print(f"Bugs Found: {result.critical_bugs}")
    print(f"Summary: {result.summary}")