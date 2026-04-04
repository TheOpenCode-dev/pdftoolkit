#!/usr/bin/env python3
import json, sys, os, yaml
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GRAPH_PATH = os.path.join(BASE_DIR, '..', '..', 'memory', 'ontology', 'graph.jsonl')
SCHEMA_PATH = os.path.join(BASE_DIR, '..', '..', 'memory', 'ontology', 'schema.yaml')

os.makedirs(os.path.dirname(GRAPH_PATH), exist_ok=True)

def load_graph():
    nodes, edges = [], []
    if os.path.exists(GRAPH_PATH):
        with open(GRAPH_PATH, 'r') as f:
            for line in f:
                item = json.loads(line.strip())
                if item['op'] == 'node': nodes.append(item['data'])
                elif item['op'] == 'edge': edges.append(item['data'])
    return nodes, edges

def save_op(op, data):
    with open(GRAPH_PATH, 'a') as f:
        json.dump({'op': op, 'data': data}, f)
        f.write('\n')

def create_node(type_name, props):
    nid = f"{type_name.lower()}_{datetime.now().strftime('%H%M%S')}"
    props['type'] = type_name
    props['id'] = nid
    save_op('node', props)
    return nid

def create_edge(from_id, rel_type, to_id):
    save_op('edge', {'from': from_id, 'rel': rel_type, 'to': to_id})

def query_nodes(type_name=None):
    nodes, _ = load_graph()
    if type_name:
        nodes = [n for n in nodes if n.get('type') == type_name]
    return nodes

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ontology.py [node|edge|query] ...")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == 'node':
        args = dict(s.split('=', 1) for s in sys.argv[2:])
        nid = create_node(args['--type'], json.loads(args.get('--props', '{}')))
        print(f"Created Node: {nid}")
    elif cmd == 'edge':
        args = dict(s.split('=', 1) for s in sys.argv[2:])
        create_edge(args['--from'], args['--rel'], args['--to'])
        print(f"Linked: {args['--from']} --[{args['--rel']}]--> {args['--to']}")
    elif cmd == 'query':
        args = dict(s.split('=', 1) for s in sys.argv[2:])
        results = query_nodes(args.get('--type'))
        print(json.dumps(results, indent=2))