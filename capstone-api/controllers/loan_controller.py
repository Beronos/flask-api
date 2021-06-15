from models import Loan
from extensions import db


def get_loans():
    return Loan.query.all()