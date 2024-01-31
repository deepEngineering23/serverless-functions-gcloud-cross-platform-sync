Cross-platform serverless code GCP 

Add cert file of firebase
Handle CORS as you want.

Using Gcloud function and pushing the data to firebase RealtimeDB

Usage -> This cute little function can help build group chats and what not.

Testing -> functions-framework --target=addMessage --port=8875

Pushing to production -> gcloud functions deploy addMessage --runtime python310 --trigger-http

Tested successfully
