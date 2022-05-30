from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("time", __name__, url_prefix="/time")

import calendar as cal


@bp.route("/calendar")
def calendar():
    year = 2020
    month_num = 4

    month = cal.Calendar().monthdatescalendar(year, month_num)

    month_name = cal.month_name[month_num]

    return render_template(
        "time/calendar.html",
        month=month,
        month_name=month_name,
    )


class calendar:
    def __init__(year, month):
        pass

    def day_name(day):
        return cal.day_name(day)
