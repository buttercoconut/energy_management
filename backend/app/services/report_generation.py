# Placeholder for report generation logic
from typing import List

class ReportGenerator:
    def __init__(self, data: List[dict]):
        self.data = data

    def generate(self) -> str:
        # Simple CSV-like string
        lines = [",".join(self.data[0].keys())]
        for row in self.data:
            lines.append(",".join(str(v) for v in row.values()))
        return "\n".join(lines)
