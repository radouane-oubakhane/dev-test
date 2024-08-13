import pandas as pd
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def handle_uploaded_file(f):
        df = pd.read_excel(f)
        required_columns = {'Cust State', 'Cust Pin', 'DPD'}
        if not required_columns.issubset(df.columns):
            raise ValueError("Invalid file. Please upload a valid Excel / CSV file.")
        
        df.rename(columns={'Cust State': 'CustState', 'Cust Pin': 'CustPin', 'DPD': 'DPD'}, inplace=True)
        summary = df[['CustState', 'CustPin', 'DPD']]
        
        return summary



def send_summary_email(summary):

    subject = 'Python Assignment - Radouane Oubakhane'
    
    email_from = 'radouane@devtest.com'
    
    recipient_list = ['tech@themedius.ai', 'yash@themedius.ai']
    
    # Render the HTML table to a string
    html_message = render_to_string('fileupload/email_summary.html', {'summary': summary.to_dict(orient='records')})
    
    # Create the email
    email = EmailMessage(subject, html_message, email_from, recipient_list)
    email.content_subtype = 'html'  # Set the email content type to HTML
    
    # Send the email
    email.send()




