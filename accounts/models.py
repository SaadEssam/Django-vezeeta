from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.

## Choices :
TYPE_OF_PERSON=(
    ('M', "Male"),
    ('F', "Female"),
)


class Profile(models.Model):

    DOCTOR_IN={
        ("جلدية", 'جلدية'),
        ('أسنان', "أسنان"),
        ('أطفال حديثي الولادة', "أطفال حديثي الولادة"),
        ('مخ وأعصاب', "مخ وأعصاب"),
        ('عظام', "عظام"),
        ('نساء وتوليد', "نساء وتوليد"),
        ('أنف وأذن وحنجرة', "أنف وأذن وحنجرة"),
        ('قلب وأوعيه دموية', "قلب وأوعيه دموية"),
        ('أمراض دم', "أمراض دم"),
        ('أورام', "أورام"),
        ('باطنة', "باطنة"),
        ('تخسيس وتغذية', "تخسيس وتغذية"),
        ('جراحة أطفال', "جراحة أطفال"),
        ('جراحة أورام', "جراحة أورام"),
        ('جراحة أوعية دموية', "جراحة أوعية دموية"),
        ('جراحة تجميل', "جراحة تجميل"),
        ('جراحة سمنة ومناظير', "جراحة سمنة ومناظير"),
        ('علاج طبيعي وأصابات ملاعب', "علاج طبيعي وأصابات ملاعب"),

    }


    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("الإسم :"), max_length=50)
    surname = models.CharField(_("اللقب :"), max_length=50)
    subtitle = models.CharField(_(" نبذه عنك :"), max_length=50)
    address = models.CharField(_("المدينة :"), max_length=50)
    address_detail = models.CharField(_("العنوان بالتفصيل :"), max_length=50)
    number_phone = models.CharField(_("الهاتف :"), max_length=50)
    working_hours = models.CharField(_("عدد ساعات العمل :"), max_length=50)
    waiting_time = models.CharField(_("مده الانتظار :"), max_length=50, blank=True, null=True)
    who_i = models.TextField(_("نبذه عني :"), max_length=250, blank=True, null=True)
    specialist_doctor = models.CharField(_("متخصص في ؟"), max_length=200, blank=True, null=True)
    price = models.IntegerField(_("سعر الكشف :"), blank=True, null=True)
    image = models.ImageField(_("الصورة الشخصية"), upload_to='profile', blank=True, null=True)
    slug = models.SlugField(_("slug"),blank=True, null=True)
    facebook = models.CharField(max_length=50,blank=True, null=True)
    twitter = models.CharField(max_length=50,blank=True, null=True)
    google = models.CharField(max_length=50,blank=True, null=True)
    type_of_person = models.CharField(_("النوع :"), choices=TYPE_OF_PERSON, max_length=50)
    doctor = models.CharField(_("دكتور ؟"), choices=DOCTOR_IN, max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


    def __str__(self):
        return '%s' %(self.user.username)



def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
