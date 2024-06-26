class MemoryBus:
    def __init__(self, memory_size=1024):
        self.memory = [0] * memory_size
    
    def load_memory(self, data):
        """Loads initial memory values from a dictionary where keys are addresses and values are data."""
        for address, value in data.items():
            self.memory[address] = value
    
    def read(self, address):
        """Reads data from memory at the specified address."""
        return self.memory[address // 4]

    def write(self, address, data):
        """Writes data to memory at the specified address."""
        self.memory[address // 4] = data 