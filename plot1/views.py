#-*- coding:utf-8 -*-

from django.shortcuts import render,get_object_or_404

from static.js import 

def plot(request):

	#GET Title ?
	graph_data =[[1, 2],[3,5.12],[5,13.1],[7,33.6],[9,85.9],[11,219.9]]
	return render (request, 'plot1/plot_page.html', "graph_data" = graph_data)

