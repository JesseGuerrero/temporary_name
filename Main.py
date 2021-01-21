import tkinter as tk
from project_management.GithubManager import getGroupProjectRepo, countCommitsByDate

repository = getGroupProjectRepo()
group = repository.get_collaborators()

for member in group:
    if member.name != None:
        commitCount = countCommitsByDate(repository, member)
        print(member.name + " commit count: " + str(commitCount))

# Tkinter blank window
window = tk.Tk()
greeting = tk.Message(text="Greetings! You can make a GUI here.")
window.minsize(300, 300)
greeting.pack()
window.mainloop()
