import vscode

def show_info(message: str):
    # Show an info message in the editor or status bar
    vscode.window.showInformationMessage(message)

def show_warning(message: str):
    # Show a warning message in the editor or status bar
    vscode.window.showWarningMessage(message)

def show_error(message: str):
    # Show an error message in the editor or status bar
    vscode.window.showErrorMessage(message)

def show_log(message: str):
    # Show a log message in the Output panel
    vscode.window.showLogMessage(message)
