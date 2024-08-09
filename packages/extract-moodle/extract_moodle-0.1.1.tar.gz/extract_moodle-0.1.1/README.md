# Extract Moodle

A tool to extract Moodle files and organize them based on question numbers. This utility helps in managing and categorizing files from Moodle zip archives by filtering them according to specified conditions. [eventually help in plag checking]

## Features

- Extracts `.zip` files from the current directory.
- Organizes files into folders based on their naming conventions.
- Supports `.cpp` and `.c`  and `.py` file extensions.

## File Handling

The tool processes files that meet the following criteria:
- **File Extensions**: It can handle files with extensions `.cpp` and `.c` and `.py` .
- **File Naming Conventions**: It filters files based on the presence of the following patterns in their names:
  - `q{number}` (e.g., `q1`, `q2`)
  - `Q{number}` (e.g., `Q1`, `Q2`)
  - `_{number}` (e.g., `_1`, `_2`)

### Required Characteristics

Files must adhere to the following characteristics to be processed correctly:
- **Naming Format**: The file name should contain a question number that corresponds to the structure `q{number}`, `Q{number}`, or `_{number}`.
- **File Types**: Only files with `.cpp` and `.c` and `.py` extensions will be considered for categorization.

## Usage

To run the tool, use the following command in your terminal:

```bash
extract_moodle --noofqs=<number_of_questions>
```

Example:

```bash
extract_moodle --noofqs=4
```

## Notes
- Ensure you are in the directory containing the folders you want to process when you run the command.
- The tool will create folders named q1, q2, ..., qN (where N is the number of questions specified) in the current directory to store the organized files.
- Any existing files or folders with the same names will be retained.