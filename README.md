# 🔢 Binary Transmission Error Detection Tool — Proyecto CE-3201

## 🧠 Overview

This repository contains the solution for a project focused on binary data encoding, conversion, and error detection, developed for a course at the Escuela de Electrónica, Tecnológico de Costa Rica.

The tool allows users to input a 4-digit octal number and performs a variety of conversions and encoding processes, including Hamming Code generation and NRZI signal visualization.

---

## 💡 Features

- 🧮 **Base Conversion**: Converts the input octal number into decimal, hexadecimal, and binary formats.
- ⚙️ **Parity Control**: User selects even or odd parity for Hamming encoding.
- 🛠️ **Hamming Code Generator**:
  - Applies parity bits to 12-bit data
  - Displays final encoded binary sequence
- 📈 **NRZI Bipolar Signal Plot**:
  - Simulates digital transmission signal assuming high level before t=0
- 🧪 **Error Simulation & Detection**:
  - Allows user to flip one bit in the encoded sequence
  - Detects and identifies the position of the faulty bit using Hamming logic
- 🗂️ **Tabular Output**: Presents results in pre-defined tables, as per course requirements.

---

## 👨‍💻 Technologies

- Language: **C++** (or optionally Python/C# depending on team choice)
- Output: Command-line interface with structured outputs
- Focus: Binary systems, digital encoding, and user-friendly interaction

