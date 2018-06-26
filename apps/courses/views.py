from django.shortcuts import render
from .models import CourseInfo
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from operations.models import UserLoveInfo, UserCourseInfo, UserCommentInfo
from utils.decorators import login_decorator
from django.db.models import Q


# Create your views here.
def course_list(request):
    all_courses = CourseInfo.objects.all()
    keywords = request.GET.get('keywords', '')
    if keywords:
        all_courses = all_courses.filter(
            Q(name__icontains=keywords) | Q(desc__icontains=keywords) | Q(detail__icontains=keywords))
    sort = request.GET.get("sort", '')
    rec_courses = all_courses.order_by('-love_num')[:3]
    if sort == 'hot':
        all_courses = all_courses.order_by('-click_num')
    elif sort == 'students':
        all_courses = all_courses.order_by('-stu_num')
    pagenum = request.GET.get('page', '')
    pa = Paginator(all_courses, 2)
    try:
        page_list = pa.page(pagenum)
    except PageNotAnInteger:
        page_list = pa.page(1)
    except EmptyPage:
        page_list = pa.page(pa.num_pages)
    # return render(request, 'coucses/course-list.html', locals())  # locals 将函数内的所有变量传过去
    return render(request, 'coucses/course-list.html', {
        'all_courses': all_courses,
        'sort': sort,
        'page_list': page_list,
        'rec_courses': rec_courses,
        'keywords': keywords
    })


def course_detail(request, cou_id):
    if cou_id:
        course = CourseInfo.objects.filter(id=cou_id)[0]
        course.click_num += 1
        course.save()
        is_love_org = False
        is_love_course = False
        if request.user.is_authenticated():
            love = UserLoveInfo.objects.filter(userinfo=request.user, love_type=1, love_id=course.orginfo.id)
            if love:
                is_love_org = love[0].love_status
            love1 = UserLoveInfo.objects.filter(userinfo=request.user, love_type=2, love_id=course.id)
            if love1:
                is_love_course = love1[0].love_status

        rec_courses = CourseInfo.objects.all().filter(name__icontains=course.name[:4])
        return render(request, 'coucses/course-detail.html', {
            "course": course,
            'rec_courses': rec_courses,
            'is_love_org': is_love_org,
            'is_love_course': is_love_course,
        })

    else:
        pass


@login_decorator
def course_video(request, cou_id):
    if cou_id:
        course = CourseInfo.objects.filter(id=cou_id)[0]
        usercourse = UserCourseInfo.objects.filter(userinfo=request.user, courseinfo=course)
        if not usercourse:
            usercourse = UserCourseInfo()
            usercourse.userinfo = request.user
            usercourse.courseinfo = course
            usercourse.save()
            # 课程学习人数+1
            course.stu_num += 1
            course.save()
            # 课程所属机构+1
            course.orginfo.study_num += 1
            course.orginfo.save()
        # 第一步 找到该课程对应的所有 UserCourseInfo 记录
        usercourseobjs = UserCourseInfo.objects.filter(courseinfo=course)
        # 第二步 找到所有的用户 UserProfile 对象
        user_list = [item.userinfo for item in usercourseobjs]
        # 第三步 找到所有的用户课程 UserCourseInfo 记录
        usercourse_list = UserCourseInfo.objects.filter(userinfo__in=user_list)
        # 第四步 找到所有的用户课程 CourseInfo 对象
        course_list = [item.courseinfo for item in usercourse_list]
        course_list = list(set(course_list))  # 去重
        course_list = [course1 for course1 in course_list if course.id != course1.id][:3]  # 切片
        return render(request, 'coucses/course-video.html', {
            "course": course,
            'course_list': course_list
        })


def course_comment(request, cou_id):
    if cou_id:
        course = CourseInfo.objects.filter(id=cou_id)[0]
        # 第一步 找到该课程对应的所有 UserCourseInfo 记录
        usercourseobjs = UserCourseInfo.objects.filter(courseinfo=course)
        # 第二步 找到所有的用户对象 UserProfile 对象
        user_list = [item.userinfo for item in usercourseobjs]
        # 第三步 找到所有的用户课程  UserCourseInfo 记录
        usercourse_list = UserCourseInfo.objects.filter(userinfo__in=user_list)
        # 第四步  找到所有的课程  CouseInfo 对象
        course_list = [item.courseinfo for item in usercourse_list]
        # 去重
        course_list = list(set(course_list))
        # 切片  并 抛去该课程
        course_list = [course1 for course1 in course_list if course != course1][:3]
        all_comments = UserCommentInfo.objects.filter(courseinfo=course)
        return render(request, 'coucses/course-comment.html', {
            "course": course,
            'course_list': course_list,
            'all_comments': all_comments,
        })
