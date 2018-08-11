from django.shortcuts import render, redirect, HttpResponse
import random, datetime

def index(request):

# Soft-Reset
    if 'total' not in request.session or request.session['total']  < 0:
        request.session['total'] = 0
    if 'log' not in request.session:
        request.session['log']=[]
# Bills
    if request.session['total'] > 75:
        rngevent1 = random.randrange(0,20)
        if rngevent1 > 0:
            temp = {
                'randnum':rngevent1*-1,
                'text': "Life's caught up to you! There's bills to pay!...("+str(rngevent1)+")",
                'now' : str(datetime.datetime.now())
            }
            request.session['total']+=temp['randnum']
            request.session.modified=True
# Meteor
    if len(request.session['log']) > 10:
        rngevent2 = random.randrange(0,10000)
        if rngevent2 < 75:
            temp = {
                'randnum':rngevent2*-20,
                'text': "Meteor. Hit. Your. House...Get Wrecked...(-"+str(rngevent2)+") ",
                'now' : str(datetime.datetime.now())
            }
            request.session['total']=temp['randnum']
            request.session.modified=True            
            
    if request.session['total']< -50:
        return redirect('reset')
    # print("*"*50)
    # print("log is : ", request.session['log'])
    # print('*'*50)
    request.session['loglen'] =  len(request.session['log']) -1
    return render(request,'index.html')

def farm(request):
    randnum = random.randrange(5,10) 
    temp ={
        'randnum' : randnum,
        'text' : "Another day wasted...(+"+str(randnum)+")" ,
        'now' : str(datetime.datetime.now())
    }
    request.session['total']+=temp['randnum']
    request.session['log'].append(temp)
    request.session.modified=True
    return redirect ('/')

def cave(request):
    randnum = random.randrange(0,40) 
    temp ={
        'randnum' : randnum,
        'text' : "Spooooky cave...(+"+str(randnum)+")",
        'now' : str(datetime.datetime.now())
    }
    request.session['total']+=temp['randnum']
    request.session['log'].append(temp)
    request.session.modified=True
    return redirect ('/')

def house(request):
    randnum = random.randrange(0,3) 
    temp ={
        'randnum' : randnum,
        'text' : "Get out of the house...(+"+str(randnum)+")",
        'now' : str(datetime.datetime.now())
    }
    request.session['total']+=temp['randnum']
    request.session['log'].append(temp)
    request.session.modified=True
    return redirect ('/')

def casino(request):
    randnum = random.randrange(0,36)
# Win/Loss condition
    if int(request.POST['guess']) != randnum:
        temp ={
            'randnum' : int(request.POST['bet'])*-1,
            'text' : "So close, you'll get it next time...(-"+request.POST['bet']+")"+ " | Number was "+ str(randnum),
            'roulette': randnum,
            'now' : str(datetime.datetime.now())
        }
    if int(request.POST['guess']) == randnum:
        temp ={
            'randnum' : int(request.POST['bet'])*35,
            'text' : "Congratulations! You guessed the number!...(+"+str(randnum)+")"+ " | Number was "+ str(randnum),
            'roulette': randnum,
            'now' : str(datetime.datetime.now())
        }
    request.session['total']+=temp['randnum']
    request.session['log'].append(temp)
    request.session.modified=True
    return redirect ('/')

def reset(request):
    request.session.flush()
    return redirect ('/')
