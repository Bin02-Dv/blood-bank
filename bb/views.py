from django.shortcuts import render, redirect
from django.contrib import messages
from itertools import chain
from django.contrib.auth.models import User, auth
from .models import *
import smtplib
import ssl
from django.conf import settings
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

# date declaration
day = datetime.datetime.now().day
month = datetime.datetime.now().month
year = datetime.datetime.now().year

def logout(request):
    auth.logout(request)
    return redirect('login')

def donate(request, id):
    donating = NewDonor.objects.get(id=id)
    blood_group = StockIncrease.objects.get(blood_group=donating.blood_group)
    donating.count += 1
    donating.due_date = f"{month+3%12}/{day}/{year}"
    donating.save()
    blood_group.unit += 1
    blood_group.save()
    new_history = History.objects.create(
        blood_group=blood_group.blood_group, unit=blood_group.unit, month=blood_group.month, year=blood_group.year
    )
    new_history.save()
    messages.info(request, 'Blood Donated Successfully.....')
    return redirect('all-donor')

def reset(request, id):
    donor_reset = NewDonor.objects.get(id=id)
    donor_reset.count = 0
    donor_reset.save()
    messages.info(request, 'Count Reset Successfully...')
    return redirect('all-donor')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password!!')
            return redirect('login')
    return render(request, 'login.html')

def birthday(request):
    birthdays = datetime.datetime.now().strftime("%m-%d")
    donors = NewDonor.objects.filter(birthday_check=birthdays)
    return render(request, 'birthday.html', {'donors':donors})

def due_date(request):
    due = f"{month}/{day}/{year}"
    donors = NewDonor.objects.filter(due_date=due)
    return render(request, 'due-date.html', {'donors':donors})


