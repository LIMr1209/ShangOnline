from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import UserRegisterForm, UserLoginForm, UserForgetForm, UserResetForm, UserChangeImageForm, \
    UserChangeInfoForm, UserChangePasswordForm, UserSendCodeForm, UserChangeEmailForm
from .models import UserProfile, EmailVerify
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from utils.send_main_tool import send_email_verify
from django.http import JsonResponse
from datetime import datetime
from operations.models import UserCourseInfo, UserLoveInfo, UserMessageInfo
from orgs.models import OrgInfo, TeacherInfo
from courses.models import CourseInfo
from .models import Banner
from django.views import View


# Create your views here.
class IndexView(View):
    def get(self, request):
        all_banners = Banner.objects.all().order_by('-add_time')[:5]
        all_bannercourses = CourseInfo.objects.filter(is_banner=True).order_by('-click_num')[:3]
        all_courses = CourseInfo.objects.filter(is_banner=False).order_by('-add_time')[:6]
        all_orgs = OrgInfo.objects.all().order_by('-click_num')[:15]
        return render(request, 'index.html', {
            'all_banners': all_banners,
            'all_bannercourses': all_bannercourses,
            'all_courses': all_courses,
            'all_orgs': all_orgs
        })


def user_register(request):
    if request.method == 'GET':
        user_register_form = UserRegisterForm()
        return render(request, 'users/register.html', {
            'user_register_form': user_register_form
        })
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']
            user = UserProfile.objects.filter(Q(username=email) | Q(email=email))
            if user:
                return render(request, 'users/register.html', {
                    'msg': '用户名已存在',
                    'user_register_form': user_register_form
                })
            else:
                user = UserProfile()
                user.email = email
                user.set_password(password)
                user.username = email
                user.save()
                # 注册成功，存储消息
                msg = UserMessageInfo()
                msg.message = '欢迎注册尚在线'
                msg.userinfo = user.id
                msg.save()
                send_email_verify(email, 'register')
                return HttpResponse('激活链接以发到你的邮箱，请你前去激活')
        else:
            return render(request, 'users/register.html', {
                'user_register_form': user_register_form
            })


def user_login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            email = user_login_form.cleaned_data['email']
            password = user_login_form.cleaned_data['password']
            # authenticate只验证username和password ，不能用Q，且django1.11 版本，自动验证is_alive 子段，如果为0，则
            # 用户名密码正确也会返回None
            a = authenticate(username=email, password=password)
            if a:
                if a.is_start:
                    login(request, a)
                    msg = UserMessageInfo()
                    msg.userinfo = a.id
                    msg.message = '欢迎登录尚在线'
                    msg.save()
                    url = request.COOKIES.get("url", "/")
                    ret = redirect(url)
                    ret.delete_cookie('url')
                    return ret
                    # return redirect(reverse('index'))
                else:
                    return HttpResponse('请先激活')
            else:
                return render(request, 'users/login.html', {
                    'msg': '用户名或密码错误'
                })
        else:
            return render(request, 'users/login.html', {
                'user_login_form': user_login_form
            })


def user_active(request, code):
    if code:
        email_ver = EmailVerify.objects.filter(code=code)[0]
        if email_ver:
            email = email_ver.email
            user = UserProfile.objects.filter(email=email)[0]
            user.is_start = True
            user.save()
            msg = UserMessageInfo()
            msg.userinfo = user.id
            msg.message = '激活成功'
            msg.save()
            return redirect(reverse('users:user_login'))
        else:
            return HttpResponse('验证码错误,激活失败')


def user_logout(request):
    logout(request)
    return redirect(reverse('index'))


def user_forget(request):
    if request.method == 'GET':
        user_forget_form = UserForgetForm()
        return render(request, 'users/forgetpwd.html', {
            'user_forget_form': user_forget_form
        })
    else:
        user_forget_form = UserForgetForm(request.POST)
        if user_forget_form.is_valid():
            email = user_forget_form.cleaned_data['email']
            user = UserProfile.objects.filter(Q(email=email) | Q(username=email))
            if user:
                send_email_verify(email, 'forget')
                return HttpResponse('链接已发到你的邮箱，请您前去重置密码')
            else:
                return render(request, 'users/forgetpwd.html', {
                    'msg': '该邮箱不存在',
                    'user_forget_form': user_forget_form
                })
        else:
            return render(request, 'users/forgetpwd.html', {
                'user_forget_form': user_forget_form
            })


def user_reset(request, code):
    if request.method == 'GET':
        if code:
            email_ver = EmailVerify.objects.filter(code=code)[0]
            email = email_ver.email
            user = UserProfile.objects.filter(email=email)[0]
            return render(request, 'users/password_reset.html', {
                'user_id': user.id,
            })
        else:
            pass
    else:
        user_reset_form = UserResetForm(request.POST)
        if user_reset_form.is_valid():
            password = user_reset_form.cleaned_data['password']
            password1 = user_reset_form.cleaned_data['password1']
            if code:
                user = UserProfile.objects.filter(id=int(code))
                if user:
                    if password == password1:
                        user[0].set_password(password)
                        user[0].save()
                        msg = UserMessageInfo()
                        msg.userinfo = user[0].id
                        msg.message = '找回密码成功'
                        msg.save()
                        return redirect(reverse('users:user_login'))
                    else:
                        return render(request, 'users/password_reset.html', {
                            'msg': '两次密码输入不一致'
                        })
                else:
                    pass
            else:
                pass
        else:
            return render(request, 'users/password_reset.html', {
                'user_reset_form': user_reset_form
            })


