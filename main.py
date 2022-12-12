import vscode
import chatgpt
import code_model
import ui
import commands
import messages

def main():
    # Create a ChatGPT instance and load the trained model
    chatbot = chatgpt.ChatGPT()
    chatbot.load_model("model.h5")
    
    # Create a CodeModel instance and load the trained model
    codemodel = code_model.CodeModel()
    codemodel.load_model("codemodel.h5")
    
    # Show the user interface and command palette
    ui.show()
    
    # Listen for user input and generate responses or code suggestions
    while True:
        user_input = ui.get_input()
        if user_input == "":
            continue
        elif user_input == "exit":
            break
        elif user_input.startswith("code "):
            # Generate code suggestions
            code_input = user_input[5:]
            code_output = codemodel.generate_code(code_input)
            ui.show_code(code_output)
        elif user_input.startswith("insert "):
            # Insert generated code into the editor
            code_input = user_input[7:]
            code_output = codemodel.generate_code(code_input)
            vscode.window.activeTextEditor.insertCode(code_output)
        else:
            # Generate chatbot responses
            chatbot_output = chatbot.generate_response(user_input)
            ui.show_response(chatbot_output)
    
    # Clean up and exit
    ui.hide()

if __name__ == "__main__":
    main()
