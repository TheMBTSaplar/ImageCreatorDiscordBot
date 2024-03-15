# Image Creator Discord Bot
This code will help you for making a image generator bot for Discord using OpenAI API.

**How To Use?**

To use this code, you need a token for your Discord bot and API key from OpenAI. And of course you need an IDE for code. I recommend Visual Studio Code for you.

**Step 1: Creating A Bot in Discord**

First of all, you need to create an application for your bot. For this, visit [Discord Developer Portal Webpage](https://discord.com/developers/applications).

![Screenshot_20240314_232139](https://github.com/TheMBTSaplar/ImageCreatorDiscordBot-/assets/98463524/be9edfd8-0bdf-4d90-b69e-09fda5680fee)

In this screen, you need to click to "New Application" button.

![Screenshot_20240314_232122](https://github.com/TheMBTSaplar/ImageCreatorDiscordBot-/assets/98463524/e5b01e8f-6103-415a-95ab-3fcf75a25f6c)

In this screen give a name to your app. I will use "AiImageCreator".

Then you click to "Create", this screen will come out.

![Screenshot_20240314_233203](https://github.com/TheMBTSaplar/ImageCreatorDiscordBot-/assets/98463524/22dbd6b1-2436-4100-8306-f9327f3374ca)

There's some informations and customisations for our app. And remember, don't share your app id to someone. Because If you lose your application ID, your application may serve malicious purposes.

Here, press the three-lined button in the upper left corner of the screen. (I cut the three-lined button on the previous image accidentally. Sorry for that.)

![Screenshot_20240314_233559](https://github.com/TheMBTSaplar/ImageCreatorDiscordBot-/assets/98463524/628d1512-478f-4d00-a378-624de2d44cdf)

In here, press the "Bot" button to open your bot options.

![Screenshot_20240314_234213](https://github.com/TheMBTSaplar/ImageCreatorDiscordBot-/assets/98463524/6e2a7da9-a062-4e56-9672-b8dd37d09970)

So, In there, click the "Reset Token" button to reset your bot token. When you reset it, it will give you a token for your bot. Copy that and save it to anywhere safe. If someone get your token, it can use your bot for his childish things. 

Then, there's some options in the blue box. You need to check these intents. When you do that, click three-lined button again and click to "OAuth2".

![Screenshot_20240315_085227](https://github.com/TheMBTSaplar/ImageCreatorDiscordBot-/assets/98463524/f103e03c-7734-44c5-bfb3-780e512d71bc)

In here, you need to select some permissions for your bot. You can do how i did it. Then, choose "bot" and "application.commands" in OAuth2 URL Generator area. 

When its done, At the bottom there is a box with a link. This is your bot's invitation link. Invite your bot to your server by copying this and opening it in a new tab.


**Step 2: Get the Open AI API**

Visit [OpenAI's website](https://platform.openai.com/docs/overview). Press the three-lined button in the upper right corner of the screen. Then click "API".

![Screenshot_20240315_210110](https://github.com/TheMBTSaplar/ImageCreatorDiscordBot-/assets/98463524/31f6640d-af1a-4ada-bbec-053791809e39)

In this screen, click "Create new secret key" and copy it. And thats all for this step.

**Step 3: Configure Your Bot**

Download and open "imagegeneratecode.py" and change 'Your_Discord_Bot_Token' with your Discord bot token, 'Your_Openai_Api_Key' with your OpenAI API key. When you done, run the code and try your bot.


