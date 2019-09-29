from django.db import models
# Create your models here.

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=12, null=True)
    street = models.CharField(max_length=30, db_index=True, null=True)
    state = models.CharField(max_length=4, null=True)
    city = models.CharField(max_length=24, null=True)
    unit = models.CharField(max_length=8,null=True)
    zip = models.PositiveIntegerField(db_index=True, null=True)

    def __str__(self):
        fmt = "<id=%s number=%s street=%s state=%s city=%s unit=%s zip=%s>"
        return fmt % (self.id, self.number, self.street, self.state, 
                      self.city, self.unit, self.zip)

    def __repr__(self):
        return self.__str__()


class Criminal(models.Model):
    id = models.AutoField(primary_key=True)
    sid = models.PositiveIntegerField(unique=True,null=False)
    full_name = models.CharField(max_length=42, db_index=True)
    sex = models.CharField(max_length=3, null=True)
    birthdate = models.DateField(db_index=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE,
                                   null=True)
    location = models.CharField(max_length=4, null=True)
    race = models.CharField(max_length=3, null=True)

    def __str__(self):
        fmt = "".join(["id=%s sid=%s full_name=%s sex=%s birthdate=%s ",
                      "location=%s race=%s"])
        return fmt % (self.id, self.sid, self.full_name, self.sex, 
                      self.birthdate, self.location, self.race)


class Attorney(models.Model):
    id = models.AutoField(primary_key=True)
    name = models .CharField(max_length=32, db_index=True, null=True)
    appointed_retained = models.CharField(max_length=3, null=True)
    bar_number = models.PositiveIntegerField(db_index=True, null=True)


class Crime(models.Model):
    id = models.AutoField(primary_key=True)
    cause = models.CharField(max_length=22, null=True)
    case_date = models.DateField(null=True)
    court = models.CharField(max_length=6, null=True)
    complaint_date = models.DateField(db_index=True, null=True)
    offense_date = models.DateField(db_index=True, null=True)
    court_date = models.DateField(db_index=True, null=True)
    court_type = models.CharField(max_length=3, null=True)
    offense_desc = models.CharField(max_length=32, db_index=True, null=True)
    offense_code = models.PositiveIntegerField(null=True)
    offense_type = models.CharField(max_length=4, null=True)
    court_cost = models.FloatField(null=True)
    custody_date = models.DateField(null=True)
    fine_amount = models.FloatField(null=True)
    case_desc = models.CharField(max_length=20, null=True)
    judgement_code = models.PositiveIntegerField(null=True)
    judgement_date = models.DateField(null=True)
    judgment_desc = models.CharField(max_length=20, null=True)
    judgement_number = models.PositiveIntegerField(null=True)
    disposition_code = models.PositiveIntegerField(null=True)
    disposition_date = models.DateField(null=True)
    disposition_desc = models.CharField(max_length=20, null=True)
    grand_jury_date = models.DateField(null=True)
    grand_jury_status = models.CharField(max_length=5, null=True)
    intake_prosecutor = models.CharField(max_length=32, null=True)
    outtake_prosecutor = models.CharField(max_length=32, null=True)
    revocation_prosecutor = models.CharField(max_length=32, null=True)
    probation_prosecutor = models.CharField(max_length=32, null=True)
    reduced_offense_code = models.PositiveIntegerField(null=True)
    reduced_offense_desc = models.CharField(max_length=32, null=True)
    reduced_offense_type = models.CharField(max_length=4, null=True)
    sentence = models.CharField(max_length=12, null=True)
    original_sentence = models.CharField(max_length=22, null=True)
    sentence_desc = models.CharField(max_length=25, null=True)
    sentence_start_date = models.DateField(null=True)
    sentence_end_date = models.DateField(null=True)
    setting_date = models.DateField(null=True)
    setting_type = models.CharField(max_length=3, null=True)
    post_judicial_date = models.DateField(null=True)
    post_judicial_field = models.CharField(max_length=21, null=True)
    bond_amount = models.FloatField(null=True)
    bond_date = models.DateField(null=True)
    bond_status = models.CharField(max_length=5, null=True)
    bondsman_name = models.CharField(max_length=32, db_index=True, null=True)
    

    criminal = models.ForeignKey(Criminal, on_delete=models.CASCADE,
                                 null=False)
    attorney = models.ForeignKey(Attorney, on_delete=models.CASCADE,
                                 null=True)
