from flask import render_template,request,redirect,url_for
from . import main
from ..models import Pitch

@main.route('/')
def index():
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
    title = 'Home - Welcome to The best pitches resource online'
    return render_template('index.html', title = title, pitches = list )


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
    title = 'Home - Welcome to The best pitches resource online'
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
    title = 'Home - Welcome to The best pitches resource online'
    return render_template('interview.html', title = title, interview = list )    

@main.route('/product')
def products():
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
    title = 'Home - Welcome to The best pitches resource online'
    return render_template('lines.html', title = title, pitches = list )    

@main.route('/promotion')
def promotion():
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
    title = 'Home - Welcome to The best pitches resource online'
    return render_template('lines.html', title = title, pitches = list )        