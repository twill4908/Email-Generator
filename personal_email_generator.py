# Define the email template with placeholders
email_template = """
 
Subject Line: {role_id} - {role_name}
 
Hey {poc_name},
 
My name is {your_name} and I'm an L11 analyst aligned to the Data & AI practice, with experience in data quality and management, primarily in the healthcare and telecommunication industry. I have a strong background in tasks like data cleansing, analysis, building reports and dashboards creation Working with  tools such as MS Excel, ETL processes and creating DAGs pipelines in Airflow, Power BI (for dashboards and KPIs), Informatica IDQ (for source-to-target mappings),  and PostgreSQL/Big Query (for validation/testing).
 
I’m also keen to learning more about the {company_name} so I can make an impact in the {role_industry} industry. I recently applied for the open role of {role_name} and believe I could be a great fit for your team
 
Here is my one-pager. Please let me know if I can grab time with you to discuss this role further.
 
Kind regards,
{your_name}
"""
 
# Function to prompt the user for inputs and generate the email
def generate_email_from_user_input():
 
    # Collect user inputs for the email --- Results from user response will be the true replacement
    poc_name = input("Enter the Point of Contact (POC) name for the role you are applying for: ")
    company_name = input("Enter the company name (client name) that you are applying for: ")
    role_id = input("Enter the ID of role that you are applying for: ")  # This could be used for any specific logic, but for now it's just captured
    role_name = input("Enter the name of the role you are applying for: ")
 
    # Create a dictionary of the user inputs for replacement
    replacements = {
 
        "{poc_name}": poc_name,
        "{company_name}": company_name,
        "{role_id}": role_id,
        "{role_name}": role_name,
        "{your_name}": your_name, # type: ignore
 
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
 
 