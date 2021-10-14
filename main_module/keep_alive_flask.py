from flask import Flask
from threading import Thread
from flask import request

app = Flask('')


@app.route('/webhook', methods=['POST'])
def dialogflow_webhook():
  req= request.get_json(silent=True, force=True)
  query_result = req["queryResult"]
  query_text = query_result["queryText"]
  query_parameters = query_result["parameters"]
  query_intent = query_result["intent"]["displayName"]
  # print(req)
  return {"fulfillmentText": query_result["fulfillmentText"]}


@app.route('/',methods=['GET'])
def main():
    return "Your bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()