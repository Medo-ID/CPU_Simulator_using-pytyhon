from cpu import CPU
from cache import Cache
from memory_bus import MemoryBus

def load_memory_from_file(filename):
    """Reads memory initialization values from a file where each line contains an address and value separated by a comma.
    Returns a dictionary with addresses as keys and values as data."""
    memory = {}
    with open(filename, 'r') as file:
        for line in file:
            address, value = line.strip().split(',')
            memory[int(address, 2)] = int(value)
    return memory

def load_instructions_from_file(filename):
    """Reads instructions from a file, maps them to their binary opcode equivalents, and returns a list of binary instructions.
    Handles MIPS-like instructions with operands separated by commas."""
    instruction_map = {
        'ADD': 0x20,
        'ADDI': 0x08,
        'SUB': 0x22,
        'SLT': 0x2A,
        'BNE': 0x05,
        'J': 0x02,
        'JAL': 0x03,
        'LW': 0x23,
        'SW': 0x2B,
        'CACHE': 0x3A,
        'HALT': 0x3F
    }
    instructions = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            op = parts[0]
            if op in instruction_map:
                if op == 'HALT':
                    instructions.append((instruction_map[op] << 26))
                elif op == 'CACHE':
                    code =int(parts[1])
                    instructions.append((instruction_map[op] << 26) | (code & 0x1F))
                elif op == 'J' or op == 'JAL':
                    target = int(parts[1])
                    instructions.append((instruction_map[op] << 26) | (target & 0x3FFFFFF))
                else:
                    rs = int(parts[2][1:]) & 0x1F
                    rt = int(parts[1][1:]) & 0x1F
                    if op == 'ADDI':
                        imm = int(parts[3])
                        instructions.append((instruction_map[op] << 26) | (rs << 21) | (rt << 16) | (imm & 0xFFFF))
                    else:
                        rd = int(parts[3][1:]) & 0x1F
                        instructions.append((rs << 21) | (rt << 16) | (rd << 11) | instruction_map[op])
    return instructions

def main():
    """Initializes the CPU, cache, and memory bus. 
    Loads initial memory values and program instructions from specified files, loads them into memory, and runs the CPU.
    Finally, prints the state of registers and a portion of memory after execution."""
    print("Phase 1")
    # Initialize components
    memory_bus = MemoryBus()
    cache = Cache()
    cpu = CPU(memory_bus, cache)
    print("Phase 2")
    # Load initial memory and program
    initial_memory = load_memory_from_file('data_input.txt')
    program = load_instructions_from_file('instruction_input.txt')
    print("Phase 3")
    memory_bus.load_memory(initial_memory)
    # Uses dictionary comprehension to create a dictionary of memory addresses and program instructions.
    memory_bus.load_memory({i + len(initial_memory): program[i] for i in range(len(program))})
    print("Phase 4")
    # Run the cpu
    cpu.run()
    print("Phase 5")
    # Output the final state
    print("Registers: ", cpu.registers)
    print("Memory: ", memory_bus.memory[:16])

# if __name__ == "__main__":
#     main()

main()