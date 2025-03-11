# how to install
1. Clone the repo
2. Install dependencies
3. Run the Flask server

step1:-
#pip3 install -r requirments.txt

#step2

python3 apps.py

To add user
curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d '{"type":"Admin", "full_name":"John Doe1", "username":"john123", "email":"john@example1.com", "password":"pass", "submitted_by":"admin"}'

to find user
curl http://127.0.0.1:5000/users

so on for other end points

