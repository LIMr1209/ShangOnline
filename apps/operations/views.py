from django.shortcuts import render
from .forms import UserAskForm, UserCommentFrom
from django.http import JsonResponse
from .models import UserLoveInfo, UserCommentInfo
from utils.decorators import login_decorator
from orgs.models import OrgInfo,TeacherInfo
from courses.models import CourseInfo

# Create your views here.
def user_ask(request):
    user_ask_form = UserAskForm(request.POST)
    if user_ask_form.is_valid():
        user_ask_form.save(commit=True)
        return JsonResponse({
            'status': 'ok',
            'msg': '咨询成功,请等待回复'
        })
    else:
        return JsonResponse({
            'status': 'fail',
            'msg': '咨询失败,重新填写'
        })

@login_decorator
def user_love(request):
    lovetype = request.GET.get('lovetype', '')
    loveid = request.GET.get('loveid', '')
    lover = None
    if lovetype and loveid:
        if lovetype == "1":
            lover = OrgInfo.objects.filter(id=int(loveid))[0]
        elif lovetype == '2':
            lover = CourseInfo.objects.filter(id=int(loveid))[0]
        elif lovetype == '3':
            lover = TeacherInfo.objects.filter(id=int(loveid))[0]
        love = UserLoveInfo.objects.filter(userinfo=request.user, love_type=int(lovetype), love_id=int(loveid))
        if love:
            if love[0].love_status:
                love[0].love_status = False
                love[0].save()
                lover.love_num -= 1
                lover.save()
                return JsonResponse({
                    'status': 'ok',
                    'msg': '收藏'
                })
            else:
                love[0].love_status = True
                love[0].save()
                lover.love_num += 1
                lover.save()
                return JsonResponse({
                    'status': 'ok',
                    'msg': '取消收藏'
                })
        else:
            a = UserLoveInfo()
            a.userinfo = request.user
            a.love_status = True
            a.love_type = int(lovetype)
            a.love_id = int(loveid)
            a.save()
            lover.love_num += 1
            lover.save()
            return JsonResponse({
                'status': 'ok',
                'msg': '取消收藏'
            })
    else:
        return JsonResponse({
            'status': 'fail',
            'msg': '收藏失败'
        })


def user_comment(request):
    user_comment_form = UserCommentFrom(request.POST)
    if user_comment_form.is_valid():
        comment = user_comment_form.cleaned_data['comment']
        courseid = user_comment_form.cleaned_data['courseid']
        a = UserCommentInfo()
        a.userinfo = request.user
        a.courseinfo_id = courseid
        a.comment_content = comment
        a.save()
        return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"status": '评论失败'})


def user_delete_love(request):
    lovetype = request.GET.get('lovetype', '')
    loveid = request.GET.get('loveid', '')
    if loveid and lovetype:
        love = UserLoveInfo.objects.filter(userinfo=request.user, love_type=int(lovetype), love_id=int(loveid))
        if love:
            love[0].love_status = False
            love[0].save()
            return JsonResponse({
                'status':'ok'
            })
        else:
            return JsonResponse({
                'status':'fail',
                'msg':'删除失败'
            })
    else:
        return JsonResponse({
            'status': 'fail',
            'msg': '删除失败'
        })