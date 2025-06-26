import re

def preprocess_bfpp(source_code):
    import re

    lines = source_code.splitlines()
    processed_lines = []

    # Regex for 'times N, "..."' pattern
    pattern = re.compile(r'^\s*times\s+(\d+)\s*,\s*"([^"]*)"\s*$')

    for line in lines:
        # Strip comments after @
        code_part = line.split('@', 1)[0].strip()
        if not code_part:
            continue

        # Handle times expansion
        m = pattern.match(code_part)
        if m:
            count = int(m.group(1))
            seq = m.group(2)
            processed_lines.append(seq * count)
        else:
            processed_lines.append(code_part)

    return ''.join(processed_lines)

def run_bfpp_live(code, input_func=input):
    # Preprocess 'times' lines and comments first
    code = preprocess_bfpp(code)

    tape = [0] * 30000
    ptr = 0
    pc = 0
    clipboard = 0
    code = [c for c in code if c in "><+-.,[]^v#&()*/:;!"]
    bracket_map = {}
    paren_map = {}

    # Precompute bracket matching
    stack = []
    for i, c in enumerate(code):
        if c == '[':
            stack.append(i)
        elif c == ']':
            j = stack.pop()
            bracket_map[i] = j
            bracket_map[j] = i

    # Precompute paren matching
    stack = []
    for i, c in enumerate(code):
        if c == '(':
            stack.append(i)
        elif c == ')':
            j = stack.pop()
            paren_map[i] = j
            paren_map[j] = i

    while pc < len(code):
        cmd = code[pc]

        if cmd == '>':
            ptr += 1
        elif cmd == '<':
            ptr -= 1
        elif cmd == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == '.':
            print(chr(tape[ptr]), end='', flush=True)
        elif cmd == ',':
            try:
                tape[ptr] = ord(input_func()[0])
            except:
                tape[ptr] = 0
        elif cmd == ':':
            print(tape[ptr], end=' ', flush=True)
        elif cmd == ';':
            try:
                tape[ptr] = int(input_func())
            except:
                tape[ptr] = 0
        elif cmd == '[':
            if tape[ptr] == 0:
                pc = bracket_map[pc]
        elif cmd == ']':
            if tape[ptr] != 0:
                pc = bracket_map[pc]
        elif cmd == '^':
            clipboard = tape[ptr]
        elif cmd == 'v':
            tape[ptr] = clipboard
        elif cmd == '#':
            tape[ptr] = 0
        elif cmd == '&':
            break
        elif cmd == '(':
            if tape[ptr] != 0:
                pc = paren_map[pc]
        elif cmd == ')':
            pass
        elif cmd == '*':
            tape[ptr] = (tape[ptr] + clipboard) % 256
        elif cmd == '/':
            tape[ptr] = (tape[ptr] - clipboard) % 256
        elif cmd == '!':
            print()
            idx = 0
            for i in tape:
                if i == 0 and idx > ptr:
                    break
                if idx == ptr:
                    print(f'[{i}]', end=' ')
                else:
                    print(i, end=' ')
                idx += 1
        pc += 1
if __name__ == '__main__':
    code = '''
@ Put your code here
'''

    run_bfpp_live(code)
