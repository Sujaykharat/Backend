## Backend (Flask API)

Invoke-RestMethod -Uri "http://127.0.0.1:5000/predict" `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{ "message": "You''ve won a free prize! Click here." }'

Run:
```bash
cd backend
python scam_model.py        # train if needed
python app.py               # run API
