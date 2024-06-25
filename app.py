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
    pass

def main():
    """Initializes the CPU, cache, and memory bus. 
    Loads initial memory values and program instructions from specified files, loads them into memory, and runs the CPU.
    Finally, prints the state of registers and a portion of memory after execution."""
    pass

if __name__ == "__main__":
    main()