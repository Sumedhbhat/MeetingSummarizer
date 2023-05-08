from transformers import pipeline, BartTokenizerFast, EncoderDecoderModel
import torch
from nltk import tokenize
import openai

# Insert your OpenAI API Key here

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

# Function to split the paragraph into sentences


def split_sentences(text):
    return tokenize.sent_tokenize(text)

# Function to merge the two texts extracted


def merge_text(text_1, text_2):
    print("In merger data")
    text = text_1 + text_2
    res = ''
    res = res.join(text)
    return res


text1 = """
Welcome. Let's get started with Lesson 1. Lesson 1's objectives are to ultimately understand first what managerial accounting is, second, why it's important, and third, introduce some contemporary issues related to this topic.
So first off, what is managerial accounting? Well, it's a very difficult concept to summarize in a single sentence. So in a very unsatisfying book definition is the following: It's the process of obtaining, creating, and analyzing relevant information to help achieve organizational goals. As we work through these slides, we'll delve into the certain -- the specific concepts that are embedded inside this definition. 
So first off, some common conceptions about accounting. When I tell people that I teach accounting, one of the first things they say to me is, "Oh, you can help me with my taxes." Well, truth be told, I'm very far from a tax expert. But there is some interrelationships between taxes and managerial accounting, and we'll see a little bit of that in the future modules, but a tax course this is not. Another common conception is that people think of financial accounting, specifically financial statements. Oh, I remember accounting. It's journal entries, debits and credits and account balances, the balance sheet, the income statement, the statement of cash flows. Well, let's explore this concept a little bit more and think about who uses the financial statements of a firm.
So first off, we can think of an organization, and just so it's easy to envision, let's think about a publicly traded global corporation. That organization is very large, and so oftentimes the owners of that organization lie outside of the organization. Those people, the investors, and people thinking about becoming owners, or potential investors, are very interested in what the content of financial statements are. Similarly, in a different type op relationship, there's banks, financial institutions and other individuals who are entering into a debt relationship with the organization.   
So creditors and those parties thinking about becoming creditors to the firm or the organization also would be interested in the financial statements. Because of the nature of the relationship between investors and the organization and creditors in the organization, the financial statement information that the organization provides is crucial to the decisions made by each of these parties. Another user is tax authorities, and for certainty, no matter what country you live in, the financial statement information is going to be of interest to the tax authorities. I want to make sure that they are paying the appropriate amount of taxes. Now, oftentimes in many countries, the information that's interesting to tax authorities is different than the information that's interesting to investors and creditors and other users. But in many countries, the financial statement information is a precursor or a building block to the tax information that's provided to those authorities. In many industries, regulatory agencies are of interest in the -- are interested in the financial statement information. In the United States, there is the Securities and Exchange Commission who is responsible for insuring that the information provided by the organization is a fair representation of the firm and its financial position.  
Other industries involve other regulatory agencies. Partners of the organization are also interested in financial statement users. Suppliers, customers, and other partners oftentimes engage in formal and informal contracts with the organization and they want to know what the financial position of the firm is, is this a good partner for me. Financial statement information, along with other information, is useful to those parties as well. And finally, you can think of the organization's competitors. Financial statement information is a useful benchmark against which competitors can assess their own performance. They might also use financial statement information to elicit competitive advantages over the organization.
Now, all these users who lie outside of the organization, financial statement information is very useful to them. In this course, however, we're not going to focus on the outside users. We're focusing on those users inside of the organization, the managers and employees who are making decisions that help the organization try to achieve its goals.
"""

