from django.shortcuts import render, redirect
import random

def root(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []

    context = {
        "locations": {"Farm": "earns 10-20 gold pieces", "Cave": "earns 5-10 gold pieces", "House": "earns 2-5 gold pieces", "Casino": "earns/takes 0-50 gold pieces"}
    }
    return render(request, "index.html", context)

def process_money(request):
    if request.POST['which_form'] == "Farm":
        gold_amount = random.randint(10,20)
        request.session['gold'] += gold_amount
        request.session['activities'].insert(0, f"{gold_amount} gold earned from the Farm")
    elif request.POST['which_form'] == "Cave":
        gold_amount = random.randint(5,10)
        request.session['gold'] += gold_amount
        request.session['activities'].insert(0, f"{gold_amount} gold earned from the Cave")
    elif request.POST['which_form'] == "House":
        gold_amount = random.randint(2,5)
        request.session['gold'] += gold_amount
        request.session['activities'].insert(0, f"{gold_amount} gold earned from the House")
    elif request.POST['which_form'] == "Casino":
        gold_amount = random.randint(-50,50)
        request.session['gold'] += gold_amount
        if gold_amount > 0:
            request.session['activities'].insert(0, f"{gold_amount} gold earned from the Casino")
        else:
            request.session['activities'].insert(0, f"You lost {gold_amount} at the Casino")
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
