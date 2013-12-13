#!/bin/python
# This file is used to generate the "out/static/js/cloud_ec2.js" file used the get-fedora-options#cloud tab
# You should only edit
# - the bellow dictionnary containing the AMI ID (get them on the wiki)
# - the python list ec2_fXX_regions
# - the template call at the end of file near "noscript" and "if JS enabled" (data/template/)

import os

OUTPUT = 'out/static/js/cloud_ec2.js'

# Returns a sorted list of unique available regions from the array
def sorted_region(arr):
	list = []
	for i in arr:
		list.append(i['region'])
	return(sorted(set(list), key=lambda  item: (int(item.partition(' ')[0]) if item[0].isdigit() else float('inf'), item)))

# Generated using the following:
# :%s#^| \([a-zA-Z*-9]*\)[ |]*\(i386\|x86_64\)[ |]*\(EBS-backed\)[ |]* \(ami.*\)#{'region':'\1', 'arch':'\2', 'store':'\3', 'id':'\4'},#g

# Get the list at: https://dl.fedoraproject.org/pub/alt/stage/20-Beta-RC2/Images/x86_64/
ec2_f20_Beta = [
			{'region':'US East (Northern Virginia)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-2f421946'},
			{'region':'US East (Northern Virginia)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-8b4219e2'},
			{'region':'Asia Pacific (Singapore)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-0ab2e758'},
			{'region':'Asia Pacific (Singapore)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-0eb2e75c'},
			{'region':'Asia Pacific (Sydney)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-e163ffdb'},
			{'region':'Asia Pacific (Sydney)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-db63ffe1'},
			{'region':'Asia Pacific (Tokyo)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-dd5135dc'},
			{'region':'Asia Pacific (Tokyo)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-e15135e0'},
			{'region':'US West (Northern California)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-56d0e613'},
			{'region':'US West (Northern California)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-00d0e645'},
			{'region':'US West (Oregon)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-5cca516c'},
			{'region':'US West (Oregon)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-48ca5178'},
			{'region':'EU (Ireland)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-ad7b99da'},
			{'region':'EU (Ireland)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-897b99fe'},
			{'region':'South America (Sao Paulo)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-4d5cfa50'},
			{'region':'South America (Sao Paulo)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-4b5cfa56'}
]

ec2_f20 = [
			{'region':'Asia Pacific (Tokyo)', 'arch':'i386',   'store':'EBS-backed', 'id':'ami-51bc3550'},
			{'region':'Asia Pacific (Tokyo)', 'arch':'x86_64', 'store':'EBS-backed', 'id':'ami-33b23b32'},
			{'region':'Asia Pacific (Singapore)', 'arch':'i386',   'store':'EBS-backed', 'id':'ami-f8357baa'},
			{'region':'Asia Pacific (Singapore)', 'arch':'x86_64', 'store':'EBS-backed', 'id':'ami-4c327c1e'},
			{'region':'Asia Pacific (Sydney)', 'arch':'i386',   'store':'EBS-backed', 'id':'ami-f5d340cf'},
			{'region':'Asia Pacific (Sydney)', 'arch':'x86_64', 'store':'EBS-backed', 'id':'ami-33d24109'},
			{'region':'EU (Ireland)',      'arch':'i386',   'store':'EBS-backed', 'id':'ami-2d819059'},
			{'region':'EU (Ireland)',      'arch':'x86_64', 'store':'EBS-backed', 'id':'ami-43809137'},
			{'region':'South America (Sao Paulo)',      'arch':'i386',   'store':'EBS-backed', 'id':'ami-d2e84dcf'},
			{'region':'South America (Sao Paulo)',      'arch':'x86_64', 'store':'EBS-backed', 'id':'ami-08eb4e15'},
			{'region':'US East (Northern Virginia)',      'arch':'i386',   'store':'EBS-backed', 'id':'ami-6f640c06'},
			{'region':'US East (Northern Virginia)',      'arch':'x86_64', 'store':'EBS-backed', 'id':'ami-b71078de'},
			{'region':'US West (Northern California)',      'arch':'i386',   'store':'EBS-backed', 'id':'ami-634f6126'},
			{'region':'US West (Northern California)',      'arch':'x86_64', 'store':'EBS-backed', 'id':'ami-674f6122'},
			{'region':'US West (Oregon)',      'arch':'i386',   'store':'EBS-backed', 'id':'ami-67930257'},
			{'region':'US West (Oregon)',      'arch':'x86_64', 'store':'EBS-backed', 'id':'ami-fd9302cd'}
]

ec2_f19 = [
			{'region':'Asia Pacific (Singapore)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-da450c88'},
			{'region':'Asia Pacific (Singapore)', 'arch':'i386',   'store':'EBS-Backed', 'id':'ami-fe450cac'},
			{'region':'Asia Pacific (Sydney)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-5565f66f'},
			{'region':'Asia Pacific (Sydney)', 'arch':'i386',   'store':'EBS-Backed', 'id':'ami-bb65f681'},
			{'region':'Asia Pacific (Tokyo)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-95b52094'},
			{'region':'Asia Pacific (Tokyo)', 'arch':'i386',   'store':'EBS-Backed', 'id':'ami-abb520aa'},
			{'region':'US East (Northern Virginia)',      'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-b22e5cdb'},
			{'region':'US East (Northern Virginia)',      'arch':'i386',   'store':'EBS-Backed', 'id':'ami-182f5d71'},
			{'region':'US West (Northern California)',      'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-10cce555'},
			{'region':'US West (Northern California)',      'arch':'i386',   'store':'EBS-Backed', 'id':'ami-50cce515'},
			{'region':'US West (Oregon)',      'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-9727b7a7'},
			{'region':'US West (Oregon)',      'arch':'i386',   'store':'EBS-Backed', 'id':'ami-c327b7f3'},
			{'region':'EU (Ireland)',      'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-f1031e85'},
			{'region':'EU (Ireland)',      'arch':'i386',   'store':'EBS-Backed', 'id':'ami-9f031eeb'},
			{'region':'South America (Sao Paulo)',      'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-b055f0ad'},
			{'region':'South America (Sao Paulo)',      'arch':'i386',   'store':'EBS-Backed', 'id':'ami-a255f0bf'}
]

