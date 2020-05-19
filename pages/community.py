from flask import jsonify, render_template, request, Response, redirect
from flask.ext.login import current_user
from sqlalchemy import desc

from functions import app
from models import User


@app.route('/community', methods=['GET'])
def community():

  if current_user.is_authenticated():
    users = User.query.order_by(desc(User.signup_date)).limit(5).all()

    args = {
        'gift_card_eligible': True,
        'cashout_ok': True,
        'user_below_silver': current_user.is_below_tier('Silver'),
        'users': users
    }

    return render_template("community.html", **args)
  else:
    return redirect("/")
