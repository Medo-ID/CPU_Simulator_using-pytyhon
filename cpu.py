"""MIPS Instructions:
Instruction         Operand         Meaning
ADD	                Rd, Rs, Rt	    Rd <- Rs + Rt;
ADDI	            Rt, Rs, immd	Rt <- Rs + immd
SUB	                Rd, Rs, Rt	    Rd <- Rs - Rt
SLT	                Rd, Rs, Rt	    If (Rs < Rt) then Rd <- 1 else Rd <- 0
BNE	                Rs, Rt, offset	If (Rs not equal Rt) then PC <- (PC + 4) + offset * 4
J	                target	        PC <- target * 4
JAL	                target	        R7 <- PC + 4; PC <- target *4
LW	                Rt, offset(Rs)	Rt <- MEM[Rs + offset]
SW	                Rt, offset(Rs)	MEM[Rs + offset] <- Rt
CACHE	            Code	        Code = 0(Cache off) Code = 1(Cache on), Code = 2(Flush cache)
HALT	            ;	            Terminate Execution
"""

class CPU:
    def __init__(self, memory_bus, cache):
        self.registers = [0] * 32 # 32 general-purpose registers
        self.pc = 0 # Program counter
        self.memory_bus = memory_bus
        self.cache = cache
        self.running = True
    
    def fetch(self):
        """Fetches the next instruction from memory using the program counter and increments the program counter."""
        instruction = self.memory_bus.read(self.pc)
        print(f"Fetched instruction: {instruction:032b} from address {self.pc}")
        self.pc += 4
        return instruction
    
    def decode_execute(self, instruction):
        """Decodes and executes the fetched instruction by identifying its opcode and performing the corresponding operation."""
        opcode = instruction >> 4  # First 4 bits
        operand = instruction & 0x0F  # Last 4 bits

        if opcode == 0x1:  # LOAD
            self.registers[0] = self.memory[operand]
        elif opcode == 0x2:  # STORE
            self.memory[operand] = self.registers[0]
        elif opcode == 0x3:  # ADD
            self.registers[0] += self.memory[operand]
        elif opcode == 0x4:  # SUB
            self.registers[0] -= self.memory[operand]
        elif opcode == 0x5:  # JMP
            self.pc = operand
        elif opcode == 0x6:  # JZ (Jump if zero)
            if self.registers[0] == 0:
                self.pc = operand
        elif opcode == 0xF:  # HALT
            self.running = False
        
        # Debug the program counter after instruction execution
        print(f"Program counter after execution: {self.pc}")
        
        # Ensure program counter is within valid memory range
        if not (0 <= self.pc < len(self.memory_bus.memory) * 4):
            print(f"Error: Program counter out of valid memory range: {self.pc}")
            self.running = False

    def run(self):
        """Runs the fetch-decode-execute cycle in a loop until a HALT instruction is encountered or an invalid state is reached."""
        while self.running:
            instruction = self.fetch()
            self.decode_execute(instruction)
    
    def enable_cache(self, code):
        """Enables, disables, or flushes the cache based on the provided code."""
        self.cache.set_cache_state(code)