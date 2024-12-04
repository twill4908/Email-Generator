mport os
 
def get_user_input():
    # Get the role information from the user
    industry = input("Enter your industry (e.g., IT, Finance, Healthcare): ").strip()
    role_id = input("Enter the role ID (e.g., 101, 102, 103): ").strip()
    role_name = input("Enter the role name (e.g., Data Engineer, Tester, Business Analyst): ").strip()
 
    return industry, role_id, role_name
 
#Defining a function - load_template that is responsible for loading the content of the template text file corresponding to the selected role.
def load_template(role_name):
    # Map role names to their respective text files
    role_templates = {
        "Data Migration": "data_migration_template.txt",
        "Tester": "tester_template.txt",
        "Data Engineer": "data_engineer_template.txt",
        "Business Analyst": "business_analyst_template.txt"
    }
 
    # Check if the role exists in the predefined templates
    if role_name in role_templates:
        file_path = role_templates[role_name]
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Template file for {role_name} not found.")
            return None
    else:
        print(f"Role template for {role_name} is not available.")
        return None
 
def customize_template(template, industry, role_id, role_name):
    # Modify the template by replacing keywords with user inputs
    template = template.replace("[Industry]", industry)
    template = template.replace("[RoleID]", role_id)
    template = template.replace("[RoleName]", role_name)
   
    # Update the "What excites you?" paragraph
    excitement_paragraph = "I'm excited to make an impact on the [Industry] industry by getting hands-on experience as a [RoleName] and taking my testing and validation experience to the next level. I am eager to contribute to the overall growth and success of the project while growing as a Subject Matter Expert (SME)."
   
    template = template.replace("I'm excited to make an impact on xyz industry", excitement_paragraph.replace("[Industry]", industry).replace("[RoleName]", role_name))
 
    return template
 
def save_and_open_output(modified_text, role_name):
    # Define output file name
    output_file = f"{role_name}_Application.txt"
 
    # Save the modified text to a new text file
    with open(output_file, 'w') as file:
        file.write(modified_text)
 
    # Open the output file in the default text editor
    try:
        if os.name == 'nt':  # For Windows
            os.system(f"notepad {output_file}")
        elif os.name == 'posix':  # For macOS/Linux
            os.system(f"open -a TextEdit {output_file}")
    except Exception as e:
        print(f"Could not open text editor: {e}")
 
def main():
    print("Welcome to the Role Application Generator!")
   
    # Get user input
    industry, role_id, role_name = get_user_input()
   
    # Load the corresponding role template
    template = load_template(role_name)
   
    if template:
        # Customize the template based on the user's inputs
        modified_text = customize_template(template, industry, role_id, role_name)
       
        # Save the modified text to a file and open it
        save_and_open_output(modified_text, role_name)
       
        print(f"Your customized application for the {role_name} role has been saved and opened.")
    else:
        print("Error: Could not process the template.")
 
if __name__ == "__main__":
    main()
 