#!/usr/bin/env python
# encoding: utf-8
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import get_object_or_404
from data.models import u,m,re,nr
import urllib2
import json

def index(request):
    t = get_template("index.html")
    c = Context({'is_index': '1'})
    html = t.render(c)
    return HttpResponse(html)

def search(request, query):
    API_KEY = '0385334896d5f9120a8f99d9c481eb36'
    base_u = 'https://api.douban.com/v2/user/'
    u_db = get_object_or_404(u, uid=query)
    ud = {}
    headers ={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36',
            'Host': 'api.douban.com',
            'Connection': 'keep-alive',
            }
    u_url = "%s%s?apikey=%s" % (base_u, query, API_KEY)
    req = urllib2.Request(u_url, headers=headers)
    data = json.loads(urllib2.urlopen(req).read())
    ud['name'] = data['name']
    ud['signi'] = data['signature']
    ud['avatar'] = data['avatar']
    r = re.objects.filter(uid=query)
    n = nr.objects.filter(uid=query)
    rex = len(r)
    rcount = 0
    ncount = 0
    ra = "0%"
    na = "0%"
    if rex > 0:
        ra = str((r[0].arating-0.7)*20)+"%"
        r = r[0].recommend.split('|')
        rcount = len(r)
    else:
        r = []
    nex = len(n)
    if nex > 0:
        na = str((5-n[0].arating)*20)+"%"
        n = n[0].recommend.split('|')
        ncount = len(n)
    else:
        n = []
    rlist = []
    nlist = []
    base_m = 'http://api.douban.com/v2/movie/subject/'
    for i in r:
        m_url = "%s%s?apikey=%s" % (base_m, i, API_KEY)
        mdata = {}
        mob = m.objects.filter(mid=i)
        if len(mob) is 0:
            mreq = urllib2.Request(m_url, headers=headers)
            mdata = json.loads(urllib2.urlopen(mreq).read())
            rlist.append({
            'id': i,
            'name': mdata['title'],
            'year': mdata['year'],
            'poster': mdata['images']['medium'],
            })
        else:
            rlist.append({
            'id': i,
            'name': mob[0].name,
            'year': mob[0].year,
            'poster': 'http://cineaste-posters.stor.sinaapp.com/'+i+'.jpg',
            })
    for i in n:
        m_url = "%s%s?apikey=%s" % (base_m, i, API_KEY)
        mdata = {}
        mob = m.objects.filter(mid=i)
        if len(mob) is 0:
            mreq = urllib2.Request(m_url, headers=headers)
            mdata = json.loads(urllib2.urlopen(mreq).read())
            nlist.append({
            'id': i,
            'name': mdata['title'],
            'year': mdata['year'],
            'poster': mdata['images']['medium'],
            })
        else:
            nlist.append({
            'id': i,
            'name': mob[0].name,
            'year': mob[0].year,
            'poster': 'http://cineaste-posters.stor.sinaapp.com/'+i+'.jpg',
            })
    t = get_template("search.html")
    c = Context({
        'u': ud,
        'rcount': rcount,
        'rlist': rlist,
        'ncount': ncount,
        'nlist': nlist,
        'ra': ra,
        'na': na,
        })
    html = t.render(c)
    return HttpResponse(html)
