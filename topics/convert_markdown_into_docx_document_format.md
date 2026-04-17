# Convert Markdown into DOCX(document) format

**URL:** https://community.simplicite.io/t/11462

## Question
Hello Team,

Could you please help us or suggest any predefined classes that can convert Markdown into a document format, similar to HTMLToPDFTool?

## Answer
PS:

I verified it is OK with a publication of a business object attribute of type "long text" with rendering "Markdown":

![image|690x278](upload://sY5BDMbhUJrZUou116yNRoRzcAX.png)

Publication code:

```java
package com.simplicite.objects.Application;

import com.simplicite.util.*;
import com.simplicite.util.annotations.*;
import com.simplicite.util.exceptions.*;
import com.simplicite.util.tools.*;

public class AppTest1 extends ObjectDB {
	@BusinessObjectPublication
	public Object toDocx(PrintTemplate pt) {
		String html =
			"<div style=\"font-family: sans-serif\">"
			+ MarkdownTool.toHTML(getFieldValue("appTstMarkdown"))
			+ "</div>";

		DocxTool dt = new DocxTool();
		dt.newDocument();
		dt.addHTML(html);
		return dt.toByteArray();
	}
}
```

Usage example of the above publication:
![image|690x236](upload://dcEn49DPioV3bnfPsC7Kz8E4L15.png)
The downloaded file looks like this:
![image|690x438](upload://AqfZtuOlrH8f7UJbhCF8tTRqorW.png)
