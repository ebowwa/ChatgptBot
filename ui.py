import vscode

def show_language_selection_menu():
    # Show a menu to allow the user to select the programming language
    languages = ["Python", "JavaScript", "C++", "Java", "C#"]
    language = vscode.window.showQuickPick(languages)
    return language

def show_style_selection_menu():
    # Show a menu to allow the user to select the code style
    styles = ["PEP 8", "JavaScript Standard Style", "Google C++ Style Guide", "Oracle Java Code Conventions", "Microsoft C# Coding Conventions"]
    style = vscode.window.showQuickPick(styles)
    return style

def show_formatting_options():
    # Show a dialog to allow the user to configure formatting options
    options = {
        "indentation": 4,
        "use_spaces": True,
        "wrap_lines": True,
        "max_line_length": 120,
        "add_newline_at_end": True,
    }
    changed_options = vscode.window.showQuickPick(options)
    return changed_options
