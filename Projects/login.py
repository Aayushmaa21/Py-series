
#LOGIN /LOGOUT TRACKER
active_logins = {}   
sessions      = []   # History of all completed sessions



def login(username, machine, time):

    if username in active_logins:
        print(username, "is already logged in!")
        return

    active_logins[username] = {
        "machine"   : machine,
        "login_time": time
    }

    print(username, "logged in to", machine, "at", time)

def logout(username, time):

    if username not in active_logins:
        print(username, "is not logged in!")
        return

    # Get login details here
    machine    = active_logins[username]["machine"]
    login_time = active_logins[username]["login_time"]

   
    sessions.append({
        "name"       : username,
        "machine"    : machine,
        "login_time" : login_time,
        "logout_time": time
    })

    # Remove from active
    del active_logins[username]

    print(username, "logged out of", machine, "at", time)



def view_active():

    print("\n--- Currently Active Users ---")

    if len(active_logins) == 0:
        print("No one is online.")
        return

    for user in active_logins:
        print(user, "---->", active_logins[user])



def view_all():

    print("\n--- All Session History ---")

    if len(sessions) == 0:
        print("No sessions yet.")
        return

    for session in sessions:
        print(session)



def view_user(username):

    print("\n--- History for", username, "---")

    for session in sessions:
        if session["name"] == username:
            print(session)



login("Aayushma",   "PC-01", "09:00")
login("Yuna",     "PC-02", "09:30")
login("Sohan", "PC-03", "10:00")

view_active()   
logout("Aayushma", "09:45")
logout("Yuna",   "11:00")

view_active()   

login("Aayushma", "PC-05", "12:00")
logout("Yuna", "13:00")

view_all()           
view_user("Aayushma")   