import json
import os
import sys
import textwrap

def load_tree(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def evaluate_condition(condition_str, current_answer, signals):
    eval_str = condition_str.replace("answer", f"'{current_answer}'")
    eval_str = eval_str.replace("||", "or").replace("&&", "and")
    
    for axis in ['axis1', 'axis2', 'axis3']:
        for trait in ['internal', 'external', 'contribution', 'entitlement', 'self', 'altro']:
            signal_key = f"signals.{axis}.{trait}"
            if signal_key in eval_str:
                eval_str = eval_str.replace(signal_key, str(signals[axis][trait]))
                
    try:
        return eval(eval_str)
    except Exception as e:
        print(f"Error evaluating condition: {condition_str} -> {e}")
        return False

def interpolate_string(text, signals):
    axis1_dom = "internal" if signals["axis1"]["internal"] >= signals["axis1"]["external"] else "external"
    axis2_dom = "contribution" if signals["axis2"]["contribution"] >= signals["axis2"]["entitlement"] else "entitlement"
    axis3_dom = "altrocentric" if signals["axis3"]["altro"] >= signals["axis3"]["self"] else "self-centric"

    res = text.replace("{axis1_dom}", axis1_dom)
    res = res.replace("{axis2_dom}", axis2_dom)
    res = res.replace("{axis3_dom}", axis3_dom)
    return res

def process_signal(signal_str, signals):
    if not signal_str:
        return
    axis, trait = signal_str.split(':')
    if axis in signals and trait in signals[axis]:
        signals[axis][trait] += 1

def print_wrapped(text, indent=0):
    wrapper = textwrap.TextWrapper(width=80, initial_indent=" " * indent, subsequent_indent=" " * indent)
    print(wrapper.fill(text))

def run_agent():
    # Robust pathing
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tree_path = os.path.join(current_dir, '..', 'tree', 'reflection-tree.json')
    
    try:
        tree_data = load_tree(tree_path)
    except FileNotFoundError:
        print(f"Error: reflection-tree.json not found at {tree_path}")
        sys.exit(1)
        
    nodes = {n['id']: n for n in tree_data['nodes']}
    
    state = {
        "answers": {},
        "current_answer": None,
        "signals": {
            "axis1": {"internal": 0, "external": 0},
            "axis2": {"contribution": 0, "entitlement": 0},
            "axis3": {"self": 0, "altro": 0}
        }
    }
    
    def get_next_node_id(current_node):
        idx = tree_data['nodes'].index(current_node)
        if idx < len(tree_data['nodes']) - 1:
            return tree_data['nodes'][idx + 1]['id']
        return None

    current_node_id = "START"
    
    while current_node_id:
        node = nodes.get(current_node_id)
        if not node:
            print(f"Error: Node {current_node_id} not found.")
            break
            
        if node['type'] == 'start':
            print("\n" + "="*80)
            print_wrapped(f"*** {node['text']} ***")
            print("="*80 + "\n")
            current_node_id = get_next_node_id(node)
            
        elif node['type'] == 'question':
            print_wrapped(interpolate_string(node['text'], state['signals']))
            print("")
            valid_options = []
            for opt in node['options']:
                print_wrapped(f"{opt['value']}) {opt['text']}", indent=2)
                valid_options.append(opt['value'])
            
            print("")
            while True:
                ans = input("Your choice: ").strip().upper()
                if ans in valid_options:
                    break
                print("Invalid choice, please select a valid option.")
                
            state['answers'][node['id']] = ans
            state['current_answer'] = ans
            
            chosen_opt = next((o for o in node['options'] if o['value'] == ans), None)
            if chosen_opt and 'signal' in chosen_opt:
                process_signal(chosen_opt['signal'], state['signals'])
                
            current_node_id = get_next_node_id(node)
            print("\n" + "-"*80 + "\n")
            
        elif node['type'] == 'decision':
            target = None
            for rule in node['rules']:
                if evaluate_condition(rule['condition'], state['current_answer'], state['signals']):
                    target = rule['target']
                    if 'signal' in rule:
                        process_signal(rule['signal'], state['signals'])
                    break
            
            if target:
                current_node_id = target
            else:
                print("Error: No decision rule matched.")
                break
                
        elif node['type'] == 'reflection':
            print_wrapped(f"Insight: {interpolate_string(node['text'], state['signals'])}")
            print("")
            input("Press Enter to continue...")
            print("\n" + "-"*80 + "\n")
            current_node_id = get_next_node_id(node)
            
        elif node['type'] == 'bridge':
            print_wrapped(f"-> {interpolate_string(node['text'], state['signals'])}")
            print("")
            current_node_id = node.get('target') or get_next_node_id(node)
            
        elif node['type'] == 'summary':
            print("="*80)
            print("SUMMARY")
            print("="*80)
            print_wrapped(interpolate_string(node['text'], state['signals']))
            print("="*80 + "\n")
            current_node_id = get_next_node_id(node)
            
        elif node['type'] == 'end':
            print_wrapped(f"*** {node['text']} ***")
            print("")
            break

if __name__ == "__main__":
    run_agent()
