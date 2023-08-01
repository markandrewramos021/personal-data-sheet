from django.shortcuts import render,redirect
from django.http import HttpResponse
from social_django import *
from datetime import date
import time
import datetime
from datetime import *
from django.contrib.auth.models import User
from .models import *
import os
from django.views.generic import View
from django.template.loader import get_template
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate,login,logout
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from PyPDF2 import PdfMerger
# from reportlab.lib.pagesizes import Folio
from reportlab.lib.units import mm, inch
#from reportlab.platypus import Table , TableStyle , SimpleDocTemplate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect(f'admindashboard/{user.pk}')
    return render(request, 'index.html')


@login_required(login_url='loginpage')
def userdashboard(request):
    if request.user.is_authenticated and  request.user.is_staff == 0:
        data = personal.objects.filter(authUser_id=request.user.id).all()
        context = {"data":data}
        return render(request, 'userdashboard.html',context)
    else:
        return redirect('logout')

@login_required(login_url='loginpage')
def personalinfo(request):
    if request.user.is_authenticated and  request.user.is_staff == 0:
        if request.method=='POST':
            print('asdasd')
            surname1=request.POST.get('surname')
            firstname1=request.POST.get('firstname')
            middlename1=request.POST.get('middlename')
            date_of_birth1=request.POST.get('date_of_birth')
            print(date_of_birth1)
            place_of_birth1=request.POST.get('place_of_birth')
            sex1=request.POST.get('sex')
            citizenship1=request.POST.get('citizenship')
            civil_status1=request.POST.get('civil_status')
            bloodtype1=request.POST.get('bloodtype')
            height1=request.POST.get('height')
            weight1=request.POST.get('weight')
            gsis1=request.POST.get('gsis')
            agency_no1=request.POST.get('agency_no')
            pagibig1=request.POST.get('pagibig')
            philhealth1=request.POST.get('philhealth')
            sss1=request.POST.get('sss')
            telno1=request.POST.get('telno')
            mobile1=request.POST.get('mobile')
            email1=request.POST.get('email')
            tin1=request.POST.get('tin')
            name_ext1=request.POST.get('name_ext')

            res_block1=request.POST.get('res_block')
            res_street1=request.POST.get('res_street')
            res_subd1=request.POST.get('res_subd')
            res_brgy1=request.POST.get('res_brgy')
            res_city1=request.POST.get('res_city')
            res_prov1=request.POST.get('res_prov')
            res_zip1=request.POST.get('res_zip')

            per_block1=request.POST.get('per_block')
            per_street1=request.POST.get('per_street')
            per_subd1=request.POST.get('per_subd')
            per_brgy1=request.POST.get('per_brgy')
            per_city1=request.POST.get('per_city')
            per_prov1=request.POST.get('per_prov')
            per_zip1=request.POST.get('per_zip')
            if personal_information.objects.filter(authUser_id=request.user.id).values_list('authUser_id',flat=True).first() != request.user.id:
                personal_information.objects.create(
                    surname=surname1,firstname=firstname1,authUser_id=request.user.id,middlename=middlename1,date_of_birth=date_of_birth1,place_of_birth=place_of_birth1,sex=sex1,
                    citizenship=citizenship1,civil_status=civil_status1,bloodtype=bloodtype1,height=height1,weight=weight1,gsis=gsis1,
                    agency_no=agency_no1,pagibig=pagibig1,philhealth=philhealth1,sss=sss1,telno=telno1,mobile=mobile1,email=email1,tin=tin1,name_ext=name_ext1,
                    res_block=res_block1, res_street=res_street1, res_subd=res_subd1, res_brgy=res_brgy1, res_city=res_city1, res_prov=res_prov1, res_zip=res_zip1,
                    per_block=per_block1, per_street=per_street1, per_subd=per_subd1, per_brgy=per_brgy1, per_city=per_city1, per_prov=per_prov1, per_zip=per_zip1,
                    )
                return redirect('personalinfo')
            else: 
                personal_information.objects.update(
                    surname=surname1,firstname=firstname1,authUser_id=request.user.id,middlename=middlename1,date_of_birth=date_of_birth1,place_of_birth=place_of_birth1,sex=sex1,
                    citizenship=citizenship1,civil_status=civil_status1,bloodtype=bloodtype1,height=height1,weight=weight1,gsis=gsis1,
                    agency_no=agency_no1,pagibig=pagibig1,philhealth=philhealth1,sss=sss1,telno=telno1,mobile=mobile1,email=email1,tin=tin1,name_ext=name_ext1,
                    res_block=res_block1, res_street=res_street1, res_subd=res_subd1, res_brgy=res_brgy1, res_city=res_city1, res_prov=res_prov1, res_zip=res_zip1,
                    per_block=per_block1, per_street=per_street1, per_subd=per_subd1, per_brgy=per_brgy1, per_city=per_city1, per_prov=per_prov1, per_zip=per_zip1,
                    )
                return redirect('personalinfo')
        data = personal.objects.filter(authUser_id=request.user.id).all()
        context = {"data":data}
        return render(request, 'personalinfo.html',context)
    else:
        return redirect('logout')

@login_required(login_url='loginpage')
def familybackground(request):
    if request.user.is_authenticated and  request.user.is_staff == 0:
        if request.method=='POST' and 'save' in request.POST:
            spouse_surname1=request.POST.get('spouse_surname')
            spouse_firstname1=request.POST.get('spouse_firstname')
            spouse_middlename1=request.POST.get('spouse_middlename')
            spouse_extension1=request.POST.get('spouse_extension')
            occupation1=request.POST.get('occupation')
            employee_name1=request.POST.get('employee_name')
            business_address1=request.POST.get('business_address')
            family_telno1=request.POST.get('family_telno')
            father_surname1=request.POST.get('father_surname')
            father_firstname1=request.POST.get('father_firstname')
            father_middlename1=request.POST.get('father_middlename')
            father_extension1=request.POST.get('father_extension')
            mother_surname1=request.POST.get('mother_surname')
            mother_firstname1=request.POST.get('mother_firstname')
            mother_middlename1=request.POST.get('mother_middlename')

            if family_background.objects.filter(authUser_id=request.user.id).values_list('authUser_id',flat=True).first() != request.user.id:
                family_background.objects.create(
                    spouse_surname=spouse_surname1,spouse_firstname=spouse_firstname1,authUser_id=request.user.id,spouse_middlename=spouse_middlename1, spouse_extension=spouse_extension1,
                    occupation=occupation1,employee_name=employee_name1,business_address=business_address1,family_telno=family_telno1,father_surname=father_surname1,
                    father_firstname=father_firstname1,father_middlename=father_middlename1, father_extension= father_extension1,mother_surname=mother_surname1,
                    mother_firstname=mother_firstname1,mother_middlename=mother_middlename1
                    )
                return redirect('familybackground')
            else: 
                family_background.objects.update(
                    spouse_surname=spouse_surname1,spouse_firstname=spouse_firstname1,authUser_id=request.user.id,spouse_middlename=spouse_middlename1, spouse_extension=spouse_extension1,
                    occupation=occupation1,employee_name=employee_name1,business_address=business_address1,family_telno=family_telno1,father_surname=father_surname1,
                    father_firstname=father_firstname1,father_middlename=father_middlename1, father_extension= father_extension1,mother_surname=mother_surname1,
                    mother_firstname=mother_firstname1,mother_middlename=mother_middlename1
                    )
                return redirect('familybackground')
        if request.method=='POST' and 'add' in request.POST:
            name1=request.POST.get('name')
            date_birth1=request.POST.get('date_birth')

            children.objects.create(
                name=name1,date_birth=date_birth1, authUser_id=request.user.id
            )
            return redirect('familybackground')
        child = personal.objects.filter(authUser_id=request.user.id).all()
        child1 = children.objects.filter(authUser_id=request.user.id).all()

        data = personal.objects.filter(authUser_id=request.user.id).all()
        context = {"data":data,"child":child,"child1":child1}
        return render(request, 'familybackground.html',context)
    else:
        return redirect('logout')

@login_required(login_url='loginpage')
def educationalbackground(request):
    if request.user.is_authenticated and  request.user.is_staff == 0:
        if request.method=='POST':
            elem_school1=request.POST.get('elem_school')
            elem_course1=request.POST.get('elem_course')
            elem_attendance_from1=request.POST.get('elem_attendance_from')
            elem_attendance_to1=request.POST.get('elem_attendance_to')
            elem_units1=request.POST.get('elem_units')
            elem_grad1=request.POST.get('elem_grad')
            elem_honors1=request.POST.get('elem_honors')
            
            secondary_school1=request.POST.get('secondary_school')
            secondary_course1=request.POST.get('secondary_course')
            secondary_attendance_from1=request.POST.get('secondary_attendance_from')
            secondary_attendance_to1=request.POST.get('secondary_attendance_to')
            secondary_units1=request.POST.get('secondary_units')
            secondary_grad1=request.POST.get('secondary_grad')
            secondary_honors1=request.POST.get('secondary_honors')

            vocational_school1=request.POST.get('vocational_school')
            vocational_course1=request.POST.get('vocational_course')
            vocational_attendance_from1=request.POST.get('vocational_attendance_from')
            vocational_attendance_to1=request.POST.get('vocational_attendance_to')
            vocational_units1=request.POST.get('vocational_units')
            vocational_grad1=request.POST.get('vocational_grad')
            vocational_honors1=request.POST.get('vocational_honors')

            college_school1=request.POST.get('college_school')
            college_course1=request.POST.get('college_course')
            college_attendance_from1=request.POST.get('college_attendance_from')
            college_attendance_to1=request.POST.get('college_attendance_to')
            college_units1=request.POST.get('college_units')
            college_grad1=request.POST.get('college_grad')
            college_honors1=request.POST.get('college_honors')

            grad_school1=request.POST.get('grad_school')
            grad_course1=request.POST.get('grad_course')
            grad_attendance_to1=request.POST.get('grad_attendance_to')
            grad_attendance_from1=request.POST.get('grad_attendance_from')
            grad_attendance_to1=request.POST.get('grad_attendance_to')        
            grad_units1=request.POST.get('grad_units')
            grad_grad1=request.POST.get('grad_grad')
            grad_honors1=request.POST.get('grad_honors')
            if educational_background.objects.filter(authUser_id=request.user.id).values_list('authUser_id',flat=True).first() != request.user.id:
                educational_background.objects.create(
                    elem_school=elem_school1,elem_course=elem_course1,authUser_id=request.user.id,elem_attendance_from=elem_attendance_from1,elem_attendance_to=elem_attendance_to1,
                    elem_units=elem_units1,elem_grad=elem_grad1,elem_honors=elem_honors1,

                    secondary_school=secondary_school1,secondary_course=secondary_course1,secondary_attendance_from=secondary_attendance_from1,
                    secondary_attendance_to=secondary_attendance_to1,secondary_units=secondary_units1,secondary_grad=secondary_grad1,secondary_honors=secondary_honors1,
                    
                    vocational_school=vocational_school1,vocational_course=vocational_course1,vocational_attendance_from=vocational_attendance_from1,
                    vocational_attendance_to=vocational_attendance_to1,vocational_units=vocational_units1,vocational_grad=vocational_grad1,vocational_honors=vocational_honors1,

                    college_school=college_school1,college_course=college_course1,college_attendance_from=college_attendance_from1,college_attendance_to=college_attendance_to1,
                    college_units=college_units1,college_grad=college_grad1,college_honors=college_honors1,

                    grad_school=grad_school1,grad_course=grad_course1,grad_units=grad_units1,grad_grad=grad_grad1,
                    grad_attendance_from=grad_attendance_from1,grad_attendance_to=grad_attendance_to1,grad_honors=grad_honors1
                    )
            else: 
                educational_background.objects.update(
                    elem_school=elem_school1,elem_course=elem_course1,authUser_id=request.user.id,elem_attendance_from=elem_attendance_from1,elem_attendance_to=elem_attendance_to1,
                    elem_units=elem_units1,elem_grad=elem_grad1,elem_honors=elem_honors1,

                    secondary_school=secondary_school1,secondary_course=secondary_course1,secondary_attendance_from=secondary_attendance_from1,
                    secondary_attendance_to=secondary_attendance_to1,secondary_units=secondary_units1,secondary_grad=secondary_grad1,secondary_honors=secondary_honors1,
                    
                    vocational_school=vocational_school1,vocational_course=vocational_course1,vocational_attendance_from=vocational_attendance_from1,
                    vocational_attendance_to=vocational_attendance_to1,vocational_units=vocational_units1,vocational_grad=vocational_grad1,vocational_honors=vocational_honors1,

                    college_school=college_school1,college_course=college_course1,college_attendance_from=college_attendance_from1,college_attendance_to=college_attendance_to1,
                    college_units=college_units1,college_grad=college_grad1,college_honors=college_honors1,

                    grad_school=grad_school1,grad_course=grad_course1,grad_units=grad_units1,grad_grad=grad_grad1,
                    grad_attendance_from=grad_attendance_from1,grad_attendance_to=grad_attendance_to1,grad_honors=grad_honors1
                    )
        data = personal.objects.filter(authUser_id=request.user.id).all()
        data1 = educational_background.objects.filter(authUser_id=request.user.id).all()
        context = {"data":data, "data1":data1}
        return render(request, 'educationalbackground.html',context)
    return redirect(logout)

@login_required(login_url='loginpage')
def civilservice(request):
    if request.user.is_authenticated and  request.user.is_staff == 0:
        if request.method=='POST':
            eligibility1=request.POST.get('eligibility')
            rating1=request.POST.get('rating')
            exam_date1=request.POST.get('exam_date')
            exam_place1=request.POST.get('exam_place')
            license_number1=request.POST.get('license_number')
            license_validity_date1=request.POST.get('license_validity_date')
            civil_service_eligibility.objects.create(
                eligibility=eligibility1,rating=rating1, exam_date=exam_date1,exam_place=exam_place1,
                license_validity_date=license_validity_date1,license_number=license_number1, authUser_id=request.user.id
            )
        data = personal.objects.filter(authUser_id=request.user.id).all()        
        data1 = civil_service_eligibility.objects.filter(authUser_id=request.user.id).all()
        context = {"data":data, "data1":data1}
        return render(request, 'civilservice.html', context)
    else:
        return redirect(logout)

@login_required(login_url='loginpage')
def workexperience(request):
    if request.user.is_authenticated and  request.user.is_staff == 0:
        if request.method=='POST':
            date_from1=request.POST.get('date_from')
            date_to1=request.POST.get('date_to')
            position1=request.POST.get('position')
            department1=request.POST.get('department')
            monthly_salary1=request.POST.get('monthly_salary')
            salary_grade1=request.POST.get('salary_grade')
            status1=request.POST.get('status')
            gov_service1=request.POST.get('gov_service')
            work_experience.objects.create(
                date_from=date_from1, date_to=date_to1, position=position1, department=department1, monthly_salary=monthly_salary1, salary_grade=salary_grade1,
                status=status1, gov_service=gov_service1 , authUser_id=request.user.id
            )
        data = personal.objects.filter(authUser_id=request.user.id).all()
        data1 = work_experience.objects.filter(authUser_id=request.user.id).all().order_by('-id')
        context = {"data":data,"data1":data1}
        return render(request, 'workexperience.html',context)
    return redirect(logout)

@login_required(login_url='loginpage')
def voluntarywork(request):
    if request.user.is_authenticated and  request.user.is_staff == 0:
        if request.method=='POST':
            org_info1=request.POST.get('org_info')
            date_from1=request.POST.get('date_from')
            date_to1=request.POST.get('date_to')
            work_hours1=request.POST.get('work_hours')
            position1=request.POST.get('position')
            voluntary_work.objects.create(
                org_info=org_info1, date_from=date_from1, date_to=date_to1, work_hours=work_hours1, position=position1, authUser_id=request.user.id
            )
        data = personal.objects.filter(authUser_id=request.user.id).all()
        data1 = voluntary_work.objects.filter(authUser_id=request.user.id).all()
        context = {"data":data,"data1":data1}
        return render(request, 'voluntarywork.html', context)
    return redirect(logout)

@login_required(login_url='loginpage')
def learning(request):
    if request.user.is_authenticated and  request.user.is_staff == 0:
        if request.method=='POST':
            title1=request.POST.get('title')
            attendance_from1=request.POST.get('attendance_from')
            attendance_to1=request.POST.get('attendance_to')
            hours1=request.POST.get('hours')
            ld1=request.POST.get('ld')
            conducted1=request.POST.get('conducted')
            learning_development.objects.create(
                title=title1, date_of_attendance_from=attendance_from1, date_of_attendance_to=attendance_to1, work_hours=hours1, type_of_ld=ld1, conducted=conducted1, authUser_id=request.user.id
            )
        data = personal.objects.filter(authUser_id=request.user.id).all()
        data1 = learning_development.objects.filter(authUser_id=request.user.id).all()
        context = {"data":data,"data1":data1}
        return render(request, 'learning.html', context)
    return redirect(logout)

@login_required(login_url='loginpage')
def otherinfo(request):
    if request.user.is_authenticated and  request.user.is_staff == 0:
        if request.method=='POST' and 'save' in request.POST:
            name11=request.POST.get('name1')
            name21=request.POST.get('name2')
            name31=request.POST.get('name3')
            address11=request.POST.get('address1')
            address21=request.POST.get('address2')
            address31=request.POST.get('address3')
            telno11=request.POST.get('telno1')
            telno21=request.POST.get('telno2')
            telno31=request.POST.get('telno3')
            gov_id1=request.POST.get('gov_id')
            license_id1=request.POST.get('license_id')
            date1=request.POST.get('date')
            indigenous1=request.POST.get('indigenous')
            indig_group1=request.POST.get('indig_group')
            disability1=request.POST.get('disability')
            disab_group1=request.POST.get('disab_group')
            solo1=request.POST.get('solo')
            solo_group1=request.POST.get('solo_group')



            if references.objects.filter(authUser_id=request.user.id).values_list('authUser_id',flat=True).first() != request.user.id:
                references.objects.create(
                    name1=name11, name2=name21,name3=name31, address1=address11, address2=address21, address3=address31, telno1=telno11, telno2=telno21, telno3=telno31,
                    gov_id=gov_id1, license_id=license_id1, date=date1, authUser_id=request.user.id, indigenous=indigenous1, indig_specify = indig_group1, disability = disability1,
                    disab_specify = disab_group1, solo_parent = solo1, solo_specify = solo_group1
                    )
                return redirect('otherinfo')
            else: 
                references.objects.update(
                    name1=name11, name2=name21,name3=name31, address1=address11, address2=address21, address3=address31, telno1=telno11, telno2=telno21, telno3=telno31,
                    gov_id=gov_id1, license_id=license_id1, date=date1,authUser_id=request.user.id, indigenous=indigenous1, indig_specify = indig_group1, disability = disability1,
                    disab_specify = disab_group1, solo_parent = solo1, solo_specify = solo_group1
                    )
                return redirect('otherinfo')
            

        if request.method=='POST' and 'add' in request.POST:
            skills_hobbies1=request.POST.get('skills_hobbies')
            non_acad_recognition1=request.POST.get('non_acad_recognition')
            membership1=request.POST.get('membership')
            other_info.objects.create(
                skills_hobbies=skills_hobbies1, non_acad_recognition=non_acad_recognition1,authUser_id=request.user.id,membership=membership1)
        data = personal.objects.filter(authUser_id=request.user.id).all()
        data1 = other_info.objects.filter(authUser_id=request.user.id).all()
        data2 = references.objects.filter(authUser_id=request.user.id).all()
        dis = references.objects.filter(authUser_id=request.user.id)
        context = {"data":data,"data1":data1,"data2":data2,'dis':dis}
        return render(request, 'otherinfo.html',context)
    return redirect(logout)

@login_required(login_url='loginpage')
def admindashboard(request,pk):
    if request.user.is_authenticated and  request.user.is_staff == 1:
        data = User.objects.all().exclude(is_staff=1)
        if 'q' in request.GET:
            q=request.GET['q']
            data = User.objects.filter(first_name__icontains=q).exclude(is_staff=1) | User.objects.filter(last_name__icontains=q).exclude(is_staff=1)
            return render(request, 'admindashboard.html',{'data':data})
        else:
            q = False
        return render(request, 'admindashboard.html',{'data':data})
    return redirect(logout)

@login_required(login_url='loginpage')
def admindashboard_activate(request, pk):
    if request.user.is_authenticated and  request.user.is_staff == 1:
        User.objects.filter(id=pk).update(is_active=1)
        print(User.objects.filter(id=pk).values_list('id',flat=True).first())
        return redirect('admindashboard', pk=request.user.id)
    return redirect(logout)

@login_required(login_url='loginpage')
def viewuser(request,pk):
    if request.user.is_authenticated and  request.user.is_staff == 1:
        if request.user.is_authenticated:
            data = User.objects.get(id=pk)
            prim = User.objects.filter(id=pk).values_list('id',flat=True)
            print(prim)
            child1 = children.objects.filter(authUser_id=pk).all()
            civil1 = civil_service_eligibility.objects.filter(authUser_id=pk).all()
            work1 = work_experience.objects.filter(authUser_id=pk).all()
            voluntary1 = voluntary_work.objects.filter(authUser_id=pk).all()
            learning1 = learning_development.objects.filter(authUser_id=pk).all()
            other1 = other_info.objects.filter(authUser_id=pk).all()
            references1 = references.objects.filter(authUser_id=pk).all()
            return render(request, 'viewuser.html',{'data':data,'child1':child1,'civil1':civil1,'work1':work1,'voluntary1':voluntary1,'learning1':learning1,
                                                    'other1':other1,'references1':references1})
    return redirect(logout)

@login_required(login_url='loginpage')
def admindashboard_deactivate(request, pk):
    if request.user.is_authenticated and  request.user.is_staff == 1:
        User.objects.filter(id=pk).update(is_active=0)
        return redirect('admindashboard', pk=request.user.id)
    return redirect(logout)

@login_required(login_url='loginpage')
def report(request, pk):
    if request.user.is_authenticated and  request.user.is_staff == 1:
        osds = personal.objects.filter(unit="Office of the SDS").count()
        oasds = personal.objects.filter(unit="Office of the ASDS").count()
        legal = personal.objects.filter(unit="Legal Services").count()
        ict = personal.objects.filter(unit="ICT Services").count()
        administrative = personal.objects.filter(unit="Administrative Services").count()
        personnel = personal.objects.filter(unit="Personnel").count()
        records = personal.objects.filter(unit="Records").count()
        cashier = personal.objects.filter(unit="Cashier").count()
        supply = personal.objects.filter(unit="Supply & Property").count()
        budget = personal.objects.filter(unit="Budget").count()
        finance = personal.objects.filter(unit="Finance").count()
        cid = personal.objects.filter(unit="CID").count()
        learning = personal.objects.filter(unit="Learning Resource Management").count()
        curriculum = personal.objects.filter(unit="Curriculum Implementation Management").count()
        district = personal.objects.filter(unit="District Instructional Management").count()
        alternative = personal.objects.filter(unit="Alternative Learning System").count()
        sgod = personal.objects.filter(unit="SGOD").count()
        monitoring = personal.objects.filter(unit="Monitoring & Evaluation").count()
        human = personal.objects.filter(unit="Human Resource Development").count()
        social = personal.objects.filter(unit="Social Mobilization").count()
        planning = personal.objects.filter(unit="Planning & Research").count()
        education = personal.objects.filter(unit="Education Facilities").count()
        health = personal.objects.filter(unit="Health & Nutrition Unit").count()

        context = {'osds':osds,'oasds':oasds,'legal':legal,'ict':ict,'administrative':administrative,'personnel':personnel,'records':records,
                'cashier':cashier,'supply':supply,'budget':budget,'finance':finance,'cid':cid,'learning':learning,'curriculum':curriculum,
                'district':district,'alternative':alternative,'sgod':sgod,'monitoring':monitoring,'human':human,'social':social,
                'planning':planning,'education':education,'health':health}
        return render(request, 'report.html', context)
    return redirect(logout)

@login_required(login_url='loginpage')
def editprofile(request):
    if request.user.is_authenticated and  request.user.is_staff == 0:
        data = personal.objects.filter(authUser_id=request.user.id).all()
        context = {"data":data} 
        try:
            if request.method=='POST':
                division1=request.POST.get('division')
                unit1=request.POST.get('unit')
                image1 = request.FILES['image']
                if personal.objects.filter(authUser_id=request.user.id).values_list('authUser_id',flat=True).first() != request.user.id:
                    personal.objects.create(division=division1,unit=unit1,authUser_id=request.user.id,image=image1)
                else:
                    one = personal.objects.filter(authUser_id=request.user.id).values_list('id',flat=True).first()
                    two = personal.objects.get(id=one)
                    two.delete()
                    personal.objects.create(division=division1,unit=unit1,authUser_id=request.user.id,image=image1)

        except:
            pass
        return render(request, 'editprofile.html',context)
    return redirect(logout)

