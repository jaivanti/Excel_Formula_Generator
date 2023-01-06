![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)
![Javascript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
# Natural Language Excel Formula Generator
Describe a formula in Natural Language Input and get a excel formula Output

![](https://github.com/jaivanti/Excel_Formula_Gen/blob/master/media/Excel_Formula.gif)

## Description
Describe a formula in natural Language and it will generate it for you.  From simple stuff that’s easier to describe than type out, to harder things incorporating regex, formulas based on contextual info, and sometimes stuff using functions you didn’t even know existed. This tool is backed by OpenAI Text-Davinci-003 model to generate better excel formula based on responses in realtime irrespective of pattern you write the formula in.
Currently, the tool is still in development mode, still working to develop in a better UI and maybe as a excel add-in.

##Run Commands
* Download the above code locally
* Open the terminal, navigate to the code folder - ```src\taskpane``` and run the FastAPI by the below command.
```bash
py -3 app.py
```
* Open the other terminal, again navigate to the ```src\taskpane``` and run the below command for the HTTP server hosting at 3000 port.
```bash
py -3 -m http.server 3000
```
* Once followed above steps, The UI will be running on ```  http://127.0.0.1:3000 ``` url.
* Also, make sure you put your OpenAI API key in the ```app.py``` code in ``` src\taskpane ```


## Technology stack

Tools and technologies used:

1. FastAPI
2. OpenAI GPT model - Text Davinci -003
3. HTML/CSS
4. Javascript
5. Python - Flask
6. Yeoman Generator for Office add-ins
7. NLP
