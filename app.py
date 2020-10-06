import pandas as pd
a=['vadapav','dabeli','shevpav','biryani','samosa']
p=['TOTAL ORDER']
l=1
dicti={}
k=[dicti]
while(1):
	r=0
	x=input().lower()
	e=x.split(' ')
	if len(e)==1 :
		e.append(1)
		e.append('xyz')
	if len(e)==2 and e[1]!='':
		e.append('xyz')
	else:
		if len(e)==2:
			e[1]='1'
			e.append('xyz')
	if len(e)==3 and e[2]=='':
		e[2]='xyz'
	b=e[0]
	f='+add'
	g='check'
	c=e[1]
	d=e[2]
	if b=='help':
		print('  (foodname amount storename) -- Method to order food')
		print('  (+add foodname )            -- To add any food item ,')
		print('  (check)                     -- To check order ,,')
		print('  (total)                     -- To take total amount')
		print('  (bill)                      -- To take total bill each store separately by entering food values ')
		
	elif b=='bill':
		w=0
		n=0
		v=1
		for j in k:
			if j != dicti:
				w=0
				for x in a:
					if x in j.keys():
						print(x)
						h=int(input())
						w=w+h*int(j[x])
				print(p[v],w)
				v+=1
			n+=w
			if j != dicti:
				print(n)
	elif b not in a and b!=f and b!=g:
		print('not added yet, you can add by entering (+add <NAME OF THE FOOD>)')
		
	elif b==f:
		a.append(c)
		a.sort()
		print('now you can order :',c)
		
	elif b in a:
		print('order placed')
		if b not in dicti.keys():
			dicti[b]=c
			if d not in p:
				p.append(d)
				m=p[l]
				m={}
				m[b]=c
				k.append(m)
				l+=1
			elif d in p:
				s=0
				for i in p:
					if d==i:
						t=k[s]
						t[b]=c
					s+=1
					
		elif b in dicti.keys():
			dicti[b]=int(dicti[b])+int(c)
			if d not in p:
				p.append(d)
				m=p[l]
				m={}
				m[b]=c
				k.append(m)
				l+=1
			elif d in p:
				s=0
				for i in p:
					if d==i:
						t=k[s]
						if b not in t.keys():
							t[b]=c
						else:
							t[b]=int(t[b])+int(c)
					s+=1
					
	elif b==g:
		for o in p:
			for q in range(r,r+1):
				print(o)
				u=k[r]
				#for y in u.keys():
					#z=[]
					#z.append(u[y])
					#u[y]=z
				#table=pd.DataFrame(u)
				print(u)
				r+=1
