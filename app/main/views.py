from flask import render_template,request,redirect,url_for
from . import main
from ..models import Pitch

@main.route('/')
def index():
    '''
    View root page function that returns the source page and some data
    '''
    title = 'Home - Welcome to The best pitches resource online'
    return render_template('index.html', title = title )


@main.route('/pickup-lines')
def lines():
    '''
    View root page function that returns the source page and some data
    '''
    list = []
    list.append(Pitch('I hope you know CPR, because you just took my breath away!','verbose',0,0))
    list.append(Pitch('So, aside from taking my breath away, what do you do for a living?','verbose',0,0))
    list.append(Pitch('Are you a parking ticket? ‘Cause you’ve got ‘fine’ written all over you.','verbose',0,0))
    list.append(Pitch('Your eyes are like the ocean; I could swim in them all day.','verbose',0,0))
    list.append(Pitch('When I look in your eyes, I see a very kind soul.','verbose',0,0))
    list.append(Pitch('If you were a vegetable, you’d be a ‘cute-cumber.’’ written all over you.','verbose',0,0))
    title = 'Pick up lines - Welcome to The best pitches resource online'
    return render_template('lines.html', title = title, pitches = list )    

@main.route('/interview')
def interview():
    '''
    View root page function that returns the source page and some data
    '''
    list = []
    list.append(Pitch('I’m [NAME], a lawyer with the government, based out of D.C. I grew up in Ohio, though, and I’m looking to relocate closer to my roots, and join a family-friendly firm. I specialize in labor law and worked for ABC firm before joining the government.','verbose',0,0))
    list.append(Pitch('I’m [NAME]. I fell in love with technology after winning a programming contest in eighth grade. That led to a degree in computer science, and I’ve now worked in IT for eight years. I recently wrapped up a contract as a senior data analyst with a big bioinformatics company, and I’m now looking for opportunities with other large medical data organizations.','verbose',0,0))
    list.append(Pitch('Hi, my name is [NAME]. After graduating with my Bachelor’s degree in Business Administration, I’ve spent the last three years building professional experience as an Executive Assistant. I’ve successfully managed end-to-end event coordination and have generated a strong professional network for my colleagues. I was excited to learn about this opportunity in the sports management space — I’ve always been passionate about the way sports brings cultures together and would love the opportunity to bring my project management and leadership abilities to this position.','verbose',0,0))
    list.append(Pitch('Hi, I’m [NAME] and I am excited about the new position with your company! I noticed that you are looking for a candidate with ____ years in the field, but let me tell you how my experience has gone above and beyond. In the same amount of time it would take another candidate to learn the ropes at my last position, I was able to raise our success rates right away. I did this by focusing on what really matters in the industry, such as ______, ______ and ______, and I was able to maximize profits in a quick and efficient way. I knew I should make these changes immediately, since I was able to identify what was slowing down their business operations. I can do the same for you in the new position. Here is my resume. Would you be willing to meet with me next week for an official interview?','verbose',0,0))
    list.append(Pitch('Hi, I’m [NAME]. Now that I have my Bachelor’s degree in Business, as well as a few internship experiences in marketing, I’m ready to contribute to the vision of a cutting-edge hospitality brand. Throughout each of my work experiences, I was often told that I was a very detail-oriented and innovative employee, which I’d love to apply in my next role. In fact, I saw on your website that you’re advertising X. I looked at what your competition is doing, and I saw that they have this interesting campaign doing Y… If I joined the team, I’d look at how we could do something even stronger, such as Z.','verbose',0,0))
    list.append(Pitch('I’m sure you’ve heard that famous sales statistic: 80% of sales are made by the top 20% of salespeople.','verbose',0,0))
    title = 'Interview - Welcome to The best pitches resource online'
    return render_template('interview.html', title = title, interview = list )    

