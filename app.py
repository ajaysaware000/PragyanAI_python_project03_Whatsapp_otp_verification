import streamlit as st
from twilio.rest import Client


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="PragyanAI - WhatsApp Verification",
    page_icon="💬",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #0e0e0f;
    }

    /* Main container */
    .main {
        padding-top: 2rem;
    }

    /* Title */
    .title {
        font-size: 32px;
        font-weight: 700;
        color: white;
        margin-bottom: 25px;
    }

    /* Section labels */
    .section-title {
        font-size: 17px;
        font-weight: 600;
        color: white;
        margin-bottom: 8px;
    }

    /* Status box */
    .status-box {
        background-color: #1b1c1f;
        border: 1px solid #33343a;
        border-radius: 5px;
        padding: 18px;
        color: #eeeeee;
        font-size: 16px;
    }

    /* Success */
    .success-status {
        color: #55e68b;
        font-weight: 500;
    }

    /* Error */
    .error-status {
        color: #ff6b6b;
        font-weight: 500;
    }

    /* Info */
    .info-status {
        color: #70b7ff;
        font-weight: 500;
    }

    /* Buttons */
    div.stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 7px;
        border: none;
        background-color: #5b5b66;
        color: white;
        font-size: 17px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #6a6a76;
        color: white;
    }

    /* Text input */
    div[data-baseweb="input"] {
        background-color: #1a1b1e;
        border-radius: 5px;
    }

    input {
        color: white !important;
    }

    /* Hide Streamlit menu/footer */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# TWILIO CONFIGURATION
# --------------------------------------------------

ACCOUNT_SID = st.secrets["TWILIO_ACCOUNT_SID"]
AUTH_TOKEN = st.secrets["TWILIO_AUTH_TOKEN"]
VERIFY_SERVICE_SID = st.secrets["TWILIO_VERIFY_SERVICE_SID"]


# --------------------------------------------------
# TWILIO CLIENT
# --------------------------------------------------

client = Client(
    ACCOUNT_SID,
    AUTH_TOKEN
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "otp_sent" not in st.session_state:
    st.session_state.otp_sent = False

if "phone_number" not in st.session_state:
    st.session_state.phone_number = ""

if "status_message" not in st.session_state:
    st.session_state.status_message = ""

if "status_type" not in st.session_state:
    st.session_state.status_type = ""


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown(
    '<div class="title">PragyanAI - WhatsApp Verification</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# WHATSAPP NUMBER
# --------------------------------------------------

st.markdown(
    '<div class="section-title">WhatsApp Number</div>',
    unsafe_allow_html=True
)

phone_number = st.text_input(
    "WhatsApp Number",
    value=st.session_state.phone_number,
    placeholder="+919876543210",
    label_visibility="collapsed"
)


# --------------------------------------------------
# SEND OTP
# --------------------------------------------------

if st.button("💬 Send WhatsApp OTP"):

    phone_number = phone_number.strip()

    # Validate phone number
    if not phone_number:

        st.session_state.status_message = (
            "Please enter your WhatsApp number."
        )

        st.session_state.status_type = "error"

    elif not phone_number.startswith("+"):

        st.session_state.status_message = (
            "Please enter the number with country code. "
            "Example: +919876543210"
        )

        st.session_state.status_type = "error"

    else:

        try:

            verification = client.verify.v2.services(
                VERIFY_SERVICE_SID
            ).verifications.create(
                to=phone_number,
                channel="whatsapp"
            )

            st.session_state.otp_sent = True
            st.session_state.phone_number = phone_number

            st.session_state.status_message = (
                "WhatsApp OTP sent successfully."
            )

            st.session_state.status_type = "success"

        except Exception as e:

            st.session_state.status_message = str(e)
            st.session_state.status_type = "error"


# --------------------------------------------------
# OTP INPUT
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Enter WhatsApp OTP</div>',
    unsafe_allow_html=True
)

otp = st.text_input(
    "Enter WhatsApp OTP",
    placeholder="Enter 6-digit OTP",
    max_chars=6,
    label_visibility="collapsed"
)


# --------------------------------------------------
# VERIFY OTP
# --------------------------------------------------

if st.button("✅ Verify WhatsApp"):

    if not phone_number:

        st.session_state.status_message = (
            "Please enter your WhatsApp number first."
        )

        st.session_state.status_type = "error"

    elif not otp:

        st.session_state.status_message = (
            "Please enter the OTP."
        )

        st.session_state.status_type = "error"

    elif len(otp) != 6:

        st.session_state.status_message = (
            "OTP must contain 6 digits."
        )

        st.session_state.status_type = "error"

    else:

        try:

            verification_check = client.verify.v2.services(
                VERIFY_SERVICE_SID
            ).verification_checks.create(
                to=phone_number,
                code=otp
            )

            if verification_check.status == "approved":

                st.session_state.status_message = (
                    "WhatsApp number verified successfully."
                )

                st.session_state.status_type = "success"

            else:

                st.session_state.status_message = (
                    "Invalid or expired OTP."
                )

                st.session_state.status_type = "error"

        except Exception as e:

            st.session_state.status_message = str(e)
            st.session_state.status_type = "error"


# --------------------------------------------------
# STATUS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">WhatsApp Status</div>',
    unsafe_allow_html=True
)

if st.session_state.status_message:

    if st.session_state.status_type == "success":

        st.markdown(
            f"""
            <div class="status-box">
                <span class="success-status">
                    ✅ {st.session_state.status_message}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif st.session_state.status_type == "error":

        st.markdown(
            f"""
            <div class="status-box">
                <span class="error-status">
                    ❌ {st.session_state.status_message}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="status-box">
                <span class="info-status">
                    ℹ️ {st.session_state.status_message}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

else:

    st.markdown(
        """
        <div class="status-box">
            <span class="info-status">
                ℹ️ Enter your WhatsApp number and send an OTP.
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )
