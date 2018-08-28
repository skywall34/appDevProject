from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail

class SendEmailDaily(CronJobBase):
    RUN_EVERY_MINS = 1 # every minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'mysite.send_email_daily'    # a unique code

    def do(self):
        send_mail('Subscription Update',
                  'Thank you for subscibing to TOGETHER! For now we are a new service so we will send updates when we can!',
                  '',
                  [''],
                  fail_silently=False, )