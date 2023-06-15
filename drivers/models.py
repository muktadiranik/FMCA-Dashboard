from django.db import models
from django.contrib.auth.models import User
import random
import string
from datetime import timedelta


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    dba = models.CharField(max_length=128, null=True, blank=True)
    full_name = models.CharField(max_length=128, null=True, blank=True)
    usdot = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=128, null=True, blank=True)
    extra_phone_number = models.CharField(
        max_length=128, null=True, blank=True)
    phone_number_2 = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(max_length=128, null=True, blank=True)
    extra_emails = models.EmailField(max_length=128, null=True, blank=True)
    email_2 = models.EmailField(max_length=128, null=True, blank=True)
    ssn = models.CharField(max_length=128, null=True, blank=True)
    ein = models.CharField(max_length=128, null=True, blank=True)
    mc_number = models.CharField(max_length=128, null=True, blank=True)
    pin_number = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    address_2 = models.CharField(max_length=256, null=True, blank=True)
    zip = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    featured_image = models.ImageField(
        default='service/no-img.png', null=True, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, blank=True)
    primary_id_number = models.CharField(
        max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    role = models.CharField(max_length=128, null=True, blank=True)
    ssn = models.CharField(max_length=128, null=True, blank=True)
    employee_id = models.CharField(max_length=128, null=True, blank=True)
    tracking_id = models.CharField(max_length=128, null=True, blank=True)
    license = models.CharField(max_length=128, null=True, blank=True)
    license_type = models.CharField(max_length=128, null=True, blank=True)
    license_expiration = models.DateField(null=True, blank=True)
    license_zip = models.CharField(max_length=128, null=True, blank=True)
    license_state = models.CharField(max_length=128, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    business_phone = models.CharField(max_length=128, null=True, blank=True)
    mobile_phone = models.CharField(max_length=128, null=True, blank=True)
    fax_number = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    on_leave = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if not self.primary_id_number:
            company_name = self.company.name[:4].upper()
            first_name = self.first_name[:3].upper()
            last_name = self.last_name[-2:].upper()
            random_chars = ''.join(random.choices(string.digits, k=8))
            self.primary_id_number = f'{company_name}:{first_name}{last_name}{random_chars}'
        super(Employee, self).save(*args, **kwargs)


class EmployeeFile(models.Model):
    FILE_FOR = (
        ('license', 'license'),
        ('dot_drug_test', 'dot_drug_test'),
    )
    FILE_TYPE = (
        ('image', 'image'),
        ('pdf', 'pdf'),
        ('docx', 'docx'),
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    file_for = models.CharField(
        max_length=128, null=True, blank=True, choices=FILE_FOR)
    file_type = models.CharField(
        max_length=128, null=True, blank=True, choices=FILE_TYPE)
    expiration_date = models.DateField(null=True, blank=True)
    two_day_before_expiration = models.DateField(null=True, blank=True)
    is_expired = models.BooleanField(default=False)
    non_expiration_type = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.file_for

    def save(self, *args, **kwargs):
        if not self.expiration_date:
            self.two_day_before_expiration = self.expiration_date - \
                timedelta(days=2)
        super(EmployeeFile, self).save(*args, **kwargs)


class OwnerEmployeeNotification(models.Model):
    NOTIFICATION_TYPE = (
        ('alert', 'alert'),
        ('simple_notification', 'simple_notification'),
    )
    NOTIFICATION_FILE_TYPE = (
        ('image', 'image'),
        ('pdf', 'pdf'),
        ('docx', 'docx'),
    )
    NOTIFICATION_DOCUMENT_TYPE = (
        ('license', 'license'),
        ('dot_drug_test', 'dot_drug_test'),
        ('none', 'none'),
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, blank=True)
    notification_sender = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    notification_receiver = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    notification_type = models.CharField(
        max_length=128, null=True, blank=True, choices=NOTIFICATION_TYPE)
    notification = models.CharField(max_length=255, null=True, blank=True)
    notification_document_type = models.CharField(
        max_length=128, null=True, blank=True, choices=NOTIFICATION_DOCUMENT_TYPE)
    notification_file_type = models.CharField(
        max_length=128, null=True, blank=True, choices=NOTIFICATION_FILE_TYPE)
    notification_file = models.FileField(null=True, blank=True)
    notification_accept = models.BooleanField(default=False)
    expire_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.notification_sender.first_name + " to " + self.notification_receiver.first_name


class MedicalTestCenter(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class DotDrugTest(models.Model):
    TEST_TYPE = (
        ('urine_drug_test', 'urine_drug_test'),
        ('urine_drug_breathe_test', 'urine_drug_breathe_test'),
    )
    DOT_FEDERAL = (
        ('dot_test', 'dot_test'),
    )
    TEST_REASON = (
        ('pre_employment', 'pre_employment'),
        ('random', 'random'),
        ('post_accident', 'post_accident'),
        ('reasonable_suspicion', 'reasonable_suspicion'),
        ('return_to_duty', 'return_to_duty'),
        ('follow_up', 'follow_up'),
        ('stipulated_agreement', 'stipulated_agreement'),
        ('phys_periodic', 'phys_periodic'),
    )
    PANEL = (
        ('5_panel_dot_test', '5_panel_dot_test'),
    )
    OBSERVER = (
        ('no_observer', 'no_observer'),
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    medical_test_center = models.ForeignKey(
        MedicalTestCenter, on_delete=models.CASCADE, null=True, blank=True)
    test_type = models.CharField(
        max_length=128, null=True, blank=True, choices=TEST_TYPE)
    dot_federal = models.CharField(
        max_length=128, null=True, blank=True, choices=DOT_FEDERAL, default='dot_test')
    test_reason = models.CharField(
        max_length=128, null=True, blank=True, choices=TEST_REASON, default='random')
    panel = models.CharField(max_length=128, null=True,
                             blank=True, choices=PANEL, default='5_panel_dot_test')
    observer = models.CharField(
        max_length=128, null=True, blank=True, choices=OBSERVER, default='no_observer')
    order_date = models.DateField(null=True, blank=True)
    order_number = models.CharField(max_length=128, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    scheduled_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.employee.first_name + " " + self.employee.last_name + " - " + self.test_type

    def save(self, *args, **kwargs):
        if not self.order_number:
            random_number = ''.join(random.choices(string.digits, k=5))
            self.order_number = f'{self.employee.primary_id_number}-{random_number}'
        super(DotDrugTest, self).save(*args, **kwargs)


class MedicalTestForm(models.Model):
    file_name = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.file_name
