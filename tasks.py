from reminders import celery, db, app
from models.appointment import Appointment
from sqlalchemy.orm.exc import NoResultFound
from twilio.rest import Client
import arrow

twilio_account_sid = app.flask_app.config['TWILIO_ACCOUNT_SID']
twilio_auth_token = app.flask_app.config['TWILIO_AUTH_TOKEN']
twilio_number = app.flask_app.config['TWILIO_NUMBER']

client = Client(twilio_account_sid, twilio_auth_token)


@celery.task()
def send_sms_reminder(msg_id):
    try:
        appointment = db.session.query(
            Appointment).filter_by(id=msg_id).one()
    except NoResultFound:
        return

    time = arrow.get(appointment.time).to(appointment.timezone)
    body = "Hey! You were feeling {0} about {1} on {2}. How have your thoughts on that incident changed? If you don't remember, text 'more' and we can send you your message! If you wouldn't like to think about it, just send 'no'.".format(
        appointment.mood,
        appointment.keyword
        time.format('h:mm a')
    )

    to = appointment.phone_number,
    client.messages.create(
        to,
        from_=twilio_number,
        body=body)