def user_info(request):
    return render(request, 'users/usercenter-info.html')


def user_change_image(request):
    # 当使用modleform验证时,仅验证字段少时，需要指定 instance =   ,文件类型的指定 request.FILES
    user_change_image_form = UserChangeImageForm(request.POST, request.FILES, instance=request.user)
    if user_change_image_form.is_valid():
        user_change_image_form.save(commit=True)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({"status": 'fail'})


def user_change_info(request):
    user_change_info_form = UserChangeInfoForm(request.POST, instance=request.user)
    if user_change_info_form.is_valid():
        user_change_info_form.save(commit=True)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({"status": 'fail', "msg": '修改失败'})


def user_change_password(request):
    user_change_password_form = UserChangePasswordForm(request.POST)
    if user_change_password_form.is_valid():
        password1 = user_change_password_form.cleaned_data['password1']
        password2 = user_change_password_form.cleaned_data['password2']
        if password1 == password2:
            user = authenticate(username=request.user.username, password=password1)
            if user:
                return JsonResponse({
                    'status': 'fail',
                    'msg': '修改失败，与原密码相同，请重新填写'
                })
            else:
                request.user.set_password(password1)
                request.user.save()
                return JsonResponse({
                    'status': 'ok',
                    'msg': '修改成功，请重新登录'
                })
        else:
            return JsonResponse({
                'status': 'fail',
                'msg': '修改失败，两次输入密码不一致，请重新填写'
            })
    else:
        return JsonResponse({
            'status': 'fail',
            'msg': '修改失败，请重新填写'
        })


def user_send_code(request):
    user_send_code_form = UserSendCodeForm(request.POST)
    if user_send_code_form.is_valid():
        email = user_send_code_form.cleaned_data['email']
        user = UserProfile.objects.filter(Q(email=email) | Q(username=email))
        if user:
            return JsonResponse({
                'status': 'fail',
                'msg': '邮箱已经被把绑定'
            })
        else:
            email_ver = EmailVerify.objects.filter(email=email, send_type='change_email').order_by('-add_time')
            if email_ver:
                if (datetime.now() - email_ver[0].add_time).seconds < 120:
                    return JsonResponse({
                        'status': 'ok',
                        'msg': '邮箱验证码已发送过'
                    })
            send_email_verify(email, 'change_email')
            return JsonResponse({
                'status': 'ok',
                'msg': '邮箱验证码已发送到您的邮箱'
            })
    else:
        return JsonResponse({
            'status': 'fail',
            'msg': '邮箱不合法'
        })


def user_change_email(request):
    user_change_email_form = UserChangeEmailForm(request.POST)
    if user_change_email_form.is_valid():
        email = user_change_email_form.cleaned_data['email']
        code = user_change_email_form.cleaned_data['code']
        email_code = EmailVerify.objects.filter(email=email, code=code, send_type='change_email')
        if email_code:
            request.user.username = email
            request.user.email = email
            request.user.save()
            return JsonResponse({
                'status': 'ok',
                'msg': '修改成功'
            })
        else:
            return JsonResponse({
                'status': 'fail',
                'msg': '修改失败，验证码错误'
            })
    else:
        return JsonResponse({
            'status': 'fail',
            'msg': '修改失败，验证码错误'
        })


def user_mycourse(request):
    usercourse_list = UserCourseInfo.objects.filter(userinfo=request.user)
    all_courses = [item.courseinfo for item in usercourse_list]
    return render(request, 'users/usercenter-mycourse.html', {
        'all_courses': all_courses
    })


def user_loveorg(request):
    userorg_list = UserLoveInfo.objects.filter(userinfo=request.user, love_type=1, love_status=True)
    all_orgs_id = [item.love_id for item in userorg_list]
    all_orgs = OrgInfo.objects.filter(id__in=all_orgs_id)
    return render(request, 'users/usercenter-fav-org.html', {
        'all_orgs': all_orgs
    })


def user_loveteacher(request):
    userorg_list = UserLoveInfo.objects.filter(userinfo=request.user, love_type=3, love_status=True)
    all_teachers_id = [item.love_id for item in userorg_list]
    all_teachers = TeacherInfo.objects.filter(id__in=all_teachers_id)
    return render(request, 'users/usercenter-fav-teacher.html', {
        'all_teachers': all_teachers
    })


def user_lovecourse(request):
    usercoure_list = UserLoveInfo.objects.filter(userinfo=request.user, love_type=2, love_status=True)
    all_courses_id = [item.love_id for item in usercoure_list]
    all_courses = CourseInfo.objects.filter(id__in=all_courses_id)
    return render(request, 'users/usercenter-fav-course.html', {
        'all_courses': all_courses
    })


def user_message(request):
    all_messages = UserMessageInfo.objects.filter(userinfo=request.user.id)
    return render(request, 'users/usercenter-message.html', {
        'all_messages': all_messages
    })


def user_readmsg(request):
    msgid = request.GET.get('msgid', '')
    if msgid:
        msg = UserMessageInfo.objects.filter(id=int(msgid))[0]
        msg.msg_status = True
        msg.save()
        return JsonResponse({
            'status': 'ok'
        })
    else:
        return JsonResponse({
            'status': 'fail',
            'msg': '读取消息失败'
        })


def handler_404(request):
    ret = render(request, '404.html')
    ret.status_code = 404
    return ret


def handler_500(request):
    ret = render(request, '500.html')
    ret.status_code = 500
    return ret


def handler_403(request):
    ret = render(request, '403.html')
    ret.status_code = 403
    return ret
