import os
newversion=os.environ['METALLBVERSION']
deplin=open('./dev/deployment.yaml','r')

#lines=deplin.readlines()
newcontent=""
for line in deplin:
    line=line.strip('\n')
    tline=line
    tline=tline.strip()
    if(tline.startswith('image')):
        tarr=tline.split(':')
        oldversion=tarr[-1]
        line=line.replace(oldversion,newversion)
    newcontent+=line+"\n"
#print(oldversion)
deplin.close()
deplout=open('./dev/deployment.yaml','w')
deplout.write(newcontent)
deplout.close()
    
