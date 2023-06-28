from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Student, Teacher
from .utils.send_mail import send_mail


@receiver(post_save, sender=Student)
def student_created(sender, instance, created, **kwargs):
    if created:
        send_mail([instance.email], "Your data has been used for School-CRM system.")
    if instance.class_rel:
        instance.class_rel.students.add(instance)
        instance.class_rel.save()


@receiver(post_save, sender=Teacher)
def student_created(sender, instance, created, **kwargs):
    if instance.class_rel:
        instance.class_rel.teacher_rel = instance
        instance.class_rel.save()


@receiver(pre_save, sender=Student)
def handle_student_class_update(sender, instance, **kwargs):
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    if old_instance.class_rel != instance.class_rel:
        if old_instance.class_rel:
            old_instance.class_rel.students.remove(old_instance)
        if instance.class_rel:
            instance.class_rel.students.add(instance)
