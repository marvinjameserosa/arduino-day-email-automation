
# Arduino Day Philippines Email Automation

This repository contains Python scripts for automating email communication related to Arduino Day Philippines, including partnership outreach and speaker invitation/acceptance.

## Table of Contents

*   [Setting Up and Activating a Virtual Environment](#setting-up-and-activating-a-virtual-environment)
*   [Non-Technical Instructions to Use This Email Automation](#non-technical-instructions-to-use-this-email-automation)
*   [Directory Structure](#directory-structure)
*   [Instructions](#instructions)
*   [Specific Notes for Speakership Acceptance Automation](#specific-notes-for-speakership-acceptance-automation)
*   [Contributing](#contributing)
*   [License](#license)

## Setting Up and Activating a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies for this project.

### Windows

1.  **Create a Virtual Environment:**

    ```sh
    python -m venv <folder-name>
    ```

    Example:

    ```sh
    python -m venv venv
    ```

2.  **Activate the Virtual Environment:**

    ```sh
    <folder-name>\Scripts\activate.bat
    ```

    Example:

    ```sh
    venv\Scripts\activate.bat
    ```

### Linux/macOS

1.  **Create a Virtual Environment:**

    ```sh
    python -m venv <folder-name>
    ```

    Example:

    ```sh
    python -m venv venv
    ```

2.  **Activate the Virtual Environment:**

    ```sh
    source <folder-name>/bin/activate
    ```

    Example:

    ```sh
    source venv/bin/activate
    ```

### Deactivating the Virtual Environment

To exit the virtual environment, run:

```sh
deactivate
```

# User-Friendly Instructions for Using this Email Automation

This document provides guidelines for utilizing the email automation scripts effectively.

## Directory Structure

-   **`automation.py`** – Main automation script for partnership emails.
-   **`ops-speakers-automation.py`** – Automation script for operations, specifically for speakership emails.
-   **`email-template\`** – Contains assets for html templates.

## Partnership Emails

To send partnership emails, manually transfer the HTML content from the `email-template` folder into the `automation.py` file.  
_Note: This process may be streamlined in future versions._

## Speakership Emails

For speakership emails, simply edit the `speakers.html` file to modify the content as needed.

## Initial Setup

Before using the email automation, follow these steps:

1.  Install the required library by running:
```sh
    pip install python-dotenv 
```
2.  Create a `.env` file in the root directory (the same directory as `automation.py` and `speakers.py`).
3.  Add the following lines to the `.env` file, replacing the placeholders with your actual credentials.
```.env
    SENDER_EMAIL=[Your Email Address]  
    SENDER_PASSWORD=[Your App Password]` 
   ```
5.  To obtain an app password for Gmail, follow these instructions:  
    [Generate an App Password on Gmail](https://support.google.com/mail/answer/185833?hl=en)

## Running the Automation

Once the setup is complete, you are ready to run the email automation. Follow the task-specific instructions given by your lead accordingly.

You can run an automation py file by simple entering in your terminal the command:
```bash
python filename.py
```
**Important:** Always test the automation using test email addresses before sending to actual recipients.

## Special Instructions for Operations – Program Committee (Speakership Acceptance Emails)

When editing `speakers.html` for speakership acceptance emails, please ensure the following:

-   Update the recipient’s name.
-   Update the topic name.
-   Modify the talk segment details as necessary.
-   Confirm with your lead that the content is accurate and up to date before sending the email.