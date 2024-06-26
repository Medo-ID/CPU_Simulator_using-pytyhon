# CPU Simulator

This project is a simulation of a CPU that mimics the functionalities of a CPU, cache, and memory bus. It can fetch and parse instructions, initialize memory values, and execute a series of MIPS instructions.

## Features

- **Instruction Set Architecture (ISA)**: Supports MIPS instructions such as ADD, ADDI, SUB, SLT, BNE, J, JAL, LW, SW, CACHE, and HALT.
- **Memory and Cache Simulation**: Simulates memory operations and a simple cache mechanism.
- **Fetch-Decode-Execute Cycle**: Implements the fundamental cycle of fetching, decoding, and executing instructions.

## MIPS Instructions

| Instruction | Operand        | Meaning                                                        |
| ----------- | -------------- | -------------------------------------------------------------- |
| ADD         | Rd, Rs, Rt     | Rd <- Rs + Rt                                                  |
| ADDI        | Rt, Rs, immd   | Rt <- Rs + immd                                                |
| SUB         | Rd, Rs, Rt     | Rd <- Rs - Rt                                                  |
| SLT         | Rd, Rs, Rt     | If (Rs < Rt) then Rd <- 1 else Rd <- 0                         |
| BNE         | Rs, Rt, offset | If (Rs not equal Rt) then PC <- (PC + 4) + offset \* 4         |
| J           | target         | PC <- target \* 4                                              |
| JAL         | target         | R7 <- PC + 4; PC <- target \* 4                                |
| LW          | Rt, offset(Rs) | Rt <- MEM[Rs + offset]                                         |
| SW          | Rt, offset(Rs) | MEM[Rs + offset] <- Rt                                         |
| CACHE       | Code           | Code = 0(Cache off), Code = 1(Cache on), Code = 2(Flush cache) |
| HALT        | ;              | Terminate Execution                                            |

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

```sh
git clone https://github.com/Medo-ID/CPU_Simulator_using-pytyhon.git
cd CPU_Simulator_using-pytyhon
```

2. Run the simulation:

```sh
python app.py
```

### File Descriptions

- `app.py`: Main application file that initializes the CPU, cache, and memory bus, loads memory values and instructions, and runs the CPU.
- `cpu.py`: Contains the CPU class that performs the fetch-decode-execute cycle.
- `cache.py`: Contains the Cache class that simulates a simple cache mechanism.
- `memory_bus.py`: Contains the MemoryBus class that simulates memory operations.
- `data_input.txt`: Input file containing initial memory values.
- `instruction_input.txt`: Input file containing program instructions.

### Usage

1. Prepare `data_input.txt` with initial memory values in the format:

```py
00000001,4
00000010,5
...
```

2. Prepare `instruction_input.txt` with program instructions in the format:

```py
CACHE,1
ADDI,R2,R2,2
...
```

3. Run `app.py` to start the simulation. The program will print the state of the registers and a portion of the memory after execution.

### Example

- Contents of `data_input.txt`:

```sh
00000001,4
00000010,5
00000011,6
00000100,7
00000101,2
00000110,3
00000111,9
```

- Contents of `instruction_input.txt`:

```sh
CACHE,1
ADDI,R2,R2,2
ADD,R3,R2,R1
J,8
HALT,;
```

- Output:

```sh
Phase 1
Phase 2
Phase 3
Phase 4
Fetched instruction: 00000000000000000000000000000000 from address 0
Decoding instruction with opcode: 000000
R-type instruction with funct: 000000, rs: 0, rt: 0, rd: 0
Fetched instruction: 00000000000000000000000000000100 from address 4
Decoding instruction with opcode: 000000
R-type instruction with funct: 000100, rs: 0, rt: 0, rd: 0
Fetched instruction: 00000000000000000000000000000101 from address 8
Decoding instruction with opcode: 000000
R-type instruction with funct: 000101, rs: 0, rt: 0, rd: 0
Fetched instruction: 00000000000000000000000000000110 from address 12
Decoding instruction with opcode: 000000
R-type instruction with funct: 000110, rs: 0, rt: 0, rd: 0
Fetched instruction: 00000000000000000000000000000111 from address 16
Decoding instruction with opcode: 000000
R-type instruction with funct: 000111, rs: 0, rt: 0, rd: 0
Fetched instruction: 00000000000000000000000000000010 from address 20
Decoding instruction with opcode: 000000
R-type instruction with funct: 000010, rs: 0, rt: 0, rd: 0
Fetched instruction: 00000000000000000000000000000011 from address 24
Decoding instruction with opcode: 000000
R-type instruction with funct: 000011, rs: 0, rt: 0, rd: 0
Fetched instruction: 11101000000000000000000000000001 from address 28
Decoding instruction with opcode: 111010
Unknown instruction with opcode: 111010
Fetched instruction: 00100000010000100000000000000010 from address 32
Decoding instruction with opcode: 001000
ADDI instruction with rs: 2, rt: 2, immediate: 2
Fetched instruction: 00000000010000110000100000100000 from address 36
Decoding instruction with opcode: 000000
R-type instruction with funct: 100000, rs: 2, rt: 3, rd: 1
Fetched instruction: 00001000000000000000000000001000 from address 40
Decoding instruction with opcode: 000010
Unknown instruction with opcode: 000010
Fetched instruction: 11111100000000000000000000000000 from address 44
Decoding instruction with opcode: 111111
HALT instruction encountered. Stopping execution.
Phase 5
Registers:  [0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Memory:  [0, 4, 5, 6, 7, 2, 3, 3892314113, 541196290, 4392992, 134217736, 4227858432, 0, 0, 0, 0]
```
