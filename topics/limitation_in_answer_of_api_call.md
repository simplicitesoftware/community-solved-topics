# Limitation in answer of API call

**URL:** https://community.simplicite.io/t/8898

## Question
### Request description

Hello, we are currently facing an issue where we have an answer to an API through a POST call on Simplicité and we are encountering a limitation of 1 million characters. Is there any limitation on Simplicité side and if so is it possible to increase the maximum characters limit or should we look on our side ?

Thank you in advance.

Thomas

## Answer
[quote="scampano, post:5, topic:8898"]
Can you please provide the code used to make the request so I can check wether the limitation could be coming from one of our tools, one of the underlying libraries, the tomcat server, etc.
[/quote]

I might have misunderstood that you were asking about a call FROM a Simplicité instance, but you're talking about an API call TO a Simplicité instance, right? In that case, I don't need the code. 

Just to make sure I understand right:
- some app calls POST a Mapped REST service (`/enterprise-repositories-alliance-suppliers/v1/bvd-interface` of a Simplicité instance)
- this instance must
    - store the content you send in the database
    - answer with the created record
- the cut result you mention is what you see in the `result` field?
- could the limit be the column size in the DB, or is the data OK there?

As far as we know, there is no set limit. If there is a problem, like an OutOfMemoryException, you should see something in the Simplicité logs.

Could you provide additional information so I can try to reproduce your case?
