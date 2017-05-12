from flask_mail import Mail, Message

from applications import ApplicationStatus

flask_mail = Mail()


def send_notification(recipient, subject, body, html=None):
    flask_mail.send(Message(
        subject=subject,
        recipients=[recipient],
        body=body,
        html=html,
        sender='brightmatter.hackathon@gmail.com'
    ))


def notify_candidate(candidate):
    if candidate.candidate_status == ApplicationStatus.ACCEPTED:
        send_notification(candidate.candidate_email, "Congratulations, you've been accepted", "Woohoo!")
    elif candidate.candidate_status == ApplicationStatus.REJECTED:
        send_notification(candidate.candidate_email, "Sorry, you've been rejected", "Aww...")
