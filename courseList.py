import classNode as cn

c3MI3 = cn.Node('compsci', '3MI3')
c4TC3 = cn.Node('compsci', '4TC3', tail=c3MI3)
c3SD3 = cn.Node('compsci', '3SD3')
c3SH3 = cn.Node('compsci', '3SH3', tail=c3SD3)
c4C03 = cn.Node('compsci', '4C03', tail=c3SH3)
c4F03 = cn.Node('compsci', '4F03', tail=c3SH3)
c4WW3 = cn.Node('compsci', '4WW3', tail=c3SH3)

b3BP3 = cn.Node('biochem', '3BP3')
b3SS3 = cn.Node('biology', '3SS3')

m1B03 = cn.Node('math', '1B03')
m2R03 = cn.Node('math', '2R03', tail=m1B03)
m3GR3 = cn.Node('math', '3GR3', tail=m2R03)
m3TP3 = cn.Node('math', '3TP3', everyTerm=False, tail=m2R03)

m2X03 = cn.Node('math', '2X03')
m3DC3 = cn.Node('math', '3DC3', everyTerm=False, tail=m2X03)
m3T03 = cn.Node('math', '3T03', tail=m2X03)

m3QC3 = cn.Node('math', '3QC3', everyTerm=False, tail=m2X03, tail2=m2R03)
m3U03 = cn.Node('math', '3U03', everyTerm=False, tail=m2X03, tail2=m2R03)
m3V03 = cn.Node('math', '3V03', everyTerm=False, tail=m2X03, tail2=m2R03)

m2C03 = cn.Node('math', '2C03', tail=m1B03)
m4MB3 = cn.Node('math', '4MB3', tail=m2C03)

m3MB3 = cn.Node('math', '3MB3', tail=m1B03)

s2D03 = cn.Node('stats', '2D03')
s3D03 = cn.Node('stats', '3D03', tail=s2D03, tail2=m2X03)
s3U03 = cn.Node('stats', '3U03', tail=s2D03, tail2=m2X03, everyTerm=False)
s4CI3 = cn.Node('stats', '4CI3', tail=s3D03, everyTerm=False)
s4P03 = cn.Node('stats', '4P03', tail=s3D03, everyTerm=False)
s4I03 = cn.Node('stats', '4I03', tail=s3D03)

c4TE3 = cn.Node('compsci', '4TE3', tail=m2X03)
c4E03 = cn.Node('compsci', '4E03', tail=s2D03)


CSNodes = [c3MI3, c4TC3, c3SD3, c3SH3, c4C03, c4F03, c4WW3, c4TE3, c4E03, s2D03, m2X03, m3MB3]
print 'CSNodes:' + str(len(CSNodes))
mathNodes = [ m1B03, m2R03, m3GR3, m3TP3, m2X03, m3DC3, m3T03, m3QC3, m3U03, m3V03, m2C03, m4MB3, m3MB3]
print 'mathNodes:' + str(len(mathNodes))
statsNodes = [m3MB3, m2C03, m4MB3, m3MB3, s2D03, s3D03, s3U03, s4CI3, s4P03, s4I03, m2X03]
print 'statsNodes:' + str(len(statsNodes))
statsMath = list(set(mathNodes + statsNodes))
print 'statsMathNodes:' + str(len(statsMath))
mathCS = list(set(mathNodes + CSNodes))
print 'mathCSNodes:' + str(len(mathCS))
statsCS = list(set(statsNodes + CSNodes))
print 'statsCSNodes:' + str(len(statsCS))
mathStatsCS = list(set(mathNodes + statsNodes + CSNodes))
print 'mathStatsCSNodes:' + str(len(mathStatsCS))
finalNodes = [c3MI3, c4TC3, c4TE3, s2D03, m2X03, m3MB3, m3DC3, m3T03, m3QC3, m3U03, m3V03, s3D03, s3U03, s4CI3, s4P03]
courseLists = ['finalNodes'] #['CSNodes', 'mathNodes', 'statsNodes', 'statsMath', 'mathCS', 'statsCS']
