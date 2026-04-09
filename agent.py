import json
from typing import Any, Callable, Dict

from openai import OpenAI

try:
    from openai.agents import Tool
    AGENTS_SDK_AVAILABLE = True
except Exception:
    AGENTS_SDK_AVAILABLE = False


class ResumeAnalyzerAgent:
    def __init__(self, api_key: str, memory_store: Any):
        self.client = OpenAI(api_key=api_key)
        self.memory_store = memory_store
        self.tools: Dict[str, Callable[..., Dict[str, Any]]] = {
            "analyze_resume": self._tool_analyze_resume,
            "suggest_improvements": self._tool_suggest_improvements,
        }

    def run_tool(self, tool_name: str, **kwargs: Any) -> Dict[str, Any]:
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' is not available.")
        return self.tools[tool_name](**kwargs)

    def _get_memory_context(self) -> str:
        return self.memory_store.get_recent_context() if self.memory_store else "No memory available."

    def _invoke_llm(self, prompt: str) -> str:
        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
            max_tokens=900,
            temperature=0.2,
        )
        if hasattr(response, "output_text") and response.output_text:
            return response.output_text
        if hasattr(response, "output"):
            output_chunks = []
            for item in response.output:
                if isinstance(item, dict) and "content" in item:
                    for block in item["content"]:
                        if block.get("type") == "output_text":
                            output_chunks.append(block.get("text", ""))
            return "".join(output_chunks)
        return str(response)

    def _parse_json(self, text: str) -> Dict[str, Any]:
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {"parsing_error": "Unable to parse JSON.", "raw_response": text}

    def _tool_analyze_resume(self, resume_text: str, target_role: str) -> Dict[str, Any]:
        memory_context = self._get_memory_context()
        prompt = f"""
You are an AI resume reviewer. Analyze the resume below and return a JSON object only.
Include: overall_score, strengths, weaknesses, role_fit, formatting_issues, suggested_actions.
Use the candidate target role and memory context.
Memory Context:
{memory_context}

Resume:
{resume_text}

Target role: {target_role}

Respond with valid JSON only.
"""
        response_text = self._invoke_llm(prompt)
        output = self._parse_json(response_text)
        if "overall_score" in output:
            return output
        return {
            "overall_score": 0,
            "strengths": [],
            "weaknesses": [],
            "role_fit": "Unknown",
            "formatting_issues": "Could not parse response cleanly.",
            "suggested_actions": [response_text],
        }

    def _tool_suggest_improvements(self, resume_text: str, target_role: str) -> Dict[str, Any]:
        memory_context = self._get_memory_context()
        prompt = f"""
You are an AI resume improver. Rewrite the resume to better match the target role.
Return JSON with keys: improved_resume, summary_of_changes, strength_statement, recommended_formatting.
Include memory context in your rewriting.

Memory Context:
{memory_context}

Resume:
{resume_text}

Target role: {target_role}

Respond with valid JSON only.
"""
        response_text = self._invoke_llm(prompt)
        output = self._parse_json(response_text)
        if "improved_resume" in output:
            return {
                "analysis": {
                    "source_role": target_role,
                    "source_length": len(resume_text),
                },
                **output,
            }
        return {
            "improved_resume": resume_text,
            "summary_of_changes": ["Unable to parse structured JSON output."],
            "strength_statement": "No improved summary could be generated.",
            "recommended_formatting": "Keep sections short, use bullet points, and add quantifiable results.",
            "raw_response": response_text,
        }

    def describe_tools(self) -> Dict[str, str]:
        descriptions = {
            "analyze_resume": "Analyze resume strengths, weaknesses, role fit, and formatting guidance.",
            "suggest_improvements": "Rewrite resume text with stronger impact and structure.",
        }
        if AGENTS_SDK_AVAILABLE:
            descriptions["sdk_available"] = "OpenAI Agents SDK import succeeded. Tools can be registered in the SDK interface."
        else:
            descriptions["sdk_available"] = "OpenAI Agents SDK import not detected; fallback prompt orchestration is active."
        return descriptions