@login_required(login_url='loginpage')
def generate_pdf(request):
    if request.user.is_authenticated and  request.user.is_staff == 0:
        pagesize1 = (8.5 * inch, 13 * inch)  # 20 inch width and 10 inch height.

        surname =personal_information.objects.filter(authUser_id=request.user.id).values_list('surname',flat=True).first() 
        firstname =personal_information.objects.filter(authUser_id=request.user.id).values_list('firstname',flat=True).first() 
        middlename =personal_information.objects.filter(authUser_id=request.user.id).values_list('middlename',flat=True).first()
        name_ext =personal_information.objects.filter(authUser_id=request.user.id).values_list('name_ext',flat=True).first()
        date_of_birth =personal_information.objects.filter(authUser_id=request.user.id).values_list('date_of_birth',flat=True).first() 
        place_of_birth =personal_information.objects.filter(authUser_id=request.user.id).values_list('place_of_birth',flat=True).first() 
        sex =personal_information.objects.filter(authUser_id=request.user.id).values_list('sex',flat=True).first()
        civil_status =personal_information.objects.filter(authUser_id=request.user.id).values_list('civil_status',flat=True).first()
        height =personal_information.objects.filter(authUser_id=request.user.id).values_list('height',flat=True).first()
        weight =personal_information.objects.filter(authUser_id=request.user.id).values_list('weight',flat=True).first()
        bloodtype =personal_information.objects.filter(authUser_id=request.user.id).values_list('bloodtype',flat=True).first()
        gsis =personal_information.objects.filter(authUser_id=request.user.id).values_list('gsis',flat=True).first()
        pagibig =personal_information.objects.filter(authUser_id=request.user.id).values_list('pagibig',flat=True).first()
        philhealth =personal_information.objects.filter(authUser_id=request.user.id).values_list('philhealth',flat=True).first()
        sss =personal_information.objects.filter(authUser_id=request.user.id).values_list('sss',flat=True).first()
        tin =personal_information.objects.filter(authUser_id=request.user.id).values_list('tin',flat=True).first()
        agency_no =personal_information.objects.filter(authUser_id=request.user.id).values_list('agency_no',flat=True).first()
        telno =personal_information.objects.filter(authUser_id=request.user.id).values_list('telno',flat=True).first()
        mobile =personal_information.objects.filter(authUser_id=request.user.id).values_list('mobile',flat=True).first()
        email =personal_information.objects.filter(authUser_id=request.user.id).values_list('email',flat=True).first()


        surname1 = f'{surname}'
        firstname1 = f'{firstname}'
        middlename1 = f'{middlename}'
        name_ext1 = f'{name_ext}'
        date_of_birth1 = f'{date_of_birth.month}/{date_of_birth.day}/{date_of_birth.year}'
        place_of_birth1 = f'{place_of_birth}'
        sex1 = f'{sex}'
        civil_status1 = f'{civil_status}'
        height1 = f'{height}'
        weight1 = f'{weight}'
        bloodtype1 = f'{bloodtype}'
        gsis1 = f'{gsis}'
        pagibig1 = f'{pagibig}'
        philhealth1 = f'{philhealth}'
        sss1 = f'{sss}'
        tin1 = f'{tin}'
        agency_no1 = f'{agency_no}'
        telno1 = f'{telno}'
        mobile1 = f'{mobile}'
        email1 = f'{email}'

        packet = io.BytesIO()

        p = canvas.Canvas(packet, pagesize= pagesize1)  

        p.setFont("Helvetica", 6)             # Init a PDF object
        p.drawString(135, 715, surname1)          # Draw a simple String    
        p.drawString(135, 700, firstname1)
        p.drawString(510, 700, name_ext1) 
        p.drawString(135, 685, middlename1)    
        p.drawString(135, 663, date_of_birth1)  
        p.drawString(135, 641, place_of_birth1)
        if sex1 == 'Male':  
            p.drawString(136, 626, '✓')
        else:
            p.drawString(211, 624, '✓')

        if civil_status1 == 'Single':  
            p.drawString(136, 610, '✓')
        elif civil_status1 == 'Widowed': 
            p.drawString(136, 600, '✓') 
        elif civil_status1 == 'Married': 
            p.drawString(211, 610, '✓')  
        elif civil_status1 == 'Separated': 
            p.drawString(211, 600, '✓')  
        else: 
            p.drawString(136, 589, '✓')   
        
        p.drawString(135, 570, height1)
        p.drawString(135, 553, weight1)
        p.drawString(135, 536, bloodtype1)
        p.drawString(135,519, gsis1)
        p.drawString(135,500, pagibig1)
        p.drawString(135,482, philhealth1)
        p.drawString(135,464, sss1)
        p.drawString(135,445, tin1)
        p.drawString(135,428, agency_no1)
        p.drawString(338,464, telno1)
        p.drawString(338,445, mobile1)
        p.drawString(338,428, email1)
        p.drawString(382,667, '✓')

        #Address
        res_block =personal_information.objects.filter(authUser_id=request.user.id).values_list('res_block',flat=True).first()
        res_street =personal_information.objects.filter(authUser_id=request.user.id).values_list('res_street',flat=True).first()
        res_subd =personal_information.objects.filter(authUser_id=request.user.id).values_list('res_subd',flat=True).first()
        res_brgy =personal_information.objects.filter(authUser_id=request.user.id).values_list('res_brgy',flat=True).first()
        res_city =personal_information.objects.filter(authUser_id=request.user.id).values_list('res_city',flat=True).first()
        res_prov =personal_information.objects.filter(authUser_id=request.user.id).values_list('res_prov',flat=True).first()
        res_street =personal_information.objects.filter(authUser_id=request.user.id).values_list('res_street',flat=True).first()
        res_zip =personal_information.objects.filter(authUser_id=request.user.id).values_list('res_zip',flat=True).first()

        res_block1 = f'{res_block}'
        res_street1 = f'{res_street}'
        res_subd1 = f'{res_subd}'
        res_brgy1 = f'{res_brgy}'
        res_city1 = f'{res_city}'
        res_prov1 = f'{res_prov}'
        res_zip1 = f'{res_zip}'

        p.drawString(350, 608, res_block1) 
        p.drawString(460, 608, res_street1) 
        p.drawString(350, 590, res_subd1) 
        p.drawString(460, 590, res_brgy1) 
        p.drawString(350, 573, res_city1) 
        p.drawString(460, 573, res_prov1)  
        p.drawString(350, 553, res_zip1 ) 

        per_block =personal_information.objects.filter(authUser_id=request.user.id).values_list('per_block',flat=True).first()
        per_street =personal_information.objects.filter(authUser_id=request.user.id).values_list('per_street',flat=True).first()
        per_subd =personal_information.objects.filter(authUser_id=request.user.id).values_list('per_subd',flat=True).first()
        per_brgy =personal_information.objects.filter(authUser_id=request.user.id).values_list('per_brgy',flat=True).first()
        per_city =personal_information.objects.filter(authUser_id=request.user.id).values_list('per_city',flat=True).first()
        per_prov =personal_information.objects.filter(authUser_id=request.user.id).values_list('per_prov',flat=True).first()
        per_zip =personal_information.objects.filter(authUser_id=request.user.id).values_list('per_zip',flat=True).first()

        per_block1 = f'{per_block}'
        per_street1 = f'{per_street}'
        per_subd1 = f'{per_subd}'
        per_brgy1 = f'{per_brgy}'
        per_city1 = f'{per_city}'
        per_prov1 = f'{per_prov}'
        per_zip1 = f'{per_zip}'
        
        p.drawString(350, 539, per_block1) 
        p.drawString(460, 539, per_street1) 
        p.drawString(350, 521, per_subd1) 
        p.drawString(460, 521, per_brgy1) 
        p.drawString(350, 504, per_city1) 
        p.drawString(460, 504, per_prov1) 
        p.drawString(350, 482, per_zip1) 

        # Family Background
        spouse_surname =family_background.objects.filter(authUser_id=request.user.id).values_list('spouse_surname',flat=True).first()
        spouse_firstname =family_background.objects.filter(authUser_id=request.user.id).values_list('spouse_firstname',flat=True).first()
        spouse_extension =family_background.objects.filter(authUser_id=request.user.id).values_list('spouse_extension',flat=True).first()
        spouse_middlename =family_background.objects.filter(authUser_id=request.user.id).values_list('spouse_middlename',flat=True).first()
        occupation =family_background.objects.filter(authUser_id=request.user.id).values_list('occupation',flat=True).first()
        employee_name =family_background.objects.filter(authUser_id=request.user.id).values_list('employee_name',flat=True).first()    
        business_address =family_background.objects.filter(authUser_id=request.user.id).values_list('business_address',flat=True).first()  
        family_telno =family_background.objects.filter(authUser_id=request.user.id).values_list('family_telno',flat=True).first() 
        father_surname =family_background.objects.filter(authUser_id=request.user.id).values_list('father_surname',flat=True).first() 
        father_firstname =family_background.objects.filter(authUser_id=request.user.id).values_list('father_firstname',flat=True).first()
        father_extension =family_background.objects.filter(authUser_id=request.user.id).values_list('father_extension',flat=True).first()
        father_middlename =family_background.objects.filter(authUser_id=request.user.id).values_list('father_middlename',flat=True).first()   
        mother_surname =family_background.objects.filter(authUser_id=request.user.id).values_list('mother_surname',flat=True).first() 
        mother_firstname =family_background.objects.filter(authUser_id=request.user.id).values_list('mother_firstname',flat=True).first()
        mother_middlename =family_background.objects.filter(authUser_id=request.user.id).values_list('mother_middlename',flat=True).first()   
                

        spouse_surname1 = f'{spouse_surname}'
        spouse_firstname1 = f'{spouse_firstname}'
        spouse_extension1 = f'{spouse_extension}'
        spouse_middlename1 = f'{spouse_middlename}'
        occupation1 = f'{occupation}'
        employee_name1 = f'{employee_name}'
        business_address1 = f'{business_address}'
        family_telno1 = f'{family_telno}'
        father_surname1 = f'{father_surname}'
        father_firstname1 = f'{father_firstname}'
        father_extension1 = f'{father_extension}'
        father_middlename1 = f'{father_middlename}'
        mother_surname1 = f'{mother_surname}'
        mother_firstname1 = f'{mother_firstname}'
        mother_middlename1 = f'{mother_middlename}'

        p.drawString(135, 400, spouse_surname1)
        p.drawString(135, 385, spouse_firstname1)
        p.drawString(317, 385, spouse_extension1)
        p.drawString(135, 369, spouse_middlename1)
        p.drawString(135, 354, occupation1)
        p.drawString(135, 338, employee_name1)
        p.drawString(135, 323, business_address1)
        p.drawString(135, 308, family_telno1)
        p.drawString(135, 293, father_surname1)
        p.drawString(135, 278, father_firstname1)
        p.drawString(317, 278, father_extension1)
        p.drawString(135, 263, father_middlename1)
        p.drawString(135, 231, mother_surname1)
        p.drawString(135, 216, mother_firstname1)
        p.drawString(135, 201, mother_middlename1)


        #educational background
        elem_school =educational_background.objects.filter(authUser_id=request.user.id).values_list('elem_school',flat=True).first()
        elem_course =educational_background.objects.filter(authUser_id=request.user.id).values_list('elem_course',flat=True).first()
        elem_attendance_to =educational_background.objects.filter(authUser_id=request.user.id).values_list('elem_attendance_to',flat=True).first()
        elem_attendance_from =educational_background.objects.filter(authUser_id=request.user.id).values_list('elem_attendance_from',flat=True).first()
        elem_units =educational_background.objects.filter(authUser_id=request.user.id).values_list('elem_units',flat=True).first()
        elem_grad =educational_background.objects.filter(authUser_id=request.user.id).values_list('elem_grad',flat=True).first()
        elem_honors =educational_background.objects.filter(authUser_id=request.user.id).values_list('elem_honors',flat=True).first()

        elem_school1 = f'{elem_school}'
        elem_course1 = f'{elem_course}'
        elem_attendance1_to = f'{elem_attendance_to}'
        elem_attendance1_from = f'{elem_attendance_from}'
        elem_units1 = f'{elem_units}'
        elem_grad1 = f'{elem_grad}'
        elem_honors1 = f'{elem_honors}'

        if len(elem_school1) > 47:
            a = elem_school1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(130,142, top_text)
            p.drawString(130,132, bottom_text)
        
        else:
            p.drawString(130, 137, elem_school1)


        
        p.drawString(262, 137, elem_course1)
        p.drawString(380, 137, elem_attendance1_to)
        p.drawString(412, 137, elem_attendance1_from)
        p.drawString(443, 137, elem_units1)
        p.drawString(494, 137, elem_grad1)
        p.drawString(533, 137, elem_honors1)


        secondary_school =educational_background.objects.filter(authUser_id=request.user.id).values_list('secondary_school',flat=True).first()
        secondary_course =educational_background.objects.filter(authUser_id=request.user.id).values_list('secondary_course',flat=True).first()
        secondary_attendance_to =educational_background.objects.filter(authUser_id=request.user.id).values_list('secondary_attendance_to',flat=True).first()
        secondary_attendance_from =educational_background.objects.filter(authUser_id=request.user.id).values_list('secondary_attendance_from',flat=True).first()
        secondary_units =educational_background.objects.filter(authUser_id=request.user.id).values_list('secondary_units',flat=True).first()
        secondary_grad =educational_background.objects.filter(authUser_id=request.user.id).values_list('secondary_grad',flat=True).first()
        secondary_honors =educational_background.objects.filter(authUser_id=request.user.id).values_list('secondary_honors',flat=True).first()

        secondary_school1 = f'{secondary_school}'
        secondary_course1 = f'{secondary_course}'
        secondary_attendance1_to = f'{secondary_attendance_to}'
        secondary_attendance1_from = f'{secondary_attendance_from}'
        secondary_units1 = f'{secondary_units}'
        secondary_grad1 = f'{secondary_grad}'
        secondary_honors1 = f'{secondary_honors}'

        if len(secondary_school1) > 47:
            a = secondary_school1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(130,122, top_text)
            p.drawString(130,112, bottom_text)
        
        else:
            p.drawString(130, 115, secondary_school1)   

        if len(secondary_course1) > 40:
            a = secondary_course1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(258,121, top_text)
            p.drawString(258,112, bottom_text)
        
        else:
            p.drawString(258, 115, secondary_course1)

        
        p.drawString(380, 115,  secondary_attendance1_to)
        p.drawString(412, 115, secondary_attendance1_from)
        p.drawString(443, 115, secondary_units1)
        p.drawString(494, 115, secondary_grad1)
        p.drawString(533, 115, secondary_honors1)

        vocational_school =educational_background.objects.filter(authUser_id=request.user.id).values_list('vocational_school',flat=True).first()
        vocational_course =educational_background.objects.filter(authUser_id=request.user.id).values_list('vocational_course',flat=True).first()
        vocational_attendance_to =educational_background.objects.filter(authUser_id=request.user.id).values_list('vocational_attendance_to',flat=True).first()
        vocational_attendance_from =educational_background.objects.filter(authUser_id=request.user.id).values_list('vocational_attendance_from',flat=True).first()
        vocational_units =educational_background.objects.filter(authUser_id=request.user.id).values_list('vocational_units',flat=True).first()
        vocational_grad =educational_background.objects.filter(authUser_id=request.user.id).values_list('vocational_grad',flat=True).first()
        vocational_honors =educational_background.objects.filter(authUser_id=request.user.id).values_list('vocational_honors',flat=True).first()

        vocational_school1 = f'{vocational_school}'
        vocational_course1 = f'{vocational_course}'
        vocational_attendance1_to = f'{vocational_attendance_to}'
        vocational_attendance1_from = f'{vocational_attendance_from}'
        vocational_units1 = f'{vocational_units}'
        vocational_grad1 = f'{vocational_grad}'
        vocational_honors1 = f'{vocational_honors}'   

        if len(vocational_school1) > 47:
            a = vocational_school1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(130,102, top_text)
            p.drawString(130,92, bottom_text)
        
        else:
            p.drawString(130, 95, vocational_school1)

        if len(vocational_course1) > 40:
            a = vocational_course1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(258,102, top_text)
            p.drawString(258,92, bottom_text)
        
        else:
            p.drawString(258, 95, vocational_course1)

        
        p.drawString(380, 95, vocational_attendance1_to)
        p.drawString(412, 95, vocational_attendance1_from)
        p.drawString(443, 95, vocational_units1)
        p.drawString(494, 95, vocational_grad1)
        p.drawString(533, 95, vocational_honors1)

        college_school =educational_background.objects.filter(authUser_id=request.user.id).values_list('college_school',flat=True).first()
        college_course =educational_background.objects.filter(authUser_id=request.user.id).values_list('college_course',flat=True).first()
        college_attendance_to =educational_background.objects.filter(authUser_id=request.user.id).values_list('college_attendance_to',flat=True).first()
        college_attendance_from =educational_background.objects.filter(authUser_id=request.user.id).values_list('college_attendance_from',flat=True).first()
        college_units =educational_background.objects.filter(authUser_id=request.user.id).values_list('college_units',flat=True).first()
        college_grad =educational_background.objects.filter(authUser_id=request.user.id).values_list('college_grad',flat=True).first()
        college_honors =educational_background.objects.filter(authUser_id=request.user.id).values_list('college_honors',flat=True).first()

        college_school1 = f'{college_school}'
        college_course1 = f'{college_course}'
        college_attendance1_to = f'{college_attendance_to}'
        college_attendance1_from = f'{college_attendance_from}'
        college_units1 = f'{college_units}'
        college_grad1 = f'{college_grad}'
        college_honors1 = f'{college_honors}'   

        if len(college_school1) > 47:
            a = college_school1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(130,82, top_text)
            p.drawString(130,72, bottom_text)
        
        else:
            p.drawString(130, 75, college_school1)

        if len(college_course1) > 40:
            a = college_course1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(258,82, top_text)
            p.drawString(258,72, bottom_text)
        
        else:
            p.drawString(258, 75, college_course1)

        p.drawString(380, 75, college_attendance1_to)
        p.drawString(412, 75, college_attendance1_from)
        p.drawString(443, 75, college_units1)
        p.drawString(494, 75, college_grad1)
        p.drawString(533, 75, college_honors1)
        
        grad_school =educational_background.objects.filter(authUser_id=request.user.id).values_list('grad_school',flat=True).first()
        grad_course =educational_background.objects.filter(authUser_id=request.user.id).values_list('grad_course',flat=True).first()
        grad_attendance_to =educational_background.objects.filter(authUser_id=request.user.id).values_list('grad_attendance_to',flat=True).first()
        grad_attendance_from =educational_background.objects.filter(authUser_id=request.user.id).values_list('grad_attendance_from',flat=True).first()
        grad_units =educational_background.objects.filter(authUser_id=request.user.id).values_list('grad_units',flat=True).first()
        grad_grad =educational_background.objects.filter(authUser_id=request.user.id).values_list('grad_grad',flat=True).first()
        grad_honors =educational_background.objects.filter(authUser_id=request.user.id).values_list('grad_honors',flat=True).first()

        grad_school1 = f'{grad_school}'
        grad_course1 = f'{grad_course}'
        grad_attendance1_to = f'{grad_attendance_to}'
        grad_attendance1_from = f'{grad_attendance_from}'
        grad_units1 = f'{grad_units}'
        grad_grad1 = f'{grad_grad}'
        grad_honors1 = f'{grad_honors}'  

        if len(grad_school1) > 47:
            a = grad_school1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(130,62, top_text)
            p.drawString(130,52, bottom_text)
        
        else:
            p.drawString(130, 54, grad_school1) 

        if len(grad_course1) > 40:
            a = grad_course1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(258, 62, top_text)
            p.drawString(258, 52, bottom_text)
        
        else:
            p.drawString(258, 54, grad_course1)

        
        p.drawString(380, 54, grad_attendance1_to)
        p.drawString(412, 54, grad_attendance1_from)
        p.drawString(443, 54, grad_units1)
        p.drawString(494, 54, grad_grad1)
        p.drawString(533, 54, grad_honors1)

        anak = children.objects.all().filter(authUser_id=request.user.id).order_by('-id')

        data2 = [['','']]
        for child in anak:
            data2.append([child.name, child.date_birth.month, child.date_birth.day, child.date_birth.year])

        startingx = 338
        startingy = 385

        try:
            data2[1]
            p.drawString(startingx, startingy, (data2[1])[0])
            p.drawString(startingx+150, startingy, str(str((data2[1])[1])+"/"))
            p.drawString(startingx+159, startingy, str(str((data2[1])[2])+"/"))
            p.drawString(startingx+167, startingy, str(str((data2[1])[3])))
        except:
            pass

        try:
            data2[2]
            p.drawString(startingx, startingy-15, (data2[2])[0])
            p.drawString(startingx+150, startingy-15, str(str((data2[2])[1])+"/"))
            p.drawString(startingx+159, startingy-15, str(str((data2[2])[2])+"/"))
            p.drawString(startingx+167, startingy-15, str(str((data2[2])[3])))
        except:
            pass

        try:
            data2[3]
            p.drawString(startingx, startingy-30, (data2[3])[0])
            p.drawString(startingx+150, startingy-30, str(str((data2[3])[1])+"/"))
            p.drawString(startingx+159, startingy-30, str(str((data2[3])[2])+"/"))
            p.drawString(startingx+167, startingy-30, str(str((data2[3])[3])))
        except:
            pass

        try:
            data2[4]
            p.drawString(startingx, startingy-45, (data2[4])[0])
            p.drawString(startingx+150, startingy-45, str(str((data2[4])[1])+"/"))
            p.drawString(startingx+159, startingy-45, str(str((data2[4])[2])+"/"))
            p.drawString(startingx+167, startingy-45, str(str((data2[4])[3])))
        except:
            pass

        try:
            data2[5]
            p.drawString(startingx, startingy-60, (data2[5])[0])
            p.drawString(startingx+150, startingy-60, str(str((data2[5])[1])+"/"))
            p.drawString(startingx+159, startingy-60, str(str((data2[5])[2])+"/"))
            p.drawString(startingx+167, startingy-60, str(str((data2[5])[3])))
        except:
            pass

        try:
            data2[6]
            p.drawString(startingx, startingy-75, (data2[6])[0])
            p.drawString(startingx+150, startingy-75, str(str((data2[6])[1])+"/"))
            p.drawString(startingx+159, startingy-75, str(str((data2[6])[2])+"/"))
            p.drawString(startingx+167, startingy-75, str(str((data2[6])[3])))
        except:
            pass

        try:
            data2[7]
            p.drawString(startingx, startingy-90, (data2[7])[0])
            p.drawString(startingx+150, startingy-90, str(str((data2[7])[1])+"/"))
            p.drawString(startingx+159, startingy-90, str(str((data2[7])[2])+"/"))
            p.drawString(startingx+167, startingy-90, str(str((data2[7])[3])))
        except:
            pass

        try:
            data2[8]
            p.drawString(startingx, startingy-105, (data2[8])[0])
            p.drawString(startingx+150, startingy-105, str(str((data2[8])[1])+"/"))
            p.drawString(startingx+159, startingy-105, str(str((data2[8])[2])+"/"))
            p.drawString(startingx+167, startingy-105, str(str((data2[8])[3])))
        except:
            pass

        try:
            data2[9]
            p.drawString(startingx, startingy-121, (data2[9])[0])
            p.drawString(startingx+150, startingy-121, str(str((data2[9])[1])+"/"))
            p.drawString(startingx+159, startingy-121, str(str((data2[9])[2])+"/"))
            p.drawString(startingx+167, startingy-121, str(str((data2[9])[3])))
        except:
            pass

        try:
            data2[10]
            p.drawString(startingx, startingy-136, (data2[10])[0])
            p.drawString(startingx+150, startingy-136, str(str((data2[10])[1])+"/"))
            p.drawString(startingx+159, startingy-136, str(str((data2[10])[2])+"/"))
            p.drawString(startingx+167, startingy-136, str(str((data2[10])[3])))
        except:
            pass

        try:
            data2[11]
            p.drawString(startingx, startingy-151, (data2[11])[0])
            p.drawString(startingx+150, startingy-151, str(str((data2[11])[1])+"/"))
            p.drawString(startingx+159, startingy-151, str(str((data2[11])[2])+"/"))
            p.drawString(startingx+167, startingy-151, str(str((data2[11])[3])))
        except:
            pass

        try:
            data2[12]
            p.drawString(startingx, startingy-166, (data2[12])[0])
            p.drawString(startingx+150, startingy-166, str(str((data2[12])[1])+"/"))
            p.drawString(startingx+159, startingy-166, str(str((data2[12])[2])+"/"))
            p.drawString(startingx+167, startingy-166, str(str((data2[12])[3])))
        except:
            pass


        p.save()

        packet.seek(0)

        new_pdf = PdfReader(packet)
        existing_pdf = PdfReader(open("var/www/django_project/page1_repaired.pdf", "rb"))
        output = PdfWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)


        output_stream = BytesIO()
        output.write(output_stream)
        output.close()
        output_stream.seek(0)
        
        return HttpResponse(output_stream, content_type='application/pdf')
    return redirect(logout)

