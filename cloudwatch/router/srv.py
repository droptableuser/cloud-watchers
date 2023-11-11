from flask import render_template, Blueprint
from cloudwatch.models.srv import SRV

srv_page = Blueprint('srv_page',__name__,template_folder="templates")


@srv_page.context_processor
def score_bg():
    return {"score_bg": _score_bg}

def _score_bg(score):
    score = float(score)

    if 0 <= score <= 3.9:
        return ("bg-blue", "text-bg-info")
    elif 4.0 <= score <= 6.9:
        return ("bg-yellow", "text-bg-warning")
    elif 7.0 <= score <= 8.9:
        return ("bg-red", "text-bg-danger")
    else:
        return ("bg-critical", "text-bg-critical")

@srv_page.route('/srv-list')
def srv_list():
    srvs = SRV.query.all()  # Fetch all SRV records
    return render_template('list.html', srvs=srvs)

@srv_page.route('/srv/modal/<string:srv_id>')
def srv_modal(srv_id):
    srv = SRV.query.filter_by(srv_id=srv_id).first_or_404()
    return render_template('srv_modal.html', srv=srv)

@srv_page.route('/srv/<string:srv_id>')
def srv_detail(srv_id):
    srv = SRV.query.filter_by(srv_id=srv_id).first_or_404()
    return render_template('srv_detail.html', srv=srv)


