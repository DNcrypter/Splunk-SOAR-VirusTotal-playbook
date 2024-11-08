
# Splunk SOAR playbook
This Lab is going to cover How we create and configure Virustotal-api app in Splunk SOAR.The motive of this lab is to reduce manual efforts and increase productivity.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/nikhil--chaudhari/)
[![Medium](https://img.shields.io/badge/Medium-Writeups-black)](https://medium.com/@nikhil-c)

## 🍁Introduction
In this Project, I will create and configure Gorman_Virustotal app that allow us to configure with Virustotal-api-key, So we can reduce efforts of searching each **Suspicious Event** manually by visiting website.

## 🍁Prequiresites
- Familiar with splunk Soar Platform
- Knowledge of Playbooks setup and App creation.

## 🍁Requirements
- RHEL 8 or later
- Vmware or Virtualbox
- Pre-installed Splunk SOAR

## 🍁Lab setup
Here, I will walk you through creating a basic App that pulls back the file report after submitting a file hash to VirusTotal, creating a simple playbook, then testing the App in an Event.

**Step 1** : Log in to Splunk **SOAR** and navigate to the Apps page. Here you can update Apps, find Apps, add Assets to Apps, etc.

But, today we are here to leverage the App Wizard to create an App. On the top right click on “APP WIZARD”.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%201.jpeg)

**Step 2** : You will be presented with a screen to enter basic App information. First you will give it a Name and Description, then some information about the Vendor and App Type.

**Step 3** : Once this is done you will upload a light themed app logo and dark themed app logo, and then click CONTINUE.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%202.jpeg)


**Note** : The App that we will create is for the VirusTotal v2 API. You can find more information about the API here: https://developers.virustotal.com/v2.0/reference/file-report.

* There are a couple of things that I want to point out before we build the App in SOAR.
* The first is VT has a Python button that you can click on under language and provides the REST call required to submit the hash and receive the json payload. 
* You will be using the requests Python library and a GET, and provide the API key, hash, and endpoint. We will use this knowledge as we build our App.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%203.jpeg)

**Step 4** : Let’s head on over back to Splunk SOAR. After hitting CONTINUE you should now see the App editor.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%204.jpeg)

**Step 5** : On the left hand side click the edit configuration details button. Here we are going to provide this app with the ability to accept an API key for connecting to VT.

**Note :** Since this is a key, you should select Password so that after this is saved it will not be in plaintext for anyone that views the Asset of the App, and make sure the Required checkbox is checked as it is needed for connecting.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%205.jpeg)

Once you click CONFIRM your Configuration Details should look something like the one below.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%206.jpeg)

-  By default each App has a “test connectivity” button. This is just to verify that you can hit the endpoint from Splunk SOAR. Here in the code you can see the function and the default endpoint is “/endpoint”.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%207.jpeg)

- If you remember, when we were looking at the API documentation, the endpoint we need is “file/report”. Let’s change that in the code.

**Step 6 : ** Now,we have to start working on the App Action for file reputation. Click on the “+” sign next to Actions.

* Here we will choose reputation for the App Category and “file reputation” for the Available Actions. When you select an Available Action it will provide a default Name, Data Type, and Description. Keep all of those the same but change the REST Endpoint from /endpoint to /file/report and click CONFIRM.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%208.jpeg)

- Your action that you just created has now been added to the code as a function with the correct endpoint.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%209.jpeg)

**Step 7 :** Scroll up until you see the Python Class with the Name of the App. Here you can see that whatever name you give the App it is assigned to the name of the Class.

**Note** : I want to point out here that I should not have put an underscore in the Name and should have used camelcase as it is best practice for the naming of a Class.

- In this Class you will want to add “self._api_key” and set that to “None”. We are going to want to retrieve this information on the left side that contains that config and we will do that in the initialize phase.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2010.jpeg)

**Step 8 :** One of the first things that is executed in the script is initialize. Let’s scroll down and find that in the code.

- We need the script to know what the endpoint is so we add that after ‘self._base_url = ‘. The next thing is having initialize point to the API Key in the config. Lets add that as well to the code.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2011.jpeg)

**Step 9 :** Now let’s work on the test connectivity action.

* By default there are certian things commented out that we would like to use. One of those is a return statement for the status if it fails, and if successful returning the message and the setting the status of success. Remove the action result for “Action not yet implemented” because we just implemented it.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2012.jpeg)

* Your test connectivity Action should now look this:

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2013.jpeg)

**Step 10 :** We are also going to want to add the paramiters that we are going to send to VirusTotal.

**Note :** Since this is just a test connectivity action I will just hard code a file hash in this function so that you don’t have to enter one every time you want to see if you can connect.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2014.jpeg)


