from django.contrib.auth import user_logged_in, user_login_failed
from django.dispatch import receiver
from .models import UserLoginActivity
from .utils import get_client_ip, dispatch_email
from .settings import accounts_config
from django.core.exceptions import ImproperlyConfigured


@receiver(user_logged_in)
def log_user_logged_in_success(sender, user, request, **kwargs):
    try:
        ip_address = get_client_ip(request)
        user_agent_info = (request.META.get("HTTP_USER_AGENT", "<unknown>")[:255],)
        user_login_activity_log = UserLoginActivity(
            login_IP=ip_address,
            login_username=user.username,
            user_agent_info=user_agent_info,
            status=UserLoginActivity.SUCCESS,
        )
        user_login_activity_log.save()

        context = {
            "ip_address": ip_address,
            "username": user.username,
            "user_agent": user_login_activity_log.user_agent_info,
            "email": user.email,
            "time": user_login_activity_log.login_datetime,
        }
        if accounts_config["EMAIL_ON_LOGIN"]:
            dispatch_email(
                subject="New Login Alert",
                email=user.email,
                template="successful_login",
                context=context,
            )

    except Exception as e:
        raise ImproperlyConfigured(e)


@receiver(user_login_failed)
def log_user_logged_in_failed(sender, credentials, request, **kwargs):
    try:
        user_agent_info = (request.META.get("HTTP_USER_AGENT", "<unknown>")[:255],)
        user_login_activity_log = UserLoginActivity(
            login_IP=get_client_ip(request),
            login_username=credentials["username"],
            user_agent_info=user_agent_info,
            status=UserLoginActivity.FAILED,
        )
        user_login_activity_log.save()
    except Exception:
        # log the error
        pass
