HTTP Cowsay Server
GET Endpoints
/
returns a valid HTML formatted response

/cowsay
returns a generic cowpy response

/cow?msg=text
returns a cowpy response which correctly displays a default cow object including the text from your query

Example
Endpoint: /cow?msg=sometext

Response Body:

< sometext >
 -------- 
  \
   \
       ___  
     {~._.~}
      ( Y )
     ()~*~()   
     (_)-(_)
POST Endpoints
/cow?msg=VALUE
Returns JSON. The key is "content", and the value is VALUE passed through cowpy.

Example
Endpoint: /cow?msg="Things"

Response Body:

{"content": " ________ \n< Things >\n -------- \n  \\\n   \\          .\n       ___   //\n     {~._.~}// \n      ( Y )K/  \n     ()~*~()   \n     (_)-(_)   \n     Luke    \n     Sywalker\n     koala"}