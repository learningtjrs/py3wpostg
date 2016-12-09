from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class BaseEntity(models.Model):
#     is_active = models.BooleanField(default=True)
#     # CharField(max_length=200)
#     created = models.DateTimeField('Created Date/Time', auto_now_add=True, auto_now=False)
#     modified = models.DateTimeField('Modified Date/Time', auto_now=True, auto_now_add=False)
#     created_by = models.ForeignKey(User)
#     modified_by = models.ForeignKey(User)
#
#     class Meta:
#         abstract = True


class BuildingNumber(models.Model):
    #bldnum_id = (PK)
    bldnum_desc = models.CharField(max_length=200)
    bldnum_note = models.CharField(max_length=200)


class Street(models.Model):
    #street_id = (PK)
    street_name = models.CharField(max_length=200)
    street_note = models.CharField(max_length=200)


class State(models.Model):
    #state_id = (PK)
    state_name = models.CharField(max_length=200)
    state_note = models.CharField(max_length=200)


class Country(models.Model):
    #country_id = (PK)
    country_name = models.CharField(max_length=200)
    country_note = models.CharField(max_length=200)


class PostalCode(models.Model):
    #poscod_id = (PK)
    poscod_desc = models.CharField(max_length=200)
    poscod_note = models.CharField(max_length=200)


class Email(models.Model):
    # the owner_id should be attached to several classes
    # name is a description
    #email_id = (PK)
    email_desc = models.EmailField(max_length=70, null=True)
    email_note = models.CharField(max_length=200, default='feel free to comment')


class ProfessionalTitle (models.Model):
    #profn_title_id = (PK)
    profn_title_name = models.CharField(max_length=20)
    profn_title_desc = models.CharField(max_length=50)
    profn_title_note = models.CharField(max_length=100)


class Phone(models.Model):
    #phone_id = (PK)
    phone_num = models.CharField(max_length=30, null=False, blank=False)
    phone_desc = models.CharField(max_length=50)
    phone_note = models.CharField(max_length=50)


class WebLink(models.Model):
    #weblk_id = (PK)
    weblk_desc = models.URLField(max_length=50)
    weblk_note = models.CharField(max_length=100, default='feel free to comment')


class Company(models.Model):
    #comp_id = (PK)
    comp_name = models.CharField(max_length=20)
    comp_desc = models.CharField(max_length=50)
    # comp_comp_add_lk_comp_id = models.ForeignKey(CompanyAddressLink)
    # comp_comp_ph_lk_comp_id = models.ForeignKey(CompanyPhoneLink)
    # comp_comp_email_lk_comp_id = models.ForeignKey(CompanyEmailLink)
    # comp_comp_weblk_lk_comp_id = models.ForeignKey(CompanyWebLinkLink)
    comp_note = models.CharField(max_length=100)


# this class is the main for persons. it will be attached to other categorized classes. like "Employee, Supplier.."
class Contact(models.Model):
    #contact_id =(PK)
    contact_first_name = models.CharField(max_length=50, default='enter your first name')
    contact_last_name = models.CharField(max_length=50, default='enter your last name')
    # contact_contact_email_lk_contact_id = models.ForeignKey(ContactEmailLink)
    # contact_contact_add_lk_contact_id = models.ForeignKey(ContactAddressLink)
    # contact_contact_profn_title_lk_contact_id = models.ForeignKey(ContactProfessionalTitleLink)
    # contact_contact_ph_lk_contact_id = models.ForeignKey(ContactPhoneLink)
    # contact_contact_weblk_lk_contact_id = models.ForeignKey(ContactWebLinkLink)
    # contact_contact_comp_lk_contact_id = models.ForeignKey(ContactCompanyLink)
    # contact_useracc_contact_id = models.ForeignKey(UserAccount)
    contact_note = models.CharField(max_length=100, default='feel free to write your command')


#this class relate 2 classes : Contact and Email
class ContactEmailLink(models.Model):
    #contact_email_lk_id =(PK)
    contact_email_lk_contact_id = models.ForeignKey(Contact)
    contact_email_lk_email_id = models.ForeignKey(Email)

#this class relate 6 classes : Contact, BuildingNumber, Street, State, Country, PostalCode
class ContactAddressLink(models.Model):
    #contact_add_lk_id = (PK)
    contact_add_lk_contact_id = models.ForeignKey(Contact)
    contact_add_lk_appnum = models.CharField(max_length=10)
    contact_add_lk_bldnum_id = models.ForeignKey(BuildingNumber)
    contact_add_lk_street_id = models.ForeignKey(Street)
    contact_add_lk_state_id = models.ForeignKey(State)
    contact_add_lk_country_id = models.ForeignKey(Country)
    contact_add_lk_poscod_id = models.ForeignKey(PostalCode)

