from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from CoreBanking.models import Member, Center
from CoreBanking.serializers import LoginSerializer, CenterCreationSerializer, BankManagerCreateUserSerializer, \
    CenterManagerCreateUserSerializer


class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login_page.html'

    def get(self, request):
        serializer = LoginSerializer
        return Response({'serializer': serializer})


class UserPanelView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                return Response(template_name='wrong_password_username_error.html')

            query = Member.objects.filter(user=user)
            member = query[0]
            if (member.membership_type == "head_manager"):
                return Response({'member': member},
                                template_name='head_manager_panel_page.html')
            if (member.membership_type == "bank_manager"):
                return Response({'member': member},
                                template_name='bank_manager_panel_page.html')

            if (member.membership_type == "legal_expert"):
                return Response({'member': member},
                                template_name='legal_expert_panel_page.html')
            if (member.membership_type == "center_manager"):
                return Response({'member': member},
                                template_name='center_manager_panel_page.html')
            if (member.membership_type == "cashier"):
                return Response({'member': member},
                                template_name='cashier_panel_page.html')
            if (member.member_ship_type == "auditor"):
                return Response({'member': member},
                                template_name='auditor_panel_page.html')
            if (member.membership_type == "accountant"):
                return Response({'member': member},
                                template_name='accountant_panel_page.html')
            if (member.membership_type == "atm_clerk"):
                return Response({'member': member},
                                template_name='atm_clerk_panel_page.html')
            return Response(template_name='not_defined_membership_type.html')
        else:
            return Response(serializers.errors)

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            query = Member.objects.filter(user=user)
            member = query[0]
        else:
            return Response(template_name="authorization_error_page.html")

        if (member.membership_type == "head_manager"):
            return Response({'member': member},
                            template_name='head_manager_panel_page.html')
        if (member.membership_type == "bank_manager"):
            return Response({'member': member},
                            template_name='bank_manager_panel_page.html')

        if (member.membership_type == "legal_expert"):
            return Response({'member': member},
                            template_name='legal_expert_panel_page.html')
        if (member.membership_type == "center_manager"):
            return Response({'member': member},
                            template_name='center_manager_panel_page.html')
        if (member.membership_type == "cashier"):
            return Response({'member': member},
                            template_name='cashier_panel_page.html')
        if (member.membership_type == "auditor"):
            return Response({'member': member},
                            template_name='auditor_panel_page.html')
        if (member.membership_type == "accountant"):
            return Response({'member': member},
                            template_name='accountant_panel_page.html')
        if (member.membership_type == "atm_clerk"):
            return Response({'member': member},
                            template_name='atm_clerk_panel_page.html')
        return Response(template_name='not_defined_membership_type.html')


class CreateCenterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            query = Member.objects.filter(user=user)
            member = query[0]
        else:
            return Response(template_name="authorization_error_page.html")

        if (member.membership_type == "head_manager"):
            serializer = CenterCreationSerializer
            return Response({'serializer': serializer}, template_name='center_create.html')
        else:
            return Response(template_name='head_manager_only.html')

    def post(self, request, format=None):
        serializer = CenterCreationSerializer(data=request.data)
        if serializer.is_valid():
            center_id = int(request.data['center_id'])
            name = request.data['name']
            address = request.data['address']
            if Center.objects.filter(center_id=center_id, name=name).count() > 0:
                return Response(template_name='center_is_defined_before.html')
            else:
                center = Center.objects.create(center_id=center_id,
                                               name=name,
                                               address=address, )
                return Response({'center': center}, template_name='center_creation_done.html')
        else:
            return Response(serializers.errors)


class CenterListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            query = Member.objects.filter(user=user)
            member = query[0]
        else:
            return Response(template_name="authorization_error_page.html")

        if (member.membership_type == "head_manager"):
            centers = Center.objects.all()
            return Response({'centers': centers}, template_name='centers_list.html')
        else:
            return Response(template_name='head_manager_only.html')


class CenterDeleteView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    print('state 1')

    @staticmethod
    def get(request):
        return Response(template_name='use_pannel.html')

    print("state 2")

    @staticmethod
    def post(request, pk):
        print('state 3')
        centers = Center.objects.filter(pk=pk)
        center = centers[0]
        center.delete()
        return Response(template_name='center_deleted.html')


class CreateUserView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            query = Member.objects.filter(user=user)
            member = query[0]
        else:
            return Response(template_name="authorization_error_page.html")

        if (member.membership_type == "head_manager"):
            serializer = BankManagerCreateUserSerializer
            centers = Center.objects.all()
            print(serializer)
            return Response({'serializer': serializer, 'centers': centers},
                            template_name='head_manager_create_user.html')

        if (member.membership_type == "center_manager"):
            serializer = CenterManagerCreateUserSerializer
            print(serializer)
            return Response({'serializer': serializer},
                            template_name='center_manager_create_user.html')

        return Response(template_name='not_defined_membership_type.html')

    def post(self, request, format=None):
        center_name = request.data['center']

        melli_code = int(request.data['melli_code'])
        username = request.data['username']
        password = request.data['password']
        membership_type = request.data['membership_type']

        if Center.objects.filter(name=center_name).count() > 0:
            query = Center.objects.filter(name=center_name)
            center = query[0]
        else:
            return Response(template_name='not_defined_center.html')

        if User.objects.filter(username=username).count() > 0:
            return Response(template_name='taken_user.html')
        if Member.objects.filter(melli_code=melli_code).count() > 0:
            return Response(template_name='taken_melli_code.html')
        if membership_type == 'center_manager' and Member.objects.filter(membership_type='center_manager',
                                                                         center=center):
            return Response(template_name='center_has_manager.html')
        user = User.objects.create(username=username, password=password)
        member = Member.objects.create(melli_code=melli_code,
                                       user=user,
                                       center=center,
                                       membership_type=membership_type)

        return Response({'member': member}, template_name='head_manager_user_creation_done.html')


class UserListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            query = Member.objects.filter(user=user)
            member = query[0]
        else:
            return Response(template_name="authorization_error_page.html")

        if (member.membership_type == "head_manager"):
            members = Member.objects.all()
            return Response({'members': members}, template_name='user_list.html')
        else:
            return Response(template_name='head_manager_only.html')

class CreateAccountView(APIView):
    pass
