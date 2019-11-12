#!/usr/bin/env python3

from flask import Flask, request, redirect, render_template
import sys
sys.path.insert(1, "PATH TO LOCAL PYTHON PACKAGES")  #OPTIONAL: Only if need to access Python packages installed on a local (non-global) directory
sys.path.insert(2, "PATH TO FLASK DIRECTORY")      #OPTIONAL: Only if you need to add the directory of your flask app

app = Flask(__name__)

@app.route('/') 
def sql_database():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'SELECT * FROM data_table'
    return render_template('sqldatabase.html', results=results, msg=msg)   
@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_datainsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        deg_min = request.form['deg_min']
        serv_id = request.form['serv_id']
        deg_max = request.form['deg_max']
        sleep_min = request.form['sleep_min']
        sleep_max = request.form['sleep_max']
        extra = request.form['extra']
        sql_edit_insert(''' INSERT INTO data_table (serv_id,deg_min,deg_max,sleep_min,sleep_max,extra) VALUES (?,?,?,?,?,?) ''', (serv_id,deg_min,deg_max,sleep_min,sleep_max,extra) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'INSERT INTO data_table (serv_id,deg_min,deg_max,sleep_min,sleep_max,extra) VALUES ('+serv_id+','+deg_min+','+deg_max+','+sleep_min+','+sleep_max+','+extra+')'
    return render_template('sqldatabase.html', results=results, msg=msg) 
@app.route('/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def sql_datadelete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        lname = request.args.get('lname')
        fname = request.args.get('fname')
        sql_delete(''' DELETE FROM data_table where serv_id = ? and deg_min = ?''', (fname,lname) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'DELETE FROM data_table WHERE serv_id = ' + fname + ' and deg_min = ' + lname
    return render_template('sqldatabase.html', results=results, msg=msg)
@app.route('/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_editlink():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
        elname = request.args.get('elname')
        efname = request.args.get('efname')
        eresults = sql_query2(''' SELECT * FROM data_table where serv_id = ? and deg_min = ?''', (efname,elname))
    results = sql_query(''' SELECT * FROM data_table''')
    return render_template('sqldatabase.html', eresults=eresults, results=results)
@app.route('/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_dataedit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        old_deg_min = request.form['old_deg_min']
        old_serv_id = request.form['old_serv_id']
        deg_min = request.form['deg_min']
        serv_id = request.form['serv_id']
        deg_max = request.form['deg_max']
        sleep_min = request.form['sleep_min']
        sleep_max = request.form['sleep_max']
        extra = request.form['extra']
        sql_edit_insert(''' UPDATE data_table set serv_id=?,deg_min=?,deg_max=?,sleep_min=?,sleep_max=?,extra=? WHERE serv_id=? and deg_min=? ''', (serv_id,deg_min,deg_max,sleep_min,sleep_max,extra,old_serv_id,old_deg_min) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'UPDATE data_table set serv_id = ' + serv_id + ', deg_min = ' + deg_min + ', deg_max = ' + deg_max + ', sleep_min = ' + sleep_min + ', sleep_max = ' + sleep_max + ', extra = ' + extra + ' WHERE serv_id = ' + old_serv_id + ' and deg_min = ' + old_deg_min
    return render_template('sqldatabase.html', results=results, msg=msg)

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")

