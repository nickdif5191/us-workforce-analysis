from Scripts.Model import Model

def run_model(model_inputs:dict):
    """
    Creates DataModel object given set of inputs and runs it

    Parameters:
        model_inputs (dict): dictionary of inputs specifying conditions of DataModel user wishes to run

    Returns:
        data_to_analyze (pd.DataFrame): DF of data relevant to the specified industry, threshold, and states
    """
    light_industry_data_model = Model(job_code_text_corpus=model_inputs["job_code_text_corpus"],
                                        relevant_states=model_inputs["relevant_states"],
                                        relevance_threshold=model_inputs["relevance_threshold"])
    
    return light_industry_data_model.data_to_analyze


light_industry_model_inputs = {

# text corpus from https://www.mastersonstaffing.com/blog/what-is-light-industrial-work/
"job_code_text_corpus" : """If you’ve been searching for new employment in the manufacturing industry, 
you’ve likely come across the term “light industrial.” The word crops up in 
job descriptions, job titles, and qualifications, but it may leave you 
scratching your head wondering:

What exactly is light industrial work? How is it different from the 
traditional manufacturing, production, or distribution jobs I’m familiar with?

As one of the top light industrial staffing agencies, we’ve helped source 
top talent for many light industrial job openings. We’re familiar with light 
industrial work and who makes the best candidates. Below, we’ll help you 
learn what light industrial work is so you can decide if it’s the right 
opportunity for you.

What Is Light Industrial Work?
Light industrial work is similar to many jobs you may find in manufacturing 
or distribution, but occurs on a much smaller scale. For example, light 
industrial work involves producing or distributing smaller products and 
parts of larger goods. Because light industrial does not require a large, 
involved production, this type of work typically:

Relies more on labor and less on machinery
Utilizes fewer materials, leading to less waste
Uses partially produced materials to produce items
As a worker in the light industrial space, you might be responsible for 
assisting with product assembly, packaging goods and preparing them for 
shipment, or performing quality control. Plus, light industrial work spans 
several industries, meaning you could be working in food production, 
automobile part assembly, home furnishings, and more.

Examples of Light Industrial Jobs
What types of positions and job titles are available in light industrial 
work? Some common job titles include:

Electronic Assembler
Inventory Clerk
Machine Operator
Quality Control Tester
Welder
As you can see with the examples above, light industrial work can involve 
anything from working on the assembly line and piecing together products to 
operating the forklift to move materials and load/unload trucks.

How to Tell if You’re a Good Fit for Light Industrial Work
If you already have some experience in the manufacturing industry, light 
industrial work should sound pretty familiar to you. However, if you’re new 
to manufacturing and light industrial, you should keep in mind that “light” 
doesn’t mean “easy.”

In fact, light industrial work is still very physical as it doesn’t utilize 
as much machinery to get the job done. So, before you apply for a light 
industrial job, you should keep in mind that the job is just as physical and 
demanding as a more “heavy” industrial job.

Want to know how you measure up against other light industrial candidates? 
The best light industrial talent tends to have the following skills:

Attention to detail
Flexibility
Ability to handle small parts and components
Dependability
These skills ensure that production is efficient and effective, but also 
shows employers that they can rely on you to get to work and finish tasks on 
time. Sound like you? Then you’d make a great candidate for a light 
industrial job.

Light Could Be Right
Light industrial work is very similar to other manufacturing, production, 
and distribution work you may find in your job search. They’re only “light” 
because they typically produce parts and components of larger products, 
allowing them to use smaller production facilities and teams. To get a job 
involving light industrial work, you still need to make sure you have all 
of the common manufacturing skills like attention to detail, reliability, 
dexterity, and more.

If light industrial work sounds ideal for your career, we can help you find 
those opportunities. See our open light industrial positions and find a job 
with us.
"""
,
# state's Traba currently operates in
"relevant_states" : ["Florida", "Texas", "Ohio", "Georgia", "Tennessee", "Michigan", "Indiana", "North Carolina",
                     "South Carolina", "Arizona", "Nevada"], 
                                                
"relevance_threshold":0.55
    }

if __name__ == "__main__":
    # model inputs that represent occupations and states relevant to Light Industry
    light_industry_data_to_analyze = run_model(model_inputs=light_industry_model_inputs)
    light_industry_data_to_analyze.to_csv("Outputs/light_industry.csv", index=False)



