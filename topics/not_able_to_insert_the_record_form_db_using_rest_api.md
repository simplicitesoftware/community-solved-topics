# Not able to insert the Record form DB using Rest API

**URL:** https://community.simplicite.io/t/10387

## Question
Hello Team,
       We are trying to insert a record into the database using an external REST service, but we are getting below mentioned error.


Error message:   “2025-07-11 08:25:40,891|SIMPLICITE|ERROR||:20058||ECORED0001|system|com.simplicite.util.ObjectDB|getField||Error Object ObjectDB: unknown field trnSimpliciteDemoFeedBack.”

![image|690x376](upload://9hO5sbRf9bhqLwLdwBO3bETv0oJ.png)


Please help for what i missed the mapping column's.

## Answer
The parameters in your `getObject` method are the wrong way around. The javadoc specifies : `getObject(String instance, String name)` : https://platform.simplicite.io/6.2/javadoc/com/simplicite/util/Grant.html#getObject(java.lang.String,java.lang.String), in your case : `getObject(null, "TrnSimpliciteDemo");`

We highly recommend you follow the platform's best practices for object manipulation :
* There is an example of a custom REST service in the tutorial : https://docs.simplicite.io/tutorial/enhancing/external-object/
* And other examples here : https://docs.simplicite.io/docs/core/objects/businessobject-code-hooks
