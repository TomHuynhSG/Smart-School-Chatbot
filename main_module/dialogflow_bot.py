PROJECT_ID="coderschool-bot-nval"
SESSION_ID="123456789"
KEY_PATH="./coderschool-bot.json"

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=KEY_PATH

from google.cloud import dialogflow

def send_message_diagflow(input_text):
  session_client = dialogflow.SessionsClient()
  session = session_client.session_path(PROJECT_ID, SESSION_ID)

  text_input = dialogflow.TextInput(text=input_text, language_code="en-US")
  query_input = dialogflow.QueryInput(text=text_input)
  response = session_client.detect_intent(
      request={"session": session, "query_input": query_input}
  )
  #print(response)
  full_res_text=""
  for m in response.query_result.fulfillment_messages:
    full_res_text+=m.text.text[0]+" "
  return {
  "question": response.query_result.query_text,
  "intent": response.query_result.intent.display_name,
  "response": full_res_text
  }