**Step 11 :** Click on SAVE then click on PUBLISH. We are going to test out the test connectivity action that we just created.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2015.jpeg)

**Step 12 :** Find your App that you created and pivot over to Asset Settings. An Asset is just the configuration information for your App. You will need an API Key from VirusTotal. Enter it here and select TEST CONNECTIVITY.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2016.jpeg)

* If everything works as planned you should see something like the following with a “Test Connectivity Passed” message.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2017.jpeg)

**Step 13 :** Find the file reputation function in your code. Lets add the params and make sure that the resource is pulling from the hash earlier in the function. which really pulls it in from whatever the user enters or is passed.

**Step 14 :** Set **params=params** from **params=None**. Comment the last line or delete it and uncomment the action result for update summary and the return for a success. And SAVE and PUBLISH the App.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2018.jpeg)

**Step 15 :** Now we are going to test the App Action for retrieving a file’s reputation from VirusTotal. We need to first create an file hash artifact in an event. Using the menu select Sources -> Events -> + Event.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2019.jpeg)

**Step 16 :** Give the Event a name and click SAVE.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2020.jpeg)
**Step 17 :** Click on the Event that was created.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2021.jpeg)

**Step 18 :** Select the Artifacts tab. Here we can create a new file artifact by clicking on ADD ARTIFACT or by clicking on the + ARTIFACT button.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2022.jpeg)

**Step 19 :** Give the Artifact a Name, CEF Field Name, and file hash in the Value field. Click SAVE.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2023.jpeg)

**Step 20 :** Lets use the file reputation action from the new App we created on this hash. Click on the hash, Run Action, then under Investigate select “file reputation”.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2024.jpeg)

* As you can see on the left hand side in the activity pane there are a few check marks meaning it was a success. Then on the right their is a widget with a STATUS of success.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2025.jpeg)

* But where is the data that was returned? Click on the gear and select “Toggle JSON view”. Here we should be able to see the request payload.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2026.jpeg)

Now we are Sure enough in the json we can see the “total” and “positives”.

* **Total** : The “total” is the total AV engines that scanned this file.  
* **Positives** : The “positives” were the AV engines that detected this file as malicious.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2027.jpeg)

**Note :** One way that we can control what the user sees is to modify the JSON. If there are certain things that you do not define in your json, you won’t see them in your App. Click on the “EDIT JSON” button below.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2028.jpeg)

**Step 21 :** Here we are going to add the following so that the positive AV engines and total AV engines are available for us to use. Click on the check mark in the top right when done then SAVE and PUBLISH.


## 🍁Playbook creation

Let’s build a Playbook and test our changes that we made.
**Step 1:** Add an Action Block and the file reputation action from our App.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2029.jpeg)

**Step 2:** As an input for this Block select the CEF field fileHash.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2030.jpeg)

**Step 3:** Next we will want to format some of the response like the postive AV engines and the total AV engines. We will use a Format Block to make this look pretty.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2031.jpeg)

**Step 4:** We will then use a Comment Block to add this in our Activity Pane once run on the Artifact in the Event.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2032.jpeg)

So after all of that your Playbook should look something like this:

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2033.jpeg)

## 🍁Test a playbook

**Step 1:** Let’s go back to the Event and run the Playbook. Search for the Playbook then click on it to select it. Click “RUN PLAYBOOK”.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2034.jpeg)

**Step 2:** As you can see it added the new information to after the Activity that we ran.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2035.jpeg)

* But what about that Widget??? We didn’t see much unless we toggled to the json which in a way defeats the purpose. Go back into the App and edit the json. Add the following for positives and total.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2036.jpeg)

**Step 3:** Go to the Artifact in the Event, click on the fileHash, Run Action, and “file reputation”. On the next screen run this action.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2037.jpeg)

**Step 4:** Now take a look at the Widget. You can now see the positive AV engines and total. You can rename these to anything you would like.

![](https://github.com/DNcrypter/Splunk-SOAR-VirusTotal-playbook/blob/main/Images/img%2038.jpeg)

## 🍁Conclusion

Finally, We have created an App with one Action. We built a simple playbook and tested it to make sure that the Activity Pane produced some usable information for consumtion. We also tested this Artifact with some modified json to produce a Widget worth looking at. All of this is so customizable.

Hope you enjoyed this and if you want more information on the App code and how to interact with the SOAR API can be found here: https://docs.splunk.com/Documentation/SOAR/current/DevelopApps/AppDevAPIRef. Happy SOARing.
 
 If you like my project make it star in your github and also follow for upcomming content.
