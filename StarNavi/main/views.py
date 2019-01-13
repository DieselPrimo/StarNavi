import json

import jwt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import User, Post


@api_view(["POST"])
def signup(request):
    body = json.loads(request.body.decode('utf-8'))
    user = User(name=body["name"], login=body["login"], password=body["password"], email=body["email"])
    if User.objects.filter(login=body['login']).exists():
        return Response(data={
            "message": "user exist"
        }, status=status.HTTP_409_CONFLICT)
    else:
        user.save()
        tk = jwt.encode({"username": body['login'], "password": body['password']}, 'SECRET', algorithm='HS256')
        return Response(data={
            "token": tk
        }, status=status.HTTP_200_OK)


@api_view(["POST"])
def login(request):
    body = json.loads(request.body.decode('utf-8'))
    try:
        res = jwt.decode(body['token'], 'SECRET', algorithm='HS256')
    except:
        return Response(data={
            "message": "no such token"
        }, status=status.HTTP_400_BAD_REQUEST)
    return Response(data=res, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_post(request):
    body = json.loads(request.body.decode('utf-8'))
    try:
        res = jwt.decode(body['token'], 'SECRET', algorithm='HS256')
    except:
        return Response(data={
            "message": "no such token"
        }, status=status.HTTP_400_BAD_REQUEST)
    try:
        user_id = User.objects.get(login=res.get('username')).id
        post = Post(user_id=user_id, title=body['title'], content=body['content'])
        post.save()
    except:
        return Response(data={
            "message": "error"
        }, status=status.HTTP_400_BAD_REQUEST)
    return Response(data="Created", status=status.HTTP_200_OK)


@api_view(["POST"])
def like(request):
    body = json.loads(request.body.decode('utf-8'))
    try:
        post = Post.objects.get(id=body['post_id'])
        post.like = True
        post.save()
    except:
        return Response(data={
            "message": "error"
        }, status=status.HTTP_400_BAD_REQUEST)
    return Response(data="OK", status=status.HTTP_200_OK)

@api_view(["POST"])
def unlike(request):
    body = json.loads(request.body.decode('utf-8'))
    try:
        post = Post.objects.get(id=body['post_id'])
        post.like = False
        post.save()
    except:
        return Response(data={
            "message": "error"
        }, status=status.HTTP_400_BAD_REQUEST)
    return Response(data="OK", status=status.HTTP_200_OK)
