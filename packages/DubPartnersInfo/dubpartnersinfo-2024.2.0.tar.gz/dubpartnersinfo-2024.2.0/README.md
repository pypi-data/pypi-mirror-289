

This is the README file for the project.

       This project creates Google Sheets based on Excel files in a specified directory.
       It performs the following steps:
       1. Assign directories to variables.
       2. Create a temporary folder if it doesn't exist.
       3. Process each file in the directory:
          a. Check if the file is a valid partner information file.
          b. Create a Google Sheet name.
          c. Open the Excel data file.
          d. Create a new Google Sheet file from a template.
          e. Read Excel vendor data from each tab.
          f. Update all tabs in the final Google Sheet file using batch update.
          g. Move the processed file to an archive directory.
       4. Display a message box with the number of files created and the processing time.