def generate_pdf2(request):
    if request.user.is_authenticated and  request.user.is_staff == 0:
        packet = io.BytesIO()
        pagesize1 = (8.5 * inch, 13 * inch)
        p = canvas.Canvas(packet, pagesize= pagesize1) 
        p.setFont("Helvetica", 7)  

        eligibility = civil_service_eligibility.objects.all().filter(authUser_id=request.user.id).order_by('-id')
        startingx = int(45)
        startingy= int(766)

        data = [['','','','','']]
        for eli in eligibility:
            data.append([eli.eligibility,eli.rating,eli.exam_date.month,eli.exam_date.day,eli.exam_date.year,eli.exam_place,eli.license_number,eli.license_validity_date.year])

        try:
            data[1]
            p.drawString(startingx, startingy, (data[1])[0])
            p.drawString(startingx+160, startingy, (data[1])[1])
            p.drawString(startingx+220, startingy, str(str((data[1])[2])+"/"))
            p.drawString(startingx+230, startingy, str(str((data[1])[3])+"/"))
            p.drawString(startingx+240, startingy, str(str((data[1])[4])))
            p.drawString(startingx+280, startingy, (data[1])[5])
            p.drawString(startingx+430, startingy, (data[1])[6])
            p.drawString(startingx+479, startingy, str(str((data[1])[7])))
        except:
            pass

        try:
            data[2]
            p.drawString(startingx, startingy-20, (data[2])[0])
            p.drawString(startingx+160, startingy-20, (data[2])[1])
            p.drawString(startingx+220, startingy-20, str(str((data[2])[2])+"/"))
            p.drawString(startingx+230, startingy-20, str(str((data[2])[3])+"/"))
            p.drawString(startingx+240, startingy-20, str(str((data[2])[4])))
            p.drawString(startingx+280, startingy-20, (data[2])[5])
            p.drawString(startingx+430, startingy-20, (data[2])[6])
            p.drawString(startingx+479, startingy-20, str(str((data[2])[7])))
        except:
            pass

        try:
            data[3]
            p.drawString(startingx, startingy-39, (data[3])[0])
            p.drawString(startingx+160, startingy-39, (data[3])[1])
            p.drawString(startingx+220, startingy-39, str(str((data[3])[2])+"/"))
            p.drawString(startingx+230, startingy-39, str(str((data[3])[3])+"/"))
            p.drawString(startingx+240, startingy-39, str(str((data[3])[4])))
            p.drawString(startingx+280, startingy-39, (data[3])[5])
            p.drawString(startingx+430, startingy-39, (data[3])[6])
            p.drawString(startingx+479, startingy-39, str(str((data[3])[7])))
        except:
            pass

        try:
            data[4]
            p.drawString(startingx, startingy-59, (data[4])[0])
            p.drawString(startingx+160, startingy-59, (data[4])[1])
            p.drawString(startingx+220, startingy-59, str(str((data[4])[2])+"/"))
            p.drawString(startingx+230, startingy-59, str(str((data[4])[3])+"/"))
            p.drawString(startingx+240, startingy-59, str(str((data[4])[4])))
            p.drawString(startingx+280, startingy-59, (data[4])[5])
            p.drawString(startingx+430, startingy-59, (data[4])[6])
            p.drawString(startingx+479, startingy-59, str(str((data[4])[7])))
        except:
            pass

        try:
            data[5]
            p.drawString(startingx, startingy-78, (data[5])[0])
            p.drawString(startingx+160, startingy-78, (data[5])[1])
            p.drawString(startingx+220, startingy-78, str(str((data[5])[2])+"/"))
            p.drawString(startingx+230, startingy-78, str(str((data[5])[3])+"/"))
            p.drawString(startingx+240, startingy-78, str(str((data[5])[4])))
            p.drawString(startingx+280, startingy-78, (data[5])[5])
            p.drawString(startingx+430, startingy-78, (data[5])[6])
            p.drawString(startingx+479, startingy-78, str(str((data[5])[7])))
        except:
            pass

        try:
            data[6]
            p.drawString(startingx, startingy-99, (data[6])[0])
            p.drawString(startingx+160, startingy-99, (data[6])[1])
            p.drawString(startingx+220, startingy-99, str(str((data[6])[2])+"/"))
            p.drawString(startingx+230, startingy-99, str(str((data[6])[3])+"/"))
            p.drawString(startingx+240, startingy-99, str(str((data[6])[4])))
            p.drawString(startingx+280, startingy-99, (data[6])[5])
            p.drawString(startingx+430, startingy-99, (data[6])[6])
            p.drawString(startingx+479, startingy-99, str(str((data[6])[7])))
        except:
            pass

        try:
            data[7]
            p.drawString(startingx, startingy-118, (data[7])[0])
            p.drawString(startingx+160, startingy-118, (data[7])[1])
            p.drawString(startingx+220, startingy-118, str(str((data[7])[2])+"/"))
            p.drawString(startingx+230, startingy-118, str(str((data[7])[3])+"/"))
            p.drawString(startingx+240, startingy-118, str(str((data[7])[4])))
            p.drawString(startingx+280, startingy-118, (data[7])[5])
            p.drawString(startingx+430, startingy-118, (data[7])[6])
            p.drawString(startingx+479, startingy-118, str(str((data[7])[7])))
        except:
            pass

        experience = work_experience.objects.all().filter(authUser_id=request.user.id).order_by('-id')
        data2 = [['','','','','','','']]
        

        startingx2 = int(45)
        startingy2= int(554)

        for exp in experience:
            data2.append([exp.date_from.month,exp.date_from.day,exp.date_from.year,exp.date_to.month,exp.date_to.day,exp.date_to.year,
                        exp.position,
                        exp.department,
                        exp.monthly_salary,
                        exp.salary_grade,
                        exp.status,
                        exp.gov_service]
                        )
            
        try:
            data2[1]

            if len((data2[1])[6]) > 35:
                a = (data2[1])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,558, top_text)
                p.drawString(126,551, bottom_text)
        
            else:
                p.drawString(126, 554, (data2[1])[6])

            
            if len((data2[1])[7]) > 35:
                a = (data2[1])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,558, top_text)
                p.drawString(260,551, bottom_text)
        
            else:
                p.drawString(260, 554, (data2[1])[7])

            

            p.drawString(startingx2, startingy2, str(str((data2[1])[0])+"/"))
            p.drawString(startingx2+6 , startingy2, str(str((data2[1])[1])+"/"))
            p.drawString(startingx2+15, startingy2, str(str((data2[1])[2])))

            p.drawString(startingx2+43, startingy2, str(str((data2[1])[3])+"/"))
            p.drawString(startingx2+50, startingy2, str(str((data2[1])[4])+"/"))
            p.drawString(startingx2+59, startingy2, str(str((data2[1])[5])))  

        
            p.drawString(startingx2+355, startingy2, (data2[1])[8])
            p.drawString(startingx2+394 , startingy2, (data2[1])[9])
            p.drawString(startingx2+440 , startingy2, (data2[1])[10])
            p.drawString(startingx2+490 , startingy2, (data2[1])[11])

        except:
            pass

        try:
            data2[2]

            if len((data2[2])[6]) > 35:
                a = (data2[2])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,539, top_text)
                p.drawString(126,531, bottom_text)

            else:
                p.drawString(126, 535, (data2[2])[6])


            if len((data2[2])[7]) > 35:
                a = (data2[2])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,539, top_text)
                p.drawString(260,531, bottom_text)

            else:
                p.drawString(260, 535, (data2[2])[7])

            

            p.drawString(startingx2, startingy2-19, str(str((data2[2])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-19, str(str((data2[2])[1])+"/"))
            p.drawString(startingx2+15, startingy2-19, str(str((data2[2])[2])))

            p.drawString(startingx2+43, startingy2-19, str(str((data2[2])[3])+"/"))
            p.drawString(startingx2+50, startingy2-19, str(str((data2[2])[4])+"/"))
            p.drawString(startingx2+59, startingy2-19, str(str((data2[2])[5])))  

            p.drawString(startingx2+355, startingy2-19, (data2[2])[8])
            p.drawString(startingx2+394 , startingy2-19, (data2[2])[9])
            p.drawString(startingx2+440 , startingy2-19, (data2[2])[10])
            p.drawString(startingx2+490 , startingy2-19, (data2[2])[11])

        except:
            pass
        
        try:
            data2[3]

            if len((data2[3])[6]) > 35:
                a = (data2[3])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,519, top_text)
                p.drawString(126,511, bottom_text)

            else:
                p.drawString(126, 515, (data2[3])[6])


            if len((data2[3])[7]) > 35:
                a = (data2[3])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,519, top_text)
                p.drawString(260,512, bottom_text)

            else:
                p.drawString(260, 515, (data2[3])[7])

            p.drawString(startingx2, startingy2-39, str(str((data2[3])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-39, str(str((data2[3])[1])+"/"))
            p.drawString(startingx2+15, startingy2-39, str(str((data2[3])[2])))

            p.drawString(startingx2+43, startingy2-39, str(str((data2[3])[3])+"/"))
            p.drawString(startingx2+50, startingy2-39, str(str((data2[3])[4])+"/"))
            p.drawString(startingx2+59, startingy2-39, str(str((data2[3])[5])))  

            p.drawString(startingx2+355, startingy2-39, (data2[3])[8])
            p.drawString(startingx2+394 , startingy2-39, (data2[3])[9])
            p.drawString(startingx2+440 , startingy2-39, (data2[3])[10])
            p.drawString(startingx2+490 , startingy2-39, (data2[3])[11])

        except:
            pass

        try:
            data2[4]

            if len((data2[4])[6]) > 35:
                a = (data2[4])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,503, top_text)
                p.drawString(126,496, bottom_text)

            else:
                p.drawString(126, 499, (data2[4])[6])


            if len((data2[4])[7]) > 35:
                a = (data2[4])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,503, top_text)
                p.drawString(260,496, bottom_text)

            else:
                p.drawString(260, 499, (data2[4])[7])

            p.drawString(startingx2, startingy2-55, str(str((data2[4])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-55, str(str((data2[4])[1])+"/"))
            p.drawString(startingx2+15, startingy2-55, str(str((data2[4])[2])))

            p.drawString(startingx2+43, startingy2-55, str(str((data2[4])[3])+"/"))
            p.drawString(startingx2+50, startingy2-55, str(str((data2[4])[4])+"/"))
            p.drawString(startingx2+59, startingy2-55, str(str((data2[4])[5])))  

            p.drawString(startingx2+355, startingy2-55, (data2[4])[8])
            p.drawString(startingx2+394 , startingy2-55, (data2[4])[9])
            p.drawString(startingx2+440 , startingy2-55, (data2[4])[10])
            p.drawString(startingx2+490 , startingy2-55, (data2[4])[11])

        except:
            pass

        try:
            data2[5]

            if len((data2[5])[6]) > 35:
                a = (data2[5])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,483, top_text)
                p.drawString(126,476, bottom_text)

            else:
                p.drawString(126, 479, (data2[5])[6])


            if len((data2[5])[7]) > 35:
                a = (data2[5])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,483, top_text)
                p.drawString(260,476, bottom_text)

            else:
                p.drawString(260, 479, (data2[5])[7])

            p.drawString(startingx2, startingy2-75, str(str((data2[5])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-75, str(str((data2[5])[1])+"/"))
            p.drawString(startingx2+15, startingy2-75, str(str((data2[5])[2])))

            p.drawString(startingx2+43, startingy2-75, str(str((data2[5])[3])+"/"))
            p.drawString(startingx2+50, startingy2-75, str(str((data2[5])[4])+"/"))
            p.drawString(startingx2+59, startingy2-75, str(str((data2[5])[5])))  

            p.drawString(startingx2+355, startingy2-75, (data2[5])[8])
            p.drawString(startingx2+394 , startingy2-75, (data2[5])[9])
            p.drawString(startingx2+440 , startingy2-75, (data2[5])[10])
            p.drawString(startingx2+490 , startingy2-75, (data2[5])[11])

        except:
            pass

        try:
            data2[6]

            if len((data2[6])[6]) > 35:
                a = (data2[6])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,463, top_text)
                p.drawString(126,456, bottom_text)

            else:
                p.drawString(126, 459, (data2[6])[6])


            if len((data2[6])[7]) > 35:
                a = (data2[6])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,463, top_text)
                p.drawString(260,456, bottom_text)

            else:
                p.drawString(260, 459, (data2[6])[7])

            p.drawString(startingx2, startingy2-95, str(str((data2[6])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-95, str(str((data2[6])[1])+"/"))
            p.drawString(startingx2+15, startingy2-95, str(str((data2[6])[2])))

            p.drawString(startingx2+43, startingy2-95, str(str((data2[6])[3])+"/"))
            p.drawString(startingx2+50, startingy2-95, str(str((data2[6])[4])+"/"))
            p.drawString(startingx2+59, startingy2-95, str(str((data2[6])[5])))  

            p.drawString(startingx2+355, startingy2-95, (data2[6])[8])
            p.drawString(startingx2+394 , startingy2-95, (data2[6])[9])
            p.drawString(startingx2+440 , startingy2-95, (data2[6])[10])
            p.drawString(startingx2+490 , startingy2-95, (data2[6])[11])

        except:
            pass

        try:
            data2[7]

            if len((data2[7])[6]) > 35:
                a = (data2[7])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,443, top_text)
                p.drawString(126,436, bottom_text)

            else:
                p.drawString(126, 439, (data2[7])[6])


            if len((data2[7])[7]) > 35:
                a = (data2[7])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,443, top_text)
                p.drawString(260,436, bottom_text)

            else:
                p.drawString(260, 439, (data2[7])[7])

            p.drawString(startingx2, startingy2-115, str(str((data2[7])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-115, str(str((data2[7])[1])+"/"))
            p.drawString(startingx2+15, startingy2-115, str(str((data2[7])[2])))

            p.drawString(startingx2+43, startingy2-115, str(str((data2[7])[3])+"/"))
            p.drawString(startingx2+50, startingy2-115, str(str((data2[7])[4])+"/"))    
            p.drawString(startingx2+59, startingy2-115, str(str((data2[7])[5])))  

            p.drawString(startingx2+355, startingy2-115, (data2[7])[8])
            p.drawString(startingx2+394 , startingy2-115, (data2[7])[9])
            p.drawString(startingx2+440 , startingy2-115, (data2[7])[10])
            p.drawString(startingx2+490 , startingy2-115, (data2[7])[11])

        except:
            pass

        try:
            data2[8]

            if len((data2[8])[6]) > 35:
                a = (data2[8])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,425, top_text)
                p.drawString(126,418, bottom_text)

            else:
                p.drawString(126, 421, (data2[8])[6])


            if len((data2[8])[7]) > 35:
                a = (data2[8])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,425, top_text)
                p.drawString(260,418, bottom_text)

            else:
                p.drawString(260, 421, (data2[8])[7])

            p.drawString(startingx2, startingy2-133, str(str((data2[8])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-133, str(str((data2[8])[1])+"/"))
            p.drawString(startingx2+15, startingy2-133, str(str((data2[8])[2])))

            p.drawString(startingx2+43, startingy2-133, str(str((data2[8])[3])+"/"))
            p.drawString(startingx2+50, startingy2-133, str(str((data2[8])[4])+"/"))
            p.drawString(startingx2+59, startingy2-133, str(str((data2[8])[5])))  

            p.drawString(startingx2+355, startingy2-133, (data2[8])[8])
            p.drawString(startingx2+394 , startingy2-133, (data2[8])[9])
            p.drawString(startingx2+440 , startingy2-133, (data2[8])[10])
            p.drawString(startingx2+490 , startingy2-133, (data2[8])[11])

        except:
            pass

        try:
            data2[9]

            if len((data2[9])[6]) > 35:
                a = (data2[9])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,407, top_text)
                p.drawString(126,400, bottom_text)

            else:
                p.drawString(126, 403, (data2[9])[6])


            if len((data2[9])[7]) > 35:
                a = (data2[9])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,407, top_text)
                p.drawString(260,400, bottom_text)

            else:
                p.drawString(260, 403, (data2[9])[7])

            p.drawString(startingx2, startingy2-151, str(str((data2[9])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-151, str(str((data2[9])[1])+"/"))
            p.drawString(startingx2+15, startingy2-151, str(str((data2[9])[2])))

            p.drawString(startingx2+43, startingy2-151, str(str((data2[9])[3])+"/"))
            p.drawString(startingx2+50, startingy2-151, str(str((data2[9])[4])+"/"))
            p.drawString(startingx2+59, startingy2-151, str(str((data2[9])[5])))  

            p.drawString(startingx2+355, startingy2-151, (data2[9])[8])
            p.drawString(startingx2+394 , startingy2-151, (data2[9])[9])
            p.drawString(startingx2+440 , startingy2-151, (data2[9])[10])
            p.drawString(startingx2+490 , startingy2-151, (data2[9])[11])

        except:
            pass

        try:
            data2[10]

            if len((data2[10])[6]) > 35:
                a = (data2[10])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,389, top_text)
                p.drawString(126,382, bottom_text)

            else:
                p.drawString(126, 385, (data2[10])[6])


            if len((data2[10])[7]) > 35:
                a = (data2[10])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,389, top_text)
                p.drawString(260,382, bottom_text)

            else:
                p.drawString(260, 385, (data2[10])[7])

            p.drawString(startingx2, startingy2-169, str(str((data2[10])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-169, str(str((data2[10])[1])+"/"))
            p.drawString(startingx2+15, startingy2-169, str(str((data2[10])[2])))

            p.drawString(startingx2+43, startingy2-169, str(str((data2[10])[3])+"/"))
            p.drawString(startingx2+50, startingy2-169, str(str((data2[10])[4])+"/"))
            p.drawString(startingx2+59, startingy2-169, str(str((data2[10])[5])))  

            p.drawString(startingx2+355, startingy2-169, (data2[10])[8])
            p.drawString(startingx2+394 , startingy2-169, (data2[10])[9])
            p.drawString(startingx2+440 , startingy2-169, (data2[10])[10])
            p.drawString(startingx2+490 , startingy2-169, (data2[10])[11])

        except:
            pass

        try:
            data2[11]

            if len((data2[11])[6]) > 35:
                a = (data2[11])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,371, top_text)
                p.drawString(126,364, bottom_text)

            else:
                p.drawString(126, 367, (data2[11])[6])


            if len((data2[11])[7]) > 35:
                a = (data2[11])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,371, top_text)
                p.drawString(260,364, bottom_text)

            else:
                p.drawString(260, 367, (data2[11])[7])

            p.drawString(startingx2, startingy2-187, str(str((data2[11])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-187, str(str((data2[11])[1])+"/"))
            p.drawString(startingx2+15, startingy2-187, str(str((data2[11])[2])))

            p.drawString(startingx2+43, startingy2-187, str(str((data2[11])[3])+"/"))
            p.drawString(startingx2+50, startingy2-187, str(str((data2[11])[4])+"/"))
            p.drawString(startingx2+59, startingy2-187, str(str((data2[11])[5])))  

            p.drawString(startingx2+355, startingy2-187, (data2[11])[8])
            p.drawString(startingx2+394 , startingy2-187, (data2[11])[9])
            p.drawString(startingx2+440 , startingy2-187, (data2[11])[10])
            p.drawString(startingx2+490 , startingy2-187, (data2[11])[11])

        except:
            pass

        try:
            data2[12]

            if len((data2[12])[6]) > 35:
                a = (data2[12])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,353, top_text)
                p.drawString(126,346, bottom_text)

            else:
                p.drawString(126, 349, (data2[12])[6])

        
            if len((data2[12])[7]) > 35:
                a = (data2[12])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,353, top_text)
                p.drawString(260,346, bottom_text)

            else:
                p.drawString(260, 349, (data2[12])[7])

            p.drawString(startingx2, startingy2-205, str(str((data2[12])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-205, str(str((data2[12])[1])+"/"))
            p.drawString(startingx2+15, startingy2-205, str(str((data2[12])[2])))

            p.drawString(startingx2+43, startingy2-205, str(str((data2[12])[3])+"/"))
            p.drawString(startingx2+50, startingy2-205, str(str((data2[12])[4])+"/"))
            p.drawString(startingx2+59, startingy2-205, str(str((data2[12])[5])))  

            p.drawString(startingx2+355, startingy2-205, (data2[12])[8])
            p.drawString(startingx2+394 , startingy2-205, (data2[12])[9])
            p.drawString(startingx2+440 , startingy2-205, (data2[12])[10])
            p.drawString(startingx2+490 , startingy2-205, (data2[12])[11])

        except:
            pass

        try:
            data2[13]

            if len((data2[13])[6]) > 35:
                a = (data2[13])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,335, top_text)
                p.drawString(126,338, bottom_text)

            else:
                p.drawString(126, 331, (data2[13])[6])


            if len((data2[13])[7]) > 35:
                a = (data2[13])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,335, top_text)
                p.drawString(260,338, bottom_text)

            else:
                p.drawString(260, 331, (data2[13])[7])

            p.drawString(startingx2, startingy2-223, str(str((data2[13])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-223, str(str((data2[13])[1])+"/"))
            p.drawString(startingx2+15, startingy2-223, str(str((data2[13])[2])))

            p.drawString(startingx2+43, startingy2-223, str(str((data2[13])[3])+"/"))
            p.drawString(startingx2+50, startingy2-223, str(str((data2[13])[4])+"/"))
            p.drawString(startingx2+59, startingy2-223, str(str((data2[13])[5])))  

            p.drawString(startingx2+355, startingy2-223, (data2[13])[8])
            p.drawString(startingx2+394 , startingy2-223, (data2[13])[9])
            p.drawString(startingx2+440 , startingy2-223, (data2[13])[10])
            p.drawString(startingx2+490 , startingy2-223, (data2[13])[11])

        except:
            pass

        try:
            data2[14]

            if len((data2[14])[6]) > 35:
                a = (data2[14])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,317, top_text)
                p.drawString(126,310, bottom_text)

            else:
                p.drawString(126, 313, (data2[14])[6])


            if len((data2[14])[7]) > 35:
                a = (data2[14])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,317, top_text)
                p.drawString(260,310, bottom_text)

            else:
                p.drawString(260, 313, (data2[14])[7])

            p.drawString(startingx2, startingy2-241, str(str((data2[14])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-241, str(str((data2[14])[1])+"/"))
            p.drawString(startingx2+15, startingy2-241, str(str((data2[14])[2])))

            p.drawString(startingx2+43, startingy2-241, str(str((data2[14])[3])+"/"))
            p.drawString(startingx2+50, startingy2-241, str(str((data2[14])[4])+"/"))
            p.drawString(startingx2+59, startingy2-241, str(str((data2[14])[5])))  

            p.drawString(startingx2+355, startingy2-241, (data2[14])[8])
            p.drawString(startingx2+394 , startingy2-241, (data2[14])[9])
            p.drawString(startingx2+440 , startingy2-241, (data2[14])[10])
            p.drawString(startingx2+490 , startingy2-241, (data2[14])[11])

        except:
            pass

        
        try:
            data2[15]

            if len((data2[15])[6]) > 35:
                a = (data2[15])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,299, top_text)
                p.drawString(126,292, bottom_text)

            else:
                p.drawString(126, 295, (data2[15])[6])


            if len((data2[15])[7]) > 35:
                a = (data2[15])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,299, top_text)
                p.drawString(260,292, bottom_text)

            else:
                p.drawString(260, 295, (data2[15])[7])

            p.drawString(startingx2, startingy2-259, str(str((data2[15])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-259, str(str((data2[15])[1])+"/"))
            p.drawString(startingx2+15, startingy2-259, str(str((data2[15])[2])))

            p.drawString(startingx2+43, startingy2-259, str(str((data2[15])[3])+"/"))
            p.drawString(startingx2+50, startingy2-259, str(str((data2[15])[4])+"/"))
            p.drawString(startingx2+59, startingy2-259, str(str((data2[15])[5])))  

            p.drawString(startingx2+355, startingy2-259, (data2[15])[8])
            p.drawString(startingx2+394 , startingy2-259, (data2[15])[9])
            p.drawString(startingx2+440 , startingy2-259, (data2[15])[10])
            p.drawString(startingx2+490 , startingy2-259, (data2[15])[11])

        except:
            pass

        try:
            data2[16]

            if len((data2[16])[6]) > 35:
                a = (data2[16])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,281, top_text)
                p.drawString(126,274, bottom_text)

            else:
                p.drawString(126, 277, (data2[16])[6])


            if len((data2[16])[7]) > 35:
                a = (data2[16])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,281, top_text)
                p.drawString(260,274, bottom_text)

            else:
                p.drawString(260, 277, (data2[16])[7])

            p.drawString(startingx2, startingy2-277, str(str((data2[16])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-277, str(str((data2[16])[1])+"/"))
            p.drawString(startingx2+15, startingy2-277, str(str((data2[16])[2])))

            p.drawString(startingx2+43, startingy2-277, str(str((data2[16])[3])+"/"))
            p.drawString(startingx2+50, startingy2-277, str(str((data2[16])[4])+"/"))
            p.drawString(startingx2+59, startingy2-277, str(str((data2[16])[5])))  

            p.drawString(startingx2+355, startingy2-277, (data2[16])[8])
            p.drawString(startingx2+394 , startingy2-277, (data2[16])[9])
            p.drawString(startingx2+440 , startingy2-277, (data2[16])[10])
            p.drawString(startingx2+490 , startingy2-277, (data2[16])[11])

        except:
            pass

        try:
            data2[17]

            if len((data2[17])[6]) > 35:
                a = (data2[17])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,263, top_text)
                p.drawString(126,256, bottom_text)

            else:
                p.drawString(126, 259, (data2[17])[6])


            if len((data2[17])[7]) > 35:
                a = (data2[17])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,263, top_text)
                p.drawString(260,256, bottom_text)

            else:
                p.drawString(260, 259, (data2[17])[7])

            p.drawString(startingx2, startingy2-295, str(str((data2[17])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-295, str(str((data2[17])[1])+"/"))
            p.drawString(startingx2+15, startingy2-295, str(str((data2[17])[2])))

            p.drawString(startingx2+43, startingy2-295, str(str((data2[17])[3])+"/"))
            p.drawString(startingx2+50, startingy2-295, str(str((data2[17])[4])+"/"))
            p.drawString(startingx2+59, startingy2-295, str(str((data2[17])[5])))  

            p.drawString(startingx2+355, startingy2-295, (data2[17])[8])
            p.drawString(startingx2+394 , startingy2-295, (data2[17])[9])
            p.drawString(startingx2+440 , startingy2-295, (data2[17])[10])
            p.drawString(startingx2+490 , startingy2-295, (data2[17])[11])

        except:
            pass

        try:
            data2[18]

            if len((data2[18])[6]) > 35:
                a = (data2[18])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,245, top_text)
                p.drawString(126,238, bottom_text)

            else:
                p.drawString(126, 241, (data2[18])[6])


            if len((data2[18])[7]) > 35:
                a = (data2[18])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,245, top_text)
                p.drawString(260,238, bottom_text)

            else:
                p.drawString(260, 241, (data2[18])[7])

            p.drawString(startingx2, startingy2-313, str(str((data2[18])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-313, str(str((data2[18])[1])+"/"))
            p.drawString(startingx2+15, startingy2-313, str(str((data2[16])[2])))

            p.drawString(startingx2+43, startingy2-313, str(str((data2[18])[3])+"/"))
            p.drawString(startingx2+50, startingy2-313, str(str((data2[18])[4])+"/"))
            p.drawString(startingx2+59, startingy2-313, str(str((data2[18])[5])))  

            p.drawString(startingx2+355, startingy2-313, (data2[18])[8])
            p.drawString(startingx2+394 , startingy2-313, (data2[18])[9])
            p.drawString(startingx2+440 , startingy2-313, (data2[18])[10])
            p.drawString(startingx2+490 , startingy2-313, (data2[18])[11])

        except:
            pass

        
        try:
            data2[19]

            if len((data2[19])[6]) > 35:
                a = (data2[19])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,227, top_text)
                p.drawString(126,220, bottom_text)

            else:
                p.drawString(126, 223, (data2[19])[6])


            if len((data2[19])[7]) > 35:
                a = (data2[19])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,227, top_text)
                p.drawString(260,220, bottom_text)

            else:
                p.drawString(260, 223, (data2[19])[7])

            p.drawString(startingx2, startingy2-331, str(str((data2[19])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-331, str(str((data2[19])[1])+"/"))
            p.drawString(startingx2+15, startingy2-331, str(str((data2[19])[2])))

            p.drawString(startingx2+43, startingy2-331, str(str((data2[19])[3])+"/"))
            p.drawString(startingx2+50, startingy2-331, str(str((data2[19])[4])+"/"))
            p.drawString(startingx2+59, startingy2-331, str(str((data2[19])[5])))  

            p.drawString(startingx2+355, startingy2-331, (data2[19])[8])
            p.drawString(startingx2+394 , startingy2-331, (data2[19])[9])
            p.drawString(startingx2+440 , startingy2-331, (data2[19])[10])
            p.drawString(startingx2+490 , startingy2-331, (data2[19])[11])

        except:
            pass

        try:
            data2[20]

            if len((data2[20])[6]) > 35:
                a = (data2[20])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,209, top_text)
                p.drawString(126,202, bottom_text)

            else:
                p.drawString(126, 205, (data2[20])[6])


            if len((data2[20])[7]) > 35:
                a = (data2[20])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,209, top_text)
                p.drawString(260,202, bottom_text)

            else:
                p.drawString(260, 205, (data2[20])[7])

            p.drawString(startingx2, startingy2-349, str(str((data2[20])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-349, str(str((data2[20])[1])+"/"))
            p.drawString(startingx2+15, startingy2-349, str(str((data2[20])[2])))

            p.drawString(startingx2+43, startingy2-349, str(str((data2[20])[3])+"/"))
            p.drawString(startingx2+50, startingy2-349, str(str((data2[20])[4])+"/"))
            p.drawString(startingx2+59, startingy2-349, str(str((data2[20])[5])))  

            p.drawString(startingx2+355, startingy2-349, (data2[20])[8])
            p.drawString(startingx2+394 , startingy2-349, (data2[20])[9])
            p.drawString(startingx2+440 , startingy2-349, (data2[20])[10])
            p.drawString(startingx2+490 , startingy2-349, (data2[20])[11])

        except:
            pass
        
        try:
            data2[21]

            if len((data2[21])[6]) > 35:
                a = (data2[21])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,192, top_text)
                p.drawString(126,184, bottom_text)

            else:
                p.drawString(126, 187, (data2[21])[6])


            if len((data2[21])[7]) > 35:
                a = (data2[21])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,192, top_text)
                p.drawString(260,184, bottom_text)

            else:
                p.drawString(260, 187, (data2[21])[7])

            p.drawString(startingx2, startingy2-367, str(str((data2[21])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-367, str(str((data2[21])[1])+"/"))
            p.drawString(startingx2+15, startingy2-367, str(str((data2[21])[2])))

            p.drawString(startingx2+43, startingy2-367, str(str((data2[21])[3])+"/"))
            p.drawString(startingx2+50, startingy2-367, str(str((data2[21])[4])+"/"))
            p.drawString(startingx2+59, startingy2-367, str(str((data2[21])[5])))  

            p.drawString(startingx2+355, startingy2-367, (data2[21])[8])
            p.drawString(startingx2+394 , startingy2-367, (data2[21])[9])
            p.drawString(startingx2+440 , startingy2-367, (data2[21])[10])
            p.drawString(startingx2+490 , startingy2-367, (data2[21])[11])

        except:
            pass
            
        try:
            data2[22]

            if len((data2[22])[6]) > 35:
                a = (data2[22])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,173, top_text)
                p.drawString(126,166, bottom_text)

            else:
                p.drawString(126, 169, (data2[22])[6])


            if len((data2[22])[7]) > 35:
                a = (data2[22])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,173, top_text)
                p.drawString(260,166, bottom_text)

            else:
                p.drawString(260, 169, (data2[22])[7])


            p.drawString(startingx2, startingy2-385, str(str((data2[22])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-385, str(str((data2[22])[1])+"/"))
            p.drawString(startingx2+15, startingy2-385, str(str((data2[22])[2])))

            p.drawString(startingx2+43, startingy2-385, str(str((data2[22])[3])+"/"))
            p.drawString(startingx2+50, startingy2-385, str(str((data2[22])[4])+"/"))
            p.drawString(startingx2+59, startingy2-385, str(str((data2[22])[5])))  

            p.drawString(startingx2+355, startingy2-385, (data2[22])[8])
            p.drawString(startingx2+394 , startingy2-385, (data2[22])[9])
            p.drawString(startingx2+440 , startingy2-385, (data2[22])[10])
            p.drawString(startingx2+490 , startingy2-385, (data2[22])[11])

        except:
            pass
            
        try:
            data2[23]

            if len((data2[23])[6]) > 35:
                a = (data2[23])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,155, top_text)
                p.drawString(126,148, bottom_text)

            else:
                p.drawString(126, 151, (data2[23])[6])


            if len((data2[23])[7]) > 35:
                a = (data2[23])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,155, top_text)
                p.drawString(260,148, bottom_text)

            else:
                p.drawString(260, 151, (data2[23])[7])

            p.drawString(startingx2, startingy2-403, str(str((data2[23])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-403, str(str((data2[23])[1])+"/"))
            p.drawString(startingx2+15, startingy2-403, str(str((data2[23])[2])))

            p.drawString(startingx2+43, startingy2-403, str(str((data2[23])[3])+"/"))
            p.drawString(startingx2+50, startingy2-403, str(str((data2[23])[4])+"/"))
            p.drawString(startingx2+59, startingy2-403, str(str((data2[23])[5])))  

            p.drawString(startingx2+355, startingy2-403, (data2[23])[8])
            p.drawString(startingx2+394 , startingy2-403, (data2[23])[9])
            p.drawString(startingx2+440 , startingy2-403, (data2[23])[10])
            p.drawString(startingx2+490 , startingy2-403, (data2[23])[11])

        except:
            pass
            
        try:
            data2[24]

            if len((data2[24])[6]) > 35:
                a = (data2[24])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,137, top_text)
                p.drawString(126,130, bottom_text)

            else:
                p.drawString(126, 133, (data2[24])[6])


            if len((data2[24])[7]) > 35:
                a = (data2[24])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,137, top_text)
                p.drawString(260,130, bottom_text)

            else:
                p.drawString(260, 133, (data2[24])[7])

            p.drawString(startingx2, startingy2-421, str(str((data2[24])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-421, str(str((data2[24])[1])+"/"))
            p.drawString(startingx2+15, startingy2-421, str(str((data2[24])[2])))

            p.drawString(startingx2+43, startingy2-421, str(str((data2[24])[3])+"/"))
            p.drawString(startingx2+50, startingy2-421, str(str((data2[24])[4])+"/"))
            p.drawString(startingx2+59, startingy2-421, str(str((data2[24])[5])))  

            p.drawString(startingx2+355, startingy2-421, (data2[24])[8])
            p.drawString(startingx2+394 , startingy2-421, (data2[24])[9])
            p.drawString(startingx2+440 , startingy2-421, (data2[24])[10])
            p.drawString(startingx2+490 , startingy2-421, (data2[24])[11])

        except:
            pass
            
        try:
            data2[25]

            if len((data2[25])[6]) > 35:
                a = (data2[25])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,119, top_text)
                p.drawString(126,112, bottom_text)

            else:
                p.drawString(126, 115, (data2[25])[6])


            if len((data2[25])[7]) > 35:
                a = (data2[25])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,119, top_text)
                p.drawString(260,112, bottom_text)

            else:
                p.drawString(260, 115, (data2[25])[7])

            p.drawString(startingx2, startingy2-439, str(str((data2[25])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-439, str(str((data2[25])[1])+"/"))
            p.drawString(startingx2+15, startingy2-439, str(str((data2[25])[2])))

            p.drawString(startingx2+43, startingy2-439, str(str((data2[25])[3])+"/"))
            p.drawString(startingx2+50, startingy2-439, str(str((data2[25])[4])+"/"))
            p.drawString(startingx2+59, startingy2-439, str(str((data2[25])[5])))  

            p.drawString(startingx2+355, startingy2-439, (data2[25])[8])
            p.drawString(startingx2+394 , startingy2-439, (data2[25])[9])
            p.drawString(startingx2+440 , startingy2-439, (data2[25])[10])
            p.drawString(startingx2+490 , startingy2-439, (data2[25])[11])

        except:
            pass
            
        try:
            data2[26]

            if len((data2[26])[6]) > 35:
                a = (data2[26])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,100, top_text)
                p.drawString(126,94, bottom_text)

            else:
                p.drawString(126, 97, (data2[26])[6])


            if len((data2[26])[7]) > 35:
                a = (data2[26])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,101, top_text)
                p.drawString(260,94, bottom_text)

            else:
                p.drawString(260, 97, (data2[26])[7])

            p.drawString(startingx2, startingy2-457, str(str((data2[26])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-457, str(str((data2[26])[1])+"/"))
            p.drawString(startingx2+15, startingy2-457, str(str((data2[26])[2])))

            p.drawString(startingx2+43, startingy2-457, str(str((data2[26])[3])+"/"))
            p.drawString(startingx2+50, startingy2-457, str(str((data2[26])[4])+"/"))
            p.drawString(startingx2+59, startingy2-457, str(str((data2[26])[5])))  

            p.drawString(startingx2+355, startingy2-457, (data2[26])[8])
            p.drawString(startingx2+394 , startingy2-457, (data2[26])[9])
            p.drawString(startingx2+440 , startingy2-457, (data2[26])[10])
            p.drawString(startingx2+490 , startingy2-457, (data2[26])[11])

        except:
            pass
            
        try:
            data2[27]

            if len((data2[27])[6]) > 35:
                a = (data2[27])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,93, top_text)
                p.drawString(126,76, bottom_text)

            else:
                p.drawString(126, 79, (data2[27])[6])


            if len((data2[27])[7]) > 35:
                a = (data2[27])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,93, top_text)
                p.drawString(260,76, bottom_text)

            else:
                p.drawString(260, 79, (data2[27])[7])

            p.drawString(startingx2, startingy2-475, str(str((data2[27])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-475, str(str((data2[27])[1])+"/"))
            p.drawString(startingx2+15, startingy2-475, str(str((data2[27])[2])))

            p.drawString(startingx2+43, startingy2-475, str(str((data2[27])[3])+"/"))
            p.drawString(startingx2+50, startingy2-475, str(str((data2[27])[4])+"/"))
            p.drawString(startingx2+59, startingy2-475, str(str((data2[27])[5])))  

            p.drawString(startingx2+355, startingy2-475, (data2[27])[8])
            p.drawString(startingx2+394 , startingy2-475, (data2[27])[9])
            p.drawString(startingx2+440 , startingy2-475, (data2[27])[10])
            p.drawString(startingx2+490 , startingy2-475, (data2[27])[11])

        except:
            pass
            
        try:
            data2[28]

            if len((data2[28])[6]) > 35:
                a = (data2[28])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,65, top_text)
                p.drawString(126,58, bottom_text)

            else:
                p.drawString(126, 61, (data2[28])[6])


            if len((data2[28])[7]) > 35:
                a = (data2[28])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,65, top_text)
                p.drawString(260,58, bottom_text)

            else:
                p.drawString(260, 61, (data2[28])[7])
                

            p.drawString(startingx2, startingy2-493, str(str((data2[28])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-493, str(str((data2[28])[1])+"/"))
            p.drawString(startingx2+15, startingy2-493, str(str((data2[28])[2])))

            p.drawString(startingx2+43, startingy2-493, str(str((data2[28])[3])+"/"))
            p.drawString(startingx2+50, startingy2-493, str(str((data2[28])[4])+"/"))
            p.drawString(startingx2+59, startingy2-493, str(str((data2[28])[5])))  

            p.drawString(startingx2+355, startingy2-493, (data2[28])[8])
            p.drawString(startingx2+394 , startingy2-493, (data2[28])[9])
            p.drawString(startingx2+440 , startingy2-493, (data2[28])[10])
            p.drawString(startingx2+490 , startingy2-493, (data2[28])[11])

        except:
            pass

        
            # eli_eligibility1 = f'{eli.eligibility}'

            # p.drawString(130, 500, eli_eligibility1)

        p.save()

        packet.seek(0)

        new_pdf = PdfReader(packet)
        existing_pdf = PdfReader(open("var/www/django_project/page2.pdf", "rb"))
        output = PdfWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)


        output_stream = BytesIO()
        output.write(output_stream)
        output.close()
        output_stream.seek(0)
        
        return HttpResponse(output_stream, content_type='application/pdf')
    return redirect(logout)

@login_required(login_url='loginpage')
def generate_pdf3(request): 
    if request.user.is_authenticated and  request.user.is_staff == 0:
        pagesize1 = (8.5 * inch, 13 * inch)  # 20 inch width and 10 inch height.
        packet = io.BytesIO()
        
        p = canvas.Canvas(packet, pagesize= pagesize1) 
        p.setFont("Helvetica", 7)  

        voluntary = voluntary_work.objects.all().filter(authUser_id=request.user.id).order_by('-id')
        startingx = int(44)
        startingy= int(756)

        data = [['','','','','']]
        for vol in voluntary:
            data.append([vol.org_info, vol.date_from.month,vol.date_from.day, vol.date_from.year, vol.date_to.month,vol.date_to.day, vol.date_to.year, vol.work_hours,
                    vol.position])
            
        try:
            data[1]

            if len((data[1])[0]) > 35:
                a = (data[1])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,753, top_text)
                p.drawString(39,759, bottom_text)
        
            else:
                p.drawString(39, 756, (data[1])[0])
            


            p.drawString(startingx+226, startingy, str(str((data[1])[1])+"/"))
            p.drawString(startingx+232, startingy, str(str((data[1])[2])+"/"))
            p.drawString(startingx+242, startingy, str(str((data[1])[3])))  

            p.drawString(startingx+263, startingy, str(str((data[1])[4])+"/"))
            p.drawString(startingx+273, startingy, str(str((data[1])[5])+"/"))
            p.drawString(startingx+283, startingy, str(str((data[1])[6])))  

            p.drawString(startingx+316, startingy, (data[1])[7])
            p.drawString(startingx+342, startingy, str(str((data[1])[8])))  

        except:
            pass

        try:
            data[2]

            if len((data[2])[0]) > 35:
                a = (data[2])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,740, top_text)
                p.drawString(39,734, bottom_text)
        
            else:
                p.drawString(39, 737, (data[2])[0])

            p.drawString(startingx+226, startingy-19, str(str((data[2])[1])+"/"))
            p.drawString(startingx+232, startingy-19, str(str((data[2])[2])+"/"))
            p.drawString(startingx+242, startingy-19, str(str((data[2])[3])))  

            p.drawString(startingx+263, startingy-19, str(str((data[2])[4])+"/"))
            p.drawString(startingx+273, startingy-19, str(str((data[2])[5])+"/"))
            p.drawString(startingx+283, startingy-19, str(str((data[2])[6])))  

            p.drawString(startingx+316, startingy-19, (data[2])[7])
            p.drawString(startingx+342, startingy-19, str(str((data[2])[8])))  

        except:
            pass

        try:
            data[3]

            if len((data[3])[0]) > 35:
                a = (data[3])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,720, top_text)
                p.drawString(39,714, bottom_text)
        
            else:
                p.drawString(39, 717, (data[3])[0])

            p.drawString(startingx+226, startingy-39, str(str((data[3])[1])+"/"))
            p.drawString(startingx+232, startingy-39, str(str((data[3])[2])+"/"))
            p.drawString(startingx+242, startingy-39, str(str((data[3])[3])))  

            p.drawString(startingx+263 , startingy-39, str(str((data[3])[4])+"/"))
            p.drawString(startingx+273, startingy-39, str(str((data[3])[5])+"/"))
            p.drawString(startingx+283, startingy-39, str(str((data[3])[6])))  

            p.drawString(startingx+316, startingy-39, (data[3])[7])
            p.drawString(startingx+342, startingy-39, str(str((data[3])[8])))  

        except:
            pass

        try:
            data[4]

            if len((data[4])[0]) > 35:
                a = (data[4])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,702, top_text)
                p.drawString(39,696, bottom_text)
        
            else:
                p.drawString(39, 699, (data[4])[0])

            p.drawString(startingx+226, startingy-57, str(str((data[4])[1])+"/"))
            p.drawString(startingx+232, startingy-57, str(str((data[4])[2])+"/"))
            p.drawString(startingx+242, startingy-57, str(str((data[4])[3])))  

            p.drawString(startingx+263, startingy-57, str(str((data[4])[4])+"/"))
            p.drawString(startingx+273, startingy-57, str(str((data[4])[5])+"/"))
            p.drawString(startingx+283, startingy-57, str(str((data[4])[6])))  

            p.drawString(startingx+316, startingy-57, (data[4])[7])
            p.drawString(startingx+342, startingy-57, str(str((data[4])[8])))  

        except:
            pass

        try:
            data[5]

            if len((data[5])[0]) > 35:
                a = (data[5])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,684, top_text)
                p.drawString(39,678, bottom_text)
        
            else:
                p.drawString(39, 681, (data[5])[0])

            p.drawString(startingx+226, startingy-75, str(str((data[5])[1])+"/"))
            p.drawString(startingx+232, startingy-75, str(str((data[5])[2])+"/"))
            p.drawString(startingx+242, startingy-75, str(str((data[5])[3])))  

            p.drawString(startingx+263, startingy-75, str(str((data[5])[4])+"/"))
            p.drawString(startingx+273, startingy-75, str(str((data[5])[5])+"/"))
            p.drawString(startingx+283, startingy-75, str(str((data[5])[6])))  

            p.drawString(startingx+316, startingy-75, (data[5])[7])
            p.drawString(startingx+342, startingy-75, str(str((data[5])[8])))  

        except:
            pass

        try:
            data[6]

            if len((data[6])[0]) > 35:
                a = (data[6])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,666, top_text)
                p.drawString(39,660, bottom_text)
        
            else:
                p.drawString(39, 663, (data[6])[0])

            p.drawString(startingx+226, startingy-93, str(str((data[6])[1])+"/"))
            p.drawString(startingx+232, startingy-93, str(str((data[6])[2])+"/"))
            p.drawString(startingx+242, startingy-93, str(str((data[6])[3])))  

            p.drawString(startingx+263, startingy-93, str(str((data[6])[4])+"/"))
            p.drawString(startingx+273, startingy-93, str(str((data[6])[5])+"/"))
            p.drawString(startingx+283, startingy-93, str(str((data[6])[6])))  

            p.drawString(startingx+316, startingy-93, (data[6])[7])
            p.drawString(startingx+342, startingy-93, str(str((data[6])[8])))  

        except:
            pass

        try:
            data[7]

            if len((data[7])[0]) > 35:
                a = (data[7])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,648, top_text)
                p.drawString(39,642, bottom_text)
        
            else:
                p.drawString(39, 645, (data[7])[0])


            p.drawString(startingx+226, startingy-111, str(str((data[7])[1])+"/"))
            p.drawString(startingx+232, startingy-111, str(str((data[7])[2])+"/"))
            p.drawString(startingx+242, startingy-111, str(str((data[7])[3])))  

            p.drawString(startingx+263, startingy-111, str(str((data[7])[4])+"/"))
            p.drawString(startingx+273, startingy-111, str(str((data[7])[5])+"/"))
            p.drawString(startingx+283, startingy-111, str(str((data[7])[6])))  

            p.drawString(startingx+316, startingy-111, (data[7])[7])
            p.drawString(startingx+342, startingy-111, str(str((data[7])[8])))  

        except:
            pass

        learning = learning_development.objects.all().filter(authUser_id=request.user.id).order_by('-id')
        startingx1 = int(44)
        startingy1= int(565)

        data2 = [['','','','','','']]
        for learn in learning:
            data2.append([learn.title, learn.date_of_attendance_from.month, learn.date_of_attendance_from.day,  learn.date_of_attendance_from.year,
                        learn.date_of_attendance_to.month, learn.date_of_attendance_to.day,  learn.date_of_attendance_to.year, learn.work_hours, learn.type_of_ld, learn.conducted])
            
        try:
            data2[1]

            if len((data2[1])[0]) > 35:
                a = (data2[1])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,562, top_text)
                p.drawString(40,569, bottom_text)
        
            else:
                p.drawString(40, 565, (data2[1])[0])

            p.drawString(startingx1+226, startingy1, str(str((data2[1])[1])+"/"))
            p.drawString(startingx1+232, startingy1, str(str((data2[1])[2])+"/"))
            p.drawString(startingx1+242, startingy1, str(str((data2[1])[3])))  

            p.drawString(startingx1+263, startingy1, str(str((data2[1])[4])+"/"))
            p.drawString(startingx1+273, startingy1, str(str((data2[1])[5])+"/"))
            p.drawString(startingx1+283, startingy1, str(str((data2[1])[6])))  

            p.drawString(startingx1+316, startingy1, (data2[1])[7])
            p.drawString(startingx1+342, startingy1, str(str((data2[1])[8])))  
            p.drawString(startingx1+386, startingy1, (data2[1])[9])

        except:
            pass

        try:
            data2[2]

            if len((data2[2])[0]) > 35:
                a = (data2[2])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,553, top_text)
                p.drawString(40,546, bottom_text)
        
            else:
                p.drawString(40, 549, (data2[2])[0])

            p.drawString(startingx1+226, startingy1-16, str(str((data2[2])[1])+"/"))
            p.drawString(startingx1+232, startingy1-16, str(str((data2[2])[2])+"/"))
            p.drawString(startingx1+242, startingy1-16, str(str((data2[2])[3])))  

            p.drawString(startingx1+263, startingy1-16, str(str((data2[2])[4])+"/"))
            p.drawString(startingx1+273, startingy1-16, str(str((data2[2])[5])+"/"))
            p.drawString(startingx1+283, startingy1-16, str(str((data2[2])[6])))  

            p.drawString(startingx1+316, startingy1-16, (data2[2])[7])
            p.drawString(startingx1+342, startingy1-16, str(str((data2[2])[8])))  
            p.drawString(startingx1+386, startingy1-16, (data2[2])[9])

        except:
            pass

        try:
            data2[3]

            if len((data2[3])[0]) > 35:
                a = (data2[3])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,536, top_text)
                p.drawString(40,529, bottom_text)
        
            else:
                p.drawString(40, 532, (data2[3])[0])

            p.drawString(startingx1+226, startingy1-33, str(str((data2[3])[1])+"/"))
            p.drawString(startingx1+232, startingy1-33, str(str((data2[3])[2])+"/"))
            p.drawString(startingx1+242, startingy1-33, str(str((data2[3])[3])))  

            p.drawString(startingx1+263, startingy1-33, str(str((data2[3])[4])+"/"))
            p.drawString(startingx1+273, startingy1-33, str(str((data2[3])[5])+"/"))
            p.drawString(startingx1+283, startingy1-33, str(str((data2[3])[6])))  

            p.drawString(startingx1+316, startingy1-33, (data2[3])[7])
            p.drawString(startingx1+342, startingy1-33, str(str((data2[3])[8])))  
            p.drawString(startingx1+386, startingy1-33, (data2[3])[9])

        except:
            pass

        try:
            data2[4]

            if len((data2[4])[0]) > 35:
                a = (data2[4])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,519, top_text)
                p.drawString(40,512, bottom_text)
        
            else:
                p.drawString(40, 515, (data2[4])[0])

            p.drawString(startingx1+226, startingy1-50, str(str((data2[4])[1])+"/"))
            p.drawString(startingx1+232, startingy1-50, str(str((data2[4])[2])+"/"))
            p.drawString(startingx1+242, startingy1-50, str(str((data2[4])[3])))  

            p.drawString(startingx1+263, startingy1-50, str(str((data2[4])[4])+"/"))
            p.drawString(startingx1+273, startingy1-50, str(str((data2[4])[5])+"/"))
            p.drawString(startingx1+283, startingy1-50, str(str((data2[4])[6])))  

            p.drawString(startingx1+316, startingy1-50, (data2[4])[7])
            p.drawString(startingx1+342, startingy1-50, str(str((data2[4])[8])))  
            p.drawString(startingx1+386, startingy1-50, (data2[4])[9])

        except:
            pass

        try:
            data2[5]

            if len((data2[5])[0]) > 35:
                a = (data2[5])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,501, top_text)
                p.drawString(40,494, bottom_text)
        
            else:
                p.drawString(40, 497, (data2[5])[0])

            p.drawString(startingx1+226, startingy1-68, str(str((data2[5])[1])+"/"))
            p.drawString(startingx1+232, startingy1-68, str(str((data2[5])[2])+"/"))
            p.drawString(startingx1+242, startingy1-68, str(str((data2[5])[3])))  

            p.drawString(startingx1+263, startingy1-68, str(str((data2[5])[4])+"/"))
            p.drawString(startingx1+273, startingy1-68, str(str((data2[5])[5])+"/"))
            p.drawString(startingx1+283, startingy1-68, str(str((data2[5])[6])))  

            p.drawString(startingx1+316, startingy1-68, (data2[5])[7])
            p.drawString(startingx1+342, startingy1-68, str(str((data2[5])[8])))  
            p.drawString(startingx1+386, startingy1-68, (data2[5])[9])

        except:
            pass

        try:
            data2[6]

            if len((data2[6])[0]) > 35:
                a = (data2[6])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,482, top_text)
                p.drawString(40,476, bottom_text)
        
            else:
                p.drawString(40, 479, (data2[6])[0])

            p.drawString(startingx1+226, startingy1-86, str(str((data2[6])[1])+"/"))
            p.drawString(startingx1+232, startingy1-86, str(str((data2[6])[2])+"/"))
            p.drawString(startingx1+242, startingy1-86, str(str((data2[6])[3])))  

            p.drawString(startingx1+263, startingy1-86, str(str((data2[6])[4])+"/"))
            p.drawString(startingx1+273, startingy1-86, str(str((data2[6])[5])+"/"))
            p.drawString(startingx1+283, startingy1-86, str(str((data2[6])[6])))  

            p.drawString(startingx1+316, startingy1-86, (data2[6])[7])
            p.drawString(startingx1+342, startingy1-86, str(str((data2[6])[8])))  
            p.drawString(startingx1+386, startingy1-86, (data2[6])[9])

        except:
            pass

        try:
            data2[7]

            if len((data2[7])[0]) > 35:
                a = (data2[7])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,467, top_text)
                p.drawString(40,460, bottom_text)
        
            else:
                p.drawString(40, 463, (data2[7])[0])

            p.drawString(startingx1+226, startingy1-102, str(str((data2[7])[1])+"/"))
            p.drawString(startingx1+232, startingy1-102, str(str((data2[7])[2])+"/"))
            p.drawString(startingx1+242, startingy1-102, str(str((data2[7])[3])))  

            p.drawString(startingx1+263, startingy1-102, str(str((data2[7])[4])+"/"))
            p.drawString(startingx1+273, startingy1-102, str(str((data2[7])[5])+"/"))
            p.drawString(startingx1+283, startingy1-102, str(str((data2[7])[6])))  

            p.drawString(startingx1+316, startingy1-102, (data2[7])[7])
            p.drawString(startingx1+342, startingy1-102, str(str((data2[7])[8])))  
            p.drawString(startingx1+386, startingy1-102, (data2[7])[9])

        except:
            pass

        try:
            data2[8]
                    
            if len((data2[8])[0]) > 35:
                a = (data2[8])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,450, top_text)
                p.drawString(40,442, bottom_text)
        
            else:
                p.drawString(40, 446, (data2[8])[0])

            p.drawString(startingx1+226, startingy1-119, str(str((data2[8])[1])+"/"))
            p.drawString(startingx1+232, startingy1-119, str(str((data2[8])[2])+"/"))
            p.drawString(startingx1+242, startingy1-119, str(str((data2[8])[3])))  

            p.drawString(startingx1+263, startingy1-119, str(str((data2[8])[4])+"/"))
            p.drawString(startingx1+273, startingy1-119, str(str((data2[8])[5])+"/"))
            p.drawString(startingx1+283, startingy1-119, str(str((data2[8])[6])))  

            p.drawString(startingx1+316, startingy1-119, (data2[8])[7])
            p.drawString(startingx1+342, startingy1-119, str(str((data2[8])[8])))  
            p.drawString(startingx1+386, startingy1-119, (data2[8])[9])

        except:
            pass

        try:
            data2[9]
                    
            if len((data2[9])[0]) > 35:
                a = (data2[9])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,432, top_text)
                p.drawString(40,425, bottom_text)
        
            else:
                p.drawString(40, 428, (data2[9])[0])

            

            p.drawString(startingx1+226, startingy1-137, str(str((data2[9])[1])+"/"))
            p.drawString(startingx1+232, startingy1-137, str(str((data2[9])[2])+"/"))
            p.drawString(startingx1+242, startingy1-137, str(str((data2[9])[3])))  

            p.drawString(startingx1+263, startingy1-137, str(str((data2[9])[4])+"/"))
            p.drawString(startingx1+273, startingy1-137, str(str((data2[9])[5])+"/"))
            p.drawString(startingx1+283, startingy1-137, str(str((data2[9])[6])))  

            p.drawString(startingx1+316, startingy1-137, (data2[9])[7])
            p.drawString(startingx1+342, startingy1-137, str(str((data2[9])[8])))  
            p.drawString(startingx1+386, startingy1-137, (data2[9])[9])

        except:
            pass

        try:
            data2[10]
                    
            if len((data2[10])[0]) > 35:
                a = (data2[10])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,416, top_text)
                p.drawString(40,409, bottom_text)
        
            else:
                p.drawString(40, 412, (data2[10])[0])

            p.drawString(startingx1+226, startingy1-153, str(str((data2[10])[1])+"/"))
            p.drawString(startingx1+232, startingy1-153, str(str((data2[10])[2])+"/"))
            p.drawString(startingx1+242, startingy1-153, str(str((data2[10])[3])))  

            p.drawString(startingx1+263, startingy1-153, str(str((data2[10])[4])+"/"))
            p.drawString(startingx1+273, startingy1-153, str(str((data2[10])[5])+"/"))
            p.drawString(startingx1+283, startingy1-153, str(str((data2[10])[6])))  

            p.drawString(startingx1+316, startingy1-153, (data2[10])[7])
            p.drawString(startingx1+342, startingy1-153, str(str((data2[10])[8])))  
            p.drawString(startingx1+386, startingy1-153, (data2[10])[9])
        except:
            pass

        try:
            data2[11]
                    
            if len((data2[11])[0]) > 35:
                a = (data2[11])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,400, top_text)
                p.drawString(40,393, bottom_text)
        
            else:
                p.drawString(40, 396, (data2[11])[0])

            p.drawString(startingx1+226, startingy1-169, str(str((data2[11])[1])+"/"))
            p.drawString(startingx1+232, startingy1-169, str(str((data2[11])[2])+"/"))
            p.drawString(startingx1+242, startingy1-169, str(str((data2[11])[3])))  

            p.drawString(startingx1+263, startingy1-169, str(str((data2[11])[4])+"/"))
            p.drawString(startingx1+273, startingy1-169, str(str((data2[11])[5])+"/"))
            p.drawString(startingx1+283, startingy1-169, str(str((data2[11])[6])))  

            p.drawString(startingx1+316, startingy1-169, (data2[11])[7])
            p.drawString(startingx1+342, startingy1-169, str(str((data2[11])[8])))  
            p.drawString(startingx1+386, startingy1-169, (data2[11])[9])
        except:
            pass

        try:
            data2[12]
                    
            if len((data2[12])[0]) > 35:
                a = (data2[12])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,382, top_text)
                p.drawString(40,375, bottom_text)
        
            else:
                p.drawString(40, 378, (data2[12])[0])

            p.drawString(startingx1+226, startingy1-187, str(str((data2[12])[1])+"/"))
            p.drawString(startingx1+232, startingy1-187, str(str((data2[12])[2])+"/"))
            p.drawString(startingx1+242, startingy1-187, str(str((data2[12])[3])))  

            p.drawString(startingx1+263, startingy1-187, str(str((data2[12])[4])+"/"))
            p.drawString(startingx1+273, startingy1-187, str(str((data2[12])[5])+"/"))
            p.drawString(startingx1+283, startingy1-187, str(str((data2[12])[6])))  

            p.drawString(startingx1+316, startingy1-187, (data2[12])[7])
            p.drawString(startingx1+342, startingy1-187, str(str((data2[12])[8])))  
            p.drawString(startingx1+386, startingy1-187, (data2[12])[9])
        except:
            pass

        try:
            data2[13]

                    
            if len((data2[13])[0]) > 35:
                a = (data2[13])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,365, top_text)
                p.drawString(40,358, bottom_text)
        
            else:
                p.drawString(40, 361, (data2[13])[0])

            p.drawString(startingx1+226, startingy1-204, str(str((data2[13])[1])+"/"))
            p.drawString(startingx1+232, startingy1-204, str(str((data2[13])[2])+"/"))
            p.drawString(startingx1+242, startingy1-204, str(str((data2[13])[3])))  

            p.drawString(startingx1+263, startingy1-204, str(str((data2[13])[4])+"/"))
            p.drawString(startingx1+273, startingy1-204, str(str((data2[13])[5])+"/"))
            p.drawString(startingx1+283, startingy1-204, str(str((data2[13])[6])))  

            p.drawString(startingx1+316, startingy1-204, (data2[13])[7])
            p.drawString(startingx1+342, startingy1-204, str(str((data2[13])[8])))  
            p.drawString(startingx1+386, startingy1-204, (data2[13])[9])
        except:
            pass

        try:
            data2[14]
                    
            if len((data2[14])[0]) > 35:
                a = (data2[14])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,348, top_text)
                p.drawString(40,341, bottom_text)
        
            else:
                p.drawString(40, 345, (data2[14])[0])
                

            p.drawString(startingx1+226, startingy1-221, str(str((data2[14])[1])+"/"))
            p.drawString(startingx1+232, startingy1-221, str(str((data2[14])[2])+"/"))
            p.drawString(startingx1+242, startingy1-221, str(str((data2[14])[3])))  

            p.drawString(startingx1+263, startingy1-221, str(str((data2[14])[4])+"/"))
            p.drawString(startingx1+273, startingy1-221, str(str((data2[14])[5])+"/"))
            p.drawString(startingx1+283, startingy1-221, str(str((data2[14])[6])))  

            p.drawString(startingx1+316, startingy1-221, (data2[14])[7])
            p.drawString(startingx1+342, startingy1-221, str(str((data2[14])[8])))  
            p.drawString(startingx1+386, startingy1-221, (data2[14])[9])
        except:
            pass

        try:
            data2[15]
            
            if len((data2[15])[0]) > 35:
                a = (data2[15])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,331, top_text)
                p.drawString(40,324, bottom_text)
        
            else:
                p.drawString(40, 327, (data2[15])[0])
                

            p.drawString(startingx1+226, startingy1-238, str(str((data2[15])[1])+"/"))
            p.drawString(startingx1+232, startingy1-238, str(str((data2[15])[2])+"/"))
            p.drawString(startingx1+242, startingy1-238, str(str((data2[15])[3])))  

            p.drawString(startingx1+263, startingy1-238, str(str((data2[15])[4])+"/"))
            p.drawString(startingx1+273, startingy1-238, str(str((data2[15])[5])+"/"))
            p.drawString(startingx1+283, startingy1-238, str(str((data2[15])[6])))  

            p.drawString(startingx1+316, startingy1-238, (data2[15])[7])
            p.drawString(startingx1+342, startingy1-238, str(str((data2[15])[8])))  
            p.drawString(startingx1+386, startingy1-238, (data2[15])[9])
        except:
            pass

        try:
            data2[16]
                    
            if len((data2[16])[0]) > 35:
                a = (data2[16])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,314, top_text)
                p.drawString(40,307, bottom_text)
        
            else:
                p.drawString(40, 310, (data2[16])[0])

            p.drawString(startingx1+226, startingy1-255, str(str((data2[16])[1])+"/"))
            p.drawString(startingx1+232, startingy1-255, str(str((data2[16])[2])+"/"))
            p.drawString(startingx1+242, startingy1-255, str(str((data2[16])[3])))  

            p.drawString(startingx1+263, startingy1-255, str(str((data2[16])[4])+"/"))
            p.drawString(startingx1+273, startingy1-255, str(str((data2[16])[5])+"/"))
            p.drawString(startingx1+283, startingy1-255, str(str((data2[16])[6])))  

            p.drawString(startingx1+316, startingy1-255, (data2[16])[7])
            p.drawString(startingx1+342, startingy1-255, str(str((data2[16])[8])))  
            p.drawString(startingx1+386, startingy1-255, (data2[16])[9])
        except:
            pass

        try:
            data2[17]
            
            if len((data2[17])[0]) > 35:
                a = (data2[17])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,297, top_text)
                p.drawString(40,290, bottom_text)
        
            else:
                p.drawString(40, 293, (data2[17])[0])

            p.drawString(startingx1+226, startingy1-272, str(str((data2[17])[1])+"/"))
            p.drawString(startingx1+232, startingy1-272, str(str((data2[17])[2])+"/"))
            p.drawString(startingx1+242, startingy1-272, str(str((data2[17])[3])))  

            p.drawString(startingx1+263, startingy1-272, str(str((data2[17])[4])+"/"))
            p.drawString(startingx1+273, startingy1-272, str(str((data2[17])[5])+"/"))
            p.drawString(startingx1+283, startingy1-272, str(str((data2[17])[6])))  

            p.drawString(startingx1+316, startingy1-272, (data2[17])[7])
            p.drawString(startingx1+342, startingy1-272, str(str((data2[17])[8])))  
            p.drawString(startingx1+386, startingy1-272, (data2[17])[9])
        except:
            pass

        try:
            data2[18]

            if len((data2[18])[0]) > 35:
                a = (data2[18])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,280, top_text)
                p.drawString(40,273, bottom_text)
        
            else:
                p.drawString(40, 276, (data2[18])[0])

            p.drawString(startingx1+226, startingy1-289, str(str((data2[18])[1])+"/"))
            p.drawString(startingx1+232, startingy1-289, str(str((data2[18])[2])+"/"))
            p.drawString(startingx1+242, startingy1-289, str(str((data2[18])[3])))  

            p.drawString(startingx1+263, startingy1-289, str(str((data2[18])[4])+"/"))
            p.drawString(startingx1+273, startingy1-289, str(str((data2[18])[5])+"/"))
            p.drawString(startingx1+283, startingy1-289, str(str((data2[18])[6])))  

            p.drawString(startingx1+316, startingy1-289, (data2[18])[7])
            p.drawString(startingx1+342, startingy1-289, str(str((data2[18])[8])))  
            p.drawString(startingx1+386, startingy1-289, (data2[18])[9])
        except:
            pass

        try:
            data2[19]

            if len((data2[19])[0]) > 35:
                a = (data2[19])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,263, top_text)
                p.drawString(40,256, bottom_text)
        
            else:
                p.drawString(40, 259, (data2[19])[0])

            p.drawString(startingx1+226, startingy1-306, str(str((data2[19])[1])+"/"))
            p.drawString(startingx1+232, startingy1-306, str(str((data2[19])[2])+"/"))
            p.drawString(startingx1+242, startingy1-306, str(str((data2[19])[3])))  

            p.drawString(startingx1+263, startingy1-306, str(str((data2[19])[4])+"/"))
            p.drawString(startingx1+273, startingy1-306, str(str((data2[19])[5])+"/"))
            p.drawString(startingx1+283, startingy1-306, str(str((data2[19])[6])))  

            p.drawString(startingx1+316, startingy1-306, (data2[19])[7])
            p.drawString(startingx1+342, startingy1-306, str(str((data2[19])[8])))  
            p.drawString(startingx1+386, startingy1-306, (data2[19])[9])
        except:
            pass

        try:
            data2[20]
            
            if len((data2[20])[0]) > 35:
                a = (data2[20])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,246, top_text)
                p.drawString(40,239, bottom_text)
        
            else:
                p.drawString(40, 242, (data2[20])[0])

            p.drawString(startingx1+226, startingy1-323, str(str((data2[20])[1])+"/"))
            p.drawString(startingx1+232, startingy1-323, str(str((data2[20])[2])+"/"))
            p.drawString(startingx1+242, startingy1-323, str(str((data2[20])[3])))  

            p.drawString(startingx1+263, startingy1-323, str(str((data2[20])[4])+"/"))
            p.drawString(startingx1+273, startingy1-323, str(str((data2[20])[5])+"/"))
            p.drawString(startingx1+283, startingy1-323, str(str((data2[20])[6])))  

            p.drawString(startingx1+316, startingy1-323, (data2[20])[7])
            p.drawString(startingx1+342, startingy1-323, str(str((data2[20])[8])))  
            p.drawString(startingx1+386, startingy1-323, (data2[20])[9])
        except:
            pass

        try:
            data2[21]
        
            if len((data2[21])[0]) > 35:
                a = (data2[21])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,229, top_text)
                p.drawString(40,222, bottom_text)
        
            else:
                p.drawString(40, 225, (data2[21])[0])

            p.drawString(startingx1+226, startingy1-340, str(str((data2[21])[1])+"/"))
            p.drawString(startingx1+232, startingy1-340, str(str((data2[21])[2])+"/"))
            p.drawString(startingx1+242, startingy1-340, str(str((data2[21])[3])))  

            p.drawString(startingx1+263, startingy1-340, str(str((data2[21])[4])+"/")) 
            p.drawString(startingx1+273, startingy1-340, str(str((data2[21])[5])+"/"))
            p.drawString(startingx1+283, startingy1-340, str(str((data2[21])[6])))  

            p.drawString(startingx1+316, startingy1-340, (data2[21])[7])
            p.drawString(startingx1+342, startingy1-340, str(str((data2[21])[8])))  
            p.drawString(startingx1+386, startingy1-340, (data2[21])[9])
        except:
            pass

        other = other_info.objects.all().filter(authUser_id=request.user.id).order_by('-id')
        startingx2 = int(44)
        startingy2= int(160 )

        data3 = [['','','']]
        for oth in other:
            data3.append([oth.skills_hobbies, oth.non_acad_recognition, oth.membership])
            
        try:
            data3[1]

            if len((data3[1])[2]) > 35:
                a = (data3[1])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,157, top_text)
                p.drawString(430,163, bottom_text)
        
            else:
                p.drawString(430, 160, (data3[1])[2])

            p.drawString(startingx2, startingy2, (data3[1])[0])
            p.drawString(startingx2+135, startingy2, (data3[1])[1])

        except:
            pass

        try:
            data3[2]

            if len((data3[2])[2]) > 35:
                a = (data3[2])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,138, top_text)
                p.drawString(430,144, bottom_text)
        
            else:
                p.drawString(430, 141, (data3[2])[2])

            p.drawString(startingx2, startingy2-19, (data3[2])[0])
            p.drawString(startingx2+135, startingy2-19, (data3[2])[1])
            
        except:
            pass

        
        try:
            data3[3]

            if len((data3[3])[2]) > 35:
                a = (data3[3])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,126, top_text)
                p.drawString(430,120, bottom_text)
        
            else:
                p.drawString(430, 123, (data3[3])[2])

            p.drawString(startingx2, startingy2-37, (data3[3])[0])
            p.drawString(startingx2+135, startingy2-37, (data3[3])[1])

        except:
            pass

        try:
            data3[4]

            if len((data3[4])[2]) > 35:
                a = (data3[4])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,108, top_text)
                p.drawString(430,102, bottom_text)
        
            else:
                p.drawString(430, 105, (data3[4])[2])

            p.drawString(startingx2, startingy2-55, (data3[4])[0])
            p.drawString(startingx2+135, startingy2-55, (data3[4])[1])

        except:
            pass

        try:
            data3[5]

            if len((data3[5])[2]) > 35:
                a = (data3[5])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,93, top_text)
                p.drawString(430,87, bottom_text)
        
            else:
                p.drawString(430, 90, (data3[5])[2])

            p.drawString(startingx2, startingy2-70, (data3[5])[0])
            p.drawString(startingx2+135, startingy2-70, (data3[5])[1])

        except:
            pass

        try:
            data3[6]

            if len((data3[6])[2]) > 35:
                a = (data3[6])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,70, top_text)
                p.drawString(430,76, bottom_text)
        
            else:
                p.drawString(430, 73, (data3[6])[2])

            p.drawString(startingx2, startingy2-87  , (data3[6])[0])
            p.drawString(startingx2+135, startingy2-87  , (data3[6])[1])


        except:
            pass

        try:
            data3[7]

            if len((data3[7])[2]) > 35:
                a = (data3[7])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,57, top_text)
                p.drawString(430,63, bottom_text)
        
            else:
                p.drawString(430, 58, (data3[7])[2])

            p.drawString(startingx2, startingy2-102, (data3[7])[0])
            p.drawString(startingx2+135, startingy2-102, (data3[7])[1])
        
        except:
            pass

        p.save()

        packet.seek(0)

        new_pdf = PdfReader(packet)
        existing_pdf = PdfReader(open("var/www/django_project/page3.pdf", "rb"))
        output = PdfWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)


        output_stream = BytesIO()
        output.write(output_stream)
        output.close()
        output_stream.seek(0)
        
        return HttpResponse(output_stream, content_type='application/pdf')
    return redirect(logout)

