'''
Q1. What is pip in Python?
Ans:
pip is Python’s package manager. It lets you install, upgrade,
and remove external libraries from the Python Package Index (PyPI).
'''
# Example
# pip --version



'''
Q2. How do you install and uninstall packages using pip?
Ans:
Use pip install <package> to add a package and pip uninstall <package>
to remove it from the current environment.
'''
# Example
# pip install numpy
# pip uninstall numpy



'''
Q3. How do you check which packages are currently installed?
Ans:
Use pip list to view all installed packages along with their versions.
'''
# Example
# pip list



'''
Q4. How do you install a specific version of a package?
Ans:
Use pkg==version inside pip install, which ensures reproducibility
and avoids compatibility issues.
'''
# Example
# pip install pandas==2.0.0



'''
Q5. How do you install packages from requirements.txt?
Ans:
Use pip install -r requirements.txt to install all packages listed
in the file. Ideal for projects and deployment.
'''
# Example
# pip install -r requirements.txt



'''
Q6. Why should you use virtual environments with pip?
Ans:
Virtual environments isolate dependencies so that each project
can have its own package versions without conflicts.
'''
# Example
# python -m venv env
# source env/bin/activate
# pip install flask



'''
Q7. Why should you update pip regularly?
Ans:
Updating pip ensures you have the latest bug fixes, security patches,
and improved dependency resolution.
'''
# Example
# python -m pip install --upgrade pip



'''
Q8. Can pip install packages from sources other than PyPI?
Ans:
Yes. pip can install from URLs, local wheels, GitHub repos, and folders.
'''
# Example
# pip install https://example.com/package.whl
# pip install git+https://github.com/user/repo.git



'''Q9
What is the difference between:
1) pip install package
2) python -m pip install package

Answer:
• pip install pkg
  → Runs the pip **command from the system PATH**.
  → May point to ANY Python installation on your machine.
  → Risk: On systems with multiple Python versions (3.8, 3.10, venvs), 
    you may install packages into the wrong Python.

• python -m pip install pkg
  → Runs pip **as a module of the exact Python interpreter** you specified.
  → Guarantees packages install into that Python version or virtual environment.
  → Safer and recommended, especially with venvs.

Why python -m pip is better?
• Avoids "Why is my package not found?" errors.
• Ensures correct interpreter is used.
• Works consistently across OSes.
• Eliminates confusion when multiple Pythons exist.
'''

Examples:

# Example 1: System has Python 3.8 and Python 3.10
# pip install numpy
# This might install into Python 3.8 accidentally.

# python3.10 -m pip install numpy
# This installs numpy into Python 3.10 for sure.

# Example 2: Inside a virtual environment
# (venv) pip install flask
# Usually works, but sometimes pip may point outside venv (rare but possible on Windows).

# (venv) python -m pip install flask
# 100% guaranteed to install into venv’s Python.

# Example 3: Using a specific interpreter
# python3.11 -m pip install pandas
# Installs pandas for Python 3.11

# Example 4: Checking pip version tied to interpreter
# python -m pip --version
# Shows which Python installation pip belongs to.



'''
Q10. What happens if you use pip without activating a virtual environment?
Ans:
Packages install into your system/global Python, which may cause
version conflicts or break other projects.
Always prefer working inside a venv.
'''
# Example
# (base) pip install flask   # installs globally (not ideal)
# (myenv) pip install flask  # installs inside venv (correct)
