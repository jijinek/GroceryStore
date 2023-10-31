from flask import Flask,request,jsonify
import jijin
from sql_connection import get_sql_connection
import uom_dao
import json


app= Flask(__name__)
connection=get_sql_connection()
@app.route('/getProducts',methods=['GET'])
def get_all_products():
    products= jijin.get_all_products(connection)
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')  
    return response

@app.route('/getUOM',methods=['GET'])
def get_uom():
    products= uom_dao.get_uoms(connection)
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')  
    return response


@app.route('/deleteProduct',methods=['POST'])
def delete_product():
    return_id=jijin.delete_product(connection,request.form['product_id'])
    response=jsonify({
        'product_id':return_id
    }
    )
    response.headers.add('Access-Control-Allow-Origin', '*')  
    return response

@app.route('/insertProduct',methods=['POST'])
def insert_product():
    request_payload=json.loads(request.form['data'])
    product_id=jijin.insert_new_product(connection,request_payload)
    response=jsonify({
        'product_id':product_id
    }
    )
    response.headers.add('Access-Control-Allow-Origin', '*')  
    return response


if __name__=="__main__":
    print("Starting python flask server for grocery management system")
    app.run(port=5000) 