import smtplib


def send_email(lat_x, lng_x):
    """sends an email with ISS coordinates"""

    email_smtp = {
        "Gmail": "smtp.gmail.com",
        "Hotmail": "smtp.live.com",
        "Outlook": "outlook.office365.com",
        "Yahoo": "smtp.mail.yahoo.com"
    }

    my_email = "day31.testing.1@gmail.com"
    my_email_provider = my_email[my_email.find("@")+1:my_email.find(".com", my_email.find("@"))].title()
    password = "testingTESTING1212"
    email_recipient = "mhutchinson25@gmail.com" #Insert your email

    SUBJECT = "ISS Locator PING"

    email_body = f"The ISS is Visible at lat: {lat_x}, lng: {lng_x}"
    email_msg = f"Subject:{SUBJECT}\n\n{email_body}".encode("utf-8")

    with smtplib.SMTP(email_smtp[my_email_provider]) as connection:
        connection.starttls()
        connection.login(user=my_email,
                         password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_recipient,
                            msg=email_msg)
