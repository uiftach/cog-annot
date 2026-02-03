"""
Cog-Annot Knowledge Graph Generator

Automatically generates knowledge graphs from annotated texts showing:
- Objects (Cog1, Cog5) and their relationships
- Properties (Cog2p) and states (Cog2t)
- Actions (Cog2v)
- Parts (Cog3Int) and products (Cog3Der)
- Environments (Cog4)
- Temporal markers (TD)
- Movement (MOV)
- Human operations (PLACTAC)
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set
from collections import defaultdict

class AnnotationParser:
    """Parse Cog-Annot format: ⟨CogType#track: text⟩"""
    
    # Regex pattern for annotations
    PATTERN = r'⟨([^#:]+)#([^:]+):\s*([^⟩]+)⟩'
    
    def __init__(self, text: str):
        self.text = text
        self.annotations = []
        self.parse()
    
    def parse(self):
        """Extract all annotations from text"""
        for match in re.finditer(self.PATTERN, self.text):
            cog_type = match.group(1).strip()
            track = match.group(2).strip()
            content = match.group(3).strip()
            
            self.annotations.append({
                'type': cog_type,
                'track': track,
                'text': content,
                'position': match.start()
            })
        
        return self.annotations
    
    def get_by_type(self, cog_type: str) -> List[dict]:
        """Get all annotations of specific type"""
        return [a for a in self.annotations if a['type'] == cog_type]
    
    def get_by_track(self, track: str) -> List[dict]:
        """Get all annotations for specific track"""
        return [a for a in self.annotations if a['track'] == track]
    
    def get_unique_tracks(self) -> Set[str]:
        """Get all unique track identifiers"""
        return set(a['track'] for a in self.annotations)


class SectionDetector:
    """Detect logical divisions in text"""
    
    # Bekker number pattern (e.g., 486a.1, 487b.15)
    BEKKER_PATTERN = r'^\d{3}[ab]\.\d+$'
    
    @staticmethod
    def find_sections(text: str) -> List[Tuple[str, int, int]]:
        """
        Find logical sections based on Bekker numbers
        Returns: [(section_id, start_pos, end_pos), ...]
        """
        sections = []
        lines = text.split('\n')
        current_section = None
        section_start = 0
        position = 0
        
        for i, line in enumerate(lines):
            line_stripped = line.strip()
            
            # Check if line is a Bekker number
            if re.match(SectionDetector.BEKKER_PATTERN, line_stripped):
                # Save previous section
                if current_section:
                    sections.append((current_section, section_start, position))
                
                # Start new section
                current_section = line_stripped
                section_start = position
            
            position += len(line) + 1  # +1 for newline
        
        # Add final section
        if current_section:
            sections.append((current_section, section_start, position))
        
        return sections
    
    @staticmethod
    def get_section_text(text: str, start: int, end: int) -> str:
        """Extract text for a section"""
        return text[start:end]


