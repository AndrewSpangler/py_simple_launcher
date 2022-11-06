from py_simple_readme import readme_generator

about = "Super simple dynamic, multi-profile launcher system written in python."
install_message = "Available on pip - `pip install py_simple_launcher`"
instructions = [
    "1. Windows only due to \\*nix systems being inconsistent.\n"
    '1. Install [Python 3.10+](https://www.python.org/downloads/) and make sure to include `IDLE, pip, tcl/tk, and check "Add python 3.* to PATH"`',
    "1. Reboot your computer",
    "1. Open a command prompt",
    "1. Type the following command to install with pip: `pip install py_simple_launcher`",
    "1. Create a folder where you want the application to run",
    '1. Create a text file in the (In Explorer: "right-click->new->Text Document")',
    '1. Rename that file to "py_simple_launcher.bat" (Without quotes)',
    "1. Edit the batch file in notepad (or other plaintext editor) to contain the following text : `start pythonw.exe -m py_simple_launcher`",
    "1. Double-Click the bat file to launch the program",
    "1. You can make another folder + bat file to create a new instance of the program (Eg for a separate set tasks like work vs home etc.)",
]
image = "![py_simple_launcher](https://raw.githubusercontent.com/AndrewSpangler/py_simple_launcher/main/example.png)"


def generate_readme(tables, changelog: dict):
    name = tables["project"]["name"]
    version = tables["project"]["version"]
    description = tables["project"]["description"]

    gen = readme_generator(title=f"{name} {version}", slogan=description)
    gen.set_changelog(changelog)
    gen.add_paragraph(image)
    gen.add_heading_2("About")
    gen.add_paragraph(about)
    gen.add_heading_2("Installation")
    gen.add_paragraph(install_message)
    gen.add_unordered_list(instructions)
    return gen.assemble()
