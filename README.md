# Code Generator

## Description

**Code Generator** is an application that allows you to automatically generate code by describing the functionality you want in natural language. The user can request, for example, "Create a sort function," and the program will generate code for that task by making API calls to OpenAI’s service.

## How it works (Background)

1. The user enters a prompt/description into the application.
2. The program loads the OpenAI API key from the `.env` file.
3. An API call is made to the OpenAI service with the user's prompt.
4. The service returns generated code, which is displayed or saved for the user.

## Requirements

- Windows 10 or later.
- An OpenAI API Key (the user must obtain their own).

## Installer Information

The installer for this program is built using Python's **tkinter** library, providing a simple graphical installation wizard for end users.  
You do not need to have Python installed on your system to run the installer.

## Installation

1. **Download the Installer**  
   Download the installer in the releases section of this repository : https://github.com/MariosGramm/code-generator/releases
2. Double-click the `installer.exe` file and follow the steps in the installation wizard.
3. During installation, you will be prompted to enter your OpenAI API key.  
   - If you do not have an API key yet, you can create one at: [OpenAI API Keys](https://platform.openai.com/api-keys)
4. After installation, open the program from the Start Menu or your Desktop shortcut.

## Usage

- Launch **Code Generator**.
- Enter a description of the function you want the code for.
- The application will communicate with the OpenAI API and display or save the generated code for you.

## Support

For questions or problems, please contact the developer or open an issue in the project's GitHub repository (if available). 
You can view live demos for the installation and usage here : https://drive.google.com/drive/folders/1NK_YrLBPYSjsO22dRWKfIxMSDFMrZtoP?usp=drive_link
