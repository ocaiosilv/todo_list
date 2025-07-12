# CLI To-Do List Application

This is a simple Command-Line To-Do List application developed in Python. I built it as part of my learning process while studying programming fundamentals and exploring how to structure small but functional projects from scratch.

The goal was to apply concepts like object-oriented design, clean code practices, and basic file persistence in a hands-on way. It’s a lightweight project, but it helped me understand how to manage state, user input, and data storage in a console-based environment.

---

## Features

- **Task Management**
  - Add new tasks
  - Update task status (`Pending`, `In Progress`, `Done`) — with logic to allow only one task “In Progress” at a time
  - Edit task descriptions
  - Delete tasks

- **List Persistence**
  - Save and load task lists as `.json` files
  - Start a new empty list when needed

---

## Technologies

- **Python 3** — Main language used  
- **InquirerPy** — Library used to create interactive and user-friendly CLI menus

---

## Getting Started

### Requirements

- Python 3.x installed on your system

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YourUsername/your-repo-name.git
   cd your-repo-name
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   ```

   - **On Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\activate
     ```

   - **On macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

---

## About the Project

This project was created as part of my practice while learning Python and working toward becoming a software developer. I wanted something that could run entirely in the terminal, be easy to use, and help reinforce topics like:

- Object-oriented programming
- JSON-based data persistence
- Structuring small CLI applications
---

## License

This project is licensed under the [MIT License](LICENSE).
