import os
import re

LEETCODE_URL = "https://leetcode.com/problems/"
SUPPORTED_EXTENSIONS = ['.py', '.cpp', '.java', '.js']

files = [f for f in os.listdir() if os.path.isfile(f) and os.path.splitext(f)[1] in SUPPORTED_EXTENSIONS]

table_lines = []
table_lines.append("| # | Problem | Solution | Language |")
table_lines.append("|---|---------|----------|----------|")

for filename in sorted(files, key=lambda x: int(re.match(r'^(\d+)', x).group(1))):
    match = re.match(r'^(\d+)\.(.+)\.(py|cpp|java|js)$', filename)
    if not match:
        continue

    problem_number = int(match.group(1))
    problem_slug = match.group(2).replace('_', '-')
    problem_title = match.group(2).replace('-', ' ').title()
    language_map = {'py': 'Python', 'cpp': 'C++', 'java': 'Java', 'js': 'JavaScript'}
    ext = match.group(3)
    language = language_map.get(ext, ext)

    problem_link = f"{LEETCODE_URL}{problem_slug}/"
    solution_link = f"./{filename}"

    table_lines.append(f"| {problem_number} | [{problem_title}]({problem_link}) | [Solution]({solution_link}) | {language} |")

with open("README.md", "w", encoding="utf-8") as f:
    f.write("# LeetCode Solutions\n\n")
    f.write(f"Total Problems Solved: {len(table_lines)-2}\n\n")
    f.write("\n".join(table_lines))

print("README.md generated!")
