import os
import subprocess
from datetime import datetime


def get_git_diff():
    result = subprocess.run(
        "git diff HEAD~1 HEAD",
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


def generate_mock_summary(diff):
    return f"""
# PR Summary (Mock Mode)

Generated at: {datetime.utcnow()}

Changes detected in this PR.
Total diff size: {len(diff.splitlines())} lines.

(This is mock mode — no API key provided.)
"""


def generate_ai_summary(diff):
    from openai import OpenAI

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a DevOps assistant. Summarize this git diff clearly."
            },
            {
                "role": "user",
                "content": diff[:8000]  # limit size
            }
        ]
    )

    return response.choices[0].message.content


def main():
    os.makedirs("docs", exist_ok=True)
    file_path = "docs/PR_SUMMARY.md"

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("# PR Summary Log\n")

    diff = get_git_diff()

    if not diff:
        print("No changes detected.")
        return

    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        print("🔮 Generating AI summary...")
        summary = generate_ai_summary(diff)
    else:
        print("⚠ No API key found. Running in mock mode...")
        summary = generate_mock_summary(diff)

    with open(file_path, "a") as f:
        f.write(summary)

    print("✅ PR summary generated at docs/PR_SUMMARY.md")


if __name__ == "__main__":
    main()
