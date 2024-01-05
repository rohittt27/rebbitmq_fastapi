
import smtplib
import logging

def mail_trigger(email_args):
    try:
        with smtplib.SMTP(email_args['server'], email_args['port']) as smtp:
            smtp.starttls()
            smtp.login(email_args['senderEmail'], email_args['password'])
            smtp.send_message(email_args['message'])
    except Exception as err:
        logging.error("Exception occurred while sending email- {}".format(err))



# import smtplib
# import logging
# import asyncio

# async def mail_trigger_async(email_args):
#     try:
#         loop = asyncio.get_running_loop()
#         await loop.run_in_executor(None, send_email, email_args)
#     except Exception as err:
#         logging.error("Exception occurred while sending email- {}".format(err))

# def send_email(email_args):
#     with smtplib.SMTP(email_args['server'], email_args['port']) as smtp:
#         smtp.starttls()
#         smtp.login(email_args['senderEmail'], email_args['password'])
#         smtp.send_message(email_args['message'])

# def mail_trigger(email_args):
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(mail_trigger_async(email_args))