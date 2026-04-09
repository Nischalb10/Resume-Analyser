import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


class MemoryStore:
    def __init__(self, path: Path):
        self.path = path
        self.data: Dict[str, Any] = {"interactions": []}

    def load(self) -> None:
        if self.path.exists():
            with self.path.open("r", encoding="utf-8") as handle:
                self.data = json.load(handle)

    def save(self) -> None:
        with self.path.open("w", encoding="utf-8") as handle:
            json.dump(self.data, handle, indent=2)

    def remember_interaction(
        self,
        resume_text: str,
        target_role: str,
        analysis: Dict[str, Any],
        improved_resume: str,
    ) -> None:
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "target_role": target_role,
            "resume_text": resume_text,
            "analysis": analysis,
            "improved_resume": improved_resume,
        }
        self.data["interactions"].append(entry)

    def get_history(self) -> List[Dict[str, Any]]:
        return self.data.get("interactions", [])

    def get_recent_context(self, limit: int = 3) -> str:
        interactions = self.get_history()[-limit:]
        if not interactions:
            return "No previous interactions available."

        lines = ["Memory summary from recent resume interactions:"]
        for idx, item in enumerate(interactions, start=1):
            lines.append(
                f"{idx}. Role: {item['target_role']}; Improvement length: {len(item['improved_resume'])} chars"
            )
        return "\n".join(lines)
