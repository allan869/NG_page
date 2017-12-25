from django.test import TestCase

# Create your tests here.
# a = [{"id": 8, "url": "https://passport.ksyun.com/?callback=https%3A%2F%2Fconsole.ksyun.com%2Findex.html%23!%2Fhome", "image": "/static/images/cloud.png", "name": "金山云控制台", "type": "运维", "mark": 1, "desc": "金山云控制台" },{ "id": 1, "url": "https://passport.ksyun.com/?callback=https%3A%2F%2Fconsole.ksyun.com%2Findex.html%23!%2Fhome", "image": "/static/images/cloud.png", "name": "金山云控制台", "type": "运维", "mark": 1, "desc": "金山云控制台" }, { "id": 2, "url": "http://confluence.cctv.cn", "image": "/static/images/confluence.png", "name": "Confluence", "type": "运维", "mark": 2, "desc": "Confluence" }, { "id": 3, "url": "https://ops.cctv.cn", "image": "/static/images/devops.png", "name": "DevOps", "type": "运维", "mark": 3, "desc": "DevOps" }, { "id": 4, "url": "http://192.168.31.240:8080/ehr/default.aspx?ReturnUrl=%2fehr", "image": "/static/images/ehr.jpeg", "name": "EHR", "type": "人事", "mark": 4, "desc": "EHR" }, { "id": 5, "url": "http://git.cctv.cn/", "image": "/static/images/gitlab.jpeg", "name": "GitLab", "type": "运维", "mark": 5, "desc": "GitLab" }, { "id": 6, "url": "http://jenkins.cctv.cn", "image": "/static/images/jenkin.jpeg", "name": "Jenkins", "type": "运维", "mark": 6, "desc": "Jenkins" }, { "id": 7, "url": "http://jira.cctv.cn/secure/Dashboard.jspa", "image": "/static/images/jira.jpg", "name": "JIRA", "type": "", "mark": 7, "desc": "JIRA" } ]
# b = [1,2,3]
# c = []
#
# # print(list(map(lambda x: a[x-1], b)))
#
# for i in b:
# 	# print('i---->', i)
# 	for k in a:
# 		# print('k--->', k['id'])
# 		if i == k['id']:
# 			c.append(k)
# # for k in a:
# # 	if k not in c:
# # 		c.append(k)
#
#
# print(len(c), c)

a = [ { "id": 2, "url": "http://confluence.cctv.cn", "image": "http://0.0.0.0:8000/static/images/static/images/confluence.png", "name": "Confluence", "type": "运维", "mark": 2, "desc": "Confluence" }, { "id": 3, "url": "https://ops.cctv.cn", "image": "http://0.0.0.0:8000/static/images/static/images/devops.png", "name": "DevOps", "type": "运维", "mark": 3, "desc": "DevOps" }, { "id": 1, "url": "https://passport.ksyun.com/?callback=https%3A%2F%2Fconsole.ksyun.com%2Findex.html%23!%2Fhome", "image": "http://0.0.0.0:8000/static/images/icons/cloud.png", "name": "金山云控制台", "type": "运维", "mark": 1, "desc": "金山云控制台" }, { "id": 4, "url": "http://192.168.31.240:8080/ehr/default.aspx?ReturnUrl=%2fehr", "image": "http://0.0.0.0:8000/static/images/static/images/ehr.jpeg", "name": "EHR", "type": "人事", "mark": 4, "desc": "EHR" }, { "id": 5, "url": "http://git.cctv.cn/", "image": "http://0.0.0.0:8000/static/images/static/images/gitlab.jpeg", "name": "GitLab", "type": "运维", "mark": 5, "desc": "GitLab" }, { "id": 6, "url": "http://jenkins.cctv.cn", "image": "http://0.0.0.0:8000/static/images/icons/jenkin.jpeg", "name": "Jenkins", "type": "运维", "mark": 6, "desc": "Jenkins" }, { "id": 7, "url": "http://jira.cctv.cn/secure/Dashboard.jspa", "image": "http://0.0.0.0:8000/static/images/static/images/jira.jpg", "name": "JIRA", "type": "其他", "mark": 7, "desc": "JIRA" } ]

for i in a:
	print(sorted(i.items(),key=lambda item:item['id']))