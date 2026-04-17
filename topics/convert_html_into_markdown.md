# Convert HTML into Markdown

**URL:** https://community.simplicite.io/t/11514

## Question
Hello Team,

is it possible to convert Html format into Markdown format (Including  Markdown syntaxes also) using any Simplicte classes. If possible please suggest us. like HTMLTool, MarkdownTool etc…

If i use HTMLTool.toPlainMarkdownText(htmlOfDocument);

This one only print Markdown test only not syntaxes i need syntaxes because i need to get the document styles and format.

## Answer
Hello

No this is the first time someone ask us to convert HTML to Markdown, so there is no helper class to do that at that stage.

Let us check if this can be achieved using one of the already included libraries.

NB: `HTMLTool.toPlainMarkdownText` and the underlying `HTMLTool.toPlainText` are helper methods to extract raw text from a formatted document
