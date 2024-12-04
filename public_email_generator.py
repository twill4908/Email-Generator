# Define the email template with placeholders
email_template = """
 
Subject Line: {role_id} - {role_name}
 
Hey {poc_name},
\n
My name is {your_name} and I'm an {management_lvl} aligned to the {alignment} practice, {experience}, primarily in the {your_industry} industry. I have a strong background in tasks {tasks}. leveraging {skills} skills.
\n
I’m also keen to learning more about the {company_name} so I can make an impact in the {role_industry} industry. I recently applied for the open role of {role_name} and believe I could be a great fit for your team
\n
Here is my one-pager. Please let me know if I can grab time with you to discuss this role further.
\n
Kind regards,
{your_name}
 
"""
 
# Function to prompt the user for inputs and generate the email
def generate_email_from_user_input():
    # Collect user inputs for the email --- Results from user response will be the true replacement
    poc_name = input("Enter the Point of Contact (POC) name for the role you are applying for: ")
    management_level = input("Enter you management level in your current position: ")
    company_name = input("Enter the company name (client name) that you are applying for: ")
    role_id = input("Enter the ID of role that you are applying for: ")  # This could be used for any specific logic, but for now it's just captured
    role_name = input("Enter the name of the role you are applying for: ")
    role_industry = input("Enter the industry you are applying to: ")
    experience = input("Enter some relevant work experience for example (I have experience in data quality and management): ")
    your_industry = input("Enter the industry of of past or current projects that align to this role: ")
    tasks = input("Enter the tasks you've done that aligns to this role: ")
    alignment = input("Enter the practice that you are aligned to: ")
    skills = input("Please enter describe some skills you'd like to highlight associated with this role: ")
    your_name = input("Enter your name: ")
 
    # Create a dictionary of the user inputs for replacement
    replacements = {
        "{poc_name}": poc_name,
        "{management_lvl}": management_level,
        "{company_name}": company_name,
        "{role_id}": role_id,
        "{role_name}": role_name,
        "{role_industry}": role_industry,
        "{your_industry}": your_industry,
        "{alignment}": alignment,
        "{experience}": experience,
        "{tasks}": tasks,
        "{skills}": skills,
        "{your_name}": your_name
    }
 
    # Generate the final email by replacing placeholders with user inputs
    final_email = email_template
    for placeholder, replacement in replacements.items():
        final_email = final_email.replace(placeholder, replacement)
 
    # Return the generated email
    return final_email
 
# Generate and print the email
final_email = generate_email_from_user_input()
print("\n--- Generated Email ---")
print(final_email)