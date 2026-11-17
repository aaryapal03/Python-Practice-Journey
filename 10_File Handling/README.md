
# Python File Handling
This folder contains my practice programs on Python file handling. Through these examples, I am learning how to read, write, and append files, use different file modes, manage files with the with statement, work with file positions, and handle binary files and pickled objects.

# Topics and Files

| Topic | File | What It Covers |

| Reading Files | read_file.py | Reading text files using read(), readline(), readlines(), and iteration |
| Writing Files | write_file.py | Creating or overwriting text files using write() and writelines() |
| Appending Files | append_file.py | Adding content to the end of a file without removing existing content |
| File Modes | file_modes.py | Exploring modes such as r, w, a, x, b, t, and + and their valid combinations |
| With Statement | with_statement.py | Managing files using with so they are closed automatically when the block exits |
| Seek and Tell | seek_and_tell.py | Using tell() to get the current file position and seek() to change it |
| Binary Files | binary_file.py | Reading and writing bytes using binary file modes |
| Pickle Module | pickle_module.py | Saving and loading Python objects using pickle.dump() and pickle.load() |
| Practice Questions | practice_questions.py | Applying file-handling concepts to solve additional problems |

# Learning Goals

- Open files using appropriate file modes.
- Read text files using different reading methods.
- Create files and write content to them.
- Append content without removing existing data.
- Understand which file modes require an existing file or overwrite content.
- Use the with statement to manage files.
- Inspect and change file positions using tell() and seek().
- Understand the difference between text and binary files.
- Read and write binary data.
- Save and load Python objects using the pickle module.
- Apply file-handling concepts to solve practice questions.

# Important Notes

- Check the filenames and paths used in each program before running it.
- Files opened in r mode must already exist.
- Opening a file in w or wb mode overwrites its existing content.
- Opening a file in a mode appends content and creates the file if needed.
- Opening a file in x mode creates a new file and fails if it already exists.
- Use disposable sample files when practicing operations that modify data.
- Use an explicit encoding, such as UTF-8, when working with text files.
- Binary file operations work with bytes rather than text strings.
- Text-mode seek() has restrictions; do not assume its positions are character indexes.
- Only load pickle files from trusted sources.
- Some programs create or modify files when executed.

#Practice Progress

- Reading files
- Writing files
- Appending files
- File modes
- With statement
- Seek and tell
- Binary files
- Pickle module
- Practice questions
  

# My Learning Notes
I will update this section with concepts I learn, mistakes I encounter, and how I correct them.
