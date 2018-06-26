from django.shortcuts import render
from .models import OrgInfo, CityInfo, TeacherInfo
from operations.models import UserLoveInfo
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.db.models import Q


# Create your views here.

def org_list(request):
    all_orgs = OrgInfo.objects.all()

    keywords = request.GET.get('keywords', '')
    if keywords:
        all_orgs = all_orgs.filter(
            Q(name__icontains=keywords) | Q(desc__icontains=keywords) | Q(detail__icontains=keywords))

    sort_orgs = all_orgs.order_by('-add_time')[:3]

    all_citys = CityInfo.objects.all()
    cat = request.GET.get('cat', '')
    if cat:
        all_orgs = all_orgs.filter(category=cat)
    cityid = request.GET.get('cityid', '')
    if cityid:
        all_orgs = all_orgs.filter(cityinfo_id=cityid)
    sort = request.GET.get('sort', '')
    if sort == 'studynum':
        all_orgs = all_orgs.order_by('-study_num')
    elif sort == 'coursenum':
        all_orgs = all_orgs.order_by('-course_num')
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(all_orgs, 3)
    try:
        page_list = pa.page(pagenum)
    except PageNotAnInteger:
        page_list = pa.page(1)
    except EmptyPage:
        page_list = pa.page(pa.num_pages)
    return render(request, 'orgs/org-list.html', {
        'all_orgs': all_orgs,
        'all_citys': all_citys,
        'page_list': page_list,
        'cat': cat,
        'cityid': cityid,
        'sort': sort,
        'sort_orgs': sort_orgs,
        'keywords': keywords

    })


def org_detail(request, org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=org_id)[0]
        org.click_num += 1
        org.save()
        is_love = False
        if request.user.is_authenticated():
            love = UserLoveInfo.objects.filter(userinfo=request.user, love_id=org_id, love_type=1)
            if love:
                is_love = love[0].love_status
            else:
                pass
        return render(request, 'orgs/org-detail-homepage.html', {
            'org': org,
            'detail_type': 'homepage',
            'is_love': is_love,
        })


def org_detail_course(request, org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=org_id)[0]
        is_love = False
        if request.user.is_authenticated():
            love = UserLoveInfo.objects.filter(userinfo=request.user, love_id=org_id, love_type=1)
            if love:
                is_love = love[0].love_status
            else:
                pass
        return render(request, 'orgs/org-detail-course.html', {
            'org': org,
            'detail_type': 'course',
            'is_love': is_love,
        })


def org_detail_desc(request, org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]
        is_love = False
        if request.user.is_authenticated():
            love = UserLoveInfo.objects.filter(userinfo=request.user, love_id=org_id, love_type=1)
            if love:
                is_love = love[0].love_status
            else:
                pass
        return render(request, 'orgs/org-detail-desc.html', {
            'org': org,
            'detail_type': 'desc',
            'is_love': is_love,
        })


def org_detail_teacher(request, org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]
        is_love = False
        if request.user.is_authenticated():
            love = UserLoveInfo.objects.filter(userinfo=request.user, love_id=org_id, love_type=1)
            if love:
                is_love = love[0].love_status
            else:
                pass
        return render(request, 'orgs/org-detail-teachers.html', {
            'org': org,
            'detail_type': 'teacher',
            'is_love': is_love,
        })


def teacher_list(request):
    all_teachers = TeacherInfo.objects.all()

    keywords = request.GET.get('keywords', '')
    if keywords:
        all_teachers = all_teachers.filter(name__icontains=keywords)

    sort = request.GET.get('sort', '')
    if sort == 'hot':
        all_teachers = all_teachers.order_by('-love_num')

    rec_teachers = all_teachers.order_by('-click_num')[:2]

    pa = Paginator(all_teachers, 2)
    pagenum = request.GET.get("page", '')
    try:
        page_list = pa.page(pagenum)
    except PageNotAnInteger:
        page_list = pa.page(1)
    except EmptyPage:
        page_list = pa.page(pa.num_pages)
    return render(request, 'orgs/teachers-list.html', {
        'all_teachers': all_teachers,
        'page_list': page_list,
        'sort': sort,
        'rec_teachers': rec_teachers,
        'keywords': keywords
    })


def teacher_detail(request, teacher_id):
    if teacher_id:
        teacher = TeacherInfo.objects.filter(id=teacher_id)[0]
        teacher.click_num +=1
        teacher.save()
        rec_teachers = TeacherInfo.objects.all().order_by('-click_num')[:2]
        is_love_org = False
        is_love_teacher = False
        if request.user.is_authenticated():
            love = UserLoveInfo.objects.filter(userinfo=request.user, love_type=1, love_id=teacher.orginfo.id)
            if love:
                is_love_org = love[0].love_status
            love = UserLoveInfo.objects.filter(userinfo=request.user, love_type=3, love_id=teacher.id)
            if love:
                is_love_teacher = love[0].love_status
        return render(request, 'orgs/teacher-detail.html', {
            "teacher": teacher,
            'rec_teachers': rec_teachers,
            'is_love_teacher': is_love_teacher,
            'is_love_org': is_love_org
        })
