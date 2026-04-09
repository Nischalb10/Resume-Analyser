import json
import os
from pathlib import Path

from dotenv import load_dotenv
from memory_store import MemoryStore
from agent import ResumeAnalyzerAgent

BASE_DIR = Path(__file__).resolve().parent


def main():
    load_dotenv(BASE_DIR / ".env")
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required in .env or environment variables.")

    memory_file = BASE_DIR / "resume_memory.json"
    memory_store = MemoryStore(memory_file)
    memory_store.load()

    agent = ResumeAnalyzerAgent(api_key=api_key, memory_store=memory_store)

    print("\nResume Analyzer & Improver")
    print("===========================\n")

    while True:
        print("Select an action:")
        print("1. Analyze resume")
        print("2. Improve resume")
        print("3. Show memory history")
        print("4. Exit")
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            resume_text = input("Paste resume text: \n")
            target_role = input("Target role or industry: ").strip()
            result = agent.run_tool("analyze_resume", resume_text=resume_text, target_role=target_role)
            print("\nStructured analysis result:\n")
            print(json.dumps(result, indent=2))

        elif choice == "2":
            resume_text = input("Paste resume text to improve: \n")
            target_role = input("Target role or industry: ").strip()
            result = agent.run_tool("suggest_improvements", resume_text=resume_text, target_role=target_role)
            print("\nImproved resume package:\n")
            print(json.dumps(result, indent=2))
            memory_store.remember_interaction(
                resume_text=resume_text,
                target_role=target_role,
                analysis=result.get("analysis", {}),
                improved_resume=result.get("improved_resume", ""),
            )
            memory_store.save()

        elif choice == "3":
            history = memory_store.get_history()
            print(json.dumps(history, indent=2))

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()
