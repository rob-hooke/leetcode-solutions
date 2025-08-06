import os
import re

LEETCODE_URL = "https://leetcode.com/problems/"
SUPPORTED_EXTENSIONS = ['.py', '.cpp', '.java', '.js']

# Only keep files matching the pattern: number.slug.extension
pattern = re.compile(r'^(\d+)\.(.+)\.(py|cpp|java|js)$')

# Filter and collect matching files
files = [f for f in os.listdir() if os.path.isfile(f) and pattern.match(f)]

# Now sort safely using the extracted number
files_sorted = sorted(files, key=lambda x: int(pattern.match(x).group(1)))

table_lines = []
table_lines.append("| # | Problem | Solution | Language |")
table_lines.append("|---|---------|----------|----------|")

language_map = {'py': 'Python', 'cpp': 'C++', 'java': 'Java', 'js': 'JavaScript'}

for filename in files_sorted:
    match = pattern.match(filename)
    problem_number = int(match.group(1))
    problem_slug = match.group(2).replace('_', '-')
    problem_title = match.group(2).replace('-', ' ').title()
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