def user_add(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exist !!!')
            return redirect('user-add')
        elif cpassword != password:
            messages.info(request, 'password and confirm password missed match !!!')
            return redirect('user-add')
        else:
            new_user = User.objects.create_superuser(
                username=username, email=email, password=password
            )
            new_user.save()
            messages.info(request, 'Admin saved successfully...')
            return redirect('user-view')

    return render(request, 'add-user.html')

def user_view(request):
    admins = User.objects.all()
    return render(request, 'view-user.html', {'admins':admins})

@login_required(login_url='login')
def index(request):
    blood_group = StockIncrease.objects.all()
    if request.method == 'POST':
        full_name = request.POST['full-name']
        father_name = request.POST['father-name']
        mother_name = request.POST['mother-name']
        dob = request.POST['dob']
        pnumber = request.POST['pnumber']
        gender = request.POST['gender']
        email = request.POST['email']
        blood_group = request.POST['blood-group']
        city = request.POST['city']
        home_address = request.POST['address']
        nationality = request.POST['nationality']
        marital = request.POST['marital']
        state_of_origin = request.POST['state-of-origin']
        lga = request.POST['lga']
        question = request.POST['question']
        due_date = f"{month+3%12}/{day}/{year}"
        date = f"{month}/{day}/{year}"

        new_donor = NewDonor.objects.create(
            full_name=full_name, father_name=father_name, mother_name=mother_name,
            dob=dob, pnumber=pnumber, gender=gender, email=email, blood_group=blood_group,
            city=city, home_address=home_address, birthday_check=dob[5:], count=0, nationality=nationality,
            marital=marital, state_of_origin=state_of_origin, question=question, due_date=due_date, date=date,
            lga=lga
        )
        new_donor.save()
        update_unit = StockIncrease.objects.get(blood_group=blood_group)
        update_unit.year = year
        if month == 1:
            update_unit.month = 'January'
            update_unit.save()
        elif month == 2:
            update_unit.month = 'February'
            update_unit.save()
        elif month == 3:
            update_unit.month = 'March'
            update_unit.save()
        elif month == 4:
            update_unit.month = 'April'
            update_unit.save()
        elif month == 5:
            update_unit.month = 'May'
            update_unit.save()
        elif month == 6:
            update_unit.month = 'June'
            update_unit.save()
        elif month == 7:
            update_unit.month = 'July'
            update_unit.save()
        elif month == 8:
            update_unit.month = 'August'
            update_unit.save()
        elif month == 9:
            update_unit.month = 'September'
            update_unit.save()
        elif month == 10:
            update_unit.month = 'October'
            update_unit.save()
        elif month == 11:
            update_unit.month = 'November'
            update_unit.save()
        elif month == 12:
            update_unit.month = 'December'
            update_unit.save()
        messages.info(request, 'Donor Added Successfully...')
        return redirect('/')
    return render(request, 'index.html', {'blood_group': blood_group})

def all_donor(request):
    blood_group = StockIncrease.objects.all()
    donors = NewDonor.objects.all().order_by()
    context = {
        'donors':donors,
        'blood_group': blood_group
    }
    if request.method == 'POST':
        full_name = request.POST['full-name']
        father_name = request.POST['father-name']
        mother_name = request.POST['mother-name']
        dob = request.POST['dob']
        pnumber = request.POST['pnumber']
        gender = request.POST['gender']
        email = request.POST['email']
        blood_group = request.POST['blood-group']
        city = request.POST['city']
        home_address = request.POST['address']
        nationality = request.POST['nationality']
        marital = request.POST['marital']
        state_of_origin = request.POST['state-of-origin']
        lga = request.POST['lga']
        question = request.POST['question']
        due_date = f"{month+3%12}/{day}/{year}"
        date = f"{month}/{day}/{year}"

        new_donor = NewDonor.objects.create(
            full_name=full_name, father_name=father_name, mother_name=mother_name,
            dob=dob, pnumber=pnumber, gender=gender, email=email, blood_group=blood_group,
            city=city, home_address=home_address, birthday_check=dob[5:], count=0, nationality=nationality,
            marital=marital, state_of_origin=state_of_origin, question=question, due_date=due_date, date=date,
            lga=lga
        )
        new_donor.save()
        
        update_unit = StockIncrease.objects.get(blood_group=blood_group)
        update_unit.year = year
        if month == 1:
            update_unit.month = 'January'
            update_unit.save()
        elif month == 2:
            update_unit.month = 'February'
            update_unit.save()
        elif month == 3:
            update_unit.month = 'March'
            update_unit.save()
        elif month == 4:
            update_unit.month = 'April'
            update_unit.save()
        elif month == 5:
            update_unit.month = 'May'
            update_unit.save()
        elif month == 6:
            update_unit.month = 'June'
            update_unit.save()
        elif month == 7:
            update_unit.month = 'July'
            update_unit.save()
        elif month == 8:
            update_unit.month = 'August'
            update_unit.save()
        elif month == 9:
            update_unit.month = 'September'
            update_unit.save()
        elif month == 10:
            update_unit.month = 'October'
            update_unit.save()
        elif month == 11:
            update_unit.month = 'November'
            update_unit.save()
        elif month == 12:
            update_unit.month = 'December'
            update_unit.save()
        messages.info(request, 'Donor Added Successfully...')
        return redirect('/all-donor')
    return render(request, 'all-donor.html', context)

def regular_donor(request):
    blood_group = StockIncrease.objects.all()
    donors = NewDonor.objects.all()
    context = {
        'donors':donors,
        'blood_group': blood_group
    }
    if request.method == 'POST':
        full_name = request.POST['full-name']
        father_name = request.POST['father-name']
        mother_name = request.POST['mother-name']
        dob = request.POST['dob']
        pnumber = request.POST['pnumber']
        gender = request.POST['gender']
        email = request.POST['email']
        blood_group = request.POST['blood-group']
        city = request.POST['city']
        home_address = request.POST['address']
        nationality = request.POST['nationality']
        marital = request.POST['marital']
        state_of_origin = request.POST['state-of-origin']
        lga = request.POST['lga']
        question = request.POST['question']
        due_date = f"{month+3%12}/{day}/{year}"
        date = f"{month}/{day}/{year}"

        new_donor = NewDonor.objects.create(
            full_name=full_name, father_name=father_name, mother_name=mother_name,
            dob=dob, pnumber=pnumber, gender=gender, email=email, blood_group=blood_group,
            city=city, home_address=home_address, birthday_check=dob[5:], count=0, nationality=nationality,
            marital=marital, state_of_origin=state_of_origin, question=question, due_date=due_date, date=date,
            lga=lga
        )
        new_donor.save()
        
        update_unit = StockIncrease.objects.get(blood_group=blood_group)
        update_unit.year = year
        if month == 1:
            update_unit.month = 'January'
            update_unit.save()
        elif month == 2:
            update_unit.month = 'February'
            update_unit.save()
        elif month == 3:
            update_unit.month = 'March'
            update_unit.save()
        elif month == 4:
            update_unit.month = 'April'
            update_unit.save()
        elif month == 5:
            update_unit.month = 'May'
            update_unit.save()
        elif month == 6:
            update_unit.month = 'June'
            update_unit.save()
        elif month == 7:
            update_unit.month = 'July'
            update_unit.save()
        elif month == 8:
            update_unit.month = 'August'
            update_unit.save()
        elif month == 9:
            update_unit.month = 'September'
            update_unit.save()
        elif month == 10:
            update_unit.month = 'October'
            update_unit.save()
        elif month == 11:
            update_unit.month = 'November'
            update_unit.save()
        elif month == 12:
            update_unit.month = 'December'
            update_unit.save()
        messages.info(request, 'Donor Added Successfully...')
        return redirect('/all-donor')
    return render(request, 'regular-donor.html', context)


def donor_details(request, id):
    donor = NewDonor.objects.get(id=id)
    return render(request, 'print-donor.html', {'donor': donor})


def stock_increase(request):
    blood_groups = StockIncrease.objects.all()
    if request.method == 'POST':
        blood_group = request.POST['blood-group']
        unit = request.POST['unit']
        new_blood_group = StockIncrease.objects.create(blood_group=blood_group, unit=unit)
        new_blood_group.save()
        messages.info(request, 'New Blood Donor Added Successfully...')

    return render(request, 'stock-increase.html', {'blood_groups':blood_groups})

def stock_decrease(request):
    blood_groups = StockIncrease.objects.all()
    if request.method == 'POST':
        blood_group = request.POST['blood-group']
        unit = request.POST['unit']
        de_blood_group = StockIncrease.objects.get(blood_group=blood_group)

        if int(unit) > de_blood_group.unit:
            messages.info(request, 'There is no enough blood for the required quantity..!!!')
            return redirect('stock-decrease')
        else:
            de_blood_group.unit -= int(unit)
            de_blood_group.save()
            messages.info(request, 'Blood Donor Deducted Successfully...')
            return redirect('stock-decrease')

    return render(request, 'stock-decrease.html', {'blood_groups':blood_groups})


# --------------------------------------------------------------------

# Delete section


def request_for_delete_donor(request, id):
    donor = NewDonor.objects.get(id=id)
    return render(request, 'request-for-delete-donor.html', {'donor':donor})

def delete_donor(request, id):
    donor = NewDonor.objects.get(id=id)
    donor.delete()
    messages.info(request, 'Donor deleted successfully..')
    return redirect('/all-donor')

def request_for_delete_blood(request, id):
    blood = StockIncrease.objects.get(id=id)
    return render(request, 'request-for-delete-blood.html', {'blood':blood})

def delete_blood(request, id):
    blood = StockIncrease.objects.get(id=id)
    blood.delete()
    messages.info(request, 'Blood deleted successfully..')
    return redirect('/stock-increase')

def request_for_delete_user(request, id):
    admin = User.objects.get(id=id)
    return render(request, 'request-for-delete-user.html', {'admin':admin})

def delete_user(request, id):
    admin = User.objects.get(id=id)
    admin.delete()
    messages.info(request, 'Admin deleted successfully..')
    return redirect('/user-view')


# --------------------------------------------------------------------

# --------------------------------------------------------------------

# Update section


def try_updating_donor(request, id):
    donor = NewDonor.objects.get(id=id)
    return render(request, 'update-donor.html', {'donor':donor})

def update_donor(request, id):
    donor = NewDonor.objects.get(id=id)
    if request.method == 'POST':
        full_name = request.POST['full-name']
        father_name = request.POST['father-name']
        mother_name = request.POST['mother-name']
        dob = request.POST['dob']
        pnumber = request.POST['pnumber']
        gender = request.POST['gender']
        email = request.POST['email']
        blood_group = request.POST['blood-group']
        city = request.POST['city']
        home_address = request.POST['address']
        nationality = request.POST['nationality']
        marital = request.POST['marital']
        state_of_origin = request.POST['state-of-origin']
        lga = request.POST['lga']
        question = request.POST['question']

        donor.full_name = full_name
        donor.father_name = father_name
        donor.mother_name = mother_name
        donor.dob = dob
        donor.pnumber = pnumber
        donor.gender = gender
        donor.email = email
        donor.blood_group = blood_group
        donor.city = city
        donor.home_address = home_address
        donor.nationality = nationality
        donor.marital = marital
        donor.state_of_origin = state_of_origin
        donor.lga = lga
        donor.question = question
        donor.save()
        messages.info(request, 'Donor Updated Successfully...')
        return redirect('/all-donor')
    
def try_updating_blood_group(request, id):
    blood = StockIncrease.objects.get(id=id)
    return render(request, 'update-blood-group.html', {'blood':blood})

def update_blood_group(request, id):
    blood = StockIncrease.objects.get(id=id)
    if request.method == 'POST':
        blood_group = request.POST['blood-group']

        blood.blood_group = blood_group
        blood.save()
        messages.info(request, 'Blood Group Updated Successfully...')
        return redirect('/stock-increase')


# --------------------------------------------------------------------

# --------------------------------------------------------------------

# Search section

# search using address
def search_address(request):
    donor_search_list = ''
    if request.method == 'POST':
        search = request.POST['search']
        donor = NewDonor.objects.filter(home_address__icontains=search)

        donor_list = []
        donor_search_list = []

        for donors in donor:
            donor_list.append(donors.id)

        for ids in donor_list:
            donor_list = NewDonor.objects.filter(id=ids)
            donor_search_list.append(donor_list)
        donor_search_list = list(chain(*donor_search_list))
    return render(request, 'search-address.html', {'donor_search_list': donor_search_list})

# search blood group
def search_blood(request):
    donor_search_list = ''
    if request.method == 'POST':
        search = request.POST['search']
        donor = NewDonor.objects.filter(blood_group__icontains=search)

        donor_list = []
        donor_search_list = []

        for donors in donor:
            donor_list.append(donors.id)

        for ids in donor_list:
            donor_list = NewDonor.objects.filter(id=ids)
            donor_search_list.append(donor_list)
        donor_search_list = list(chain(*donor_search_list))
    return render(request, 'search-blood.html', {'donor_search_list': donor_search_list})


def search_blood_rate_month(request):
    blood_search_list = ''
    if request.method == 'POST':
        search = request.POST['search']
        blood = History.objects.filter(month__icontains=search)

        blood_list = []
        blood_search_list = []

        for bloods in blood:
            blood_list.append(bloods.id)

        for ids in blood_list:
            blood_list = History.objects.filter(id=ids)
            blood_search_list.append(blood_list)
        blood_search_list = list(chain(*blood_search_list))
    return render(request, 'charts-monthly.html', {'blood_search_list': blood_search_list})


def search_blood_rate_year(request):
    blood_search_list = ''
    if request.method == 'POST':
        search = request.POST['search']
        blood = History.objects.filter(year__icontains=search)

        blood_list = []
        blood_search_list = []

        for bloods in blood:
            blood_list.append(bloods.id)

        for ids in blood_list:
            blood_list = History.objects.filter(id=ids)
            blood_search_list.append(blood_list)
        blood_search_list = list(chain(*blood_search_list))
    return render(request, 'charts-yearly.html', {'blood_search_list': blood_search_list})


# --------------------------------------------------------------------

# --------------------------------------------------------------------

# Sending Email function

bock = False

def try_sending_email(request, id):
    donor = NewDonor.objects.get(id=id)
    return render(request, 'send-email.html', {'donor':donor})

def bock_sending_email(request):
    bock = True
    donors = NewDonor.objects.all()
    return render(request, 'send-email.html', {'donors':donors, "bock":bock})

def send_email(request):
    donor = NewDonor.objects.all()
    if request.method == 'POST':
        smtp_port = 587
        smtp_server = "smtp.gmail.com"
        email_from = ""
        email_to = [email.email for email in donor]
        print(email_to)
        body_message = request.POST['message']
        # email = request.POST['email']
        # title = request.POST['title']

        # pwd = 'dbkheifamfbarjya'
        pwd = ''

        sample_email_context = ssl.create_default_context()



        try:
            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls(context=sample_email_context)
            TIE_server.login(email_from, pwd)

            TIE_server.sendmail(email_from, email_to, body_message)
            messages.info(request, 'Email send successfully....')
            return redirect('all-donor')

        except Exception as e:
            messages.info(request, e)
            return redirect('all-donor')
    

# --------------------------------------------------------------------
