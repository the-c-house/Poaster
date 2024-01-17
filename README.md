# Poaster
POAAASSTINNGGG assistance

This is a writing assistant for David Hogg specifically. It generates outlines and text for you to post on twitter, substack, etc. It's a simple frontend that you can upload your documents to, and then you can talk to the bot about what you're looking for. It will generate an outline for you, and then you can ask it to write it for you. It will also rank the outlines/text/tweets for you.

## Requirements
-Python
-Streamlit for frontend
-sqlite3 for database
-Simple frontend that can do:
    -upload your documents (pdfs, website links, paste in text, etc)
        -encode their documents into vector database or summarization or both?
    -you can talk to the bot about what you're looking for
        -button for presets for substack, twitter, add more later
    -one text prompt 1:1 command to get a proposed outline, and then asks if you like the outline, and then it writes it for you
        -if you don't like the outline, you can ask for another one
        -if you like the outline, you can ask for it to write it for you
    -ranking system for the outlines/text/tweets

    -easy way to read the generated text

-TODO: internal evaluation of real vs. generated text

client side data
    -user text (request for stuff to write)

-database
    -user documents, user links, user pdfs, user tweets, user name, openai api key
    -dictionary keyid, parsed text, uri

-writing accuracy validation agent (verify based on references what has been written, is it correct?)
-agent for writing substack
    -web search function
    -we need longform writing from him/transcripts
-agent for writing twitter
    -web search function
    -old twitter posts (manual I guess)


OPENAI Assisstants API:
    -write in the style of david hogg based on uploade documents

    

    