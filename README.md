# About group project
If you start on the projects below I can make them interact with each other. Above in the repository there are modules where you can run each project/app. 

<h3>Obtain code for an API using Postman</h3>
There is no need to write your own code in every language when working with APIs. Postman does it for you. Here is an example of what information looks like from an API(This is a history of Bitcoin transactions):<img src = "https://i.gyazo.com/4edc446fcac5db03035e80d487deb154.png"><br><br>

Postman automatically makes code : <img src="https://i.gyazo.com/2e139510a8cc5ec826d49a0f58656fe8.png">

Here is an example Youtube tutorial, there are better ones out there though: https://youtu.be/t5n07Ybz7yI

<h3>Update the website to the latest code</h3>
I can do this for you every time there is an update. It will be good practice for you to learn to do this as well. With Ubuntu Service there are less steps to starting, checking and stopping the web server but it comes with a caveat. You have to check the website feedback separately. To update the private server go into your SSH: 
<ol>
  <li>"ssh [username]@144.91.84.171"</li>
  <li>go into directory "/home/group_project/temporary_name</li>
  <li>Type "sudo git pull origin master", you should see updates, if there are errors let me know and ill fix it</li> 
  <li>Next, Enter "sudo systemctl restart group_project" to restart the website with updates from github.</li>
  <li>You should see the updates at the ip</li>
</ol>
To see the server console feed back you have to stop the service and run the flask app with "python3 app.py" in the flask_apps directory.<br><br>

Service commands:<br>
sudo systemctl start group_project<br>
sudo systemctl restart group_project<br>
sudo systemctl stop group_project(Here is where you stop it then run app.py on its own to see debug info)<br>
sudo systemctl status group_project

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
<li>Bitcoin history tracker with a chart Api(2nd derivative)</li>
 <li>Customer service bot using Rasa</li>
</ul>

<h3>Contributors</h3>
-Jesus A. Guerrero <br>
-Sabari Manikandan <br>
-Vibin Mathew <br>
-Nishank Vyas <br>
