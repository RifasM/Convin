from celery import shared_task

from Convin.settings import EMAIL_HOST_USER


@shared_task(bind=True,
             name='Send_Emails_Everyday',
             max_retries=3,
             soft_time_limit=20)
def send_daily_email(data):
    subject = "Daily Email for Task Type: {}".format(data.task_type)
    text_email = "Task Type: {}\n" \
                 "Task Description: {}\n" \
                 "Thank You\nTeam Convin". \
        format(data.task_type, data.task_desc)
    """send_mail(
        subject=subject,
        message=text_email,
        from_email=EMAIL_HOST_USER,
        recipient_list=[data.email.to],
        fail_silently=False
    )"""
    print(subject, text_email)
    print("Sending to: ", EMAIL_HOST_USER)


@shared_task(bind=True,
             name='Send_Emails_Every_Week',
             max_retries=3,
             soft_time_limit=20)
def send_weekly_email(data):
    subject = "Weekly Email for Task Type: {}".format(data.task_type)
    text_email = "Task Type: {}\n" \
                 "Task Description: {}\n" \
                 "Thank You\nTeam Convin". \
        format(data.task_type, data.task_desc)
    """send_mail(
        subject=subject,
        message=text_email,
        from_email=EMAIL_HOST_USER,
        recipient_list=[data.email.to],
        fail_silently=False
    )"""
    print(subject, text_email)
    print("Sending to: ", EMAIL_HOST_USER)


@shared_task(bind=True,
             name='Send_Emails_Every_Month',
             max_retries=3,
             soft_time_limit=20)
def send_monthly_email(data):
    subject = "Monthly Email for Task Type: {}".format(data.task_type)
    text_email = "Task Type: {}\n" \
                 "Task Description: {}\n" \
                 "Thank You\nTeam Convin". \
        format(data.task_type, data.task_desc)
    """send_mail(
        subject=subject,
        message=text_email,
        from_email=EMAIL_HOST_USER,
        recipient_list=[data.email.to],
        fail_silently=False
    )"""
    print(subject, text_email)
    print("Sending to: ", EMAIL_HOST_USER)
