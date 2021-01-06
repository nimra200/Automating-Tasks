# Getting-Started-with-APIs

This mini-project served as an introduction to using APIs in Python. 

The [Datamuse API](https://www.datamuse.com/api/) lets developers find English words that may be useful in a given context.

This program asks the user to input a word, and returns a few words commonly associated with it.
When the given word is a noun, the most common adjectives describing the noun are also given. 

### Key concepts learned in this project:

1. An API can be used in any programming language. It allows us to access tons of data and useful functions; we can use these functions in our own programs without worrying about how they were implemented. 

2. We can **request** the API for information. In this project, we needed a 'GET' request to retrieve data from a URL. 

3. The response of a request is formatted in JSON. For example, when we request the most common adjectives for a noun, JSON formats the data nicely for us, and the information becomes human-readable. 

4. All requests have a status code. The status code '200' tells us that everything was successful. A status code starting with '4' or '5' means something went wrong. A common example of this is '404 error: file not found'. 

### Resources
[Prashanth Xavier](https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236) and [Josh Devlin](https://www.dataquest.io/blog/python-api-tutorial/) have made incredibly helpful tutorials on getting started with APIs in Python. 