text2 = """
In this exercise, we're going to explore Bootstrap's tab-based navigation, Bootstrap's support for tabs, and how tabs can be used to organize content on your web page. 
And how you can navigate from one tab to another tab, and then reveal content in each of those tabs in web page. 
Now, you will here see me using the nav class, and then further qualify it using the nav tabs class. 
The same approach can be also used with the nav pills that we looked at in the previous lecture. 
To get started with this exercise, we will go into aboutus.html page. 
And then right there, where we have the corporate leadership content there, after the h2, I'm going to introduce the tabbed navigation. 
So, this is where I'm going to make use of the ul with the class nav nav-tabs. 
So, you have seen that earlier when we constructed the nav bar, we also used the ul inside the nav bar to specify the navigation items there. 
Similar approach here, except that here we're going to use the ul with the nav and the nav tabs here. 
So, inside this ul, we will construct the navigation structure for this tabbed navigation here. 
So in there, I will use the list item with the class nav-item, and construct the navigation around this list item. 
So, this introduces the first item into my nav tabs. Right after that, inside there I will introduce an a with the class nav-link active. 
So, this one, as you see, if you recall from the way we use the ul with the nav item and nav link. 
In the nav bar, we are seeing a similar approach here. So, nav-item active, and then href. 
So, this would be a reference to tab pane later on, which would have the ID of peter there, and role is tab for this one, and data-toggle tab. 
So, you can see the Bootstrap's javascript component coming into picture here. 
And then I will say Peter Pan, and then close off the a tag there. 
So, this would complete our first tab in our tabbed navigation. 
Let me complete the rest of the code, and then we'll come back and review the rest of the code there. 
So, here you can see that I have completed this navigation structure here. 
Similarly, I am defining the list items for the remaining free corporate leaders here. 
Now this, let me save the change. And then let's go and take a quick look at the web page. 
Switching to the web page, you now see how using the nav nav tabs we have created this navigation structure right below the corporate leadership here. 
So, this navigation structure meaning that I should be able to navigate and view each one of them in more detail by clicking on this. 
So, that is how the tabbed navigation works here. 
Now, obviously, the content of each one of them should appropriately show only that person's details here. 
So, this is where the use of tabbed content and the tab pane classes will come into effect. 
And we're going to enclose this content using that. And then tie this to those navigation, tab navigation up here, so that only one single corporate leader's information is displayed on the screen at a time. 
Once we complete setting up that tabbed navigation, then we'll move down into the actual content here. 
"""

text3 = """
We'll look at how we apply accordions to be able to reveal and hide content in our web page in this exercise. 
Going back to About Us at HTML page where we had the corporate leadership information. 
Now, I'm going to replace the top navigation with an accordion based navigation. 
I'm going to remove this UL that defines the term navigation completely. 
And then we're gonna design the accordion around the content that we already have. 
So, let's delete this UL that contains the tab navigation so they will be left with just this part which is enclosed inside the top panel and the top content. 
So, we're going to go and modify this. Going to this div here, I'm going to remove this class from there and then I apply the id as accordion. 
We need this id later on to be able to create the accordion that div, that contains this content is still in place there. 
So, the top content is now changed to accordion. 
Now, each of this content in here, we're going to convert that into a card based structure there so that they can reveal the content in each of those cards so you will see me using the card and the card body classes there to enclose this content. 
Now, going into the actual content here, I'm going to start applying the card class here with the div there. 
So, we'll say, "div class card" and then close the div there and then this content goes into the div there.
Now, in here, we are going to go in and create a div with the class "card header." 
I'm going to show you for one of them and then we are going to repeat this process for the remaining three also. 
So, we'll say, "card header roll tab" and then "id peterhead." I'm going to take this h3 from down below here, cut it out and then paste it into the card panel. 
So, this h3 that defines the name of the corporate leadership person is cut from inside the tab panel and then moved in to the card header here. 
This is going to act as my navigation aid. Now, to this h3, I'm going to apply a class called mb-0. So, this is mb-0 here. 
Now, this name itself, I'm going to enclose this inside and an a, so I will go to the next line and then say, "a data toggle" and the data toggle will say, "collapse." 
So, now, you see that you're using the collapse plugin. So, we have this closing h3 there. 
So, I'm going to shift it to the next line here and then I'm going to close the a tag right there. 
So, with this the a tag now encloses the name of the CEO in here. And then the h3 tag of course closes the h3 on top and then this is inside the div which is the class card header. 
So, this forms the header structure for my accordion div. Going now to the tab panel below, I'm going to change this class from tab panel fade to collapse. 
So this would be a collapse plugin which will be useful for our accordion and also I will remove this active class for this and the id will be left as peter for this. 
And then you'll say, "data parent" and you would specify accordion. You see why we gave the id of accordion to the div that encloses all these content. 
So, this is the way to specify that this is going to form part of the accordion that you are constructing there. So, that's why data parent accordion. 
Now, the content inside this tab panel, I'm going to enclose it inside the div with the class card body and close off that div here, and then indent this content in there. 
Let's save the changes and then go and take a look at our web page on this moment. 
Going to our web page you now notice that in the corporate leadership, the CEO's name is highlighted here in the card header here. 
And then the content is down below here. Now, we will create the remaining three down below and then enclose all of them in there. 
I'm going to repeat the same structure for the remaining ones. So, I will have the card with the card header, and the card header will enclose the name of the person like this. 
"""

