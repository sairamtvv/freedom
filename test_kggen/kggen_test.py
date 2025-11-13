from kg_gen import KGGen
from pathlib import Path


output_path = Path(__file__).parent/"graphs"/"test_kggen.html"
output_path.parent.mkdir(parents=True, exist_ok=True)

# Initialize KGGen with optional configuration
kg = KGGen(
  model="ollama/qwen3:8b", 
#   model="openai/gpt-4o",  # Default model
  temperature=0.0,        # Default temperature
  # Optional if set in environment or using a local model
)

# EXAMPLE 1: Single string with context
text_input = "Linda is Josh's mother. Ben is Josh's brother. Andrew is Josh's father."
graph = kg.generate(
  input_data=text_input,
  context="Family relationships"
)


KGGen.visualize(graph, output_path, open_in_browser=True)
