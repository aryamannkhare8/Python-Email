# Email PDF Attachment from CSV Data

This Python script is designed to perform the following tasks:

- **Extract Data from CSV**: Reads a CSV file containing 'Name' and 'Email' columns and extracts the data.
- **Attachment Handling**: Searches for corresponding PDF files in a specified directory based on the 'Name' column extracted from the CSV.
- **Email Sending**: Sends an email to each recipient, attaching the relevant PDF file if found.

## Usage

### Requirements

- Python 3.x
- Libraries: `csv`, `smtplib`, `email`, `glob`

### Setup

1. **CSV File**: Prepare a CSV file containing 'Name' and 'Email' columns.
2. **PDF Directory**: Specify the path to the directory containing the PDF files.

### Execution

1. **File Configuration**:
   - Replace `file_path` variable with the path to your CSV file in the `emailListname.csv`.
   - Replace `pdf_directory` variable with the path to the directory containing the PDF files.
   - Update the sender's email address and password.

2. **Run Script**: Execute the Python script in your preferred environment.

### Notes

- The script attempts to find a PDF file for each 'Name' in the specified directory. If found, it sends an email with the attached PDF; otherwise, it prints a notification about the missing PDF for a particular name.
- Ensure the proper configuration of sender's email and its authorization to send emails programmatically.

### Sample Usage

```bash
python email_pdf_sender.py
```

### Author: Aryamann Khare  
### Contact: aryamannkhare8@gmail.com  
### LinkedIn: www.linkedin.com/in/aryamann-khare-8b9453178
