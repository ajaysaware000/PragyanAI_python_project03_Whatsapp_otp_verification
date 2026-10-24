# WhatsApp OTP Verification System

A Python-based web application that sends an OTP to a user’s WhatsApp number using the Twilio Verify service and verifies the OTP entered by the user.

## Problem Statement

Many applications need to verify a user’s phone number during registration or login. SMS-based OTP verification can sometimes be delayed or fail to deliver. Therefore, a simple WhatsApp-based OTP verification system is needed to send and verify OTPs quickly using Twilio.

## Project Description

This project sends a One-Time Password (OTP) to the user’s WhatsApp number using the Twilio Verify service. The user enters the received OTP in the web application, and the system verifies whether it is correct. If the OTP is correct, the user is verified successfully; otherwise, an error message is displayed.

The application was developed and tested in Google Colab using Gradio. A Streamlit web application was created for the frontend and connected to GitHub for deployment.

## Features

- Send OTP to a user’s WhatsApp number
- Verify the OTP entered by the user
- Display verification success or failure message
- Simple and interactive web interface
- Developed using Python and Twilio

## Technologies Used

- Python
- Twilio Verify Service
- Gradio
- Streamlit
- Google Colab
- GitHub
- Streamlit Cloud

## Workflow

1. User opens the WhatsApp OTP Verification application.
2. User enters their WhatsApp phone number.
3. The application sends an OTP to the user’s WhatsApp using Twilio.
4. User receives the OTP on WhatsApp.
5. User enters the OTP in the application.
6. The system verifies the OTP.
7. If correct, it displays “Verification Successful.”
8. If incorrect, it displays “Invalid OTP.”

## How to Run

1. Clone this repository:
   ```bash
   git clone <your-repository-link>
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your Twilio credentials securely using environment variables or Streamlit secrets.

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Security Note

Twilio credentials such as Account SID, Auth Token, and Verify Service SID should not be uploaded directly to GitHub. Use environment variables or Streamlit secrets to keep them secure.

## Output

- OTP is sent successfully to the user’s WhatsApp number.
- User enters the received OTP in the application.
- The system verifies the OTP and displays the result.

## Live Application

[https://pragyanaipythonproject03whatsappotpverification-em8fgrd6gxzcfl.streamlit.app/]

## Future Scope

- Add resend OTP option
- Add OTP expiry time limit
- Store verified user details securely in a database
- Add login and registration features
- Improve the user interface

## Developed By

[Ajay Saware]