class KnowledgeGraphGenerator:
    """Generate GraphViz DOT format knowledge graphs"""
    
    def __init__(self, annotations: List[dict], section_id: str = ""):
        self.annotations = annotations
        self.section_id = section_id
        self.tracks = defaultdict(list)
        self.organize_annotations()
    
    def organize_annotations(self):
        """Organize annotations by track"""
        for ann in self.annotations:
            self.tracks[ann['track']].append(ann)
    
    def generate_dot(self) -> str:
        """Generate DOT format graph"""
        lines = [
            'digraph CogAnnot {',
            '  rankdir=TB;',
            '  node [shape=box, style=rounded];',
            '  graph [fontname="Arial", nodesep=0.5, ranksep=0.8];',
            '  node [fontname="Arial"];',
            '  edge [fontname="Arial"];',
            ''
        ]
        
        # Add title
        if self.section_id:
            lines.append(f'  label="{self.section_id}";')
            lines.append('  labelloc=t;')
            lines.append('  fontsize=16;')
            lines.append('')
        
        # Track which nodes we've created
        created_nodes = set()
        
        # Process each track
        for track_id, anns in self.tracks.items():
            # Find primary object (Cog1)
            cog1_anns = [a for a in anns if a['type'] == 'Cog1' or a['type'] == 'Cog1gen']
            
            if cog1_anns:
                # Create primary object node
                obj = cog1_anns[0]
                node_id = f"obj_{track_id}"
                label = obj['text'].replace('"', '\\"')
                
                lines.append(f'  {node_id} [label="{label}", fillcolor="#FFE6E6", style="rounded,filled"];')
                created_nodes.add(node_id)
                
                # Add properties (Cog2p)
                for ann in anns:
                    if ann['type'] == 'Cog2p':
                        prop_id = f"prop_{track_id}_{len(created_nodes)}"
                        prop_label = ann['text'].replace('"', '\\"')
                        lines.append(f'  {prop_id} [label="{prop_label}", fillcolor="#E6F3FF", style="rounded,filled"];')
                        lines.append(f'  {node_id} -> {prop_id} [label="has property", color="#0066CC"];')
                        created_nodes.add(prop_id)
                    
                    # Add states (Cog2t)
                    elif ann['type'] == 'Cog2t':
                        state_id = f"state_{track_id}_{len(created_nodes)}"
                        state_label = ann['text'].replace('"', '\\"')
                        lines.append(f'  {state_id} [label="{state_label}", fillcolor="#FFF9E6", style="rounded,filled"];')
                        lines.append(f'  {node_id} -> {state_id} [label="in state", color="#CC9900"];')
                        created_nodes.add(state_id)
                    
                    # Add actions (Cog2v)
                    elif ann['type'] == 'Cog2v':
                        action_id = f"action_{track_id}_{len(created_nodes)}"
                        action_label = ann['text'].replace('"', '\\"')
                        lines.append(f'  {action_id} [label="{action_label}", fillcolor="#E6FFE6", style="rounded,filled", shape=ellipse];')
                        lines.append(f'  {node_id} -> {action_id} [label="does", color="#00AA00"];')
                        created_nodes.add(action_id)
                    
                    # Add parts (Cog3Int)
                    elif ann['type'] == 'Cog3Int':
                        part_id = f"part_{track_id}_{len(created_nodes)}"
                        part_label = ann['text'].replace('"', '\\"')
                        lines.append(f'  {part_id} [label="{part_label}", fillcolor="#F0E6FF", style="rounded,filled"];')
                        lines.append(f'  {node_id} -> {part_id} [label="has part", color="#9900CC"];')
                        created_nodes.add(part_id)
                    
                    # Add products (Cog3Der)
                    elif ann['type'] == 'Cog3Der':
                        prod_id = f"prod_{track_id}_{len(created_nodes)}"
                        prod_label = ann['text'].replace('"', '\\"')
                        lines.append(f'  {prod_id} [label="{prod_label}", fillcolor="#FFE6F0", style="rounded,filled"];')
                        lines.append(f'  {node_id} -> {prod_id} [label="produces", color="#CC0066"];')
                        created_nodes.add(prod_id)
                    
                    # Add environment (Cog4)
                    elif ann['type'].startswith('Cog4'):
                        env_id = f"env_{len(created_nodes)}"
                        env_label = ann['text'].replace('"', '\\"')
                        lines.append(f'  {env_id} [label="{env_label}", fillcolor="#E6F9FF", style="rounded,filled", shape=house];')
                        lines.append(f'  {node_id} -> {env_id} [label="in", color="#0099CC"];')
                        created_nodes.add(env_id)
        
        # Add Cog5 (secondary objects)
        cog5_anns = [a for a in self.annotations if a['type'] == 'Cog5']
        for ann in cog5_anns:
            node_id = f"cog5_{ann['track']}"
            if node_id not in created_nodes:
                label = ann['text'].replace('"', '\\"')
                lines.append(f'  {node_id} [label="{label}", fillcolor="#FFE6CC", style="rounded,filled,dashed"];')
                created_nodes.add(node_id)
        
        # Add temporal markers
        td_anns = [a for a in self.annotations if a['type'].startswith('TD_')]
        if td_anns:
            lines.append('')
            lines.append('  // Temporal markers')
            for ann in td_anns:
                td_id = f"td_{len(created_nodes)}"
                label = f"{ann['type']}: {ann['text']}"
                label = label.replace('"', '\\"')
                lines.append(f'  {td_id} [label="{label}", fillcolor="#FFFFCC", style="rounded,filled", shape=note];')
                created_nodes.add(td_id)
        
        # Add movement markers
        mov_anns = [a for a in self.annotations if a['type'].startswith('MOV_')]
        if mov_anns:
            lines.append('')
            lines.append('  // Movement markers')
            for ann in mov_anns:
                mov_id = f"mov_{len(created_nodes)}"
                label = f"{ann['type']}: {ann['text']}"
                label = label.replace('"', '\\"')
                lines.append(f'  {mov_id} [label="{label}", fillcolor="#E6CCFF", style="rounded,filled", shape=diamond];')
                created_nodes.add(mov_id)
        
        # Add PLACTAC
        plac_anns = [a for a in self.annotations if a['type'].startswith('PLACTAC')]
        if plac_anns:
            lines.append('')
            lines.append('  // Human operations')
            for ann in plac_anns:
                plac_id = f"plac_{len(created_nodes)}"
                label = ann['text'].replace('"', '\\"')
                lines.append(f'  {plac_id} [label="{label}", fillcolor="#FFD6CC", style="rounded,filled", shape=octagon];')
                created_nodes.add(plac_id)
        
        lines.append('}')
        return '\n'.join(lines)
    
    def save_dot(self, filename: str):
        """Save DOT file"""
        dot_content = self.generate_dot()
        Path(filename).write_text(dot_content, encoding='utf-8')
        print(f"Graph saved to: {filename}")
        return filename


