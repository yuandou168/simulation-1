In this folder are four different implementations of the IC-PCP algorithm, see    
'Deadline-constrained workflow scheduling algorithms for infrastructure as a service clouds',  
S. Abrishami, M. Naghibzadeh, D. H. Epema,  
Future Generation Computer Systems 29 (1) (2013) 158–169.

The four different implementations are:  
PCP_org_v0.py: greedy implementation of the IC-PCP algorithm  
PCP_org_v1.py: more stringent implementation of the IC-PCP algorithm  
PCP_org_v01.py: greedy implementation of the IC-PCP algorithm with final repair cycle  
PCP_org_v11.py: more stringent implementation of the IC-PCP algorithm  with final repair cycle

These four implementations and their performance is described in the paper:  
'Profiling the scheduling decisions for handling critical paths in deadline-constrained cloud workflows'  
Arie Taal, Junchao Wang, Cees de Laat, Zhiming Zhao  
Submitted to Future Generation Computer Systems.

The python code perf_all.py can be used to test the performance of these implementations as
described in the file 'Performance_HowTo.txt'.

The zip archive 'input.zip' contains the different workflow topologies used in the
submitted paper.

The excel sheet 'ICPCP_performance.xlsx' contains all performance data with the figures presented in the submitted paper.
