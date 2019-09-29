from bexar import settings
from django.db import transaction, connection
from criminal.models import Criminal, Address, Crime, Attorney
import sys


def printf(format,*args): sys.stdout.write(format%args)

CHUNK_SIZE = 10000

def delete_loop(cursor, query):
    total_deleted = 0
    while cursor.execute(query + " limit %s" % CHUNK_SIZE) > 0:
        total_deleted += CHUNK_SIZE
        printf("%s deleted %s rows: %s\n", total_deleted, CHUNK_SIZE, query)

def run():
    c = connection.cursor()
    printf("Deleting crime\n")
    delete_loop(c, "delete from criminal_crime")
    printf("deleting attorney\n")
    delete_loop(c, "delete from criminal_attorney")
    printf("deleting from criminal\n")
    delete_loop(c, "delete from criminal_criminal")
    printf("Deleting addresses\n")
    delete_loop(c, "delete from criminal_address")
     