# The idea is to get something similar to http://jsfiddle.net/shaiton/wChSv/5/
# But we have to generate it in order to have to maintain only one list of AMI ID
# Simply read the output at "out/static/js/cloud_ec2.js"
def gen_js(*args):
	js="// File generated from cloud-tab.html.\n"
	js+="addEventListener('DOMContentLoaded', function(){\n"

	for release in args:
		js+="\tvar element = document.getElementById('cloud_options_" + release[0] + "');\n"
		js+="\tif (element != null)\n"
		js+="\t\telement.style.visibility='visible';\n"
		js+="\telement = document.getElementById('amihref_" + release[0] + "');\n"
		js+="\tif (element != null)\n"
		js+="\t\telement.style.visibility='hidden';\n"
	js+="});\n"

	js+="\nfunction getval() {\n"
	js+="\t// We get the number of regions, and define a two dimensional array (region,arch) to store the AMI ID\n"
	js+="\t// We limit to i > 1 as we don't need the first null entry'\n"
	js+="\t// For each release providen. '\n"
	js+="\tvar region_name = {\n"
 	js+="\t  'Asia Pacific (Tokyo)': 'ap-northeast-1',\n"
	js+="\t  'Asia Pacific (Singapore)': 'ap-southeast-1',\n"
	js+="\t  'Asia Pacific (Sydney)': 'ap-southeast-2',\n"
	js+="\t  'EU (Ireland)': 'eu-west-1',\n"
	js+="\t  'South America (Sao Paulo)': 'sa-east-1',\n"
	js+="\t  'US East (Northern Virginia)': 'us-east-1',\n"
	js+="\t  'US West (Northern California)': 'us-west-1',\n"
	js+="\t  'US West (Oregon)': 'us-west-2'\n"
	js+="\t}\n"
	for release in args:
		js+="\n\tvar form_" + release[0] + " = document.forms['cloud_options_" + release[0] + "'];\n"
		js+="\n\tvar is_form_" + release[0] + " = typeof form_" + release[0] + ";\n"
		js+="\tif (is_form_" + release[0] + " != 'undefined' && form_" + release[0] + ".region_" + release[0] + ".value != 'null') {\n"
		js+="\t\tfor (var i = form_" + release[0] + ".region_" + release[0] + ".options.length, id_" + release[0] + " = new Array(form_" + release[0] + ".region_" + release[0] + ".options.length); i > 1; i--)\n"
		js+="\t\t\tid_" + release[0] + "[form_" + release[0] + ".region_" + release[0] + ".options[i - 1].value] = new Array(2);\n\n"

		for img in release[1]:
			js+="\t\tid_" + release[0] + "['" + img['region'] + "']['" + img['arch'] + "'] = '" + img['id'] + "';\n"
		js+="\t}\n"
	for release in args:
		js+="\n\tif (is_form_" + release[0] + " != 'undefined') {\n"
		js+="\n\t\tif (form_" + release[0] + ".region_" + release[0] + ".value != 'null') {\n"
		js+="\t\t\tvar ami_id = id_" + release[0] + "[form_" + release[0] + ".region_" + release[0] + ".value][form_" + release[0] + ".arch_" + release[0] + ".value];\n"
		js+="\t\t\tvar url = 'https://console.aws.amazon.com/ec2/v2/home?region=' + region_name[form_" + release[0] + ".region_" + release[0] + ".value] + '#LaunchInstanceWizard:ami=' + ami_id;\n"
		js+="\t\t\tdocument.getElementById('amihref_" + release[0] + "').href = url;\n"
		js+="\t\t\tdocument.getElementById('amihref_" + release[0] + "').style.visibility='visible';\n"
		js+="\t\t\tdocument.getElementById('label_" + release[0] + "').innerHTML = ami_id;\n"
		js+="\t\t} else {\n"
		js+="\t\t\tdocument.getElementById('amihref_" + release[0] + "').href = '';\n"
		js+="\t\t\tdocument.getElementById('amihref_" + release[0] + "').style.visibility='hidden';\n"
		js+="\t\t\tdocument.getElementById('label_" + release[0] + "').innerHTML = '';\n"
		js+="\t\t}\n"
		js+="\t}\n"
	js+="}\n"
	f = open(OUTPUT, 'w+')
	f.write(js)
	f.close()

def get_amis():
    ec2_f20_Beta_regions = sorted_region(ec2_f20_Beta)
    ec2_f20_regions = sorted_region(ec2_f20)
    ec2_f19_regions = sorted_region(ec2_f19)
    
    if not os.path.exists(OUTPUT):
        gen_js(
        	['20',ec2_f20],
            ['19',ec2_f19],
            ['20_Beta',ec2_f20_Beta])

    return {
        'f20':ec2_f20, 'f20_regions':ec2_f20_regions,
        'f19':ec2_f19, 'f19_regions':ec2_f19_regions,
        'f20_Beta':ec2_f20_Beta, 'f20_Beta_regions':ec2_f20_Beta_regions
           }

