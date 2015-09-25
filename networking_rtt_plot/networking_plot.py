import matplotlib.pyplot as plt
# This assignment was to calculate the ratio of actual RTT of a ping
# vs the idealized time based on distance, and to plot them

lightspeed = 299792.457 #km/s
data = {
		"umass.edu (Amherst, MA)":
			{
				"rtt": 94.055, #ms
				"distToBerk": 4200.5 #km
			},
		"ucsd.edu (San Diego, CA)": 
			{
				"rtt": 16.687,
				"distToBerk": 735.5
			},
		"utexas.edu (San Antonio, TX)":
			{
				"rtt": 63.747,
				"distToBerk": 2383.8
			},
		"columbia.edu (New York, NY)":
			{
				"rtt": 107.643,
				"distToBerk": 4114.1
			},
		"www.ed.ac.uk (Edinburgh, Scotland)":
			{
				"rtt": 183.955,
				"distToBerk": 8108.7
			},
		"www.tsinghua.edu.cn (Beijing, China)":
			{
				"rtt": 159.239,
				"distToBerk": 9503.2
			},
		"hi.is (Reykjavik, Iceland)":
			{
				"rtt": 328.845,
				"distToBerk": 6738.8
			},
		"lu.lv (Riga, Latvia)":
			{
				"rtt": 332.625,
				"distToBerk": 9008.6
			},
		"aalto.fi (Helsinki, Finland)":
			{
				"rtt": 181.372,
				"distToBerk": 8707.6
			},
	}
	
rtt_time = [data[x]["rtt"] for x in data]
distances = [data[x]["distToBerk"] for x in data]
labels = [x for x in data]
ratios = [rtt/(2 * (d / lightspeed) * 1000) for rtt,d in zip(rtt_time, distances)]


plt.plot(distances, ratios, 'ro')
plt.axis([0, 10000, 0, 5])
plt.title("RTT Ratio vs Distance")
plt.xlabel("Distance from Berkeley (km)")
plt.ylabel("Ratio of RTT to 2T")
plt.show()