text4 = """
[MUSIC] Let us now try to understand
several mechanisms to enable us to display information to the users
overlaying the content of your web page. So here we'll look at three different
constructs that are available in Bootstrap called tooltips, popovers, and modals. So what are tooltips, popovers and
modals and how are they useful? We'll look at some basic ideas first ,and
then we'll go on to look at some examples. In the exercise that follows,
we'll use tooltips and modals in our web page, and
we'll look at an example of popovers. So, as I mentioned, tooltips, popovers,
and modals are a way of revealing content to the users, when the user interacts
with certain elements on your web page. Say for example when the user's mouse clicks on a button, or
hovers over a button, or clicks on a link, or reaches a certain
point on your web page. So all these will trigger information
to be displayed to the users. So in this case, the information is displayed as
an overlay on top of your web page. So the underlying content of
the web page is still there, but this is laid out on top of
the underlying content. So in terms of flexibility, tooltips
are the simplest to implement, but at the same time have limited flexibility
in how they can display information. Popovers are more flexible than tooltips,
but they also have their own limitations. Modals give you the most
extensive support for displaying content in
a wide variety of ways. As an example, let's go to our
webpage that we have been working on. You see that when we hover our
mouse pointer onto this button. You see this message popping
up on the screen here, with some additional information. This is an example of a tooltip. This allows you to display smaller
amounts of information to the users. So for example if you are trying to
guide users through your website and want them to know what happens when you
click various locations any web page, these maybe a good way of reminding
them of what is expected. So you could easily design for example, walkthroughs of your website using
these tooltips to indicate to users. If you want a bit more
detailed information, then popovers would be more useful. The same example, implement and
using a popover would look like this. Now in this case, you will have to explicitly click
on the button to show the popover. So in that case, the popover is shown
with some title information, and then the actual content at
the bottom in that popover. Now, dismissing the popover will require
you again to click on the bottom there. So this is the behavior of a popover. In some circumstances,
popovers are more useful than tooltips. Our third kind of data
overlay is the modal. A modal allows you to present more detailed information to the users
than a tooltip and popover. The content of the modal is itself divided
into a header, body, and the footer. And the modal itself can contain
a lot more detailed information. And you can use the entire Bootstrap grid, inside the modal body,
to organize the actual content. We look at a couple of examples
of the use of modals next. Going to our web page,
you will see that on the right hand side, here we have a link here called Login. So when you click on that link,
you will notice that this modal with their login form is
popped up on the screen. So this is the typical
behavior of a modal. And so
here you can type in the information, and then click on the Sign In button
to sign in to your website. Going to your Coursera page, here is
a real life example of the use of a modal. So for example,
if you click on the Log In button here, you can see that on Coursera,
a form pops up on the screen. So this is another use of
a modal in your web page. Now that you have seen examples of
tooltips, popovers, and modals, let's go to the next exercise, where we'll
create a tooltip on our index.html page. We'll also create a modal that allows
the user to type in information for logging in into our web page. [MUSIC]
"""
# Function to generate the summary of the text


def generate_summary_pipeline(text):
    summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")
    summary = summarizer(text, max_length=500, min_length=200, do_sample=False)
    # print(summary[0]['summary_text'])

    return summary[0]['summary_text']


def generate_summary_generative(text):
    summary = ""
    prompt = f"Summarize this : {text}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=2000,
    )
    summary = response["choices"][0]["text"]
    return summary


def generate_summary_gpt(text):
    print("have entered gpt")
    summary = ""
    prompt = f"Summarize this : {text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    summary = response["choices"][0]["message"]["content"]
    return summary


def generate_title(text):
    title = ""
    prompt = f"Generate a title for this text : {text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    title = response["choices"][0]["message"]["content"]
    return title


print(generate_title(text4))
