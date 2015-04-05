#!/usr/bin/python 

from flask import * 
from flask import url_for, request, session, redirect
from flask_oauth import OAuth

app = Flask(__name__) 
app.secret_key = "super secret"

@app.route('/')
def home(): 
	return render_template('index.html')


@app.route('/login')
def login():
	return render_template('login3.html')

@app.route('/fb_test')
def fb(): 
	data = facebook.get('/me').data
	if 'id' in data and 'name' in data: 
		user_id = data['id']
		user_name = data['name']

	return render_template('fb_test.html', id=user_id, name=user_name)


#----------------------------------------
# facebook authentication
#-------------------


FACEBOOK_APP_ID = '1626770800876369'
FACEBOOK_APP_SECRET = '34a81ae3bad388550d59284c9e2422c4'

oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': ('email, ')}
)

@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')

def pop_login_session():
    session.pop('logged_in', None)
    session.pop('facebook_token', None)

@app.route("/facebook_login")
def facebook_login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next'), _external=True))

@app.route("/facebook_authorized")
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('home')
    if resp is None or 'access_token' not in resp:
        return redirect(next_url)

    session['logged_in'] = True
    session['facebook_token'] = (resp['access_token'], '')

    return redirect(next_url)

@app.route("/logout")
def logout():
    pop_login_session()
    return redirect(url_for('home'))

# --------------------
# Personality IBM 
#--------------------


PERSONALITY_USERNAME = '80662f4f-763a-488a-9735-6a82f906fe6f'
PERSONALITY_PASSWORD = 'Ren5g0rlLWEv'

#URL: https://gateway.watsonplatform.net/personality

@app.route('/personality', methods=['GET', 'POST'])
def personality():
    if request.method == 'POST': 
        return None

    else: 
        return render_template('bio.html')

@app.route('/speech')
def speech():
    return render_template('speech.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
