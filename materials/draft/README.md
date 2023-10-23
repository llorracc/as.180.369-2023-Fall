# “The Draft”

## Overview

## Mon Oct 2

<!-- - *MZ*: Before class, create a public repo with the presentation. -->
<!-- - *MZ*: Prepare to be able to explain how to get a FredAPI key. -->

[Zoom recording. Requires JHU login.](https://livejohnshopkins-my.sharepoint.com/personal/mzahn2_jh_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fmzahn2%5Fjh%5Fedu%2FDocuments%2FFall%202023%20AS%2E160%2E369%20Class%20Recordings%2F2023%2E10%2E02%20Class%205%2Emp4&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0RpcmVjdCJ9fQ&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0RpcmVjdCJ9fQ&ga=1)

**Agenda**
- *CR* Discuss best practices for the visual communication of quantitative information.
- *CR* Review (and improve!) data visualizations from Matt Zahn's Code Demo
    - How to create Pull Request with our improvements.
- *MZ* Get and use your own FredAPI Key!

**Homework**
- Improve the data visualizations from [Matt Zahn's Code Demo](https://github.com/llorracc/as.180.369/blob/main/materials/code-demo/ZahnMVStockReturns.ipynb)
    - Copy Matt’s Notebook into YOUR contrib folder and give it a new name.
    - Update the visualization in this notebook you copied/renamed.
    - `git add` and `git commit` your work.
    - `git push` your changes from Jupyterhub to Github.
    - Do this across at least 3 commits over 2 days. 
- *MZ* Review [Matt Zahn's ‘Job Market Paper’](https://github.com/matthew-zahn/matthew-zahn.github.io/blob/master/files/papers/choice_cost/JMPZahn.pdf). Bonus points for the person that finds the most typos!

## Mon Oct 9 — Coping Strategies

[Zoom recording. Requires JHU login.](https://livejohnshopkins-my.sharepoint.com/:v:/g/personal/mzahn2_jh_edu/EQdZHFe5L8pJu5vCz0mMYIYBtB5NVxPLGpiDp8IxA43Nsg?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0RpcmVjdCJ9fQ&e=uE33s1)

**Agenda**
- Share your *improved* visualization!
    - Students will use Zoom to share their screen & Jupyter Notebook.
    - Speak to the improvements made on the data visualization and justify
      why you made those changes.
    - We will work through any `git` difficulties you encountered.

- *CR* Coping with `git` and https://github.com (30 min.)
    - Getting your bearing at the command line
    - Getting your bearing with `git`
    - Debugging common issues with `git` and [github](https://github.com)
    - `git` cheatsheet

- *CR* Coping with Jupyter Notebooks (30 min.)
    - Missing packages and environments
        - What are `pip install` and `conda install`?
        - How to recognize when packages are missing?
        - How to find and document missing packages?

**Homework**
- Continue working on the Introduction and Abstract for final papers.
- Use ChatGPT to improve your writing. Please save your ChatGPT prompts in your commit messages.
- Spread out commit messages over at least three days.

**Helpful notes**
- Abstract:
    - Results you hope to get. Write as if you got the results you wanted that align with your hypothesis.
    - Note why people should care about your findings.
    - Tight: Less than 200 words.
- Introduction:
    - Longer than Abstract.
    - Position the paper in terms of our current understanding/debates on the subject.
    - Motivate why you are studying this topic and why it is important. Big pictire, what is the point of your paper. 
    - Aim for about a page or a page and a half (~500 to 750 words).
    - Focus on writing well. The content is less important than the process and demonstration of using the tools to improve the content you generate.


## Mon Oct 16

[Zoom recording. Requires JHU login.](https://livejohnshopkins-my.sharepoint.com/:v:/g/personal/mzahn2_jh_edu/EZZescblGOBEpvWgNGqhJ6YB3dSjrDGW49exKc_EnpGmSw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0RpcmVjdCJ9fQ&e=6m0VKz)

**Agenda**
- Show us your Abstract & Introduction!
    - Share you experience in crafting Chat GPT prompts to give you feedback.
    - What advice did you accept? What advice did you reject?

- Discuss next steps for your paper.
    - Literature you plan to use (show latest Litmaps/paperpile).
    - What is the question that you will address with data?
    - What kind of data exist that you can use to answer your question?

- *JP* Working with Data in your Jupyter Notebook
    - What is tabular data? What is a pandas DataFrame?
    - How do I select columns from a DataFrame, how do I filter rows?
    - How do I perform aggregations/compute summary statistics?
    - How do I perform econometrics?
    - How do I create a new `pandas` DataFrame from some other data source?
        - How read a `.csv`, how to read an excel file (`.xls`, `.xlsx`)

- *MZ* Coping with the research process (30 min.)
    - What do I do when I can’t move my research forward?
    - What do I do when I can’t think of what else to write?
    - How do I know I can trust my results?

**Homework**
- Obtain and explore some data that are relevant to your topic.
    - Conduct an exploration/preliminary analysis of your obtained data set(s).
- Be prepared to present to the class on your preliminary analysis of the data.
- Make sure you are working on your Jupterhub and are `git add`ing and `git commit`ing 
  your work regularly.
  - **Spread out commit messages over at least three days.**
- Prepare for 10 minute discussion where you are in the next class.
- Prepare to identify the tools/ideas you would consider using from the Korinek paper.
  - In the next class, you will write a paragraph on the above.

## Mon Oct 23

**Agenda**
- Discussions 
- Review pandas data loading
- Write a paragraph on the tools/ideas you would consider using from the Korinek paper.
- *CR* Demonstration of citation tools.
    - Bibtex files generated by Paperpile.
    - Syntax for citing a paper using its Bibtex cite key.
    - [myst](https://mystmd.org) to create a webpage with bibliography.

```sh
# copy jupyterbook folder contrib/cam/jupyterbook to your own contrib folder
# navigate to the new copy of /jupyterbook your contrib folder

# start terminal session in the folder of your notebook
# alternatively, use `cd` to navigate to your notebook folder

build-jb

# open link jhu.econ-ark.org/user/{your user name}/proxy/{...}/ in new tab
# note that this link should appear in your terminal screen, simply click on it to open it in a new tab.
```

**Homework**
- Write a first draft of your literature summary.
- Write a first draft of your methodology.
- The above 2 sections of your paper should be in *separate* Markdown cells in your Jupyter Notebook.
    - For a reference, use [Matt Zahn's ‘Job Market Paper’](https://github.com/matthew-zahn/matthew-zahn.github.io/blob/master/files/papers/choice_cost/JMPZahn.pdf).

## Mon Oct 30

**Agenda**

- Present your literature summary & methodology sections.
    - 10 minutes per student.
- *MZ* Short presentation on job talk paper
- *MZ* Coping with Rejection (30 min.)
    - Rejection from a Journal.
    - Rejection from Graduate School.
    - Rejection from a Job.

**Homework**
- Write the first draft of the results section.
    - You should break your text into a number of smaller markdown cells.
        - This makes it easier to use ChatGPT for editing.
    - Be sure to get ChatGPT feedback on your writing.
    - In the commits you write, please include the prompts you used in ChatGPT.

## Mon Nov 6
