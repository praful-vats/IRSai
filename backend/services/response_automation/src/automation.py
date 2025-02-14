def automate_response(incident):
    if incident["severity"] == "high":
        return "Triggering high-severity response!"
    return "Logging incident response."