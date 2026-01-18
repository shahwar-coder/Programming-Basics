'''
- The file must be opened using `with open(...)` to keep it alive
- All file operations must happen **inside** the `with` block
- Code outside `with` cannot read the file (it’s auto-closed)
- `with` ensures proper resource management (no leaks)
- File is closed immediately after exiting the `with` scope
- Readers like `csv.DictReader` depend on an open file handle
- Incorrect indentation breaks file-dependent logic
'''
