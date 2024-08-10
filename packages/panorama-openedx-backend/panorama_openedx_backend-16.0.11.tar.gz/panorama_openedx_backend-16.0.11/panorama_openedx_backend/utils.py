"""
Utility functions to access the Panorama configurations.
"""
import logging

from django.conf import settings
from django.contrib.auth import get_user_model

from .models import DashboardType, UserAccessConfiguration

User = get_user_model()

logger = logging.getLogger(__name__)


def panorama_mode() -> str:
    """
    Return the Panorama mode.
    """
    return settings.PANORAMA_MODE


def has_access_to_panorama(user: User) -> bool:
    """
    Has access to panorama function.

    Return true if the user can access Panorama, i.e., if there is a record in the user access configuration model
    or if the user is superuser.
    In SaaS and Custom modes, if the student view is enabled, everybody has access to Panorama.
    In DEMO mode, the backend may not be initialized so only superusers have access.
    """
    if panorama_mode() in ['DEMO', 'FREE']:
        return user.is_superuser
    else:
        return (getattr(settings, 'PANORAMA_ENABLE_STUDENT_VIEW', False)
                or UserAccessConfiguration.objects.filter(user=user).exists()
                or user.is_superuser)


def get_user_role(user: User) -> str:
    """
    Get the Panorama user role.

    In DEMO mode, the backend may not be initialized so superusers have READ access.
    """
    if panorama_mode() in ['DEMO', 'FREE']:
        role = "READER" if user.is_superuser else None
    else:
        try:
            user_access_configuration = UserAccessConfiguration.objects.get(user=user)
            role = user_access_configuration.role
        except UserAccessConfiguration.DoesNotExist:
            role = "READER" if user.is_superuser else "STUDENT"

    return role


def get_user_arn(user: User) -> str:
    """
    Get the AWS user ARN mapping to this user.
    """
    try:
        user_access_configuration = UserAccessConfiguration.objects.get(user=user)
        return user_access_configuration.arn
    except UserAccessConfiguration.DoesNotExist:
        return settings.PANORAMA_DEFAULT_USER_ARN


def get_user_dashboards(user: User) -> list:
    """
    Get the list of user dashboards to import from the Django admin configuration.
    """
    try:
        user_access_configuration = UserAccessConfiguration.objects.get(user=user)

        dashboard_type = user_access_configuration.dashboard_type

        dashboard_list = []
        for dashboard in dashboard_type.dashboards.all().order_by('priority'):
            dashboard_list.append({
                "name": dashboard.name,
                "displayName": dashboard.display_name,
                "id": dashboard.dashboard_id,
            })

        return dashboard_list

    except UserAccessConfiguration.DoesNotExist:
        if settings.PANORAMA_ENABLE_STUDENT_VIEW:
            return get_student_dashboards()
        else:
            return []


def get_student_dashboards() -> list:
    """
    Get the list of dashboards available for students.
    """
    student_dashboard_types = DashboardType.objects.filter(student_view=True)

    dashboard_list = []
    for dashboard_type in student_dashboard_types:
        for dashboard in dashboard_type.dashboards.all().order_by('priority'):
            dashboard_list.append({
                "name": dashboard.name,
                "displayName": dashboard.display_name,
                "id": dashboard.dashboard_id,
            })

    return dashboard_list
