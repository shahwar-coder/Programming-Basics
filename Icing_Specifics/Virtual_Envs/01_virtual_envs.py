'''
Q1. What is a Python virtual environment and why do we use it?
Ans:
A virtual environment is an isolated Python setup for each project.
It keeps its own Python interpreter and libraries, preventing conflicts
between different projects and keeping the system Python clean.
'''
# Example
# Project A → Django 4.0
# Project B → Django 3.2
# Both work safely because each has its own venv.



'''
Q2. How do you create a new virtual environment?
Ans:
Use the venv module:
Windows → python -m venv myenv
Mac/Linux → python3 -m venv myenv
This creates a folder containing an isolated Python installation.
'''
# Example
# Terminal:
# python3 -m venv env_project



'''
Q3. How do you activate and deactivate a virtual environment?
Ans:
Activation:
- Windows CMD: myenv\Scripts\activate
- Windows PowerShell: .\myenv\Scripts\Activate.ps1
- Linux/Mac: source myenv/bin/activate
Deactivation:
- deactivate
'''
# Example
# (env) appears in terminal → proves venv is active



'''
Q4. How do you install packages inside a virtual environment?
Ans:
Once a venv is active, pip installs packages only into that environment.
Use: pip install <package> or pip install <pkg>==<version>.
'''
# Example
# pip install numpy
# pip install pandas==2.0.0



'''
Q5. How do you delete or remove a virtual environment?
Ans:
Just delete the venv folder. The environment is self-contained
and removing the directory fully removes the venv.
'''
# Example
# rm -rf myenv   (Linux/Mac)
# rmdir /s myenv (Windows)



'''
Q6. How can you check if a virtual environment is currently active?
Ans:
1. Terminal prompt shows: (myenv)
2. python -V shows venv’s Python version.
3. which python / where python shows path inside venv folder.
'''
# Example
# which python → /Users/.../myenv/bin/python



'''
Q7. What are recommended best practices when working with virtual environments?
Ans:
- Create one venv per project.
- Never commit venv folder to Git.
- Use requirements.txt for reproducibility.
- Recreate environments using pip install -r requirements.txt.
'''
# Example
# pip freeze > requirements.txt
# pip install -r requirements.txt



'''
Q8. Why is a virtual environment essential for large or multi-version projects?
Ans:
Different projects may need different package versions.
A venv ensures each project has its own isolated dependency set,
preventing version clashes and breaking other projects.
'''
# Example
# One project: Flask 2.3
# Another: Flask 1.1 (old)
# Both run safely in their own venv.



'''
Q9. What is a typical workflow using virtual environments?
Ans:
1. Create venv
2. Activate
3. Install packages
4. Run Python programs
5. Deactivate
This keeps each project clean and organized.
'''
# Example
# python3 -m venv venv
# source venv/bin/activate
# pip install requests
# python app.py
# deactivate
