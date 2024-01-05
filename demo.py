
# import logging
# import os
# from typing import Optional
# from fastapi import FastAPI
# from pydantic import BaseModel
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from utils import mail_trigger
# import threading
# from dotenv import load_dotenv
# import pika
# import json

# load_dotenv('.env')

# app = FastAPI()

# # RABBITMQ_HOST = "localhost"
# # RABBITMQ_QUEUE = "user_registered"

# html = """
#     <html>
#         <body>
#             <h1>Registration Successful</h1>
#             <p>Thank you for registering!</p>
#         </body>
#     </html>
# """


# class EmailSchema(BaseModel):
#     email_to: str
#     cc: Optional[str] = ""
#     bcc: Optional[str] = ""
#     subject: str
#     template: str
#     template_data: dict


# def consume_from_rabbitmq():
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

#     channel = connection.channel()

#     channel.queue_declare(queue='email_queue')

#     print(' [*] Waiting for logs. To exit press CTRL+C')

#     def callback(ch, method, properties, body):
#         body_str = body.decode('utf-8')
#         event_data = json.loads(body_str)
#         if event_data['event_type'] == 'user_registered':
#             email_schema_instance = EmailSchema(**event_data['body'])
#             print(f" [x] Received {event_data['event_type']} message: {event_data['body']}")
#             handle_user_registration(event_data['body'], email_schema_instance)

#     channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)
#     channel.start_consuming()

# def handle_user_registration(user_data, email):
#     try:
#         print(f" [x] Handling user registration: {user_data}")
#         host = os.environ.get('EMAIL_HOST')
#         host_email = os.environ.get('EMAIL_HOST_USER')
#         host_password = os.environ.get('EMAIL_HOST_PASSWORD')
#         port = os.environ.get('EMAIL_PORT')

#         body = html

#         message = MIMEMultipart()
#         message['From'] = host_email
#         message['To'] = user_data['email_to']
#         # message['Cc'] = email.cc
#         # message['Bcc'] = email.bcc
#         message['Subject'] = user_data['subject']
#         message.attach(MIMEText(body, "html"))

#         email_args = {
#             'senderEmail': host_email,
#             'port': port,
#             'password': host_password,
#             'body': body,
#             'message': message,
#             'server': host,
#         }
#         t = threading.Thread(target=mail_trigger, args=[email_args])
#         t.start()

#     except Exception as err:
#         logging.error("Exception occurred during user registration handling - {}".format(err))

# # Run the consumer in a separate thread
# threading.Thread(target=consume_from_rabbitmq).start()
# consumer_thread = threading.Thread(target=consume_from_rabbitmq)
# consumer_thread.start()
# consumer_thread.join()  # Wait for the consumer thread to finish before exiting


#############################



# import logging
# import os
# from typing import Optional
# from fastapi import FastAPI
# from pydantic import BaseModel
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from utils import mail_trigger
# import threading
# from dotenv import load_dotenv
# import pika
# import json

# load_dotenv('.env')

# app = FastAPI()

# # RABBITMQ_HOST = "localhost"
# # RABBITMQ_QUEUE = "user_registered"

# html = """
#     <html>
#         <body>
#             <h1>Registration Successful</h1>
#             <p>Thank you for registering!</p>
#         </body>
#     </html>
# """


# class EmailSchema(BaseModel):
#     email_to: str
#     cc: Optional[str] = ""
#     bcc: Optional[str] = ""
#     subject: str
#     template: str
#     template_data: dict


# def consume_from_rabbitmq():
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

#     channel = connection.channel()

#     channel.queue_declare(queue='email_queue')

#     print(' [*************] Waiting for logs. To exit press CTRL+C')

#     def callback(ch, method, properties, body):
#         body_str = body.decode('utf-8')
#         event_data = json.loads(body_str)
#         if event_data['event_type'] == 'user_registered':
#             email_schema_instance = EmailSchema(**event_data['body'])
#             print(f" [x] Received {event_data['event_type']} message: {event_data['body']}")
#             handle_user_registration(event_data['body'], email_schema_instance)

#     channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)
#     channel.start_consuming()

# def handle_user_registration(user_data, email):
#     try:
#         print(f" [x] Handling user registration: {user_data}")
#         host = os.environ.get('EMAIL_HOST')
#         host_email = os.environ.get('EMAIL_HOST_USER')
#         host_password = os.environ.get('EMAIL_HOST_PASSWORD')
#         port = os.environ.get('EMAIL_PORT')

#         body = html

#         message = MIMEMultipart()
#         message['From'] = host_email
#         message['To'] = user_data['email_to']
#         # message['Cc'] = email.cc
#         # message['Bcc'] = email.bcc
#         message['Subject'] = user_data['subject']
#         message.attach(MIMEText(body, "html"))

#         email_args = {
#             'senderEmail': host_email,
#             'port': port,
#             'password': host_password,
#             'body': body,
#             'message': message,
#             'server': host,
#         }
#         breakpoint()
#         t = threading.Thread(target=mail_trigger, args=[email_args])
#         t.start()

#     except Exception as err:
#         logging.error("Exception occurred during user registration handling - {}".format(err))

# # Run the consumer in a separate thread
# threading.Thread(target=consume_from_rabbitmq).start()