def generate_graph_for_section(text_file: str, section_id: str = None, output_dir: str = "graphs"):
    """
    Generate knowledge graph for a specific section or entire file
    
    Args:
        text_file: Path to annotated text file
        section_id: Bekker number (e.g., "486a.1") or None for entire file
        output_dir: Directory to save graph files
    """
    # Read text
    text = Path(text_file).read_text(encoding='utf-8')
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    if section_id:
        # Find specific section
        sections = SectionDetector.find_sections(text)
        section_found = False
        
        for sec_id, start, end in sections:
            if sec_id == section_id:
                section_text = SectionDetector.get_section_text(text, start, end)
                parser = AnnotationParser(section_text)
                
                # Generate graph
                generator = KnowledgeGraphGenerator(parser.annotations, section_id)
                output_file = output_path / f"graph_{section_id.replace('.', '_')}.dot"
                generator.save_dot(str(output_file))
                
                print(f"\nFound {len(parser.annotations)} annotations in section {section_id}")
                section_found = True
                break
        
        if not section_found:
            print(f"Section '{section_id}' not found!")
            print("\nAvailable sections:")
            for sec_id, _, _ in sections:
                print(f"  - {sec_id}")
    
    else:
        # Generate for entire file
        parser = AnnotationParser(text)
        generator = KnowledgeGraphGenerator(parser.annotations, "Full Document")
        
        base_name = Path(text_file).stem
        output_file = output_path / f"graph_{base_name}.dot"
        generator.save_dot(str(output_file))
        
        print(f"\nFound {len(parser.annotations)} annotations in full document")


def list_sections(text_file: str):
    """List all sections in a file"""
    text = Path(text_file).read_text(encoding='utf-8')
    sections = SectionDetector.find_sections(text)
    
    print(f"\nFound {len(sections)} sections in {text_file}:")
    print()
    
    for sec_id, start, end in sections:
        # Get preview text
        section_text = SectionDetector.get_section_text(text, start, end)
        parser = AnnotationParser(section_text)
        ann_count = len(parser.annotations)
        
        # Get first few words
        preview = section_text[:80].strip()
        if len(section_text) > 80:
            preview += "..."
        
        print(f"  {sec_id:12} - {ann_count:3} annotations - {preview}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Generate knowledge graphs from Cog-Annot annotated texts"
    )
    parser.add_argument("file", help="Path to annotated text file")
    parser.add_argument("-s", "--section", help="Section ID (Bekker number, e.g., 486a.1)")
    parser.add_argument("-o", "--output", default="graphs", help="Output directory for graph files")
    parser.add_argument("-l", "--list", action="store_true", help="List all sections in file")
    
    args = parser.parse_args()
    
    if args.list:
        list_sections(args.file)
    else:
        generate_graph_for_section(args.file, args.section, args.output)
        print("\nTo visualize: install GraphViz and run:")
        if args.section:
            print(f"  dot -Tpng graphs/graph_{args.section.replace('.', '_')}.dot -o graph.png")
        else:
            base_name = Path(args.file).stem
            print(f"  dot -Tpng graphs/graph_{base_name}.dot -o graph.png")
