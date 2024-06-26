class Cache:
    def __init__(self):
        self.enabled = False
        self.cache_memory = {}
    
    def set_cache_state(self, code):
        """Sets the state of the cache: 0 for disabled, 1 for enabled, and 2 for flushing the cache."""
        if code == 0:
            self.enabled = False
            self.cache_memory.clear()
        elif code == 1:
            self.enabled = True
        elif code == 2:
            self.cache_memory.clear()
    
    def read(self, address, memory_bus):
        """Reads data from the cache if enabled and present; otherwise, reads from the memory bus and stores it in the cache if enabled."""
        if self.enable and address in self.cache_memory:
            return self.cache_memory[address]
        data = memory_bus.read(address)
        if self.enabled:
            self.cache_memory[address] = data
        return data
    
    def write(self, address, data, memory_bus):
        """Writes data to the cache if enabled and also writes to the memory bus."""
        if self.enabled:
            self.cache_memory[address] = data
        memory_bus.write(address, data)