#this class relate 2 classes : Contact and ProfessionalTitle
class ContactProfessionalTitleLink(models.Model):
    #contact_profn_title_lk_id = (PK)
    contact_profn_title_lk_contact_id = models.ForeignKey(Contact)
    contact_profn_title_lk_profn_title_id = models.ForeignKey(ProfessionalTitle)

#this class relate 2 classes : Contact and Phone
class ContactPhoneLink(models.Model):
    #contact_ph_lk_id = (PK)
    contact_ph_lk_contact_id = models.ForeignKey(Contact)
    contact_ph_lk_phone_id = models.ForeignKey(Phone)

#this class relate 2 classes : Contact and WebLink
class ContactWebLinkLink(models.Model):
    #contact_weblk_lk_id =(PK)
    contact_weblk_lk_contact_id = models.ForeignKey(Contact)
    contact_weblk_lk_weblk_id = models.ForeignKey(WebLink)

class UserAccount(models.Model):
    #useracc_id = (PK)
    useracc_contact_id = models.ForeignKey(Contact)
    #useracc_email (here the primary e-mail should be defined)
    useracc_username = models.CharField(max_length=15)
    useracc_password = models.CharField(max_length=15)
    useracc_is_active = models.BooleanField(default=True)
    useracc_is_stuff = models.BooleanField(default=False)
    useracc_is_admin = models.BooleanField(default=False)
    #useracc_permission_role = !!!!!! this info should come from another table like "permission" for example
    useracc_is_employee = models.BooleanField(default=True)

class CompanyAddressLink(models.Model):
    #comp_add_lk_id = (PK)
    comp_add_lk_comp_id = models.ForeignKey(Company)
    comp_add_lk_appnum = models.CharField(max_length=10)
    comp_add_lk_bldnum_id = models.ForeignKey(BuildingNumber)
    comp_add_lk_street_id = models.ForeignKey(Street)
    comp_add_lk_state_id = models.ForeignKey(State)
    comp_add_lk_country_id = models.ForeignKey(Country)
    comp_add_lk_poscod_id = models.ForeignKey(PostalCode)

class CompanyPhoneLink(models.Model):
    #comp_ph_lk_id = (PK)
    comp_ph_lk_comp_id = models.ForeignKey(Company)
    comp_ph_lk_phone_id = models.ForeignKey(Phone)

class CompanyEmailLink(models.Model):
    #comp_email_lk_id = (PK)
    comp_email_lk_comp_id = models.ForeignKey(Company)
    comp_email_lk_email_id = models.ForeignKey(Email)

class CompanyWebLinkLink(models.Model):
    #comp_weblk_lk_id = (PK)
    comp_weblk_lk_comp_id = models.ForeignKey(Company)
    comp_weblk_lk_weblk_id = models.ForeignKey(WebLink)

class ContactCompanyLink(models.Model):
    #contact_comp_lk_id = (PK)
    contact_comp_lk_contact_id = models.ForeignKey(Contact)
    contact_comp_lk_comp_id = models.ForeignKey(Company)


########## samples ###################

# class WebLink(models.Model):
#     owner_id = models.ForeignKey(User)
#
#     WEB1 = 'W1'
#     WEB2 = 'W2'
#     WEB3 = 'W3'
#
#     WeblinkTypeChoices = (
#         (WEB1, 'WebLink1'),
#         (WEB2, 'WebLink2'),
#         (WEB3, 'WebLink3'),
#     )
#
#     type = models.CharField(max_length=2,
#                             choices=WeblinkTypeChoices,
#                             default=WEB1)
#
#     url = models.CharField(max_length=50)
#
#
# class Company(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.ForeignKey(Email)
#     address = models.ForeignKey(Address)
#     # phone = models.ForeignKey(Phone)
#     web_link = models.ForeignKey(WebLink)


# class CustomerProfile(models.Model):
#
#     CUSTOMER = 'CU'
#     PROSPECT = 'PR'
#     LEAD = 'LD'
#
#     CUSTOMER_TYPE_CHOICES = (
#         (CUSTOMER, 'Customer'),
#         (PROSPECT, 'Prospect'),
#         (LEAD, 'Lead'),
#     )
#
#     type = models.CharField(max_length=2,
#                             choices=CUSTOMER_TYPE_CHOICES,
#                             default=CUSTOMER)
#
#     contact = models.ForeignKey(Contact)
#     loyalty_id = models.CharField(max_length=50)
#     terms = models.CharField(max_length=10)

# class Employee(models.Model):
#     phone = models.For
#     address = models.ForeignKey(Address)
#
#
# class Role(models.Model):