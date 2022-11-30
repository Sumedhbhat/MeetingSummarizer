from transformers import pipeline, BartTokenizerFast, EncoderDecoderModel
import torch

text = """
Welcome. Let's get started with Lesson 1. Lesson 1's objectives are to ultimately understand first what managerial accounting is, second, why it's important, and third, introduce some contemporary issues related to this topic.
So first off, what is managerial accounting? Well, it's a very difficult concept to summarize in a single sentence. So in a very unsatisfying book definition is the following: It's the process of obtaining, creating, and analyzing relevant information to help achieve organizational goals. As we work through these slides, we'll delve into the certain -- the specific concepts that are embedded inside this definition. 
So first off, some common conceptions about accounting. When I tell people that I teach accounting, one of the first things they say to me is, "Oh, you can help me with my taxes." Well, truth be told, I'm very far from a tax expert. But there is some interrelationships between taxes and managerial accounting, and we'll see a little bit of that in the future modules, but a tax course this is not. Another common conception is that people think of financial accounting, specifically financial statements. Oh, I remember accounting. It's journal entries, debits and credits and account balances, the balance sheet, the income statement, the statement of cash flows. Well, let's explore this concept a little bit more and think about who uses the financial statements of a firm.
So first off, we can think of an organization, and just so it's easy to envision, let's think about a publicly traded global corporation. That organization is very large, and so oftentimes the owners of that organization lie outside of the organization. Those people, the investors, and people thinking about becoming owners, or potential investors, are very interested in what the content of financial statements are. Similarly, in a different type op relationship, there's banks, financial institutions and other individuals who are entering into a debt relationship with the organization.   
So creditors and those parties thinking about becoming creditors to the firm or the organization also would be interested in the financial statements. Because of the nature of the relationship between investors and the organization and creditors in the organization, the financial statement information that the organization provides is crucial to the decisions made by each of these parties. Another user is tax authorities, and for certainty, no matter what country you live in, the financial statement information is going to be of interest to the tax authorities. I want to make sure that they are paying the appropriate amount of taxes. Now, oftentimes in many countries, the information that's interesting to tax authorities is different than the information that's interesting to investors and creditors and other users. But in many countries, the financial statement information is a precursor or a building block to the tax information that's provided to those authorities. In many industries, regulatory agencies are of interest in the -- are interested in the financial statement information. In the United States, there is the Securities and Exchange Commission who is responsible for insuring that the information provided by the organization is a fair representation of the firm and its financial position.  
Other industries involve other regulatory agencies. Partners of the organization are also interested in financial statement users. Suppliers, customers, and other partners oftentimes engage in formal and informal contracts with the organization and they want to know what the financial position of the firm is, is this a good partner for me. Financial statement information, along with other information, is useful to those parties as well. And finally, you can think of the organization's competitors. Financial statement information is a useful benchmark against which competitors can assess their own performance. They might also use financial statement information to elicit competitive advantages over the organization.
Now, all these users who lie outside of the organization, financial statement information is very useful to them. In this course, however, we're not going to focus on the outside users. We're focusing on those users inside of the organization, the managers and employees who are making decisions that help the organization try to achieve its goals.
"""

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#tokenizer = BartTokenizerFast.from_pretrained('knkarthick/MEETING_SUMMARY')
#model = EncoderDecoderModel.from_pretrained('knkarthick/MEETING_SUMMARY')


def generate_summary_pipeline(text):
    summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")
    summary = summarizer(text, max_length=400, min_length=50, do_sample=False)
    print(summary[0]['summary_text'])

    return summary[0]['summary_text']


"""def generate_summary(text):
    inputs = tokenizer([text], padding='max_length',
                       truncation=True, max_length=400, return_tensors='pt')
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)

    output = model.generate(input_ids, attention_mask=attention_mask)
    return tokenizer.decode(output[0], skip_special_tokens=True)
"""

print(generate_summary_pipeline(text))
