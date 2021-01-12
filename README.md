# About Group project
If you start on the projects below I can make them interact with each other. Above in the repository there are modules where you can run each project/app. 

<h3>Update the website to the latest code</h3>
I can do this for you every time there is an update. It will be good practice for you to learn to do this as well. I use a Linux library called "Screen" to run apps in the background on Ubuntu. To update the private server go into your SSH: 
<ol>
  <li>"ssh [username]@144.91.84.171"</li>
  <li>go into directory "/home/group_project/temporary_name</li>
  <li>Type "sudo git pull origin master", you should see updates, if there are errors let me know and ill fix it</li> 
  <li>Next, Enter "screen -ls" to list current screens</li>
  <li>Find the ID of the screen labeled "flask" or "group_project"</li>
  <li>Enter "screen -R [Screen ID]" to resume a seperate window/screen by ID</li>
  <li>Shut down the website with CTRL+C and run "python3 app.py" in the flask app folder</li>
  <li>Use "CTRL+A" keep holding CTRL, let go of "A" and push "D". It will exit the screen and the website will still be running</li>
  <li>You should see the updates at the ip</li>
</ol>
<h3>Libraries/APIs</h3>
<ul>
<li>Bitcoin API: https://bitcoincharts.com/about/markets-api/ </li>
<li>Flask: https://flask.palletsprojects.com/en/1.1.x/ </li>
<li>Send e-mail in Python: https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/</li>
<li>Chatbot library: https://www.coursera.org/projects/chatbot-rasa-python</li>
<li>PyGame: https://www.pygame.org/news</li>
</ul> 
<br>
<h3>Project ideas</h3>
<ul>
<li>Simple email notifier in Flask</li>
<li>Mock blog application in Flask</li>
<li>2D life sim in PyGame, we could make the game a bitcoin, stock and life simulator</li>
<li>Bitcoin history tracker with a chart Api</li>
 <li>Customer service bot using Rasa</li>
</ul>

<h3>Contributors</h3>
-Jesus A. Guerrero <br>
-Sabari Manikandan <br>
-Vibin Mathew
