***Test ABACO LATAM***

---> ADECOTESTGUILLERMO
    ---> adecotestguillermo
        ---> __pycache__
        ---> __init__.py
        ---> asgi.py
        ---> settings.py
        ---> urls.py
        ---> wsgi.py
    ---> guilletes
        ---> __pycache__
        ---> migrations
        ---> static
            ---> css
                ---> styles.css
            ---> js
                ---> scripts.js
    ---> templates
        ---> home-scraping.html
        ---> home.html
        ---> login.html
        ---> other-user.html
        ---> register.html
        ---> scraping.history.html
    ---> __init__.py
    ---> admin.py
    ---> apps.py
    ---> forms.py
    ---> models.py
    ---> scraping.py
    ---> tests.py
    ---> views.py
---> .README
---> db.sqlite3
---> manage.py

# Data structure from scraping.py process def outputs:

output_list = [{
   'Song_Artis': 'song and artist data...',
   'Tag': 'data tags...'
}, {}, {}, ....]

data_followings_json = {
    'Genders': 'genders by user'
}

reliability = #Number
elapsed_time_formatted = #Number
reg_count_aux = #Number

# How to execute this application:

Step 01:
 Make git clone: git@github.com:guille1989/abaco.git

Step 02:
 Make CD to project folder /abaco

Step 03:
 Open terminal, run command: python manage.py runserver    #Make sure you have pytgon installed.

Step 04:
 Test the web application !


