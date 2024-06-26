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
        self.pc += 4
        print(f"Fetched instruction: {instruction:032b} from address {self.pc - 4}")
        return instruction
    
    def decode_execute(self, instruction):
        """Decodes and executes the fetched instruction by identifying its opcode and performing the corresponding operation."""
        opcode = (instruction >> 26) & 0x3F
        print(f"Decoding instruction with opcode: {opcode:06b}")
        if opcode == 0:  # R-type instructions
            funct = instruction & 0x3F
            rs = (instruction >> 21) & 0x1F
            rt = (instruction >> 16) & 0x1F
            rd = (instruction >> 11) & 0x1F
            print(f"R-type instruction with funct: {funct:06b}, rs: {rs}, rt: {rt}, rd: {rd}")
            if funct == 0x20:  # ADD
                self.registers[rd] = self.registers[rs] + self.registers[rt]
            elif funct == 0x22:  # SUB
                self.registers[rd] = self.registers[rs] - self.registers[rt]
            elif funct == 0x2A:  # SLT
                self.registers[rd] = 1 if self.registers[rs] < self.registers[rt] else 0
        elif opcode == 0x08:  # ADDI
            rs = (instruction >> 21) & 0x1F
            rt = (instruction >> 16) & 0x1F
            immediate = instruction & 0xFFFF
            print(f"ADDI instruction with rs: {rs}, rt: {rt}, immediate: {immediate}")
            self.registers[rt] = self.registers[rs] + immediate
        elif opcode == 0x04:  # BNE
            rs = (instruction >> 21) & 0x1F
            rt = (instruction >> 16) & 0x1F
            offset = instruction & 0xFFFF
            print(f"BNE instruction with rs: {rs}, rt: {rt}, offset: {offset}")
            if self.registers[rs] != self.registers[rt]:
                self.pc += offset * 4
        elif opcode == 0x02:  # J
            target = instruction & 0x3FFFFFF
            print(f"J instruction with target: {target}")
            self.pc = (target << 2) & 0xFFFFFFFF
        elif opcode == 0x03:  # JAL
            target = instruction & 0x3FFFFFF
            print(f"JAL instruction with target: {target}")
            self.registers[31] = self.pc
            self.pc = (target << 2) & 0xFFFFFFFF
        elif opcode == 0x23:  # LW
            rs = (instruction >> 21) & 0x1F
            rt = (instruction >> 16) & 0x1F
            offset = instruction & 0xFFFF
            address = self.registers[rs] + offset
            print(f"LW instruction with rs: {rs}, rt: {rt}, address: {address}")
            self.registers[rt] = self.memory_bus.read(address)
        elif opcode == 0x2B:  # SW
            rs = (instruction >> 21) & 0x1F
            rt = (instruction >> 16) & 0x1F
            offset = instruction & 0xFFFF
            address = self.registers[rs] + offset
            print(f"SW instruction with rs: {rs}, rt: {rt}, address: {address}")
            self.memory_bus.write(address, self.registers[rt])
        elif opcode == 0x3F:  # HALT
            print("HALT instruction encountered. Stopping execution.")
            self.running = False

    def run(self):
        """Runs the fetch-decode-execute cycle in a loop until a HALT instruction is encountered."""
        while self.running:
            instruction = self.fetch()
            self.decode_execute(instruction)
    
    def enable_cache(self, code):
        """Enables, disables, or flushes the cache based on the provided code."""
        self.cache.set_cache_state(code)