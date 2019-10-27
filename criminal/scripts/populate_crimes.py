
from bexar import settings
from django.db import transaction
from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from criminal.models import Criminal, Address, Crime, Attorney
import sqlalchemy
import sqlalchemy.orm
import time
import sys


def printf(format,*args): sys.stdout.write(format%args)

Base = declarative_base()

def get_engine(conf_file="/etc/bexar.yaml"):
    conf = settings.load_yaml(conf_file)
    engine = sqlalchemy.create_engine(conf["SQLALCHEMY"], pool_recycle=60)
    return engine



def attach_engine(engine):
    Session.configure(bind=engine)


Session = sqlalchemy.orm.sessionmaker()

CHUNK_SIZE = 10000

# This is the bexar court table via SQL alchemy this is not the django
# Database

def t(str_or_none):
    if str_or_none:
        return str_or_none.strip()

class Court(Base):
    __tablename__ = 'court'
    id = Column(Integer, primary_key=True)
    addr_city = Column(String(24))
    addr_house_nbr = Column(String(12))
    addr_post_direction = Column(String(4))
    addr_pre_direction = Column(String(4))
    addr_state = Column(String(4))
    addr_street = Column(String(24))
    addr_street_suffix = Column(String(6))
    addr_unit = Column(String(8))
    addr_zip_code = Column(Integer)
    addr_zip_plus_4 = Column(Integer)
    alias = Column(String(3))
    attorney = Column(String(32))
    attorney_appointed_retained = Column(String(3))
    attorney_bar_nbr = Column(Integer)
    birthdate = Column(Date)
    bond_amount = Column(Float)
    bond_date = Column(Date)
    bond_status = Column(String(5))
    bondsman_name = Column(String(32))
    case_cause_nbr = Column(String(22))
    case_date = Column(Date)
    case_desc = Column(String(20))
    complaint_date = Column(Date)
    court = Column(String(6))
    court_costs = Column(Float)
    court_type = Column(String(4))
    custody_date = Column(Date)
    disposition_code = Column(Integer)
    disposition_date = Column(Date)
    disposition_desc = Column(String(20))
    filing_agency_description = Column(String(42))
    fine_amount = Column(Float)
    full_name = Column(String(42))
    g_jury_date = Column(Date)
    g_jury_status = Column(String(5))
    house_suf = Column(String(3))
    intake_prosecutor = Column(String(32))
    judgement_code = Column(Integer)
    judgement_date = Column(Date)
    judgement_desc = Column(String(20))
    judicial_nbr = Column(Integer)
    location = Column(String(5))
    offense_code = Column(Integer)
    offense_date = Column(Date)
    offense_desc = Column(String(32))
    offense_type = Column(String(4))
    original_sentence = Column(String(22))
    outtake_prosecutor = Column(String(32))
    post_judicial_date = Column(Date)
    post_judicial_field = Column(String(21))
    probation_prosecutor = Column(String(32))
    race = Column(String(3))
    reduced_offense_code = Column(Integer)
    reduced_offense_desc = Column(String(32))
    reduced_offense_type = Column(String(4))
    revokation_prosecutor = Column(String(32))
    sentence = Column(String(12))
    sentence_desc = Column(String(25))
    sentence_end_date = Column(Date)
    sentence_start_date = Column(Date)
    setting_date = Column(Date)
    setting_type = Column(String(3))
    sex = Column(String(3))
    sid = Column(Integer)


def run():
    engine = get_engine()
    attach_engine(engine)
    transaction.commit()
    transaction.set_autocommit(False)
    s = Session()
    sids = {}
    attorney = {}
    total_rows = 0
    i = 0
    start_time = time.time()
    for c in s.query(Court).yield_per(CHUNK_SIZE):
        i += 1
        total_rows += 1
        if i >= CHUNK_SIZE:
            transaction.commit()
            stop_time = time.time()
            elapsed_time = stop_time - start_time
            fmt = "commiting %d rows total_rows = %s  done in %s secs\n"
            printf(fmt, CHUNK_SIZE, total_rows, elapsed_time)
            start_time = stop_time
            i = 0

        #Build criminal
        if c.sid not in sids:
            cr = Criminal()
            sids[c.sid] = cr
            cr.sid = c.sid
            cr.full_name = t(c.full_name)
            cr.sex = t(c.sex)
            cr.birthdate = c.birthdate
            cr.location = t(c.location)
            cr.race = t(c.race)

            #Build Address table
            a = Address()
            a.number = t(c.addr_house_nbr)
            a.street = t(c.addr_street)
            a.state = t(c.addr_state)
            a.city = t(c.addr_city)
            a.unit = t(c.addr_unit)
            a.zip = c.addr_zip_code
            a.save()
            cr.address = a
            cr.save()
        cr = sids[c.sid]
        # build crime table
        of = Crime() # Offense
        of.criminal = cr 
        of.cause = c.case_cause_nbr
        of.case_date = c.case_date
        of.court = c.court
        of.complaint_date = c.complaint_date
        of.offense_date = c.offense_date
        of.court_date = c.case_date
        of.court_type = c.court_type
        of.offense_desc = c.offense_desc
        of.offense_code = c.offense_code
        of.offense_type = c.offense_type
        of.court_cost = c.court_costs
        of.custody_date = c.custody_date
        of.fine_amount = c.fine_amount
        of.case_desc = c.case_desc
        of.judgment_code = c.judgement_code
        of.judgement_date = c.judgement_date
        of.judgement_number = c.judicial_nbr
        of.disposition_date = c.disposition_date
        of.disposition_code = c.disposition_code
        of.disposition_desc = c.disposition_desc
        of.grand_jury_date = c.g_jury_date
        of.grand_jury_status = c.g_jury_status
        of.intake_prosecutor = c.intake_prosecutor
        of.outtake_prosecutor = c.outtake_prosecutor
        of.revocation_prosecutor = c.revokation_prosecutor
        of.probation_prosecutor = c.probation_prosecutor
        of.reduced_offense_code = c.reduced_offense_code
        of.reduced_offense_desc = c.reduced_offense_desc
        of.reduced_offense_type = c.reduced_offense_type
        of.sentence = c.sentence
        of.original_sentence = c.original_sentence
        of.sentence_desc = c.sentence_desc
        of.sentence_start_date = c.sentence_start_date
        of.sentence_end_date = c.sentence_end_date
        of.setting_date = c.setting_date
        of.setting_type = c.setting_type
        of.post_judicial_date = c.post_judicial_date
        of.post_judicial_field = c.post_judicial_field

        # Link attorney
        try:
            key = c.attorney_bar_nbr
        except ValueError:
            key = c.attorney
        if key not in attorney:
            at = Attorney()
            at.name = c.attorney
            at.appointed_retained = c.attorney_appointed_retained
            at.bar_number = c.attorney_bar_nbr
            at.save()
            attorney[key] = at
            of.attorney = at
        else:
            of.attorney = attorney[key]

        of.bond_amount = c.bond_amount
        of.bond_date = c.bond_date
        of.bond_status = c.bond_status
        of.bondsman_name = c.bondsman_name

        of.save()
    transaction.commit()
