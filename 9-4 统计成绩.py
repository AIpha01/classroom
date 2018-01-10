# coding: gbk

with open('report.txt','r',encoding='gbk') as f:     #读取成绩
    lines = f.readlines()
    list = []
    for line in lines:
        score = line.split()
        #print('Score:',score)

        sum = 0         
        avg = 0
        for m in score[1:]:
            m = int(m)
            sum += int(m)     #成绩总分
            avg = round(sum/(len(score)-1),2)     #平均分
        #print('Sum:',sum)
        #print('Avg:',avg)
        score.append(sum)
        score.append(avg)
        list.append(score)
    list.sort(key=lambda x:x[-2],reverse=True)     #成绩排名
    #print(list)

    each_avg = []     #每科平均分汇总
    for x in range(1,12):
        sub_sum = 0
        for y in list:
            sub_sum += int(y[x])
            sub_avg = round(sub_sum/len(list),2)
        each_avg.append(sub_avg)
    each_avg.insert(0,'平均')
    list.insert(0, each_avg)
    #print(list)

    for x in list:
        for y in x[1:10]:
            if int(y) < 60:
                 x[x.index(y)] = '不及格'       #替换不及格分数
    #print(list)
                 
    #添加标题
    title = ['名次','姓名','语文', '数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']
    list.insert(0, title)    
    #print(list)

r = 0     #添加名次
for x in list[1:]:
    x.insert(0, r)
    x.append('\n')
    r += 1
#print(list)

with open('new_report.txt', 'w', encoding='gbk') as f:
	for line in list:
		for index in range(len(line)):
			line[index] = str(line[index])
		content = '  '.join(line) + '\n'
		f.writelines(content)
    

    



            
    
    

            
                
                