@login_required(login_url='loginpage')
def generate_pdf4(request):
    if request.user.is_authenticated and  request.user.is_staff == 0:
        pagesize1 = (8.5 * inch, 13 * inch)  # 20 inch width and 10 inch height.
        packet = io.BytesIO()
        
        p = canvas.Canvas(packet, pagesize= pagesize1) 
        p.setFont("Helvetica", 7) 


        name1 = references.objects.filter(authUser_id=request.user.id).values_list('name1',flat=True).first() 
        name2 = references.objects.filter(authUser_id=request.user.id).values_list('name2',flat=True).first() 
        name3 = references.objects.filter(authUser_id=request.user.id).values_list('name3',flat=True).first() 
        address1 = references.objects.filter(authUser_id=request.user.id).values_list('address1',flat=True).first() 
        address2 = references.objects.filter(authUser_id=request.user.id).values_list('address2',flat=True).first() 
        address3 = references.objects.filter(authUser_id=request.user.id).values_list('address3',flat=True).first() 
        telno1 = references.objects.filter(authUser_id=request.user.id).values_list('telno1',flat=True).first() 
        telno2 = references.objects.filter(authUser_id=request.user.id).values_list('telno2',flat=True).first() 
        telno3 = references.objects.filter(authUser_id=request.user.id).values_list('telno3',flat=True).first()
        gov_id = references.objects.filter(authUser_id=request.user.id).values_list('gov_id',flat=True).first()
        license_id = references.objects.filter(authUser_id=request.user.id).values_list('license_id',flat=True).first()
        date = references.objects.filter(authUser_id=request.user.id).values_list('date',flat=True).first()
        indigenous = references.objects.filter(authUser_id=request.user.id).values_list('indigenous',flat=True).first()
        indig_specify = references.objects.filter(authUser_id=request.user.id).values_list('indig_specify',flat=True).first()
        disability = references.objects.filter(authUser_id=request.user.id).values_list('disability',flat=True).first()
        disab_specify = references.objects.filter(authUser_id=request.user.id).values_list('disab_specify',flat=True).first()
        solo_parent = references.objects.filter(authUser_id=request.user.id).values_list('solo_parent',flat=True).first()
        solo_specify= references.objects.filter(authUser_id=request.user.id).values_list('solo_specify',flat=True).first()

        name11 = f'{name1}'
        name21 = f'{name2}'
        name31 = f'{name3}'
        address11 = f'{address1}'
        address21 = f'{address2}'
        address31 = f'{address3}'
        telno11 = f'{telno1}'
        telno21 = f'{telno2}'
        telno31 = f'{telno3}'
        gov_id1 = f'{gov_id}'
        license_id1 = f'{license_id}'
        date1 = f'{date.month}/{date.day}/{date.year}'
        indig_specify1 = f'{indig_specify}'
        disab_specify1 = f'{disab_specify}'
        solo_specify1 = f'{solo_specify}'

        p.drawString(431, 770, '✓')
        p.drawString(431, 756, '✓')
        p.drawString(431, 715, '✓')
        p.drawString(434, 670, '✓')
        p.drawString(437, 615, '✓')
        p.drawString(438, 572, '✓')
        p.drawString(442, 535, '✓')
        p.drawString(443, 509, '✓')
        p.drawString(442, 478, '✓')

        if indigenous == 'yes':  
            p.drawString(375, 413, '✓')
        else:
            p.drawString(444, 413, '✓')
        
        p.drawString(475, 403, indig_specify1)

        if disability == 'yes':  
            p.drawString(375, 391, '✓')
        else:
            p.drawString(444, 391, '✓')

        p.drawString(475, 379, disab_specify1)

        if solo_parent == 'yes':  
            p.drawString(375, 368, '✓')
        else:
            p.drawString(444, 368, '✓')

        p.drawString(475, 358, solo_specify1)
        
        p.drawString(40, 305, name11)

        if len(address11) > 40:
            a = address11.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(240,308, top_text)
            p.drawString(240,301, bottom_text)
        
        else:
            p.drawString(240, 305, address11)

        p.drawString(365, 305, telno11)

        p.drawString(40, 285, name21)

        if len(address21) > 40:
            a = address21.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(240,288, top_text)
            p.drawString(240,281, bottom_text)
        
        else:
            p.drawString(240, 285, address21)

        p.drawString(365, 285, telno21)

        p.drawString(40, 265, name31)

        if len(address31) > 40:
            a = address31.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(240,269, top_text)
            p.drawString(240,262, bottom_text)
        
        else:
            p.drawString(240, 265, address31)

        p.drawString(365, 265, telno31)

        p.drawString(110, 158, gov_id1)
        p.drawString(110, 140, license_id1)
        p.drawString(110, 123, date1)

        p.save()

        packet.seek(0)

        new_pdf = PdfReader(packet)
        existing_pdf = PdfReader(open("var/www/django_project/page4.pdf", "rb"))
        output = PdfWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)


        output_stream = BytesIO()
        output.write(output_stream)
        output.close()
        output_stream.seek(0)

        return HttpResponse(output_stream, content_type='application/pdf')
    return redirect('logout')

