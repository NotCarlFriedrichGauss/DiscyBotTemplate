# DiscyBotTemplate

To host your Discord bot using `discord.py` on Replit, follow these steps:

1. **Create a Replit Account**:
   If you don't have a Replit account, sign up for one at [replit.com](https://replit.com/).

2. **Create a New Replit Project**:

   - Click on the "New Repl" button.
   - Choose "Import From Github" and add "https://github.com/NotCarlFriedrichGauss/DiscyBotTemplate"
   

3. **Add Your Bot Token**:
   
   Step 1: Create a Discord Application
   
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click on "New Application" and give your application a name. This will be your bot's name.
   
   Step 2: Create a Bot User
   
   - In your application settings, click on the "Bot" section in the left sidebar.
   - Click "Add Bot" to create a new bot user for your application.
   - Make sure that you have enabled all the necessary permissions

   Step 3: Obtain the Bot Token
   
   - Under the "Token" section, you will find your bot's token. Click the "Copy" button to copy it to your clipboard.
   - Keep this token secure and never share it publicly
   - Head to "main.py", and replace `#Enter Your Bot Token Here` with your bot token.

5. **Install Required Packages**:

   Replit automatically manages dependencies using a `requirements.txt` file. Create a `requirements.txt` file in your project if it doesn't already exist and add the following line to it to install the `discord.py` library:

```bash
pip install -r requirements.txt
```


5. **Running Your Bot on Replit**:

   - In Replit, click the "Run" button to start your bot. This will install the necessary dependencies and run your bot.
   - Ensure that your bot is running without any errors.

7. **Keep Your Bot Running**:

   Replit projects stop running when you close the browser or if they're inactive for a period. To keep your bot online 24/7, you can upgrade to a paid Replit plan or use a service like [UptimeRobot](https://uptimerobot.com/) to send periodic requests to your Replit project.

8. **Inviting Your Bot to a Server**:

   As mentioned in the previous response, go to the Discord Developer Portal, create an OAuth2 URL with the "bot" scope and the necessary permissions, and invite your bot to your server.

Please note that Replit has certain limitations, and your bot may go offline if the project is not active or if it encounters heavy traffic. For more stable hosting, you might consider other cloud hosting services or self-hosting on a dedicated server or VPS.

Make sure to consult the latest Replit documentation for any specific updates or changes to their platform.

# Bot Usage

**1. `!ping` Command:**
   - **Purpose:** This is a simple custom command that allows users to check if the bot is responsive.

   - **Usage:**
     1. A user enters the command `!ping`.
     2. The bot responds with "Pong!" to indicate that it is active and responsive.

   - **Example:**
     - User: `!ping`
     - Bot: "Pong!"


**2. `!addprompt` Command:**
   - **Purpose:** This command allows users to add custom prompts and replies to the bot. A "prompt" is a keyword or phrase, and a "reply" is what the bot should say when it encounters the prompt in a message.

   - **Usage:**
     1. A user enters the command `!addprompt`.
     2. The bot responds by asking the user to enter the prompt. The user types the prompt and sends it.
     3. The bot then asks the user to enter the reply associated with the prompt. The user types the reply and sends it.
     4. The bot stores this prompt-reply pair in the `prompts_and_replies` dictionary.

   - **Example:**
     - User: `!addprompt`
     - Bot: "Please enter the prompt:"
     - User: "Hello, bot"
     - Bot: "Please enter the reply for the prompt:"
     - User: "Hi there! How can I help you?"
     - Bot: "Prompt added: 'Hello, bot' -> 'Hi there! How can I help you?'"

**3. `!editprompt` Command:**
   - **Purpose:** This command allows users to edit an existing prompt and replace it with a new one.

   - **Usage:**
     1. A user enters the command `!editprompt`.
     2. The bot responds by listing all available prompts that the user can edit.
     3. The user selects a prompt to edit.
     4. The bot asks the user to enter the new prompt.
     5. The bot updates the prompt with the new value in the `prompts_and_replies` dictionary.

   - **Example:**
     - User: `!editprompt`
     - Bot: "Here are the prompts available for editing:"
     - Bot: "1. 'Hello, bot'"
     - Bot: "2. 'Good morning'"
     - Bot: "Please enter the prompt you want to edit:"
     - User: "Good morning"
     - Bot: "Please enter the new prompt:"
     - User: "Good day"
     - Bot: "Prompt updated: 'Good morning' -> 'Good day'"

**4. `!editreply` Command:**
   - **Purpose:** This command allows users to edit the reply associated with an existing prompt.

   - **Usage:**
     1. A user enters the command `!editreply`.
     2. The bot responds by listing all available prompts that the user can edit the replies for.
     3. The user selects a prompt for which they want to edit the reply.
     4. The bot asks the user to enter the new reply.
     5. The bot updates the reply for the selected prompt in the `prompts_and_replies` dictionary.

   - **Example:**
     - User: `!editreply`
     - Bot: "Here are the prompts available for editing:"
     - Bot: "1. 'Hello, bot'"
     - Bot: "2. 'Good morning'"
     - Bot: "Please enter the prompt for which you want to edit the reply:"
     - User: "Good morning"
     - Bot: "Please enter the new reply:"
     - User: "Morning to you too!"
     - Bot: "Reply updated for 'Good morning'"



Have fun !!! :)
