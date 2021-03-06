
%reset
%matplotlib

#-----simulation parameters-------
popsize = 1000
chrlen = 1000000
ratevec = .01
tstart = 5
dmipos = (.3,.7)
seldmi = 0
selanc = 0
domdmi = 2
#---------------------------------
ratevec = [.01,.05,.1]
markers = 1000
npts = 20
maxlen = 1
pop = 1
Ls = [1]
migscheme = 'source'  #'source' or 'hybrid'

exec(open("/home/joelsmith/Projects/dmis/dmitracts/forqs_tractlengths.py").read())
exec(open("/home/joelsmith/Projects/dmis/dmitracts/dfuse_tractlengths.py").read())

print_fitness_matrix(seldmi,selanc,domdmi)

#-----------forqs neutral tract length distributions-------------------
run_forqs(ratevec, tstart, popsize, chrlen, migscheme)
get_forqs_tracts(ratevec, chrlen, maxlen, npts, migscheme)
plot_figure_forqs(ratevec, tstart, Ls, pop, maxlen, npts, migscheme)

#-----------dfuse neutral tract length distributions-------------------
run_dfuse(ratevec, tstart, popsize, markers)
get_dfuse_tracts(ratevec,npts,maxlen,chrlen)
plot_figure_dfuse(ratevec, tstart, Ls, pop, maxlen, npts, chrlen)
plot_image_dfuse(ratevec)

#-------------Locus-specific tract length distributions-----------
plot_locus_tractlengths(ratevec,tstart,Ls,pop,maxlen,npts,chrlen)

#----------------DMI tract length distributions-------------------
run_dfuse_dmis(rate, tstart, popsize, markers, dmipos, seldmi, selanc, domdmi)
get_dfuse_tracts_dmis(rate, npts, maxlen, chrlen, dmipos)
plot_figure_dfuse_dmis(rate, tstart, Ls, pop, maxlen, npts, chrlen)
plot_image_dfuse_dmis(rate)