def inactive(request):
    return render(request, 'inactive.html')

@login_required(login_url='loginpage')
def admin_generate_pdf(request, pk):
    if request.user.is_authenticated and  request.user.is_staff == 1:
        pagesize1 = (8.5 * inch, 13 * inch)  # 20 inch width and 10 inch height.


        surname =personal_information.objects.filter(authUser_id=pk).values_list('surname',flat=True).first() 
        firstname =personal_information.objects.filter(authUser_id=pk).values_list('firstname',flat=True).first() 
        middlename =personal_information.objects.filter(authUser_id=pk).values_list('middlename',flat=True).first()
        name_ext =personal_information.objects.filter(authUser_id=pk).values_list('name_ext',flat=True).first()
        date_of_birth =personal_information.objects.filter(authUser_id=pk).values_list('date_of_birth',flat=True).first() 
        place_of_birth =personal_information.objects.filter(authUser_id=pk).values_list('place_of_birth',flat=True).first() 
        sex =personal_information.objects.filter(authUser_id=pk).values_list('sex',flat=True).first()
        civil_status =personal_information.objects.filter(authUser_id=pk).values_list('civil_status',flat=True).first()
        height =personal_information.objects.filter(authUser_id=pk).values_list('height',flat=True).first()
        weight =personal_information.objects.filter(authUser_id=pk).values_list('weight',flat=True).first()
        bloodtype =personal_information.objects.filter(authUser_id=pk).values_list('bloodtype',flat=True).first()
        gsis =personal_information.objects.filter(authUser_id=pk).values_list('gsis',flat=True).first()
        pagibig =personal_information.objects.filter(authUser_id=pk).values_list('pagibig',flat=True).first()
        philhealth =personal_information.objects.filter(authUser_id=pk).values_list('philhealth',flat=True).first()
        sss =personal_information.objects.filter(authUser_id=pk).values_list('sss',flat=True).first()
        tin =personal_information.objects.filter(authUser_id=pk).values_list('tin',flat=True).first()
        agency_no =personal_information.objects.filter(authUser_id=pk).values_list('agency_no',flat=True).first()
        telno =personal_information.objects.filter(authUser_id=pk).values_list('telno',flat=True).first()
        mobile =personal_information.objects.filter(authUser_id=pk).values_list('mobile',flat=True).first()
        email =personal_information.objects.filter(authUser_id=pk).values_list('email',flat=True).first()


        surname1 = f'{surname}'
        firstname1 = f'{firstname}'
        middlename1 = f'{middlename}'
        name_ext1 = f'{name_ext}'
        date_of_birth1 = f'{date_of_birth.month}/{date_of_birth.day}/{date_of_birth.year}'
        print(firstname1)
        place_of_birth1 = f'{place_of_birth}'
        sex1 = f'{sex}'
        civil_status1 = f'{civil_status}'
        height1 = f'{height}'
        weight1 = f'{weight}'
        bloodtype1 = f'{bloodtype}'
        gsis1 = f'{gsis}'
        pagibig1 = f'{pagibig}'
        philhealth1 = f'{philhealth}'
        sss1 = f'{sss}'
        tin1 = f'{tin}'
        agency_no1 = f'{agency_no}'
        telno1 = f'{telno}'
        mobile1 = f'{mobile}'
        email1 = f'{email}'

        packet = io.BytesIO()

        p = canvas.Canvas(packet, pagesize= pagesize1)  

        p.setFont("Helvetica", 6)             # Init a PDF object
        p.drawString(135, 715, surname1)          # Draw a simple String    
        p.drawString(135, 700, firstname1)
        p.drawString(510, 700, name_ext1) 
        p.drawString(135, 685, middlename1)    
        #p.drawString(135, 663, date_of_birth1)  
        p.drawString(135, 641, place_of_birth1)
        if sex1 == 'Male':  
            p.drawString(136, 626, '✓')
        else:
            p.drawString(211, 624, '✓')

        if civil_status1 == 'Single':  
            p.drawString(136, 610, '✓')
        elif civil_status1 == 'Widowed': 
            p.drawString(136, 600, '✓') 
        elif civil_status1 == 'Married': 
            p.drawString(211, 610, '✓')  
        elif civil_status1 == 'Separated': 
            p.drawString(211, 600, '✓')  
        else: 
            p.drawString(136, 589, '✓')   
        
        p.drawString(135, 570, height1)
        p.drawString(135, 553, weight1)
        p.drawString(135, 536, bloodtype1)
        p.drawString(135,519, gsis1)
        p.drawString(135,500, pagibig1)
        p.drawString(135,482, philhealth1)
        p.drawString(135,464, sss1)
        p.drawString(135,445, tin1)
        p.drawString(135,428, agency_no1)
        p.drawString(338,464, telno1)
        p.drawString(338,445, mobile1)
        p.drawString(338,428, email1)
        p.drawString(382,667, '✓')

        #Address
        res_block =personal_information.objects.filter(authUser_id=pk).values_list('res_block',flat=True).first()
        res_street =personal_information.objects.filter(authUser_id=pk).values_list('res_street',flat=True).first()
        res_subd =personal_information.objects.filter(authUser_id=pk).values_list('res_subd',flat=True).first()
        res_brgy =personal_information.objects.filter(authUser_id=pk).values_list('res_brgy',flat=True).first()
        res_city =personal_information.objects.filter(authUser_id=pk).values_list('res_city',flat=True).first()
        res_prov =personal_information.objects.filter(authUser_id=pk).values_list('res_prov',flat=True).first()
        res_street =personal_information.objects.filter(authUser_id=pk).values_list('res_street',flat=True).first()
        res_zip =personal_information.objects.filter(authUser_id=pk).values_list('res_zip',flat=True).first()

        res_block1 = f'{res_block}'
        res_street1 = f'{res_street}'
        res_subd1 = f'{res_subd}'
        res_brgy1 = f'{res_brgy}'
        res_city1 = f'{res_city}'
        res_prov1 = f'{res_prov}'
        res_zip1 = f'{res_zip}'

        p.drawString(350, 608, res_block1) 
        p.drawString(460, 608, res_street1) 
        p.drawString(350, 590, res_subd1) 
        p.drawString(460, 590, res_brgy1) 
        p.drawString(350, 573, res_city1) 
        p.drawString(460, 573, res_prov1)  
        p.drawString(350, 553, res_zip1 ) 

        per_block =personal_information.objects.filter(authUser_id=pk).values_list('per_block',flat=True).first()
        per_street =personal_information.objects.filter(authUser_id=pk).values_list('per_street',flat=True).first()
        per_subd =personal_information.objects.filter(authUser_id=pk).values_list('per_subd',flat=True).first()
        per_brgy =personal_information.objects.filter(authUser_id=pk).values_list('per_brgy',flat=True).first()
        per_city =personal_information.objects.filter(authUser_id=pk).values_list('per_city',flat=True).first()
        per_prov =personal_information.objects.filter(authUser_id=pk).values_list('per_prov',flat=True).first()
        per_zip =personal_information.objects.filter(authUser_id=pk).values_list('per_zip',flat=True).first()

        per_block1 = f'{per_block}'
        per_street1 = f'{per_street}'
        per_subd1 = f'{per_subd}'
        per_brgy1 = f'{per_brgy}'
        per_city1 = f'{per_city}'
        per_prov1 = f'{per_prov}'
        per_zip1 = f'{per_zip}'
        
        p.drawString(350, 539, per_block1) 
        p.drawString(460, 539, per_street1) 
        p.drawString(350, 521, per_subd1) 
        p.drawString(460, 521, per_brgy1) 
        p.drawString(350, 504, per_city1) 
        p.drawString(460, 504, per_prov1) 
        p.drawString(350, 482, per_zip1) 

        # Family Background
        spouse_surname =family_background.objects.filter(authUser_id=pk).values_list('spouse_surname',flat=True).first()
        spouse_firstname =family_background.objects.filter(authUser_id=pk).values_list('spouse_firstname',flat=True).first()
        spouse_extension =family_background.objects.filter(authUser_id=pk).values_list('spouse_extension',flat=True).first()
        spouse_middlename =family_background.objects.filter(authUser_id=pk).values_list('spouse_middlename',flat=True).first()
        occupation =family_background.objects.filter(authUser_id=pk).values_list('occupation',flat=True).first()
        employee_name =family_background.objects.filter(authUser_id=pk).values_list('employee_name',flat=True).first()    
        business_address =family_background.objects.filter(authUser_id=pk).values_list('business_address',flat=True).first()  
        family_telno =family_background.objects.filter(authUser_id=pk).values_list('family_telno',flat=True).first() 
        father_surname =family_background.objects.filter(authUser_id=pk).values_list('father_surname',flat=True).first() 
        father_firstname =family_background.objects.filter(authUser_id=pk).values_list('father_firstname',flat=True).first()
        father_extension =family_background.objects.filter(authUser_id=pk).values_list('father_extension',flat=True).first()
        father_middlename =family_background.objects.filter(authUser_id=pk).values_list('father_middlename',flat=True).first()   
        mother_surname =family_background.objects.filter(authUser_id=pk).values_list('mother_surname',flat=True).first() 
        mother_firstname =family_background.objects.filter(authUser_id=pk).values_list('mother_firstname',flat=True).first()
        mother_middlename =family_background.objects.filter(authUser_id=pk).values_list('mother_middlename',flat=True).first()   
                

        spouse_surname1 = f'{spouse_surname}'
        spouse_firstname1 = f'{spouse_firstname}'
        spouse_extension1 = f'{spouse_extension}'
        spouse_middlename1 = f'{spouse_middlename}'
        occupation1 = f'{occupation}'
        employee_name1 = f'{employee_name}'
        business_address1 = f'{business_address}'
        family_telno1 = f'{family_telno}'
        father_surname1 = f'{father_surname}'
        father_firstname1 = f'{father_firstname}'
        father_extension1 = f'{father_extension}'
        father_middlename1 = f'{father_middlename}'
        mother_surname1 = f'{mother_surname}'
        mother_firstname1 = f'{mother_firstname}'
        mother_middlename1 = f'{mother_middlename}'

        p.drawString(135, 400, spouse_surname1)
        p.drawString(135, 385, spouse_firstname1)
        p.drawString(317, 385, spouse_extension1)
        p.drawString(135, 369, spouse_middlename1)
        p.drawString(135, 354, occupation1)
        p.drawString(135, 338, employee_name1)
        p.drawString(135, 323, business_address1)
        p.drawString(135, 308, family_telno1)
        p.drawString(135, 293, father_surname1)
        p.drawString(135, 278, father_firstname1)
        p.drawString(317, 278, father_extension1)
        p.drawString(135, 263, father_middlename1)
        p.drawString(135, 231, mother_surname1)
        p.drawString(135, 216, mother_firstname1)
        p.drawString(135, 201, mother_middlename1)


        #educational background
        elem_school =educational_background.objects.filter(authUser_id=pk).values_list('elem_school',flat=True).first()
        elem_course =educational_background.objects.filter(authUser_id=pk).values_list('elem_course',flat=True).first()
        elem_attendance_to =educational_background.objects.filter(authUser_id=pk).values_list('elem_attendance_to',flat=True).first()
        elem_attendance_from =educational_background.objects.filter(authUser_id=pk).values_list('elem_attendance_from',flat=True).first()
        elem_units =educational_background.objects.filter(authUser_id=pk).values_list('elem_units',flat=True).first()
        elem_grad =educational_background.objects.filter(authUser_id=pk).values_list('elem_grad',flat=True).first()
        elem_honors =educational_background.objects.filter(authUser_id=pk).values_list('elem_honors',flat=True).first()

        elem_school1 = f'{elem_school}'
        elem_course1 = f'{elem_course}'
        elem_attendance1_to = f'{elem_attendance_to}'
        elem_attendance1_from = f'{elem_attendance_from}'
        elem_units1 = f'{elem_units}'
        elem_grad1 = f'{elem_grad}'
        elem_honors1 = f'{elem_honors}'

        if len(elem_school1) > 47:
            a = elem_school1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(130,142, top_text)
            p.drawString(130,132, bottom_text)
        
        else:
            p.drawString(130, 137, elem_school1)


        
        p.drawString(262, 137, elem_course1)
        p.drawString(380, 137, elem_attendance1_to)
        p.drawString(412, 137, elem_attendance1_from)
        p.drawString(443, 137, elem_units1)
        p.drawString(494, 137, elem_grad1)
        p.drawString(533, 137, elem_honors1)


        secondary_school =educational_background.objects.filter(authUser_id=pk).values_list('secondary_school',flat=True).first()
        secondary_course =educational_background.objects.filter(authUser_id=pk).values_list('secondary_course',flat=True).first()
        secondary_attendance_to =educational_background.objects.filter(authUser_id=pk).values_list('secondary_attendance_to',flat=True).first()
        secondary_attendance_from =educational_background.objects.filter(authUser_id=pk).values_list('secondary_attendance_from',flat=True).first()
        secondary_units =educational_background.objects.filter(authUser_id=pk).values_list('secondary_units',flat=True).first()
        secondary_grad =educational_background.objects.filter(authUser_id=pk).values_list('secondary_grad',flat=True).first()
        secondary_honors =educational_background.objects.filter(authUser_id=pk).values_list('secondary_honors',flat=True).first()

        secondary_school1 = f'{secondary_school}'
        secondary_course1 = f'{secondary_course}'
        secondary_attendance1_to = f'{secondary_attendance_to}'
        secondary_attendance1_from = f'{secondary_attendance_from}'
        secondary_units1 = f'{secondary_units}'
        secondary_grad1 = f'{secondary_grad}'
        secondary_honors1 = f'{secondary_honors}'

        if len(secondary_school1) > 47:
            a = secondary_school1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(130,122, top_text)
            p.drawString(130,112, bottom_text)
        
        else:
            p.drawString(130, 115, secondary_school1)   

        if len(secondary_course1) > 40:
            a = secondary_course1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(258,121, top_text)
            p.drawString(258,112, bottom_text)
        
        else:
            p.drawString(258, 115, secondary_course1)

        
        p.drawString(380, 115,  secondary_attendance1_to)
        p.drawString(412, 115, secondary_attendance1_from)
        p.drawString(443, 115, secondary_units1)
        p.drawString(494, 115, secondary_grad1)
        p.drawString(533, 115, secondary_honors1)

        vocational_school =educational_background.objects.filter(authUser_id=pk).values_list('vocational_school',flat=True).first()
        vocational_course =educational_background.objects.filter(authUser_id=pk).values_list('vocational_course',flat=True).first()
        vocational_attendance_to =educational_background.objects.filter(authUser_id=pk).values_list('vocational_attendance_to',flat=True).first()
        vocational_attendance_from =educational_background.objects.filter(authUser_id=pk).values_list('vocational_attendance_from',flat=True).first()
        vocational_units =educational_background.objects.filter(authUser_id=pk).values_list('vocational_units',flat=True).first()
        vocational_grad =educational_background.objects.filter(authUser_id=pk).values_list('vocational_grad',flat=True).first()
        vocational_honors =educational_background.objects.filter(authUser_id=pk).values_list('vocational_honors',flat=True).first()

        vocational_school1 = f'{vocational_school}'
        vocational_course1 = f'{vocational_course}'
        vocational_attendance1_to = f'{vocational_attendance_to}'
        vocational_attendance1_from = f'{vocational_attendance_from}'
        vocational_units1 = f'{vocational_units}'
        vocational_grad1 = f'{vocational_grad}'
        vocational_honors1 = f'{vocational_honors}'   

        if len(vocational_school1) > 47:
            a = vocational_school1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(130,102, top_text)
            p.drawString(130,92, bottom_text)
        
        else:
            p.drawString(130, 95, vocational_school1)

        if len(vocational_course1) > 40:
            a = vocational_course1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(258,102, top_text)
            p.drawString(258,92, bottom_text)
        
        else:
            p.drawString(258, 95, vocational_course1)

        
        p.drawString(380, 95, vocational_attendance1_to)
        p.drawString(412, 95, vocational_attendance1_from)
        p.drawString(443, 95, vocational_units1)
        p.drawString(494, 95, vocational_grad1)
        p.drawString(533, 95, vocational_honors1)

        college_school =educational_background.objects.filter(authUser_id=pk).values_list('college_school',flat=True).first()
        college_course =educational_background.objects.filter(authUser_id=pk).values_list('college_course',flat=True).first()
        college_attendance_to =educational_background.objects.filter(authUser_id=pk).values_list('college_attendance_to',flat=True).first()
        college_attendance_from =educational_background.objects.filter(authUser_id=pk).values_list('college_attendance_from',flat=True).first()
        college_units =educational_background.objects.filter(authUser_id=pk).values_list('college_units',flat=True).first()
        college_grad =educational_background.objects.filter(authUser_id=pk).values_list('college_grad',flat=True).first()
        college_honors =educational_background.objects.filter(authUser_id=pk).values_list('college_honors',flat=True).first()

        college_school1 = f'{college_school}'
        college_course1 = f'{college_course}'
        college_attendance1_to = f'{college_attendance_to}'
        college_attendance1_from = f'{college_attendance_from}'
        college_units1 = f'{college_units}'
        college_grad1 = f'{college_grad}'
        college_honors1 = f'{college_honors}'   

        if len(college_school1) > 47:
            a = college_school1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(130,82, top_text)
            p.drawString(130,72, bottom_text)
        
        else:
            p.drawString(130, 75, college_school1)

        if len(college_course1) > 40:
            a = college_course1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(258,82, top_text)
            p.drawString(258,72, bottom_text)
        
        else:
            p.drawString(258, 75, college_course1)

        p.drawString(380, 75, college_attendance1_to)
        p.drawString(412, 75, college_attendance1_from)
        p.drawString(443, 75, college_units1)
        p.drawString(494, 75, college_grad1)
        p.drawString(533, 75, college_honors1)
        
        grad_school =educational_background.objects.filter(authUser_id=pk).values_list('grad_school',flat=True).first()
        grad_course =educational_background.objects.filter(authUser_id=pk).values_list('grad_course',flat=True).first()
        grad_attendance_to =educational_background.objects.filter(authUser_id=pk).values_list('grad_attendance_to',flat=True).first()
        grad_attendance_from =educational_background.objects.filter(authUser_id=pk).values_list('grad_attendance_from',flat=True).first()
        grad_units =educational_background.objects.filter(authUser_id=pk).values_list('grad_units',flat=True).first()
        grad_grad =educational_background.objects.filter(authUser_id=pk).values_list('grad_grad',flat=True).first()
        grad_honors =educational_background.objects.filter(authUser_id=pk).values_list('grad_honors',flat=True).first()

        grad_school1 = f'{grad_school}'
        grad_course1 = f'{grad_course}'
        grad_attendance1_to = f'{grad_attendance_to}'
        grad_attendance1_from = f'{grad_attendance_from}'
        grad_units1 = f'{grad_units}'
        grad_grad1 = f'{grad_grad}'
        grad_honors1 = f'{grad_honors}'  

        if len(grad_school1) > 47:
            a = grad_school1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(130,62, top_text)
            p.drawString(130,52, bottom_text)
        
        else:
            p.drawString(130, 54, grad_school1) 

        if len(grad_course1) > 40:
            a = grad_course1.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(258, 62, top_text)
            p.drawString(258, 52, bottom_text)
        
        else:
            p.drawString(258, 54, grad_course1)

        
        p.drawString(380, 54, grad_attendance1_to)
        p.drawString(412, 54, grad_attendance1_from)
        p.drawString(443, 54, grad_units1)
        p.drawString(494, 54, grad_grad1)
        p.drawString(533, 54, grad_honors1)

        anak = children.objects.all().filter(authUser_id=pk).order_by('-id')

        data2 = [['','']]
        for child in anak:
            data2.append([child.name, child.date_birth.month, child.date_birth.day, child.date_birth.year])

        startingx = 338
        startingy = 385

        try:
            data2[1]
            p.drawString(startingx, startingy, (data2[1])[0])
            p.drawString(startingx+150, startingy, str(str((data2[1])[1])+"/"))
            p.drawString(startingx+159, startingy, str(str((data2[1])[2])+"/"))
            p.drawString(startingx+167, startingy, str(str((data2[1])[3])))
        except:
            pass

        try:
            data2[2]
            p.drawString(startingx, startingy-15, (data2[2])[0])
            p.drawString(startingx+150, startingy-15, str(str((data2[2])[1])+"/"))
            p.drawString(startingx+159, startingy-15, str(str((data2[2])[2])+"/"))
            p.drawString(startingx+167, startingy-15, str(str((data2[2])[3])))
        except:
            pass

        try:
            data2[3]
            p.drawString(startingx, startingy-30, (data2[3])[0])
            p.drawString(startingx+150, startingy-30, str(str((data2[3])[1])+"/"))
            p.drawString(startingx+159, startingy-30, str(str((data2[3])[2])+"/"))
            p.drawString(startingx+167, startingy-30, str(str((data2[3])[3])))
        except:
            pass

        try:
            data2[4]
            p.drawString(startingx, startingy-45, (data2[4])[0])
            p.drawString(startingx+150, startingy-45, str(str((data2[4])[1])+"/"))
            p.drawString(startingx+159, startingy-45, str(str((data2[4])[2])+"/"))
            p.drawString(startingx+167, startingy-45, str(str((data2[4])[3])))
        except:
            pass

        try:
            data2[5]
            p.drawString(startingx, startingy-60, (data2[5])[0])
            p.drawString(startingx+150, startingy-60, str(str((data2[5])[1])+"/"))
            p.drawString(startingx+159, startingy-60, str(str((data2[5])[2])+"/"))
            p.drawString(startingx+167, startingy-60, str(str((data2[5])[3])))
        except:
            pass

        try:
            data2[6]
            p.drawString(startingx, startingy-75, (data2[6])[0])
            p.drawString(startingx+150, startingy-75, str(str((data2[6])[1])+"/"))
            p.drawString(startingx+159, startingy-75, str(str((data2[6])[2])+"/"))
            p.drawString(startingx+167, startingy-75, str(str((data2[6])[3])))
        except:
            pass

        try:
            data2[7]
            p.drawString(startingx, startingy-90, (data2[7])[0])
            p.drawString(startingx+150, startingy-90, str(str((data2[7])[1])+"/"))
            p.drawString(startingx+159, startingy-90, str(str((data2[7])[2])+"/"))
            p.drawString(startingx+167, startingy-90, str(str((data2[7])[3])))
        except:
            pass

        try:
            data2[8]
            p.drawString(startingx, startingy-105, (data2[8])[0])
            p.drawString(startingx+150, startingy-105, str(str((data2[8])[1])+"/"))
            p.drawString(startingx+159, startingy-105, str(str((data2[8])[2])+"/"))
            p.drawString(startingx+167, startingy-105, str(str((data2[8])[3])))
        except:
            pass

        try:
            data2[9]
            p.drawString(startingx, startingy-121, (data2[9])[0])
            p.drawString(startingx+150, startingy-121, str(str((data2[9])[1])+"/"))
            p.drawString(startingx+159, startingy-121, str(str((data2[9])[2])+"/"))
            p.drawString(startingx+167, startingy-121, str(str((data2[9])[3])))
        except:
            pass

        try:
            data2[10]
            p.drawString(startingx, startingy-136, (data2[10])[0])
            p.drawString(startingx+150, startingy-136, str(str((data2[10])[1])+"/"))
            p.drawString(startingx+159, startingy-136, str(str((data2[10])[2])+"/"))
            p.drawString(startingx+167, startingy-136, str(str((data2[10])[3])))
        except:
            pass

        try:
            data2[11]
            p.drawString(startingx, startingy-151, (data2[11])[0])
            p.drawString(startingx+150, startingy-151, str(str((data2[11])[1])+"/"))
            p.drawString(startingx+159, startingy-151, str(str((data2[11])[2])+"/"))
            p.drawString(startingx+167, startingy-151, str(str((data2[11])[3])))
        except:
            pass

        try:
            data2[12]
            p.drawString(startingx, startingy-166, (data2[12])[0])
            p.drawString(startingx+150, startingy-166, str(str((data2[12])[1])+"/"))
            p.drawString(startingx+159, startingy-166, str(str((data2[12])[2])+"/"))
            p.drawString(startingx+167, startingy-166, str(str((data2[12])[3])))
        except:
            pass


        p.save()

        packet.seek(0)

        new_pdf = PdfReader(packet)
        existing_pdf = PdfReader(open("page1_repaired.pdf", "rb"))
        output = PdfWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)


        output_stream = BytesIO()
        output.write(output_stream)
        output.close()
        output_stream.seek(0)
        
        return HttpResponse(output_stream, content_type='application/pdf')
    else:
        return redirect('logout')

