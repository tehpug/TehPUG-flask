# encoding: utf-8
import khayyam

from app import app
import persian


@app.template_filter()
def localize_date(date):
    jalali = khayyam.JalaliDatetime.from_datetime(date).strftime(
        u'%A، %d %B %Y')
    return persian.enToPersianNumb(jalali.encode('utf-8')).decode('utf-8')