@main.route('/enterpreneurship')
def product():
    '''
    View root page function that returns the source page and some data
    '''
    list = []
    list.append(Pitch('Hi, my name is [NAME] and my company develops and designs personalized online sales funnels [what your company does]. That means two things: one, online customers enjoy a flawless user experience tailored to their needs and interests, and two: our clients get automated solutions that dramatically boost sales [unique business proposition]. We helped our last client increase online revenue by 120 percent month-over-month [hard numbers behind your results]. Does your company have any experience with e-commerce automation? [engaging question]','verbose',0,0))
    list.append(Pitch('I’m [NAME], and I am the owner and wardrobe stylist at The Style Foundry. We are a full-service wardrobe styling business that helps you take the stress out of getting dressed through our styling services. A typical customer cycle starts with a Closet Cleanse, where I clean out your closet, tell you what to keep and get rid of, take pictures of all of the yeses and then upload them to an app/website where I mix and match them into over 100 different outfits from what you already own. From there, I am able to really see what’s missing and what you need. We can tackle that by personal shopping, which is done in-person at your favorite stores or ones I suggest; virtual shopping, which is done online (I send you my finds, you buy what you like, and then when all of the items arrive at your house, I come in for a fitting); or through our mobile boutique, which we can pull up in your driveway and fill it with our pieces that best fit your style and shopping list. It’s the best of online and boutique shopping.','verbose',0,0))
    list.append(Pitch('Has this ever happened to you? You’re rushing to get the kids out the door in the morning so you can get them to school on time and not be late for an important meeting — and then you realize that you can’t find your car keys. This happens all the time to me. In fact, did you know that the average suburban professional misplaces their keys more than five times per month? That’s more than 600 million times per year! Using bluetooth technology, I’ve created a low cost key fob that helps people find their keys and other lost items in record time, making it easier to get out the door on busy mornings. We’ve got a working prototype and now we’re looking to raise funds to go into large-scale production. We’ve got some new team members on board with extensive manufacturing experience and supply chain expertise, so we’re hoping to get to market in the next six months.','verbose',0,0))
    list.append(Pitch('Hi, I’m [NAME], the founder of Merchant Machine. We make it easy to say ‘thank you’ at work. Merchant Machine helps small businesses quickly and easily save money on their credit card processing costs by comparing the leading options in the market. It’s completely free to the end user, there are no obligations and takes just one minute to do. Can we set up a time to chat tomorrow?','verbose',0,0))
    list.append(Pitch('Hi, I’m [NAME]. I got your email address from [NAME]. My co-founders and I founded Grasshopper and Engine Yard, in which Amazon, Benchmark, and NEA invested. Our new company, Chargify, is a simple recurring billing management tool. We’re looking for angel capital to fill in some gaps. Maybe you’re interested in such an investment?','verbose',0,0))
    list.append(Pitch('Hi, I’m [NAME], the founder of Merchant Machine. We make it easy to say ‘thank you’ at work. Merchant Machine helps small businesses quickly and easily save money on their credit card processing costs by comparing the leading options in the market. It’s completely free to the end user, there are no obligations and takes just one minute to do. Can we set up a time to chat tomorrow?','verbose',0,0))
    title = 'Enterpreneurship - Welcome to The best pitches resource online'
    return render_template('product.html', title = title, product = list )    

@main.route('/product-pitch')
def sales():
    '''
    View root page function that returns the source page and some data
    '''
    list = []
    list.append(Pitch('For 130 years, Merck (known as MSD outside of the U.S. and Canada) has been inventing for life, bringing forward medicines and vaccines for many of the world’s most challenging diseases in pursuit of our mission to save and improve lives.','verbose',0,0))
    list.append(Pitch('Gap Inc. is a leading global retailer with a collection of brands including Old Navy, Gap, Banana Republic, and Athleta. We\'re committed to serving the needs of our customers while delivering long-term value to our shareholders.','verbose',0,0))
    list.append(Pitch('G2 plays a huge role by providing unique, authentic peer advice in real time. We give buyers better guidance than traditional analyst firms, which can take up to 2 years to update and publish technology research. That timeline just can’t keep up with the pace of technology. At G2, we aim to be a trusted source that helps every business professional in the world make better technology decisions.','verbose',0,0))
    list.append(Pitch('Van’s honest and poignant social commentary has made him one of the most compelling and powerful public voices in America. His reach transcends age, race, geography, and political ideology.','verbose',0,0))
    list.append(Pitch('Investing isn\'t just about creating wealth. It\'s about what money can help you do. Build a brighter future for yourself and your loved ones. Or design a better world for all of us. Our single focus is helping you achieve what\'s most important to you.','verbose',0,0))
    list.append(Pitch('There’s a better way to grow. HubSpot offers marketing, sales, service, and operations software that helps your business grow without compromise. Because ‘good for the business’ should also mean ‘good for the customer.','verbose',0,0))
    list.append(Pitch('We provide advice, banking, insurance, investment options, and guidance on how you can live generously. Money itself isn’t your end goal. (But it can help you get there.) Our financial guidance can help you move forward in life and reach your own higher purpose. We take the time to learn what matters most to you and provide resources that help you put your values into action.','verbose',0,0))
    title = 'Sales - Welcome to The best pitches resource online'
    return render_template('sales.html', title = title, sales = list )        