@login_required(login_url='loginpage')
def admin_generate_pdf2(request, pk):
    if request.user.is_authenticated and  request.user.is_staff == 1:
        packet = io.BytesIO()
        pagesize1 = (8.5 * inch, 13 * inch)
        p = canvas.Canvas(packet, pagesize= pagesize1) 
        p.setFont("Helvetica", 7)  

        eligibility = civil_service_eligibility.objects.all().filter(authUser_id=pk).order_by('-id')
        startingx = int(45)
        startingy= int(766)

        data = [['','','','','']]
        for eli in eligibility:
            data.append([eli.eligibility,eli.rating,eli.exam_date.month,eli.exam_date.day,eli.exam_date.year,eli.exam_place,eli.license_number,eli.license_validity_date.year])

        try:
            data[1]
            p.drawString(startingx, startingy, (data[1])[0])
            p.drawString(startingx+160, startingy, (data[1])[1])
            p.drawString(startingx+220, startingy, str(str((data[1])[2])+"/"))
            p.drawString(startingx+230, startingy, str(str((data[1])[3])+"/"))
            p.drawString(startingx+240, startingy, str(str((data[1])[4])))
            p.drawString(startingx+280, startingy, (data[1])[5])
            p.drawString(startingx+430, startingy, (data[1])[6])
            p.drawString(startingx+479, startingy, str(str((data[1])[7])))
        except:
            pass

        try:
            data[2]
            p.drawString(startingx, startingy-20, (data[2])[0])
            p.drawString(startingx+160, startingy-20, (data[2])[1])
            p.drawString(startingx+220, startingy-20, str(str((data[2])[2])+"/"))
            p.drawString(startingx+230, startingy-20, str(str((data[2])[3])+"/"))
            p.drawString(startingx+240, startingy-20, str(str((data[2])[4])))
            p.drawString(startingx+280, startingy-20, (data[2])[5])
            p.drawString(startingx+430, startingy-20, (data[2])[6])
            p.drawString(startingx+479, startingy-20, str(str((data[2])[7])))
        except:
            pass

        try:
            data[3]
            p.drawString(startingx, startingy-39, (data[3])[0])
            p.drawString(startingx+160, startingy-39, (data[3])[1])
            p.drawString(startingx+220, startingy-39, str(str((data[3])[2])+"/"))
            p.drawString(startingx+230, startingy-39, str(str((data[3])[3])+"/"))
            p.drawString(startingx+240, startingy-39, str(str((data[3])[4])))
            p.drawString(startingx+280, startingy-39, (data[3])[5])
            p.drawString(startingx+430, startingy-39, (data[3])[6])
            p.drawString(startingx+479, startingy-39, str(str((data[3])[7])))
        except:
            pass

        try:
            data[4]
            p.drawString(startingx, startingy-59, (data[4])[0])
            p.drawString(startingx+160, startingy-59, (data[4])[1])
            p.drawString(startingx+220, startingy-59, str(str((data[4])[2])+"/"))
            p.drawString(startingx+230, startingy-59, str(str((data[4])[3])+"/"))
            p.drawString(startingx+240, startingy-59, str(str((data[4])[4])))
            p.drawString(startingx+280, startingy-59, (data[4])[5])
            p.drawString(startingx+430, startingy-59, (data[4])[6])
            p.drawString(startingx+479, startingy-59, str(str((data[4])[7])))
        except:
            pass

        try:
            data[5]
            p.drawString(startingx, startingy-78, (data[5])[0])
            p.drawString(startingx+160, startingy-78, (data[5])[1])
            p.drawString(startingx+220, startingy-78, str(str((data[5])[2])+"/"))
            p.drawString(startingx+230, startingy-78, str(str((data[5])[3])+"/"))
            p.drawString(startingx+240, startingy-78, str(str((data[5])[4])))
            p.drawString(startingx+280, startingy-78, (data[5])[5])
            p.drawString(startingx+430, startingy-78, (data[5])[6])
            p.drawString(startingx+479, startingy-78, str(str((data[5])[7])))
        except:
            pass

        try:
            data[6]
            p.drawString(startingx, startingy-99, (data[6])[0])
            p.drawString(startingx+160, startingy-99, (data[6])[1])
            p.drawString(startingx+220, startingy-99, str(str((data[6])[2])+"/"))
            p.drawString(startingx+230, startingy-99, str(str((data[6])[3])+"/"))
            p.drawString(startingx+240, startingy-99, str(str((data[6])[4])))
            p.drawString(startingx+280, startingy-99, (data[6])[5])
            p.drawString(startingx+430, startingy-99, (data[6])[6])
            p.drawString(startingx+479, startingy-99, str(str((data[6])[7])))
        except:
            pass

        try:
            data[7]
            p.drawString(startingx, startingy-118, (data[7])[0])
            p.drawString(startingx+160, startingy-118, (data[7])[1])
            p.drawString(startingx+220, startingy-118, str(str((data[7])[2])+"/"))
            p.drawString(startingx+230, startingy-118, str(str((data[7])[3])+"/"))
            p.drawString(startingx+240, startingy-118, str(str((data[7])[4])))
            p.drawString(startingx+280, startingy-118, (data[7])[5])
            p.drawString(startingx+430, startingy-118, (data[7])[6])
            p.drawString(startingx+479, startingy-118, str(str((data[7])[7])))
        except:
            pass

        experience = work_experience.objects.all().filter(authUser_id=pk).order_by('-id')
        data2 = [['','','','','','','']]
        

        startingx2 = int(45)
        startingy2= int(554)

        for exp in experience:
            data2.append([exp.date_from.month,exp.date_from.day,exp.date_from.year,exp.date_to.month,exp.date_to.day,exp.date_to.year,
                        exp.position,
                        exp.department,
                        exp.monthly_salary,
                        exp.salary_grade,
                        exp.status,
                        exp.gov_service]
                        )
            
        try:
            data2[1]

            if len((data2[1])[6]) > 35:
                a = (data2[1])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,558, top_text)
                p.drawString(126,551, bottom_text)
        
            else:
                p.drawString(126, 554, (data2[1])[6])

            
            if len((data2[1])[7]) > 35:
                a = (data2[1])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,558, top_text)
                p.drawString(260,551, bottom_text)
        
            else:
                p.drawString(260, 554, (data2[1])[7])

            

            p.drawString(startingx2, startingy2, str(str((data2[1])[0])+"/"))
            p.drawString(startingx2+6 , startingy2, str(str((data2[1])[1])+"/"))
            p.drawString(startingx2+15, startingy2, str(str((data2[1])[2])))

            p.drawString(startingx2+43, startingy2, str(str((data2[1])[3])+"/"))
            p.drawString(startingx2+50, startingy2, str(str((data2[1])[4])+"/"))
            p.drawString(startingx2+59, startingy2, str(str((data2[1])[5])))  

        
            p.drawString(startingx2+355, startingy2, (data2[1])[8])
            p.drawString(startingx2+394 , startingy2, (data2[1])[9])
            p.drawString(startingx2+440 , startingy2, (data2[1])[10])
            p.drawString(startingx2+490 , startingy2, (data2[1])[11])

        except:
            pass

        try:
            data2[2]

            if len((data2[2])[6]) > 35:
                a = (data2[2])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,539, top_text)
                p.drawString(126,531, bottom_text)

            else:
                p.drawString(126, 535, (data2[2])[6])


            if len((data2[2])[7]) > 35:
                a = (data2[2])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,539, top_text)
                p.drawString(260,531, bottom_text)

            else:
                p.drawString(260, 535, (data2[2])[7])

            

            p.drawString(startingx2, startingy2-19, str(str((data2[2])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-19, str(str((data2[2])[1])+"/"))
            p.drawString(startingx2+15, startingy2-19, str(str((data2[2])[2])))

            p.drawString(startingx2+43, startingy2-19, str(str((data2[2])[3])+"/"))
            p.drawString(startingx2+50, startingy2-19, str(str((data2[2])[4])+"/"))
            p.drawString(startingx2+59, startingy2-19, str(str((data2[2])[5])))  

            p.drawString(startingx2+355, startingy2-19, (data2[2])[8])
            p.drawString(startingx2+394 , startingy2-19, (data2[2])[9])
            p.drawString(startingx2+440 , startingy2-19, (data2[2])[10])
            p.drawString(startingx2+490 , startingy2-19, (data2[2])[11])

        except:
            pass
        
        try:
            data2[3]

            if len((data2[3])[6]) > 35:
                a = (data2[3])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,519, top_text)
                p.drawString(126,511, bottom_text)

            else:
                p.drawString(126, 515, (data2[3])[6])


            if len((data2[3])[7]) > 35:
                a = (data2[3])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,519, top_text)
                p.drawString(260,512, bottom_text)

            else:
                p.drawString(260, 515, (data2[3])[7])

            p.drawString(startingx2, startingy2-39, str(str((data2[3])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-39, str(str((data2[3])[1])+"/"))
            p.drawString(startingx2+15, startingy2-39, str(str((data2[3])[2])))

            p.drawString(startingx2+43, startingy2-39, str(str((data2[3])[3])+"/"))
            p.drawString(startingx2+50, startingy2-39, str(str((data2[3])[4])+"/"))
            p.drawString(startingx2+59, startingy2-39, str(str((data2[3])[5])))  

            p.drawString(startingx2+355, startingy2-39, (data2[3])[8])
            p.drawString(startingx2+394 , startingy2-39, (data2[3])[9])
            p.drawString(startingx2+440 , startingy2-39, (data2[3])[10])
            p.drawString(startingx2+490 , startingy2-39, (data2[3])[11])

        except:
            pass

        try:
            data2[4]

            if len((data2[4])[6]) > 35:
                a = (data2[4])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,503, top_text)
                p.drawString(126,496, bottom_text)

            else:
                p.drawString(126, 499, (data2[4])[6])


            if len((data2[4])[7]) > 35:
                a = (data2[4])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,503, top_text)
                p.drawString(260,496, bottom_text)

            else:
                p.drawString(260, 499, (data2[4])[7])

            p.drawString(startingx2, startingy2-55, str(str((data2[4])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-55, str(str((data2[4])[1])+"/"))
            p.drawString(startingx2+15, startingy2-55, str(str((data2[4])[2])))

            p.drawString(startingx2+43, startingy2-55, str(str((data2[4])[3])+"/"))
            p.drawString(startingx2+50, startingy2-55, str(str((data2[4])[4])+"/"))
            p.drawString(startingx2+59, startingy2-55, str(str((data2[4])[5])))  

            p.drawString(startingx2+355, startingy2-55, (data2[4])[8])
            p.drawString(startingx2+394 , startingy2-55, (data2[4])[9])
            p.drawString(startingx2+440 , startingy2-55, (data2[4])[10])
            p.drawString(startingx2+490 , startingy2-55, (data2[4])[11])

        except:
            pass

        try:
            data2[5]

            if len((data2[5])[6]) > 35:
                a = (data2[5])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,483, top_text)
                p.drawString(126,476, bottom_text)

            else:
                p.drawString(126, 479, (data2[5])[6])


            if len((data2[5])[7]) > 35:
                a = (data2[5])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,483, top_text)
                p.drawString(260,476, bottom_text)

            else:
                p.drawString(260, 479, (data2[5])[7])

            p.drawString(startingx2, startingy2-75, str(str((data2[5])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-75, str(str((data2[5])[1])+"/"))
            p.drawString(startingx2+15, startingy2-75, str(str((data2[5])[2])))

            p.drawString(startingx2+43, startingy2-75, str(str((data2[5])[3])+"/"))
            p.drawString(startingx2+50, startingy2-75, str(str((data2[5])[4])+"/"))
            p.drawString(startingx2+59, startingy2-75, str(str((data2[5])[5])))  

            p.drawString(startingx2+355, startingy2-75, (data2[5])[8])
            p.drawString(startingx2+394 , startingy2-75, (data2[5])[9])
            p.drawString(startingx2+440 , startingy2-75, (data2[5])[10])
            p.drawString(startingx2+490 , startingy2-75, (data2[5])[11])

        except:
            pass

        try:
            data2[6]

            if len((data2[6])[6]) > 35:
                a = (data2[6])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,463, top_text)
                p.drawString(126,456, bottom_text)

            else:
                p.drawString(126, 459, (data2[6])[6])


            if len((data2[6])[7]) > 35:
                a = (data2[6])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,463, top_text)
                p.drawString(260,456, bottom_text)

            else:
                p.drawString(260, 459, (data2[6])[7])

            p.drawString(startingx2, startingy2-95, str(str((data2[6])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-95, str(str((data2[6])[1])+"/"))
            p.drawString(startingx2+15, startingy2-95, str(str((data2[6])[2])))

            p.drawString(startingx2+43, startingy2-95, str(str((data2[6])[3])+"/"))
            p.drawString(startingx2+50, startingy2-95, str(str((data2[6])[4])+"/"))
            p.drawString(startingx2+59, startingy2-95, str(str((data2[6])[5])))  

            p.drawString(startingx2+355, startingy2-95, (data2[6])[8])
            p.drawString(startingx2+394 , startingy2-95, (data2[6])[9])
            p.drawString(startingx2+440 , startingy2-95, (data2[6])[10])
            p.drawString(startingx2+490 , startingy2-95, (data2[6])[11])

        except:
            pass

        try:
            data2[7]

            if len((data2[7])[6]) > 35:
                a = (data2[7])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,443, top_text)
                p.drawString(126,436, bottom_text)

            else:
                p.drawString(126, 439, (data2[7])[6])


            if len((data2[7])[7]) > 35:
                a = (data2[7])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,443, top_text)
                p.drawString(260,436, bottom_text)

            else:
                p.drawString(260, 439, (data2[7])[7])

            p.drawString(startingx2, startingy2-115, str(str((data2[7])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-115, str(str((data2[7])[1])+"/"))
            p.drawString(startingx2+15, startingy2-115, str(str((data2[7])[2])))

            p.drawString(startingx2+43, startingy2-115, str(str((data2[7])[3])+"/"))
            p.drawString(startingx2+50, startingy2-115, str(str((data2[7])[4])+"/"))    
            p.drawString(startingx2+59, startingy2-115, str(str((data2[7])[5])))  

            p.drawString(startingx2+355, startingy2-115, (data2[7])[8])
            p.drawString(startingx2+394 , startingy2-115, (data2[7])[9])
            p.drawString(startingx2+440 , startingy2-115, (data2[7])[10])
            p.drawString(startingx2+490 , startingy2-115, (data2[7])[11])

        except:
            pass

        try:
            data2[8]

            if len((data2[8])[6]) > 35:
                a = (data2[8])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,425, top_text)
                p.drawString(126,418, bottom_text)

            else:
                p.drawString(126, 421, (data2[8])[6])


            if len((data2[8])[7]) > 35:
                a = (data2[8])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,425, top_text)
                p.drawString(260,418, bottom_text)

            else:
                p.drawString(260, 421, (data2[8])[7])

            p.drawString(startingx2, startingy2-133, str(str((data2[8])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-133, str(str((data2[8])[1])+"/"))
            p.drawString(startingx2+15, startingy2-133, str(str((data2[8])[2])))

            p.drawString(startingx2+43, startingy2-133, str(str((data2[8])[3])+"/"))
            p.drawString(startingx2+50, startingy2-133, str(str((data2[8])[4])+"/"))
            p.drawString(startingx2+59, startingy2-133, str(str((data2[8])[5])))  

            p.drawString(startingx2+355, startingy2-133, (data2[8])[8])
            p.drawString(startingx2+394 , startingy2-133, (data2[8])[9])
            p.drawString(startingx2+440 , startingy2-133, (data2[8])[10])
            p.drawString(startingx2+490 , startingy2-133, (data2[8])[11])

        except:
            pass

        try:
            data2[9]

            if len((data2[9])[6]) > 35:
                a = (data2[9])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,407, top_text)
                p.drawString(126,400, bottom_text)

            else:
                p.drawString(126, 403, (data2[9])[6])


            if len((data2[9])[7]) > 35:
                a = (data2[9])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,407, top_text)
                p.drawString(260,400, bottom_text)

            else:
                p.drawString(260, 403, (data2[9])[7])

            p.drawString(startingx2, startingy2-151, str(str((data2[9])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-151, str(str((data2[9])[1])+"/"))
            p.drawString(startingx2+15, startingy2-151, str(str((data2[9])[2])))

            p.drawString(startingx2+43, startingy2-151, str(str((data2[9])[3])+"/"))
            p.drawString(startingx2+50, startingy2-151, str(str((data2[9])[4])+"/"))
            p.drawString(startingx2+59, startingy2-151, str(str((data2[9])[5])))  

            p.drawString(startingx2+355, startingy2-151, (data2[9])[8])
            p.drawString(startingx2+394 , startingy2-151, (data2[9])[9])
            p.drawString(startingx2+440 , startingy2-151, (data2[9])[10])
            p.drawString(startingx2+490 , startingy2-151, (data2[9])[11])

        except:
            pass

        try:
            data2[10]

            if len((data2[10])[6]) > 35:
                a = (data2[10])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,389, top_text)
                p.drawString(126,382, bottom_text)

            else:
                p.drawString(126, 385, (data2[10])[6])


            if len((data2[10])[7]) > 35:
                a = (data2[10])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,389, top_text)
                p.drawString(260,382, bottom_text)

            else:
                p.drawString(260, 385, (data2[10])[7])

            p.drawString(startingx2, startingy2-169, str(str((data2[10])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-169, str(str((data2[10])[1])+"/"))
            p.drawString(startingx2+15, startingy2-169, str(str((data2[10])[2])))

            p.drawString(startingx2+43, startingy2-169, str(str((data2[10])[3])+"/"))
            p.drawString(startingx2+50, startingy2-169, str(str((data2[10])[4])+"/"))
            p.drawString(startingx2+59, startingy2-169, str(str((data2[10])[5])))  

            p.drawString(startingx2+355, startingy2-169, (data2[10])[8])
            p.drawString(startingx2+394 , startingy2-169, (data2[10])[9])
            p.drawString(startingx2+440 , startingy2-169, (data2[10])[10])
            p.drawString(startingx2+490 , startingy2-169, (data2[10])[11])

        except:
            pass

        try:
            data2[11]

            if len((data2[11])[6]) > 35:
                a = (data2[11])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,371, top_text)
                p.drawString(126,364, bottom_text)

            else:
                p.drawString(126, 367, (data2[11])[6])


            if len((data2[11])[7]) > 35:
                a = (data2[11])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,371, top_text)
                p.drawString(260,364, bottom_text)

            else:
                p.drawString(260, 367, (data2[11])[7])

            p.drawString(startingx2, startingy2-187, str(str((data2[11])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-187, str(str((data2[11])[1])+"/"))
            p.drawString(startingx2+15, startingy2-187, str(str((data2[11])[2])))

            p.drawString(startingx2+43, startingy2-187, str(str((data2[11])[3])+"/"))
            p.drawString(startingx2+50, startingy2-187, str(str((data2[11])[4])+"/"))
            p.drawString(startingx2+59, startingy2-187, str(str((data2[11])[5])))  

            p.drawString(startingx2+355, startingy2-187, (data2[11])[8])
            p.drawString(startingx2+394 , startingy2-187, (data2[11])[9])
            p.drawString(startingx2+440 , startingy2-187, (data2[11])[10])
            p.drawString(startingx2+490 , startingy2-187, (data2[11])[11])

        except:
            pass

        try:
            data2[12]

            if len((data2[12])[6]) > 35:
                a = (data2[12])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,353, top_text)
                p.drawString(126,346, bottom_text)

            else:
                p.drawString(126, 349, (data2[12])[6])

        
            if len((data2[12])[7]) > 35:
                a = (data2[12])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,353, top_text)
                p.drawString(260,346, bottom_text)

            else:
                p.drawString(260, 349, (data2[12])[7])

            p.drawString(startingx2, startingy2-205, str(str((data2[12])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-205, str(str((data2[12])[1])+"/"))
            p.drawString(startingx2+15, startingy2-205, str(str((data2[12])[2])))

            p.drawString(startingx2+43, startingy2-205, str(str((data2[12])[3])+"/"))
            p.drawString(startingx2+50, startingy2-205, str(str((data2[12])[4])+"/"))
            p.drawString(startingx2+59, startingy2-205, str(str((data2[12])[5])))  

            p.drawString(startingx2+355, startingy2-205, (data2[12])[8])
            p.drawString(startingx2+394 , startingy2-205, (data2[12])[9])
            p.drawString(startingx2+440 , startingy2-205, (data2[12])[10])
            p.drawString(startingx2+490 , startingy2-205, (data2[12])[11])

        except:
            pass

        try:
            data2[13]

            if len((data2[13])[6]) > 35:
                a = (data2[13])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,335, top_text)
                p.drawString(126,338, bottom_text)

            else:
                p.drawString(126, 331, (data2[13])[6])


            if len((data2[13])[7]) > 35:
                a = (data2[13])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,335, top_text)
                p.drawString(260,338, bottom_text)

            else:
                p.drawString(260, 331, (data2[13])[7])

            p.drawString(startingx2, startingy2-223, str(str((data2[13])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-223, str(str((data2[13])[1])+"/"))
            p.drawString(startingx2+15, startingy2-223, str(str((data2[13])[2])))

            p.drawString(startingx2+43, startingy2-223, str(str((data2[13])[3])+"/"))
            p.drawString(startingx2+50, startingy2-223, str(str((data2[13])[4])+"/"))
            p.drawString(startingx2+59, startingy2-223, str(str((data2[13])[5])))  

            p.drawString(startingx2+355, startingy2-223, (data2[13])[8])
            p.drawString(startingx2+394 , startingy2-223, (data2[13])[9])
            p.drawString(startingx2+440 , startingy2-223, (data2[13])[10])
            p.drawString(startingx2+490 , startingy2-223, (data2[13])[11])

        except:
            pass

        try:
            data2[14]

            if len((data2[14])[6]) > 35:
                a = (data2[14])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,317, top_text)
                p.drawString(126,310, bottom_text)

            else:
                p.drawString(126, 313, (data2[14])[6])


            if len((data2[14])[7]) > 35:
                a = (data2[14])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,317, top_text)
                p.drawString(260,310, bottom_text)

            else:
                p.drawString(260, 313, (data2[14])[7])

            p.drawString(startingx2, startingy2-241, str(str((data2[14])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-241, str(str((data2[14])[1])+"/"))
            p.drawString(startingx2+15, startingy2-241, str(str((data2[14])[2])))

            p.drawString(startingx2+43, startingy2-241, str(str((data2[14])[3])+"/"))
            p.drawString(startingx2+50, startingy2-241, str(str((data2[14])[4])+"/"))
            p.drawString(startingx2+59, startingy2-241, str(str((data2[14])[5])))  

            p.drawString(startingx2+355, startingy2-241, (data2[14])[8])
            p.drawString(startingx2+394 , startingy2-241, (data2[14])[9])
            p.drawString(startingx2+440 , startingy2-241, (data2[14])[10])
            p.drawString(startingx2+490 , startingy2-241, (data2[14])[11])

        except:
            pass

        
        try:
            data2[15]

            if len((data2[15])[6]) > 35:
                a = (data2[15])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,299, top_text)
                p.drawString(126,292, bottom_text)

            else:
                p.drawString(126, 295, (data2[15])[6])


            if len((data2[15])[7]) > 35:
                a = (data2[15])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,299, top_text)
                p.drawString(260,292, bottom_text)

            else:
                p.drawString(260, 295, (data2[15])[7])

            p.drawString(startingx2, startingy2-259, str(str((data2[15])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-259, str(str((data2[15])[1])+"/"))
            p.drawString(startingx2+15, startingy2-259, str(str((data2[15])[2])))

            p.drawString(startingx2+43, startingy2-259, str(str((data2[15])[3])+"/"))
            p.drawString(startingx2+50, startingy2-259, str(str((data2[15])[4])+"/"))
            p.drawString(startingx2+59, startingy2-259, str(str((data2[15])[5])))  

            p.drawString(startingx2+355, startingy2-259, (data2[15])[8])
            p.drawString(startingx2+394 , startingy2-259, (data2[15])[9])
            p.drawString(startingx2+440 , startingy2-259, (data2[15])[10])
            p.drawString(startingx2+490 , startingy2-259, (data2[15])[11])

        except:
            pass

        try:
            data2[16]

            if len((data2[16])[6]) > 35:
                a = (data2[16])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,281, top_text)
                p.drawString(126,274, bottom_text)

            else:
                p.drawString(126, 277, (data2[16])[6])


            if len((data2[16])[7]) > 35:
                a = (data2[16])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,281, top_text)
                p.drawString(260,274, bottom_text)

            else:
                p.drawString(260, 277, (data2[16])[7])

            p.drawString(startingx2, startingy2-277, str(str((data2[16])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-277, str(str((data2[16])[1])+"/"))
            p.drawString(startingx2+15, startingy2-277, str(str((data2[16])[2])))

            p.drawString(startingx2+43, startingy2-277, str(str((data2[16])[3])+"/"))
            p.drawString(startingx2+50, startingy2-277, str(str((data2[16])[4])+"/"))
            p.drawString(startingx2+59, startingy2-277, str(str((data2[16])[5])))  

            p.drawString(startingx2+355, startingy2-277, (data2[16])[8])
            p.drawString(startingx2+394 , startingy2-277, (data2[16])[9])
            p.drawString(startingx2+440 , startingy2-277, (data2[16])[10])
            p.drawString(startingx2+490 , startingy2-277, (data2[16])[11])

        except:
            pass

        try:
            data2[17]

            if len((data2[17])[6]) > 35:
                a = (data2[17])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,263, top_text)
                p.drawString(126,256, bottom_text)

            else:
                p.drawString(126, 259, (data2[17])[6])


            if len((data2[17])[7]) > 35:
                a = (data2[17])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,263, top_text)
                p.drawString(260,256, bottom_text)

            else:
                p.drawString(260, 259, (data2[17])[7])

            p.drawString(startingx2, startingy2-295, str(str((data2[17])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-295, str(str((data2[17])[1])+"/"))
            p.drawString(startingx2+15, startingy2-295, str(str((data2[17])[2])))

            p.drawString(startingx2+43, startingy2-295, str(str((data2[17])[3])+"/"))
            p.drawString(startingx2+50, startingy2-295, str(str((data2[17])[4])+"/"))
            p.drawString(startingx2+59, startingy2-295, str(str((data2[17])[5])))  

            p.drawString(startingx2+355, startingy2-295, (data2[17])[8])
            p.drawString(startingx2+394 , startingy2-295, (data2[17])[9])
            p.drawString(startingx2+440 , startingy2-295, (data2[17])[10])
            p.drawString(startingx2+490 , startingy2-295, (data2[17])[11])

        except:
            pass

        try:
            data2[18]

            if len((data2[18])[6]) > 35:
                a = (data2[18])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,245, top_text)
                p.drawString(126,238, bottom_text)

            else:
                p.drawString(126, 241, (data2[18])[6])


            if len((data2[18])[7]) > 35:
                a = (data2[18])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,245, top_text)
                p.drawString(260,238, bottom_text)

            else:
                p.drawString(260, 241, (data2[18])[7])

            p.drawString(startingx2, startingy2-313, str(str((data2[18])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-313, str(str((data2[18])[1])+"/"))
            p.drawString(startingx2+15, startingy2-313, str(str((data2[16])[2])))

            p.drawString(startingx2+43, startingy2-313, str(str((data2[18])[3])+"/"))
            p.drawString(startingx2+50, startingy2-313, str(str((data2[18])[4])+"/"))
            p.drawString(startingx2+59, startingy2-313, str(str((data2[18])[5])))  

            p.drawString(startingx2+355, startingy2-313, (data2[18])[8])
            p.drawString(startingx2+394 , startingy2-313, (data2[18])[9])
            p.drawString(startingx2+440 , startingy2-313, (data2[18])[10])
            p.drawString(startingx2+490 , startingy2-313, (data2[18])[11])

        except:
            pass

        
        try:
            data2[19]

            if len((data2[19])[6]) > 35:
                a = (data2[19])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,227, top_text)
                p.drawString(126,220, bottom_text)

            else:
                p.drawString(126, 223, (data2[19])[6])


            if len((data2[19])[7]) > 35:
                a = (data2[19])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,227, top_text)
                p.drawString(260,220, bottom_text)

            else:
                p.drawString(260, 223, (data2[19])[7])

            p.drawString(startingx2, startingy2-331, str(str((data2[19])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-331, str(str((data2[19])[1])+"/"))
            p.drawString(startingx2+15, startingy2-331, str(str((data2[19])[2])))

            p.drawString(startingx2+43, startingy2-331, str(str((data2[19])[3])+"/"))
            p.drawString(startingx2+50, startingy2-331, str(str((data2[19])[4])+"/"))
            p.drawString(startingx2+59, startingy2-331, str(str((data2[19])[5])))  

            p.drawString(startingx2+355, startingy2-331, (data2[19])[8])
            p.drawString(startingx2+394 , startingy2-331, (data2[19])[9])
            p.drawString(startingx2+440 , startingy2-331, (data2[19])[10])
            p.drawString(startingx2+490 , startingy2-331, (data2[19])[11])

        except:
            pass

        try:
            data2[20]

            if len((data2[20])[6]) > 35:
                a = (data2[20])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,209, top_text)
                p.drawString(126,202, bottom_text)

            else:
                p.drawString(126, 205, (data2[20])[6])


            if len((data2[20])[7]) > 35:
                a = (data2[20])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,209, top_text)
                p.drawString(260,202, bottom_text)

            else:
                p.drawString(260, 205, (data2[20])[7])

            p.drawString(startingx2, startingy2-349, str(str((data2[20])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-349, str(str((data2[20])[1])+"/"))
            p.drawString(startingx2+15, startingy2-349, str(str((data2[20])[2])))

            p.drawString(startingx2+43, startingy2-349, str(str((data2[20])[3])+"/"))
            p.drawString(startingx2+50, startingy2-349, str(str((data2[20])[4])+"/"))
            p.drawString(startingx2+59, startingy2-349, str(str((data2[20])[5])))  

            p.drawString(startingx2+355, startingy2-349, (data2[20])[8])
            p.drawString(startingx2+394 , startingy2-349, (data2[20])[9])
            p.drawString(startingx2+440 , startingy2-349, (data2[20])[10])
            p.drawString(startingx2+490 , startingy2-349, (data2[20])[11])

        except:
            pass
        
        try:
            data2[21]

            if len((data2[21])[6]) > 35:
                a = (data2[21])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,192, top_text)
                p.drawString(126,184, bottom_text)

            else:
                p.drawString(126, 187, (data2[21])[6])


            if len((data2[21])[7]) > 35:
                a = (data2[21])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,192, top_text)
                p.drawString(260,184, bottom_text)

            else:
                p.drawString(260, 187, (data2[21])[7])

            p.drawString(startingx2, startingy2-367, str(str((data2[21])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-367, str(str((data2[21])[1])+"/"))
            p.drawString(startingx2+15, startingy2-367, str(str((data2[21])[2])))

            p.drawString(startingx2+43, startingy2-367, str(str((data2[21])[3])+"/"))
            p.drawString(startingx2+50, startingy2-367, str(str((data2[21])[4])+"/"))
            p.drawString(startingx2+59, startingy2-367, str(str((data2[21])[5])))  

            p.drawString(startingx2+355, startingy2-367, (data2[21])[8])
            p.drawString(startingx2+394 , startingy2-367, (data2[21])[9])
            p.drawString(startingx2+440 , startingy2-367, (data2[21])[10])
            p.drawString(startingx2+490 , startingy2-367, (data2[21])[11])

        except:
            pass
            
        try:
            data2[22]

            if len((data2[22])[6]) > 35:
                a = (data2[22])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,173, top_text)
                p.drawString(126,166, bottom_text)

            else:
                p.drawString(126, 169, (data2[22])[6])


            if len((data2[22])[7]) > 35:
                a = (data2[22])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,173, top_text)
                p.drawString(260,166, bottom_text)

            else:
                p.drawString(260, 169, (data2[22])[7])


            p.drawString(startingx2, startingy2-385, str(str((data2[22])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-385, str(str((data2[22])[1])+"/"))
            p.drawString(startingx2+15, startingy2-385, str(str((data2[22])[2])))

            p.drawString(startingx2+43, startingy2-385, str(str((data2[22])[3])+"/"))
            p.drawString(startingx2+50, startingy2-385, str(str((data2[22])[4])+"/"))
            p.drawString(startingx2+59, startingy2-385, str(str((data2[22])[5])))  

            p.drawString(startingx2+355, startingy2-385, (data2[22])[8])
            p.drawString(startingx2+394 , startingy2-385, (data2[22])[9])
            p.drawString(startingx2+440 , startingy2-385, (data2[22])[10])
            p.drawString(startingx2+490 , startingy2-385, (data2[22])[11])

        except:
            pass
            
        try:
            data2[23]

            if len((data2[23])[6]) > 35:
                a = (data2[23])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,155, top_text)
                p.drawString(126,148, bottom_text)

            else:
                p.drawString(126, 151, (data2[23])[6])


            if len((data2[23])[7]) > 35:
                a = (data2[23])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,155, top_text)
                p.drawString(260,148, bottom_text)

            else:
                p.drawString(260, 151, (data2[23])[7])

            p.drawString(startingx2, startingy2-403, str(str((data2[23])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-403, str(str((data2[23])[1])+"/"))
            p.drawString(startingx2+15, startingy2-403, str(str((data2[23])[2])))

            p.drawString(startingx2+43, startingy2-403, str(str((data2[23])[3])+"/"))
            p.drawString(startingx2+50, startingy2-403, str(str((data2[23])[4])+"/"))
            p.drawString(startingx2+59, startingy2-403, str(str((data2[23])[5])))  

            p.drawString(startingx2+355, startingy2-403, (data2[23])[8])
            p.drawString(startingx2+394 , startingy2-403, (data2[23])[9])
            p.drawString(startingx2+440 , startingy2-403, (data2[23])[10])
            p.drawString(startingx2+490 , startingy2-403, (data2[23])[11])

        except:
            pass
            
        try:
            data2[24]

            if len((data2[24])[6]) > 35:
                a = (data2[24])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,137, top_text)
                p.drawString(126,130, bottom_text)

            else:
                p.drawString(126, 133, (data2[24])[6])


            if len((data2[24])[7]) > 35:
                a = (data2[24])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,137, top_text)
                p.drawString(260,130, bottom_text)

            else:
                p.drawString(260, 133, (data2[24])[7])

            p.drawString(startingx2, startingy2-421, str(str((data2[24])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-421, str(str((data2[24])[1])+"/"))
            p.drawString(startingx2+15, startingy2-421, str(str((data2[24])[2])))

            p.drawString(startingx2+43, startingy2-421, str(str((data2[24])[3])+"/"))
            p.drawString(startingx2+50, startingy2-421, str(str((data2[24])[4])+"/"))
            p.drawString(startingx2+59, startingy2-421, str(str((data2[24])[5])))  

            p.drawString(startingx2+355, startingy2-421, (data2[24])[8])
            p.drawString(startingx2+394 , startingy2-421, (data2[24])[9])
            p.drawString(startingx2+440 , startingy2-421, (data2[24])[10])
            p.drawString(startingx2+490 , startingy2-421, (data2[24])[11])

        except:
            pass
            
        try:
            data2[25]

            if len((data2[25])[6]) > 35:
                a = (data2[25])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,119, top_text)
                p.drawString(126,112, bottom_text)

            else:
                p.drawString(126, 115, (data2[25])[6])


            if len((data2[25])[7]) > 35:
                a = (data2[25])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,119, top_text)
                p.drawString(260,112, bottom_text)

            else:
                p.drawString(260, 115, (data2[25])[7])

            p.drawString(startingx2, startingy2-439, str(str((data2[25])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-439, str(str((data2[25])[1])+"/"))
            p.drawString(startingx2+15, startingy2-439, str(str((data2[25])[2])))

            p.drawString(startingx2+43, startingy2-439, str(str((data2[25])[3])+"/"))
            p.drawString(startingx2+50, startingy2-439, str(str((data2[25])[4])+"/"))
            p.drawString(startingx2+59, startingy2-439, str(str((data2[25])[5])))  

            p.drawString(startingx2+355, startingy2-439, (data2[25])[8])
            p.drawString(startingx2+394 , startingy2-439, (data2[25])[9])
            p.drawString(startingx2+440 , startingy2-439, (data2[25])[10])
            p.drawString(startingx2+490 , startingy2-439, (data2[25])[11])

        except:
            pass
            
        try:
            data2[26]

            if len((data2[26])[6]) > 35:
                a = (data2[26])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,100, top_text)
                p.drawString(126,94, bottom_text)

            else:
                p.drawString(126, 97, (data2[26])[6])


            if len((data2[26])[7]) > 35:
                a = (data2[26])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,101, top_text)
                p.drawString(260,94, bottom_text)

            else:
                p.drawString(260, 97, (data2[26])[7])

            p.drawString(startingx2, startingy2-457, str(str((data2[26])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-457, str(str((data2[26])[1])+"/"))
            p.drawString(startingx2+15, startingy2-457, str(str((data2[26])[2])))

            p.drawString(startingx2+43, startingy2-457, str(str((data2[26])[3])+"/"))
            p.drawString(startingx2+50, startingy2-457, str(str((data2[26])[4])+"/"))
            p.drawString(startingx2+59, startingy2-457, str(str((data2[26])[5])))  

            p.drawString(startingx2+355, startingy2-457, (data2[26])[8])
            p.drawString(startingx2+394 , startingy2-457, (data2[26])[9])
            p.drawString(startingx2+440 , startingy2-457, (data2[26])[10])
            p.drawString(startingx2+490 , startingy2-457, (data2[26])[11])

        except:
            pass
            
        try:
            data2[27]

            if len((data2[27])[6]) > 35:
                a = (data2[27])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,93, top_text)
                p.drawString(126,76, bottom_text)

            else:
                p.drawString(126, 79, (data2[27])[6])


            if len((data2[27])[7]) > 35:
                a = (data2[27])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,93, top_text)
                p.drawString(260,76, bottom_text)

            else:
                p.drawString(260, 79, (data2[27])[7])

            p.drawString(startingx2, startingy2-475, str(str((data2[27])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-475, str(str((data2[27])[1])+"/"))
            p.drawString(startingx2+15, startingy2-475, str(str((data2[27])[2])))

            p.drawString(startingx2+43, startingy2-475, str(str((data2[27])[3])+"/"))
            p.drawString(startingx2+50, startingy2-475, str(str((data2[27])[4])+"/"))
            p.drawString(startingx2+59, startingy2-475, str(str((data2[27])[5])))  

            p.drawString(startingx2+355, startingy2-475, (data2[27])[8])
            p.drawString(startingx2+394 , startingy2-475, (data2[27])[9])
            p.drawString(startingx2+440 , startingy2-475, (data2[27])[10])
            p.drawString(startingx2+490 , startingy2-475, (data2[27])[11])

        except:
            pass
            
        try:
            data2[28]

            if len((data2[28])[6]) > 35:
                a = (data2[28])[6].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(126,65, top_text)
                p.drawString(126,58, bottom_text)

            else:
                p.drawString(126, 61, (data2[28])[6])


            if len((data2[28])[7]) > 35:
                a = (data2[28])[7].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(260,65, top_text)
                p.drawString(260,58, bottom_text)

            else:
                p.drawString(260, 61, (data2[28])[7])
                

            p.drawString(startingx2, startingy2-493, str(str((data2[28])[0])+"/"))
            p.drawString(startingx2+6 , startingy2-493, str(str((data2[28])[1])+"/"))
            p.drawString(startingx2+15, startingy2-493, str(str((data2[28])[2])))

            p.drawString(startingx2+43, startingy2-493, str(str((data2[28])[3])+"/"))
            p.drawString(startingx2+50, startingy2-493, str(str((data2[28])[4])+"/"))
            p.drawString(startingx2+59, startingy2-493, str(str((data2[28])[5])))  

            p.drawString(startingx2+355, startingy2-493, (data2[28])[8])
            p.drawString(startingx2+394 , startingy2-493, (data2[28])[9])
            p.drawString(startingx2+440 , startingy2-493, (data2[28])[10])
            p.drawString(startingx2+490 , startingy2-493, (data2[28])[11])

        except:
            pass

        
            # eli_eligibility1 = f'{eli.eligibility}'

            # p.drawString(130, 500, eli_eligibility1)

        p.save()

        packet.seek(0)

        new_pdf = PdfReader(packet)
        existing_pdf = PdfReader(open("var/www/django_project/page2.pdf", "rb"))
        output = PdfWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)


        output_stream = BytesIO()
        output.write(output_stream)
        output.close()
        output_stream.seek(0)
        
        return HttpResponse(output_stream, content_type='application/pdf')
    else:
        return redirect('logout')

@login_required(login_url='loginpage')
def admin_generate_pdf3(request, pk): 
    if request.user.is_authenticated and  request.user.is_staff == 1:
        pagesize1 = (8.5 * inch, 13 * inch)  # 20 inch width and 10 inch height.
        packet = io.BytesIO()
        
        p = canvas.Canvas(packet, pagesize= pagesize1) 
        p.setFont("Helvetica", 7)  

        voluntary = voluntary_work.objects.all().filter(authUser_id=pk).order_by('-id')
        startingx = int(44)
        startingy= int(756)

        data = [['','','','','']]
        for vol in voluntary:
            data.append([vol.org_info, vol.date_from.month,vol.date_from.day, vol.date_from.year, vol.date_to.month,vol.date_to.day, vol.date_to.year, vol.work_hours,
                    vol.position])
            
        try:
            data[1]

            if len((data[1])[0]) > 35:
                a = (data[1])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,753, top_text)
                p.drawString(39,759, bottom_text)
        
            else:
                p.drawString(39, 756, (data[1])[0])
            


            p.drawString(startingx+226, startingy, str(str((data[1])[1])+"/"))
            p.drawString(startingx+232, startingy, str(str((data[1])[2])+"/"))
            p.drawString(startingx+242, startingy, str(str((data[1])[3])))  

            p.drawString(startingx+263, startingy, str(str((data[1])[4])+"/"))
            p.drawString(startingx+273, startingy, str(str((data[1])[5])+"/"))
            p.drawString(startingx+283, startingy, str(str((data[1])[6])))  

            p.drawString(startingx+316, startingy, (data[1])[7])
            p.drawString(startingx+342, startingy, str(str((data[1])[8])))  

        except:
            pass

        try:
            data[2]

            if len((data[2])[0]) > 35:
                a = (data[2])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,740, top_text)
                p.drawString(39,734, bottom_text)
        
            else:
                p.drawString(39, 737, (data[2])[0])

            p.drawString(startingx+226, startingy-19, str(str((data[2])[1])+"/"))
            p.drawString(startingx+232, startingy-19, str(str((data[2])[2])+"/"))
            p.drawString(startingx+242, startingy-19, str(str((data[2])[3])))  

            p.drawString(startingx+263, startingy-19, str(str((data[2])[4])+"/"))
            p.drawString(startingx+273, startingy-19, str(str((data[2])[5])+"/"))
            p.drawString(startingx+283, startingy-19, str(str((data[2])[6])))  

            p.drawString(startingx+316, startingy-19, (data[2])[7])
            p.drawString(startingx+342, startingy-19, str(str((data[2])[8])))  

        except:
            pass

        try:
            data[3]

            if len((data[3])[0]) > 35:
                a = (data[3])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,720, top_text)
                p.drawString(39,714, bottom_text)
        
            else:
                p.drawString(39, 717, (data[3])[0])

            p.drawString(startingx+226, startingy-39, str(str((data[3])[1])+"/"))
            p.drawString(startingx+232, startingy-39, str(str((data[3])[2])+"/"))
            p.drawString(startingx+242, startingy-39, str(str((data[3])[3])))  

            p.drawString(startingx+263 , startingy-39, str(str((data[3])[4])+"/"))
            p.drawString(startingx+273, startingy-39, str(str((data[3])[5])+"/"))
            p.drawString(startingx+283, startingy-39, str(str((data[3])[6])))  

            p.drawString(startingx+316, startingy-39, (data[3])[7])
            p.drawString(startingx+342, startingy-39, str(str((data[3])[8])))  

        except:
            pass

        try:
            data[4]

            if len((data[4])[0]) > 35:
                a = (data[4])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,702, top_text)
                p.drawString(39,696, bottom_text)
        
            else:
                p.drawString(39, 699, (data[4])[0])

            p.drawString(startingx+226, startingy-57, str(str((data[4])[1])+"/"))
            p.drawString(startingx+232, startingy-57, str(str((data[4])[2])+"/"))
            p.drawString(startingx+242, startingy-57, str(str((data[4])[3])))  

            p.drawString(startingx+263, startingy-57, str(str((data[4])[4])+"/"))
            p.drawString(startingx+273, startingy-57, str(str((data[4])[5])+"/"))
            p.drawString(startingx+283, startingy-57, str(str((data[4])[6])))  

            p.drawString(startingx+316, startingy-57, (data[4])[7])
            p.drawString(startingx+342, startingy-57, str(str((data[4])[8])))  

        except:
            pass

        try:
            data[5]

            if len((data[5])[0]) > 35:
                a = (data[5])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,684, top_text)
                p.drawString(39,678, bottom_text)
        
            else:
                p.drawString(39, 681, (data[5])[0])

            p.drawString(startingx+226, startingy-75, str(str((data[5])[1])+"/"))
            p.drawString(startingx+232, startingy-75, str(str((data[5])[2])+"/"))
            p.drawString(startingx+242, startingy-75, str(str((data[5])[3])))  

            p.drawString(startingx+263, startingy-75, str(str((data[5])[4])+"/"))
            p.drawString(startingx+273, startingy-75, str(str((data[5])[5])+"/"))
            p.drawString(startingx+283, startingy-75, str(str((data[5])[6])))  

            p.drawString(startingx+316, startingy-75, (data[5])[7])
            p.drawString(startingx+342, startingy-75, str(str((data[5])[8])))  

        except:
            pass

        try:
            data[6]

            if len((data[6])[0]) > 35:
                a = (data[6])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,666, top_text)
                p.drawString(39,660, bottom_text)
        
            else:
                p.drawString(39, 663, (data[6])[0])

            p.drawString(startingx+226, startingy-93, str(str((data[6])[1])+"/"))
            p.drawString(startingx+232, startingy-93, str(str((data[6])[2])+"/"))
            p.drawString(startingx+242, startingy-93, str(str((data[6])[3])))  

            p.drawString(startingx+263, startingy-93, str(str((data[6])[4])+"/"))
            p.drawString(startingx+273, startingy-93, str(str((data[6])[5])+"/"))
            p.drawString(startingx+283, startingy-93, str(str((data[6])[6])))  

            p.drawString(startingx+316, startingy-93, (data[6])[7])
            p.drawString(startingx+342, startingy-93, str(str((data[6])[8])))  

        except:
            pass

        try:
            data[7]

            if len((data[7])[0]) > 35:
                a = (data[7])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(39,648, top_text)
                p.drawString(39,642, bottom_text)
        
            else:
                p.drawString(39, 645, (data[7])[0])


            p.drawString(startingx+226, startingy-111, str(str((data[7])[1])+"/"))
            p.drawString(startingx+232, startingy-111, str(str((data[7])[2])+"/"))
            p.drawString(startingx+242, startingy-111, str(str((data[7])[3])))  

            p.drawString(startingx+263, startingy-111, str(str((data[7])[4])+"/"))
            p.drawString(startingx+273, startingy-111, str(str((data[7])[5])+"/"))
            p.drawString(startingx+283, startingy-111, str(str((data[7])[6])))  

            p.drawString(startingx+316, startingy-111, (data[7])[7])
            p.drawString(startingx+342, startingy-111, str(str((data[7])[8])))  

        except:
            pass

        learning = learning_development.objects.all().filter(authUser_id=pk).order_by('-id')
        startingx1 = int(44)
        startingy1= int(565)

        data2 = [['','','','','','']]
        for learn in learning:
            data2.append([learn.title, learn.date_of_attendance_from.month, learn.date_of_attendance_from.day,  learn.date_of_attendance_from.year,
                        learn.date_of_attendance_to.month, learn.date_of_attendance_to.day,  learn.date_of_attendance_to.year, learn.work_hours, learn.type_of_ld, learn.conducted])
            
        try:
            data2[1]

            if len((data2[1])[0]) > 35:
                a = (data2[1])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,562, top_text)
                p.drawString(40,569, bottom_text)
        
            else:
                p.drawString(40, 565, (data2[1])[0])

            p.drawString(startingx1+226, startingy1, str(str((data2[1])[1])+"/"))
            p.drawString(startingx1+232, startingy1, str(str((data2[1])[2])+"/"))
            p.drawString(startingx1+242, startingy1, str(str((data2[1])[3])))  

            p.drawString(startingx1+263, startingy1, str(str((data2[1])[4])+"/"))
            p.drawString(startingx1+273, startingy1, str(str((data2[1])[5])+"/"))
            p.drawString(startingx1+283, startingy1, str(str((data2[1])[6])))  

            p.drawString(startingx1+316, startingy1, (data2[1])[7])
            p.drawString(startingx1+342, startingy1, str(str((data2[1])[8])))  
            p.drawString(startingx1+386, startingy1, (data2[1])[9])

        except:
            pass

        try:
            data2[2]

            if len((data2[2])[0]) > 35:
                a = (data2[2])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,553, top_text)
                p.drawString(40,546, bottom_text)
        
            else:
                p.drawString(40, 549, (data2[2])[0])

            p.drawString(startingx1+226, startingy1-16, str(str((data2[2])[1])+"/"))
            p.drawString(startingx1+232, startingy1-16, str(str((data2[2])[2])+"/"))
            p.drawString(startingx1+242, startingy1-16, str(str((data2[2])[3])))  

            p.drawString(startingx1+263, startingy1-16, str(str((data2[2])[4])+"/"))
            p.drawString(startingx1+273, startingy1-16, str(str((data2[2])[5])+"/"))
            p.drawString(startingx1+283, startingy1-16, str(str((data2[2])[6])))  

            p.drawString(startingx1+316, startingy1-16, (data2[2])[7])
            p.drawString(startingx1+342, startingy1-16, str(str((data2[2])[8])))  
            p.drawString(startingx1+386, startingy1-16, (data2[2])[9])

        except:
            pass

        try:
            data2[3]

            if len((data2[3])[0]) > 35:
                a = (data2[3])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,536, top_text)
                p.drawString(40,529, bottom_text)
        
            else:
                p.drawString(40, 532, (data2[3])[0])

            p.drawString(startingx1+226, startingy1-33, str(str((data2[3])[1])+"/"))
            p.drawString(startingx1+232, startingy1-33, str(str((data2[3])[2])+"/"))
            p.drawString(startingx1+242, startingy1-33, str(str((data2[3])[3])))  

            p.drawString(startingx1+263, startingy1-33, str(str((data2[3])[4])+"/"))
            p.drawString(startingx1+273, startingy1-33, str(str((data2[3])[5])+"/"))
            p.drawString(startingx1+283, startingy1-33, str(str((data2[3])[6])))  

            p.drawString(startingx1+316, startingy1-33, (data2[3])[7])
            p.drawString(startingx1+342, startingy1-33, str(str((data2[3])[8])))  
            p.drawString(startingx1+386, startingy1-33, (data2[3])[9])

        except:
            pass

        try:
            data2[4]

            if len((data2[4])[0]) > 35:
                a = (data2[4])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,519, top_text)
                p.drawString(40,512, bottom_text)
        
            else:
                p.drawString(40, 515, (data2[4])[0])

            p.drawString(startingx1+226, startingy1-50, str(str((data2[4])[1])+"/"))
            p.drawString(startingx1+232, startingy1-50, str(str((data2[4])[2])+"/"))
            p.drawString(startingx1+242, startingy1-50, str(str((data2[4])[3])))  

            p.drawString(startingx1+263, startingy1-50, str(str((data2[4])[4])+"/"))
            p.drawString(startingx1+273, startingy1-50, str(str((data2[4])[5])+"/"))
            p.drawString(startingx1+283, startingy1-50, str(str((data2[4])[6])))  

            p.drawString(startingx1+316, startingy1-50, (data2[4])[7])
            p.drawString(startingx1+342, startingy1-50, str(str((data2[4])[8])))  
            p.drawString(startingx1+386, startingy1-50, (data2[4])[9])

        except:
            pass

        try:
            data2[5]

            if len((data2[5])[0]) > 35:
                a = (data2[5])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,501, top_text)
                p.drawString(40,494, bottom_text)
        
            else:
                p.drawString(40, 497, (data2[5])[0])

            p.drawString(startingx1+226, startingy1-68, str(str((data2[5])[1])+"/"))
            p.drawString(startingx1+232, startingy1-68, str(str((data2[5])[2])+"/"))
            p.drawString(startingx1+242, startingy1-68, str(str((data2[5])[3])))  

            p.drawString(startingx1+263, startingy1-68, str(str((data2[5])[4])+"/"))
            p.drawString(startingx1+273, startingy1-68, str(str((data2[5])[5])+"/"))
            p.drawString(startingx1+283, startingy1-68, str(str((data2[5])[6])))  

            p.drawString(startingx1+316, startingy1-68, (data2[5])[7])
            p.drawString(startingx1+342, startingy1-68, str(str((data2[5])[8])))  
            p.drawString(startingx1+386, startingy1-68, (data2[5])[9])

        except:
            pass

        try:
            data2[6]

            if len((data2[6])[0]) > 35:
                a = (data2[6])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,482, top_text)
                p.drawString(40,476, bottom_text)
        
            else:
                p.drawString(40, 479, (data2[6])[0])

            p.drawString(startingx1+226, startingy1-86, str(str((data2[6])[1])+"/"))
            p.drawString(startingx1+232, startingy1-86, str(str((data2[6])[2])+"/"))
            p.drawString(startingx1+242, startingy1-86, str(str((data2[6])[3])))  

            p.drawString(startingx1+263, startingy1-86, str(str((data2[6])[4])+"/"))
            p.drawString(startingx1+273, startingy1-86, str(str((data2[6])[5])+"/"))
            p.drawString(startingx1+283, startingy1-86, str(str((data2[6])[6])))  

            p.drawString(startingx1+316, startingy1-86, (data2[6])[7])
            p.drawString(startingx1+342, startingy1-86, str(str((data2[6])[8])))  
            p.drawString(startingx1+386, startingy1-86, (data2[6])[9])

        except:
            pass

        try:
            data2[7]

            if len((data2[7])[0]) > 35:
                a = (data2[7])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,467, top_text)
                p.drawString(40,460, bottom_text)
        
            else:
                p.drawString(40, 463, (data2[7])[0])

            p.drawString(startingx1+226, startingy1-102, str(str((data2[7])[1])+"/"))
            p.drawString(startingx1+232, startingy1-102, str(str((data2[7])[2])+"/"))
            p.drawString(startingx1+242, startingy1-102, str(str((data2[7])[3])))  

            p.drawString(startingx1+263, startingy1-102, str(str((data2[7])[4])+"/"))
            p.drawString(startingx1+273, startingy1-102, str(str((data2[7])[5])+"/"))
            p.drawString(startingx1+283, startingy1-102, str(str((data2[7])[6])))  

            p.drawString(startingx1+316, startingy1-102, (data2[7])[7])
            p.drawString(startingx1+342, startingy1-102, str(str((data2[7])[8])))  
            p.drawString(startingx1+386, startingy1-102, (data2[7])[9])

        except:
            pass

        try:
            data2[8]
                    
            if len((data2[8])[0]) > 35:
                a = (data2[8])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,450, top_text)
                p.drawString(40,442, bottom_text)
        
            else:
                p.drawString(40, 446, (data2[8])[0])

            p.drawString(startingx1+226, startingy1-119, str(str((data2[8])[1])+"/"))
            p.drawString(startingx1+232, startingy1-119, str(str((data2[8])[2])+"/"))
            p.drawString(startingx1+242, startingy1-119, str(str((data2[8])[3])))  

            p.drawString(startingx1+263, startingy1-119, str(str((data2[8])[4])+"/"))
            p.drawString(startingx1+273, startingy1-119, str(str((data2[8])[5])+"/"))
            p.drawString(startingx1+283, startingy1-119, str(str((data2[8])[6])))  

            p.drawString(startingx1+316, startingy1-119, (data2[8])[7])
            p.drawString(startingx1+342, startingy1-119, str(str((data2[8])[8])))  
            p.drawString(startingx1+386, startingy1-119, (data2[8])[9])

        except:
            pass

        try:
            data2[9]
                    
            if len((data2[9])[0]) > 35:
                a = (data2[9])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,432, top_text)
                p.drawString(40,425, bottom_text)
        
            else:
                p.drawString(40, 428, (data2[9])[0])

            

            p.drawString(startingx1+226, startingy1-137, str(str((data2[9])[1])+"/"))
            p.drawString(startingx1+232, startingy1-137, str(str((data2[9])[2])+"/"))
            p.drawString(startingx1+242, startingy1-137, str(str((data2[9])[3])))  

            p.drawString(startingx1+263, startingy1-137, str(str((data2[9])[4])+"/"))
            p.drawString(startingx1+273, startingy1-137, str(str((data2[9])[5])+"/"))
            p.drawString(startingx1+283, startingy1-137, str(str((data2[9])[6])))  

            p.drawString(startingx1+316, startingy1-137, (data2[9])[7])
            p.drawString(startingx1+342, startingy1-137, str(str((data2[9])[8])))  
            p.drawString(startingx1+386, startingy1-137, (data2[9])[9])

        except:
            pass

        try:
            data2[10]
                    
            if len((data2[10])[0]) > 35:
                a = (data2[10])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,416, top_text)
                p.drawString(40,409, bottom_text)
        
            else:
                p.drawString(40, 412, (data2[10])[0])

            p.drawString(startingx1+226, startingy1-153, str(str((data2[10])[1])+"/"))
            p.drawString(startingx1+232, startingy1-153, str(str((data2[10])[2])+"/"))
            p.drawString(startingx1+242, startingy1-153, str(str((data2[10])[3])))  

            p.drawString(startingx1+263, startingy1-153, str(str((data2[10])[4])+"/"))
            p.drawString(startingx1+273, startingy1-153, str(str((data2[10])[5])+"/"))
            p.drawString(startingx1+283, startingy1-153, str(str((data2[10])[6])))  

            p.drawString(startingx1+316, startingy1-153, (data2[10])[7])
            p.drawString(startingx1+342, startingy1-153, str(str((data2[10])[8])))  
            p.drawString(startingx1+386, startingy1-153, (data2[10])[9])
        except:
            pass

        try:
            data2[11]
                    
            if len((data2[11])[0]) > 35:
                a = (data2[11])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,400, top_text)
                p.drawString(40,393, bottom_text)
        
            else:
                p.drawString(40, 396, (data2[11])[0])

            p.drawString(startingx1+226, startingy1-169, str(str((data2[11])[1])+"/"))
            p.drawString(startingx1+232, startingy1-169, str(str((data2[11])[2])+"/"))
            p.drawString(startingx1+242, startingy1-169, str(str((data2[11])[3])))  

            p.drawString(startingx1+263, startingy1-169, str(str((data2[11])[4])+"/"))
            p.drawString(startingx1+273, startingy1-169, str(str((data2[11])[5])+"/"))
            p.drawString(startingx1+283, startingy1-169, str(str((data2[11])[6])))  

            p.drawString(startingx1+316, startingy1-169, (data2[11])[7])
            p.drawString(startingx1+342, startingy1-169, str(str((data2[11])[8])))  
            p.drawString(startingx1+386, startingy1-169, (data2[11])[9])
        except:
            pass

        try:
            data2[12]
                    
            if len((data2[12])[0]) > 35:
                a = (data2[12])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,382, top_text)
                p.drawString(40,375, bottom_text)
        
            else:
                p.drawString(40, 378, (data2[12])[0])

            p.drawString(startingx1+226, startingy1-187, str(str((data2[12])[1])+"/"))
            p.drawString(startingx1+232, startingy1-187, str(str((data2[12])[2])+"/"))
            p.drawString(startingx1+242, startingy1-187, str(str((data2[12])[3])))  

            p.drawString(startingx1+263, startingy1-187, str(str((data2[12])[4])+"/"))
            p.drawString(startingx1+273, startingy1-187, str(str((data2[12])[5])+"/"))
            p.drawString(startingx1+283, startingy1-187, str(str((data2[12])[6])))  

            p.drawString(startingx1+316, startingy1-187, (data2[12])[7])
            p.drawString(startingx1+342, startingy1-187, str(str((data2[12])[8])))  
            p.drawString(startingx1+386, startingy1-187, (data2[12])[9])
        except:
            pass

        try:
            data2[13]

                    
            if len((data2[13])[0]) > 35:
                a = (data2[13])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,365, top_text)
                p.drawString(40,358, bottom_text)
        
            else:
                p.drawString(40, 361, (data2[13])[0])

            p.drawString(startingx1+226, startingy1-204, str(str((data2[13])[1])+"/"))
            p.drawString(startingx1+232, startingy1-204, str(str((data2[13])[2])+"/"))
            p.drawString(startingx1+242, startingy1-204, str(str((data2[13])[3])))  

            p.drawString(startingx1+263, startingy1-204, str(str((data2[13])[4])+"/"))
            p.drawString(startingx1+273, startingy1-204, str(str((data2[13])[5])+"/"))
            p.drawString(startingx1+283, startingy1-204, str(str((data2[13])[6])))  

            p.drawString(startingx1+316, startingy1-204, (data2[13])[7])
            p.drawString(startingx1+342, startingy1-204, str(str((data2[13])[8])))  
            p.drawString(startingx1+386, startingy1-204, (data2[13])[9])
        except:
            pass

        try:
            data2[14]
                    
            if len((data2[14])[0]) > 35:
                a = (data2[14])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,348, top_text)
                p.drawString(40,341, bottom_text)
        
            else:
                p.drawString(40, 345, (data2[14])[0])
                

            p.drawString(startingx1+226, startingy1-221, str(str((data2[14])[1])+"/"))
            p.drawString(startingx1+232, startingy1-221, str(str((data2[14])[2])+"/"))
            p.drawString(startingx1+242, startingy1-221, str(str((data2[14])[3])))  

            p.drawString(startingx1+263, startingy1-221, str(str((data2[14])[4])+"/"))
            p.drawString(startingx1+273, startingy1-221, str(str((data2[14])[5])+"/"))
            p.drawString(startingx1+283, startingy1-221, str(str((data2[14])[6])))  

            p.drawString(startingx1+316, startingy1-221, (data2[14])[7])
            p.drawString(startingx1+342, startingy1-221, str(str((data2[14])[8])))  
            p.drawString(startingx1+386, startingy1-221, (data2[14])[9])
        except:
            pass

        try:
            data2[15]
            
            if len((data2[15])[0]) > 35:
                a = (data2[15])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,331, top_text)
                p.drawString(40,324, bottom_text)
        
            else:
                p.drawString(40, 327, (data2[15])[0])
                

            p.drawString(startingx1+226, startingy1-238, str(str((data2[15])[1])+"/"))
            p.drawString(startingx1+232, startingy1-238, str(str((data2[15])[2])+"/"))
            p.drawString(startingx1+242, startingy1-238, str(str((data2[15])[3])))  

            p.drawString(startingx1+263, startingy1-238, str(str((data2[15])[4])+"/"))
            p.drawString(startingx1+273, startingy1-238, str(str((data2[15])[5])+"/"))
            p.drawString(startingx1+283, startingy1-238, str(str((data2[15])[6])))  

            p.drawString(startingx1+316, startingy1-238, (data2[15])[7])
            p.drawString(startingx1+342, startingy1-238, str(str((data2[15])[8])))  
            p.drawString(startingx1+386, startingy1-238, (data2[15])[9])
        except:
            pass

        try:
            data2[16]
                    
            if len((data2[16])[0]) > 35:
                a = (data2[16])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,314, top_text)
                p.drawString(40,307, bottom_text)
        
            else:
                p.drawString(40, 310, (data2[16])[0])

            p.drawString(startingx1+226, startingy1-255, str(str((data2[16])[1])+"/"))
            p.drawString(startingx1+232, startingy1-255, str(str((data2[16])[2])+"/"))
            p.drawString(startingx1+242, startingy1-255, str(str((data2[16])[3])))  

            p.drawString(startingx1+263, startingy1-255, str(str((data2[16])[4])+"/"))
            p.drawString(startingx1+273, startingy1-255, str(str((data2[16])[5])+"/"))
            p.drawString(startingx1+283, startingy1-255, str(str((data2[16])[6])))  

            p.drawString(startingx1+316, startingy1-255, (data2[16])[7])
            p.drawString(startingx1+342, startingy1-255, str(str((data2[16])[8])))  
            p.drawString(startingx1+386, startingy1-255, (data2[16])[9])
        except:
            pass

        try:
            data2[17]
            
            if len((data2[17])[0]) > 35:
                a = (data2[17])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,297, top_text)
                p.drawString(40,290, bottom_text)
        
            else:
                p.drawString(40, 293, (data2[17])[0])

            p.drawString(startingx1+226, startingy1-272, str(str((data2[17])[1])+"/"))
            p.drawString(startingx1+232, startingy1-272, str(str((data2[17])[2])+"/"))
            p.drawString(startingx1+242, startingy1-272, str(str((data2[17])[3])))  

            p.drawString(startingx1+263, startingy1-272, str(str((data2[17])[4])+"/"))
            p.drawString(startingx1+273, startingy1-272, str(str((data2[17])[5])+"/"))
            p.drawString(startingx1+283, startingy1-272, str(str((data2[17])[6])))  

            p.drawString(startingx1+316, startingy1-272, (data2[17])[7])
            p.drawString(startingx1+342, startingy1-272, str(str((data2[17])[8])))  
            p.drawString(startingx1+386, startingy1-272, (data2[17])[9])
        except:
            pass

        try:
            data2[18]

            if len((data2[18])[0]) > 35:
                a = (data2[18])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,280, top_text)
                p.drawString(40,273, bottom_text)
        
            else:
                p.drawString(40, 276, (data2[18])[0])

            p.drawString(startingx1+226, startingy1-289, str(str((data2[18])[1])+"/"))
            p.drawString(startingx1+232, startingy1-289, str(str((data2[18])[2])+"/"))
            p.drawString(startingx1+242, startingy1-289, str(str((data2[18])[3])))  

            p.drawString(startingx1+263, startingy1-289, str(str((data2[18])[4])+"/"))
            p.drawString(startingx1+273, startingy1-289, str(str((data2[18])[5])+"/"))
            p.drawString(startingx1+283, startingy1-289, str(str((data2[18])[6])))  

            p.drawString(startingx1+316, startingy1-289, (data2[18])[7])
            p.drawString(startingx1+342, startingy1-289, str(str((data2[18])[8])))  
            p.drawString(startingx1+386, startingy1-289, (data2[18])[9])
        except:
            pass

        try:
            data2[19]

            if len((data2[19])[0]) > 35:
                a = (data2[19])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,263, top_text)
                p.drawString(40,256, bottom_text)
        
            else:
                p.drawString(40, 259, (data2[19])[0])

            p.drawString(startingx1+226, startingy1-306, str(str((data2[19])[1])+"/"))
            p.drawString(startingx1+232, startingy1-306, str(str((data2[19])[2])+"/"))
            p.drawString(startingx1+242, startingy1-306, str(str((data2[19])[3])))  

            p.drawString(startingx1+263, startingy1-306, str(str((data2[19])[4])+"/"))
            p.drawString(startingx1+273, startingy1-306, str(str((data2[19])[5])+"/"))
            p.drawString(startingx1+283, startingy1-306, str(str((data2[19])[6])))  

            p.drawString(startingx1+316, startingy1-306, (data2[19])[7])
            p.drawString(startingx1+342, startingy1-306, str(str((data2[19])[8])))  
            p.drawString(startingx1+386, startingy1-306, (data2[19])[9])
        except:
            pass

        try:
            data2[20]
            
            if len((data2[20])[0]) > 35:
                a = (data2[20])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,246, top_text)
                p.drawString(40,239, bottom_text)
        
            else:
                p.drawString(40, 242, (data2[20])[0])

            p.drawString(startingx1+226, startingy1-323, str(str((data2[20])[1])+"/"))
            p.drawString(startingx1+232, startingy1-323, str(str((data2[20])[2])+"/"))
            p.drawString(startingx1+242, startingy1-323, str(str((data2[20])[3])))  

            p.drawString(startingx1+263, startingy1-323, str(str((data2[20])[4])+"/"))
            p.drawString(startingx1+273, startingy1-323, str(str((data2[20])[5])+"/"))
            p.drawString(startingx1+283, startingy1-323, str(str((data2[20])[6])))  

            p.drawString(startingx1+316, startingy1-323, (data2[20])[7])
            p.drawString(startingx1+342, startingy1-323, str(str((data2[20])[8])))  
            p.drawString(startingx1+386, startingy1-323, (data2[20])[9])
        except:
            pass

        try:
            data2[21]
        
            if len((data2[21])[0]) > 35:
                a = (data2[21])[0].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(40,229, top_text)
                p.drawString(40,222, bottom_text)
        
            else:
                p.drawString(40, 225, (data2[21])[0])

            p.drawString(startingx1+226, startingy1-340, str(str((data2[21])[1])+"/"))
            p.drawString(startingx1+232, startingy1-340, str(str((data2[21])[2])+"/"))
            p.drawString(startingx1+242, startingy1-340, str(str((data2[21])[3])))  

            p.drawString(startingx1+263, startingy1-340, str(str((data2[21])[4])+"/")) 
            p.drawString(startingx1+273, startingy1-340, str(str((data2[21])[5])+"/"))
            p.drawString(startingx1+283, startingy1-340, str(str((data2[21])[6])))  

            p.drawString(startingx1+316, startingy1-340, (data2[21])[7])
            p.drawString(startingx1+342, startingy1-340, str(str((data2[21])[8])))  
            p.drawString(startingx1+386, startingy1-340, (data2[21])[9])
        except:
            pass

        other = other_info.objects.all().filter(authUser_id=pk).order_by('-id')
        startingx2 = int(44)
        startingy2= int(160 )

        data3 = [['','','']]
        for oth in other:
            data3.append([oth.skills_hobbies, oth.non_acad_recognition, oth.membership])
            
        try:
            data3[1]

            if len((data3[1])[2]) > 35:
                a = (data3[1])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,157, top_text)
                p.drawString(430,163, bottom_text)
        
            else:
                p.drawString(430, 160, (data3[1])[2])

            p.drawString(startingx2, startingy2, (data3[1])[0])
            p.drawString(startingx2+135, startingy2, (data3[1])[1])

        except:
            pass

        try:
            data3[2]

            if len((data3[2])[2]) > 35:
                a = (data3[2])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,138, top_text)
                p.drawString(430,144, bottom_text)
        
            else:
                p.drawString(430, 141, (data3[2])[2])

            p.drawString(startingx2, startingy2-19, (data3[2])[0])
            p.drawString(startingx2+135, startingy2-19, (data3[2])[1])
            
        except:
            pass

        
        try:
            data3[3]

            if len((data3[3])[2]) > 35:
                a = (data3[3])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,126, top_text)
                p.drawString(430,120, bottom_text)
        
            else:
                p.drawString(430, 123, (data3[3])[2])

            p.drawString(startingx2, startingy2-37, (data3[3])[0])
            p.drawString(startingx2+135, startingy2-37, (data3[3])[1])

        except:
            pass

        try:
            data3[4]

            if len((data3[4])[2]) > 35:
                a = (data3[4])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,108, top_text)
                p.drawString(430,102, bottom_text)
        
            else:
                p.drawString(430, 105, (data3[4])[2])

            p.drawString(startingx2, startingy2-55, (data3[4])[0])
            p.drawString(startingx2+135, startingy2-55, (data3[4])[1])

        except:
            pass

        try:
            data3[5]

            if len((data3[5])[2]) > 35:
                a = (data3[5])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,93, top_text)
                p.drawString(430,87, bottom_text)
        
            else:
                p.drawString(430, 90, (data3[5])[2])

            p.drawString(startingx2, startingy2-70, (data3[5])[0])
            p.drawString(startingx2+135, startingy2-70, (data3[5])[1])

        except:
            pass

        try:
            data3[6]

            if len((data3[6])[2]) > 35:
                a = (data3[6])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,70, top_text)
                p.drawString(430,76, bottom_text)
        
            else:
                p.drawString(430, 73, (data3[6])[2])

            p.drawString(startingx2, startingy2-87  , (data3[6])[0])
            p.drawString(startingx2+135, startingy2-87  , (data3[6])[1])


        except:
            pass

        try:
            data3[7]

            if len((data3[7])[2]) > 35:
                a = (data3[7])[2].split()

                length = int(len(a))

                divide = int(length/2)
                other_half = int(length - divide)

                new_list = []
                for index in range(0, divide):
                    new_list.append(a[index])

                other_list = a[-other_half:]

                top_text = " ".join(new_list)

                bottom_text = " ".join(other_list)

                p.drawString(430,57, top_text)
                p.drawString(430,63, bottom_text)
        
            else:
                p.drawString(430, 58, (data3[7])[2])

            p.drawString(startingx2, startingy2-102, (data3[7])[0])
            p.drawString(startingx2+135, startingy2-102, (data3[7])[1])
        
        except:
            pass

        p.save()

        packet.seek(0)

        new_pdf = PdfReader(packet)
        existing_pdf = PdfReader(open("var/www/django_project/page3.pdf", "rb"))
        output = PdfWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)


        output_stream = BytesIO()
        output.write(output_stream)
        output.close()
        output_stream.seek(0)
        
        return HttpResponse(output_stream, content_type='application/pdf')

    else:
        return redirect('logout')

