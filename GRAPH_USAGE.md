# Knowledge Graph Generator Usage Guide

## Quick Start

### 1. List all sections in your annotated text:
```bash
python generate_graph.py "Aristoteles/HA/HA raw text to 491.14.txt" --list
```

### 2. Generate graph for a specific section:
```bash
python generate_graph.py "Aristoteles/HA/HA raw text to 491.14.txt" -s "487b.15"
```

### 3. Generate graph for entire document:
```bash
python generate_graph.py "Aristoteles/HA/HA raw text to 491.14.txt"
```

## Installation

### Python (required):
```bash
# Already installed on Windows
python --version
```

### GraphViz (for visualization):
```bash
# Windows: Download from https://graphviz.org/download/
# Or use Chocolatey:
choco install graphviz

# Or winget:
winget install graphviz
```

## Visualizing Graphs

### Convert DOT to PNG:
```bash
dot -Tpng graphs/graph_487b_15.dot -o graph_487b_15.png
```

### Convert DOT to SVG (scalable):
```bash
dot -Tsvg graphs/graph_487b_15.dot -o graph_487b_15.svg
```

### Convert DOT to PDF:
```bash
dot -Tpdf graphs/graph_487b_15.dot -o graph_487b_15.pdf
```

### Interactive HTML (recommended):
```bash
dot -Tsvg graphs/graph_487b_15.dot | python -c "import sys; print('<html><body>' + sys.stdin.read() + '</body></html>')" > graph.html
```

## Graph Color Coding

- **Pink (#FFE6E6)**: Primary objects (Cog1)
- **Light Blue (#E6F3FF)**: Properties (Cog2p)
- **Light Yellow (#FFF9E6)**: States (Cog2t)
- **Light Green (#E6FFE6)**: Actions (Cog2v) - ellipse shape
- **Purple (#F0E6FF)**: Parts (Cog3Int)
- **Rose (#FFE6F0)**: Products (Cog3Der)
- **Cyan (#E6F9FF)**: Environment (Cog4) - house shape
- **Orange (#FFE6CC)**: Secondary objects (Cog5) - dashed border
- **Light Yellow (#FFFFCC)**: Temporal markers (TD) - note shape
- **Lavender (#E6CCFF)**: Movement markers (MOV) - diamond shape
- **Peach (#FFD6CC)**: Human operations (PLACTAC) - octagon shape

## Examples

### Working with Greek texts:
```bash
# List sections by Bekker numbers
python generate_graph.py "Aristoteles/HA/HA raw text to 491.14.txt" --list

# Generate for Book I, section 486a.15
python generate_graph.py "Aristoteles/HA/HA raw text to 491.14.txt" -s "486a.15"

# Visualize
dot -Tpng graphs/graph_486a_15.dot -o graph_486a_15.png
```

### Batch processing:
```bash
# Generate graphs for multiple sections
for section in 486a.15 486b.10 487a.10; do
    python generate_graph.py "Aristoteles/HA/HA raw text to 491.14.txt" -s $section
    dot -Tpng graphs/graph_${section//./_}.dot -o graphs/graph_${section//./_}.png
done
```

## VS Code Integration (Future)

You can create a VS Code task or command to:
1. Detect current cursor position
2. Identify the section
3. Auto-generate and display graph
4. Update as you move through the text

## Output Directory

All graphs are saved to `graphs/` directory by default.

To change output location:
```bash
python generate_graph.py "yourfile.txt" -s "section" -o "output_folder"
```

## Understanding the Graphs

### Node shapes:
- **Rectangle**: Objects, properties, states
- **Ellipse**: Actions (what objects do)
- **House**: Environment/habitat
- **Diamond**: Movement endpoints
- **Octagon**: Human operations
- **Note**: Time markers

### Edge colors:
- **Blue**: "has property"
- **Yellow/Brown**: "in state"
- **Green**: "does" (action)
- **Purple**: "has part"
- **Pink**: "produces"
- **Cyan**: "in" (environment)

## Troubleshooting

### "python is not recognized":
- Make sure Python is installed
- Restart terminal after installation

### "dot is not recognized":
- Install GraphViz (see Installation section)
- Add to PATH: `C:\Program Files\Graphviz\bin`
- Restart terminal

### Graph too large:
- Generate for specific sections instead of entire document
- Use SVG format for better scaling
- Adjust graph parameters in generate_graph.py

### Unicode/Greek characters not displaying:
- Make sure your terminal supports UTF-8
- Use SVG or PNG output formats
- Install fonts that support Greek characters

## Advanced Usage

### Programmatic access:
```python
from generate_graph import AnnotationParser, KnowledgeGraphGenerator

text = Path("yourfile.txt").read_text(encoding='utf-8')
parser = AnnotationParser(text)
generator = KnowledgeGraphGenerator(parser.annotations, "Section Title")
dot_content = generator.generate_dot()
```

### Custom graph styling:
Edit `generate_graph.py` to modify:
- Colors (fillcolor values)
- Shapes (shape attribute)
- Layout (rankdir: TB, LR, etc.)
- Spacing (nodesep, ranksep)

## Next Steps

1. Install GraphViz for visualization
2. Try generating graphs for different sections
3. Explore different output formats (PNG, SVG, PDF)
4. Integrate into your workflow
