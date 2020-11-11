from os import name
from flask import jsonify, request
from flask_pymongo import pymongo
from app import create_app
from bson.json_util import dumps
import db_config as db

app = create_app()

secretToken = "no834fgn02wgy503"

@app.route('/test/')
def test():
    return jsonify({
        "message": "API working ok"
    })

@app.route('/api_minecraft/wiki')
def wiki():
    return jsonify({
        "wiki_url":"https://minecraft.gamepedia.com/Mob#List_of_mobs"
    })

@app.route('/api_minecraft/mobs/', methods=['GET'])
def show_mobs():
    
    mobs = list(db.db.api_minecraft.find())
    for mob in mobs:
        del mob ["_id"]

    return jsonify({"All_Mobs":mobs})
    
@app.route('/api_minecraft/mob/<string:name>/', methods=['GET'])
def show_mob(name):
    mob = db.db.api_minecraft.find_one({'name':name})
    if mob == 'null':
        return jsonify({"Mob":f"Mob {name} not found"})
    else:
        del mob ["_id"]
        return jsonify({f"Mob {name}":mob})


@app.route('/api_minecraft/new_mob/<string:tokenUser>', methods=['POST'])
def add_new_mob(tokenUser):
    if tokenUser == secretToken:
        db.db.api_minecraft.insert_one({
            "name": request.json["name"],
            "type":request.json["type"],
            "java":request.json["java"],
            "bedrock":request.json["bedrock"],
            "education":request.json["bedrock"],
            "img":request.json["img"],
            "wiki_url":request.json["wiki_url"]
        })
        return jsonify({
            "message":"A new mob wass added with success",
            "status": 200,
        })
    else:
        return jsonify({
        "message":"Incorrect token",
        "status": 700,
    })
        

@app.route('/api_minecraft/mobs/update/<string:name>/<string:tokenUser>',methods=['PUT'])
def update_mob(name, tokenUser):
    if tokenUser == secretToken:
        if db.db.api_minecraft.find_one({'name':name}):
            db.db.api_minecraft.update_one({'name':name},
            {'$set':{
                "name": request.json["name"],
                "type":request.json["type"],
                "java":request.json["java"],
                "bedrock":request.json["bedrock"],
                "education":request.json["bedrock"],
                "img":request.json["img"],
                "wiki_url":request.json["wiki_url"]
            }})
        else:
            return jsonify({"status":400, "message": f"Mob {name} not found"})
        return jsonify({"status":200, "message": f"Mob {name} was updated"})
    else:
        return jsonify({
        "message":"Incorrect token",
        "status": 700,
    })


@app.route('/api_minecraft/mobs/del/<string:name>/<string:tokenUser>',methods=['DELETE'])
def delete_mob(name, tokenUser):
    if tokenUser == secretToken:
        if db.db.api_minecraft.find_one({'name':name}):
            db.db.api_minecraft.delete_one({'name':name})
        else:
            return jsonify({"status":400, "message": f"Mob {name} not found"})
        return jsonify({"status":200, "message": f"Mob {name} was deleted"})
    else:
        return jsonify({
        "message":"Incorrect token",
        "status": 700,
    })


if __name__ == '__main__':
    app.run(load_dotenv=True, port=8080)