@login_required(login_url='loginpage')
def admin_generate_pdf4(request, pk):
    if request.user.is_authenticated and  request.user.is_staff == 1:
        pagesize1 = (8.5 * inch, 13 * inch)  # 20 inch width and 10 inch height.
        packet = io.BytesIO()
        
        p = canvas.Canvas(packet, pagesize= pagesize1) 
        p.setFont("Helvetica", 7) 


        name1 = references.objects.filter(authUser_id=pk).values_list('name1',flat=True).first() 
        name2 = references.objects.filter(authUser_id=pk).values_list('name2',flat=True).first() 
        name3 = references.objects.filter(authUser_id=pk).values_list('name3',flat=True).first() 
        address1 = references.objects.filter(authUser_id=pk).values_list('address1',flat=True).first() 
        address2 = references.objects.filter(authUser_id=pk).values_list('address2',flat=True).first() 
        address3 = references.objects.filter(authUser_id=pk).values_list('address3',flat=True).first() 
        telno1 = references.objects.filter(authUser_id=pk).values_list('telno1',flat=True).first() 
        telno2 = references.objects.filter(authUser_id=pk).values_list('telno2',flat=True).first() 
        telno3 = references.objects.filter(authUser_id=pk).values_list('telno3',flat=True).first()
        gov_id = references.objects.filter(authUser_id=pk).values_list('gov_id',flat=True).first()
        license_id = references.objects.filter(authUser_id=pk).values_list('license_id',flat=True).first()
        date = references.objects.filter(authUser_id=pk).values_list('date',flat=True).first()
        indigenous = references.objects.filter(authUser_id=pk).values_list('indigenous',flat=True).first()
        indig_specify = references.objects.filter(authUser_id=pk).values_list('indig_specify',flat=True).first()
        disability = references.objects.filter(authUser_id=pk).values_list('disability',flat=True).first()
        disab_specify = references.objects.filter(authUser_id=pk).values_list('disab_specify',flat=True).first()
        solo_parent = references.objects.filter(authUser_id=pk).values_list('solo_parent',flat=True).first()
        solo_specify= references.objects.filter(authUser_id=pk).values_list('solo_specify',flat=True).first()

        name11 = f'{name1}'
        name21 = f'{name2}'
        name31 = f'{name3}'
        address11 = f'{address1}'
        address21 = f'{address2}'
        address31 = f'{address3}'
        telno11 = f'{telno1}'
        telno21 = f'{telno2}'
        telno31 = f'{telno3}'
        gov_id1 = f'{gov_id}'
        license_id1 = f'{license_id}'
        date1 = f'{date.month}/{date.day}/{date.year}'
        indig_specify1 = f'{indig_specify}'
        disab_specify1 = f'{disab_specify}'
        solo_specify1 = f'{solo_specify}'

        p.drawString(431, 770, '✓')
        p.drawString(431, 756, '✓')
        p.drawString(431, 715, '✓')
        p.drawString(434, 670, '✓')
        p.drawString(437, 615, '✓')
        p.drawString(438, 572, '✓')
        p.drawString(442, 535, '✓')
        p.drawString(443, 509, '✓')
        p.drawString(442, 478, '✓')

        if indigenous == 'yes':  
            p.drawString(375, 413, '✓')
        else:
            p.drawString(444, 413, '✓')
        
        p.drawString(475, 403, indig_specify1)

        if disability == 'yes':  
            p.drawString(375, 391, '✓')
        else:
            p.drawString(444, 391, '✓')

        p.drawString(475, 379, disab_specify1)

        if solo_parent == 'yes':  
            p.drawString(375, 368, '✓')
        else:
            p.drawString(444, 368, '✓')

        p.drawString(475, 358, solo_specify1)
        
        p.drawString(40, 305, name11)

        if len(address11) > 40:
            a = address11.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(240,308, top_text)
            p.drawString(240,301, bottom_text)
        
        else:
            p.drawString(240, 305, address11)

        p.drawString(365, 305, telno11)

        p.drawString(40, 285, name21)

        if len(address21) > 40:
            a = address21.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(240,288, top_text)
            p.drawString(240,281, bottom_text)
        
        else:
            p.drawString(240, 285, address21)

        p.drawString(365, 285, telno21)

        p.drawString(40, 265, name31)

        if len(address31) > 40:
            a = address31.split()

            length = int(len(a))

            divide = int(length/2)
            other_half = int(length - divide)

            new_list = []
            for index in range(0, divide):
                new_list.append(a[index])

            other_list = a[-other_half:]

            top_text = " ".join(new_list)

            bottom_text = " ".join(other_list)

            p.drawString(240,269, top_text)
            p.drawString(240,262, bottom_text)
        
        else:
            p.drawString(240, 265, address31)

        p.drawString(365, 265, telno31)

        p.drawString(110, 158, gov_id1)
        p.drawString(110, 140, license_id1)
        p.drawString(110, 123, date1)

        p.save()

        packet.seek(0)

        new_pdf = PdfReader(packet)
        existing_pdf = PdfReader(open("var/www/django_project/page4.pdf", "rb"))
        output = PdfWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)


        output_stream = BytesIO()
        output.write(output_stream)
        output.close()
        output_stream.seek(0)

        return HttpResponse(output_stream, content_type='application/pdf')

    else:
        return redirect('logout')


print("sheesh")
