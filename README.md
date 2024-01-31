Cross-platform serverless code GCP 

Using Gcloud function and pushing the data to firebase RealtimeDB

Usage -> This cute little function can help build group chats and what not.

Testing -> functions-framework --target=addMessage --port=8875

Pushing to production -> gcloud functions deploy addMessage --runtime python310 --trigger-http
