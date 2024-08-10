# Buck the Duck
Get to know Buck, your duckling companion that will help you use generating AI and make your commits more meaningful without any interaction at all.

Buck knows to read your recent changes before you commit them and helps you with your less important day-to-day tasks to improve maintenance of your project.
Buck knows to read only the files you want it to read, Buck is not nosey it will only read the classes & methods* without the content to keep the exposure to the minimum (* only React files will be sent fully)

Buck today knows - Python, NodeJS (+Typescript), but it can get around other languages (but see * above)

Buck knows to integrate today with OpenAI ChatGPT and Google Gemini and knows to use them both in case your tokens run out!
## Installation
`pip install BuckTheDuck`

## Getting started
1. Get a token from either [OpenAI](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) or [Gemini](https://ai.google.dev/gemini-api/docs/api-key) 
2. Run `buck init`
   1. Choose the Gen AI you wish to use and add the API key - Don't worry it is only being saved on your machine.
   2. You can set both OpenAI and Gemini as your Generative AI if you with to have a fallback by running the init again
3. Run `buck help` to see the manu
4. GA features are 
   1. `buck commit` - will automatically generate commit message on your changes
      1. `buck commit -c` - will open a conversation with the generative AI to be able to give feedback to it 
   2. `buck cop` - commit and push, will also create the branch at the remote if necessary
5. Beta features
   1. `buck cr` - Will try to help you with code review on your changes
   2. `buck branch_summarize` - Will generate a summary of the current changes, currently only will be written to the prompt

## Authors and acknowledgment
Yoav Alroy as sole Author

## License
MIT License

## Project status
The backlog is rich, any that wish to assist may contact me at yoavalro@gmail.com
