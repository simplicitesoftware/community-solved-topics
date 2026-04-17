# Need A UI design in Simplicite tool , where they look like AI forums like Copilot, Chat GPT

**URL:** https://community.simplicite.io/t/11348

## Question
### **Title**

Need Support for Designing a ChatGPT / Copilot-like Responsive UI (Web) using Simplicite tool

---

### **Description**

Hi Community,

I am looking for guidance, references, or reusable templates to design a **modern conversational UI** similar to **ChatGPT** or **GitHub Copilot Chat**.

The requirement is to build a **fully responsive UI interface page using Simplicite tool** that supports an AI/chat-based interaction pattern with a clean and minimal user experience.

---

### **Key UI Requirements**

* **Chat-style layout**

  * User messages on the right

  * Assistant/system messages on the left

* **Scrollable conversation panel**

* **Fixed input area** at the bottom with:

  * Text input

  * Send button

  * Optional attachment icon

* **Typing indicator / loading state**

* **Support for long responses** (code blocks, formatted text)

---

### **Functional Expectations (UI Only)**

* Frontend UI only (backend/AI integration will be handled separately)

* Component-based design preferred

* Should be easy to integrate with APIs later

---

### **Preferred Tech Stack (Open to suggestions)**

* HTML / CSS / JavaScript

* OR React / Angular / Vue

---

### **What I’m Looking For**

* Open-source **UI templates**

* GitHub repositories

* Design systems or Figma files

* Best practices for conversational UI

* Sample implementations similar to ChatGPT or Copilot

---

### **Any references, examples, or suggestions would be highly appreciated.**

Thanks in advance!

---

## 🔹 Short Version (If Forum Needs Concise Post)

> Looking for references or templates to design a **ChatGPT / Copilot-like responsive chat UI** for a web application.
> Need suggestions for **open-source templates, GitHub repos, or Figma designs** that support chat layout, fixed input bar, scrolling messages, dark/light mode, and responsive behavior.

---

> *The UI should be adaptable to enterprise applications and support extensibility.*

## Answer
Hello,

I don't think the standard "Social posts" widget could be used, at that stage, to that purpose => it would require some changes to be more customizable.

So at that stage I think you will need to implement a custom UI component (a "responsive UI external object" in Simplicité vocabulary) such as the one present in the "Demo AI integration" module of the app store:

![image|518x499, 50%](upload://aCZzM1eo9nucytlkNsJZgrkIHW3.png)

In this module the "chatbot" widget is displayed embedded on the home page, as a full page or in a popup:

![image|650x500](upload://3QpWHDP2c911US2XxTF0A0VjGrU.png)

I think you can take this as an inspiration for what you need to implement

@Candice is in charge of this module and can help you if needed
