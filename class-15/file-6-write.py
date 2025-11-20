log_message = "User logged in at 21:55\n"
with open("server_logs.txt", "x") as file:
    file.write(log_message)