import flask
from flask import Flask, request, url_for, redirect, render_template
import pandas as pd
from load_ml_model.con_fil import content_filtering

cf = content_filtering()

app = Flask(__name__, template_folder='templates')

app.static_folder = 'static'

main_df = pd.read_csv('c:/Users/naray/OneDrive/Desktop/content/Travel-Itinerary-Recommendation-Engine-master/Datasets/complete_all_data.csv')

print(main_df.columns)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/form", methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        user_ip = flask.request.form
        user_ip = user_ip.to_dict(flat=False)
        user_ip = pd.DataFrame.from_dict(user_ip, orient='index')
        user_ip = user_ip.transpose()
        user_ip = user_ip.reset_index(drop=True)
        user_ip['Name'] = user_ip['Name'].fillna(user_ip['Name'].values[0])
        user_ip['State'] = user_ip['State'].fillna(user_ip['State'].values[0])
        user_ip['Budget'] = user_ip['Budget'].fillna(user_ip['Budget']).values[0]
        user_ip['n_days'] = user_ip['n_days'].fillna(user_ip['n_days'].values[0])
        print(user_ip)
        # print(user_ip['Name'], user_ip.columns)
        # call function to return value
        recom_model = cf.cnt_flt(user_ip, main_df)
        print(recom_model)
        if(user_ip['Name'].values[0] !=None):
            return render_template('results.html', state=user_ip['State'].values[0], name=user_ip['Name'].values[0], tables=recom_model, other_recom=recom_model['other_recomms'].values[0])
        else:
            return ('Please choose an option')

# @app.route('/plot', methods=['GET', 'POST'])
# def plot():
#     return render_template('plot.html')



if __name__ == "__main__":
    app.run(debug=True)