from pydantic import BaseModel, Field
from typing import List

class LogAnalysisResult(BaseModel):
    status: str = Field(description="The status of the analysis, e.g., 'Success', 'Error', or 'Warning'.")
    critical_bugs: List[str] = Field(description="List of critical bugs or errors found in the input log.")
    severity_score: int = Field(description="Severity rating from 1 (Low) to 10 (Critical).")
    summary: str = Field(description="A concise one-sentence technical summary of the log state.")