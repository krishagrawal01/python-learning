# ==========================================================
#               PYTHON + VENV + PIP + GIT CHEATSHEET
# ==========================================================

# =========================
# DIRECTORY COMMANDS
# =========================

# Show current directory
# PowerShell:
# pwd

# CMD:
# cd

# Go into a folder
# cd FolderName

# Example:
# cd Projects

# Go back one folder
# cd ..


# =========================
# VIRTUAL ENVIRONMENT
# =========================

# Create a virtual environment (Run ONLY ONCE per project)
# python -m venv .venv

# OR
# python -m venv venv

# Activate virtual environment (PowerShell)
# .venv\Scripts\activate
# OR
# .venv\Scripts\Activate.ps1

# Activate virtual environment (CMD)
# .venv\Scripts\activate

# Deactivate virtual environment
# deactivate


# =========================
# PIP COMMANDS
# =========================

# Install a package
# pip install pandas

# Install multiple packages
# pip install pandas streamlit pypdf

# Upgrade a package
# pip install --upgrade pandas

# Uninstall a package
# pip uninstall pandas

# Show all installed packages
# pip list

# Show information about a package
# pip show pandas

# Show installed packages with exact versions
# pip freeze

# Save installed packages to requirements.txt
# (Overwrites existing requirements.txt)
# pip freeze > requirements.txt

# Install packages from requirements.txt
# pip install -r requirements.txt


# =========================
# PYTHON COMMANDS
# =========================

# Show Python version
# python --version

# Show current Python executable
# python -c "import sys; print(sys.executable)"

# Show all Python executables
# PowerShell:
# where.exe python

# CMD:
# where python


# =========================
# GIT COMMANDS
# =========================

# Initialize Git repository
# git init

# Check repository status
# git status

# Add all files
# git add .

# Commit changes
# git commit -m "Your commit message"

# Push changes
# git push

# Pull latest changes
# git pull

# Clone repository
# git clone <repository-url>


# =========================
# NEW PROJECT WORKFLOW
# =========================

# cd MyProject
# python -m venv .venv
# .venv\Scripts\activate
# pip install streamlit pypdf pandas
# pip freeze > requirements.txt
# git init
# git add .
# git commit -m "Initial Commit"
# git push


# =========================
# OPENING PROJECT NEXT DAY
# =========================

# cd MyProject
# .venv\Scripts\activate

# If you cloned someone else's project:
# pip install -r requirements.txt


# =========================
# MOST IMPORTANT COMMANDS
# =========================

# python -m venv .venv
# .venv\Scripts\activate
# deactivate

# pip install <package-name>
# pip list
# pip show <package-name>
# pip freeze
# pip freeze > requirements.txt
# pip install -r requirements.txt

# python --version
# python -c "import sys; print(sys.executable)"
# where.exe python

# git status
# git add .
# git commit -m "message"
# git push
# git pull


# =========================
# NOTES
# =========================

# requirements.txt stores all project dependencies
# Use:
# pip freeze > requirements.txt

# To recreate the same environment:
# pip install -r requirements.txt