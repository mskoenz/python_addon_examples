#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    22.01.2015 14:27:01 CET
# File:    plot.py

from ..helper import *
from ..parameter import *

from .help_plot import *
from .xml_parser import *
from .import_pyplot import *

import copy
import collections

lower_min = np.array([ np.inf,  np.inf])
upper_max = np.array([-np.inf, -np.inf])

def reset_lim():
    global lower_min, upper_max
    lower_min = np.array([ np.inf,  np.inf])
    upper_max = np.array([-np.inf, -np.inf])

def update_lim(xdata, ydata):
    lower_min[0] = min(lower_min[0], min(xdata))
    upper_max[0] = max(upper_max[0], max(xdata))
    lower_min[1] = min(lower_min[1], min(ydata))
    upper_max[1] = max(upper_max[1], max(ydata))

def set_lim(ax, opt):
    border = opt.border
    
    if is_list(border):
        dperc = np.array(border)
    else:
        dperc = np.array([border, border])
    
    if "xlim" in opt.keys():
        lower_min[0] = opt.xlim[0]
        upper_max[0] = opt.xlim[1]
    if "ylim" in opt.keys():
        lower_min[1] = opt.ylim[0]
        upper_max[1] = opt.ylim[1]
    
    range_ = upper_max - lower_min
    
    lower = lower_min - range_ * dperc
    upper = upper_max + range_ * dperc
    ax.set_xlim(lower[0], upper[0])
    ax.set_ylim(lower[1], upper[1])

def apply_manipulator(data, idx, opt, error = False):
    if "acc" in opt.keys():
        if opt.acc[idx] == 1:
            if error:
                data = np.sqrt(np.add.accumulate(np.square(data)))
            else:
                data = np.add.accumulate(data)
        
    return data

def get_select(xdata, ydata, additional, y_i, opt, kw):
    if kw in opt.keys():
        if len(opt[kw][y_i]) == 2:
            b, sp = opt[kw][y_i]
            e = len(xdata)
        else:
            b, e, sp = opt[kw][y_i]
        
        xdata = xdata[b:e][0::sp]
        ydata = ydata[b:e][0::sp]
        
        if "xerr" in additional.keys():
            additional["xerr"] = additional["xerr"][b:e][0::sp]
        if "yerr" in additional.keys():
            additional["yerr"] = additional["yerr"][b:e][0::sp]
    
    return xdata, ydata

def plot_handler(pns, p):
    #------------------- show available labels -------------------
    if "l" in p.flag:
        for l, l_i in zipi(pns.label):
            print("{green}pos {greenb}{:0>2}{green} = {green}{}{none}".format(l_i, l, **color))
        return
    #=================== plot ===================
    #------------------- prepare plot opt dict -------------------
    valid_plot_option = [
                       # data
                         "x"
                       , "y"
                       , "xerr"
                       , "yerr"
                       # param
                       , "parameter"
                       , "parameter_loc"
                       # manipulation
                       , "acc"
                       , "dselect"
                       , "pselect"
                       , "linreg"
                       # destination
                       , "o"
                       # style
                       , "title"
                       , "size_inch"
                       , "style"
                       , "xticks"
                       , "yticks"
                       , "xlabel"
                       , "ylabel"
                       , "xlim"
                       , "ylim"
                       , "border"
                       , "markersize"
                       , "legend_loc"
                       ]
    
    special_option = ["update", "isel", "osel", "conv", "l", "cp_opt", "conf"]
    
    
    #------------------- defaults options -------------------
    legend_dict = {"best": 0, "upper_right": 1, "upper_left": 2, "lower_left": 3, "lower_right": 4, "right": 5, "center_left": 6, "center_right": 7, "lower_center": 8, "upper_center": 9, "center": 10}
    opt = namespace()
    opt.legend_loc = "best"
    opt.o = "unnamed.pdf"
    opt.x = 0
    opt.y = 1
    opt.border = .05
    opt.style = ["r^-", "b^-", "g^-", "y^-"] 
    opt.size_inch = [8.0, 6.0]
    isel = p.get("isel", 0)
    osel = p.get("osel", isel)
    
    if pns != None and len(pns.plot_option) > isel:
        opt.update(dict_select(pns.plot_option[isel], valid_plot_option)) #overwrite by xml info
    opt.update(dict_select(p, valid_plot_option))               #overwrite by argv info
    
    #------------------- delete parameter if given as flags -------------------
    for f in p.flag:
        if f in opt.keys():
            del opt[f]
    
    opt_save = copy.deepcopy(opt) # for saving (we want to keep human readable labels, not 1,2,0)
    
    #=================== help and config print ===================
    if "conf" in p.keys():
        print_conf(p, opt, legend_dict)
        return
    if "help" in p.keys():
        print_help(valid_plot_option, special_option, p.get("help", "all"))
        return
    
    #------------------- convert labels/string to numbers -------------------
    label_to_number = lambda x: (-1 if x == "none" else pns.label.index(x)) if is_str(x) else x
    get_label = lambda lbl_nr, label, idx = None: (opt[label] if idx == None else opt[label][idx]) if label in opt.keys() else pns.label[lbl_nr]
    
    if is_str(opt.legend_loc):
        opt.legend_loc = legend_dict[opt.legend_loc]
        
    opt.y = make_list(opt.y)
    if not is_list(opt.x):
        opt.x = [opt.x for i in range(len(opt.y))]
    
    for i in range(len(opt.x)):
        opt.x[i] = label_to_number(opt.x[i])
    
    for i in range(len(opt.y)):
        opt.y[i] = label_to_number(opt.y[i])
    
    if "xerr" in opt.keys():
        if not is_list(opt.yerr):
            opt.xerr = [opt.xerr  for i in range(len(opt.x))]
        for i in range(len(opt.xerr)):
            opt.xerr[i] = label_to_number(opt.xerr[i])
        
    if "yerr" in opt.keys():
        if not is_list(opt.yerr):
            opt.yerr = [opt.yerr  for i in range(len(opt.y))]
        for i in range(len(opt.yerr)):
            opt.yerr[i] = label_to_number(opt.yerr[i])
    
    #------------------- handle shorthand notation -------------------
    expand = [["dselect", lambda x: is_list(x[0])]
            , ["pselect", lambda x: is_list(x[0])]
            , ["linreg", lambda x: is_list(x[0])]
            , ["acc", lambda x: is_list(x)]
            , ["markersize", lambda x: is_list(x)]
            ]
    
    for key, test in expand:
        if key in opt.keys():
            if not test(opt[key]):
                opt[key] = [opt[key] for i in range(len(opt.y))]
    
    #------------------- lazy notation -------------------
    if opt.o[-4] != ".":
        opt.o += "/" + filename(pns.file_)[:-4] + ".pdf"
    
    #=================== main plot ===================
    fig, ax = pyplot.subplots()
    opt.style = collections.deque(opt.style)
    
    additional = {}
    plot_fct = ax.errorbar
    
    
    for y, y_i in zipi(opt.y):
        #------------------- set data -------------------
        xdata = pns.data[opt.x[y_i]]
        ydata = pns.data[y]
        if "xerr" in opt.keys():
            additional["xerr"] = pns.data[opt.xerr[y_i]]
        if "yerr" in opt.keys() and opt.yerr[y_i] != -1:
            additional["yerr"] = pns.data[opt.yerr[y_i]]
        
        #------------------- apply manipulatros to data -------------------
        xdata, ydata = get_select(xdata, ydata, additional, y_i, opt, "dselect")
        
        ydata = apply_manipulator(ydata, y_i, opt)
        if "yerr" in opt.keys() and opt.yerr[y_i] != -1:
            additional["yerr"] = apply_manipulator(additional["yerr"], y_i, opt, error = True)
        
        #~ p = len(ydata)//2
        #~ print(xdata[p], ydata[p], additional["yerr"][p])
        
        #------------------- style -------------------
        if "markersize" in opt.keys():
            additional["markersize"] = opt.markersize[y_i]
            
        additional["fmt"] = opt.style[0]
        opt.style.rotate(-1)
        
        #------------------- get plot selection -------------------
        xdata, ydata = get_select(xdata, ydata, additional, y_i, opt, "pselect")
        plot_fct(xdata, ydata, label = get_label(y, "ylabel", y_i), **additional)
        update_lim(xdata, ydata)
        #------------------- linreg -------------------
        if "linreg" in opt.keys():
            linreg = opt.linreg[y_i]
            if linreg != "none":
                m,b = np.polyfit(xdata, ydata, 1)
                if is_list(linreg):
                    xdata = np.array(linreg)
                ax.plot(xdata, m*xdata+b, opt.style[0])
                opt.style.rotate(-1)

    #------------------- set lims -------------------
    set_lim(ax, opt)
    
    #------------------- set title -------------------
    if "title" in opt.keys():
        ax.set_title(opt.title.format(**pns.param))
    
    #------------------- set labels / legend -------------------
    if "xticks" in opt.keys():
        low, upper, incr = opt.xticks
        ax.set_xticks(range(low, upper+incr, incr))
    if "yticks" in opt.keys():
        low, upper, incr = opt.yticks
        ax.set_yticks(range(low, upper+incr, incr))
    
    ax.set_xlabel(get_label(opt.x[0], "xlabel"))
    if len(opt.y) == 1:
        ax.set_ylabel(get_label(opt.y[0], "ylabel", 0))
    else:
        ax.legend(loc = opt.legend_loc)
        if "ylabel" in opt.keys():
            if len(opt.ylabel) > len(opt.y):
                ax.set_ylabel(opt.ylabel[-1])
    
    #------------------- set parameter box -------------------
    if "parameter" in opt.keys():
        if opt.parameter == "all":
            opt.parameter = ""
            for k in nsx.param.keys():
                opt.parameter += k + ": {" + k + "}{nl}"
            opt.parameter = opt.parameter[:-4]
        loc = opt.get("parameter_loc", [0, 0])
        
        text = opt.parameter.format(**merge_dict({"nl": "\n"}, pns.param))
        
        ax.text(loc[0], loc[1]
            , text
            , transform=ax.transAxes
            , fontsize=12
            , verticalalignment='center'
            , horizontalalignment='left'
            , bbox=dict(boxstyle='square', facecolor=background_color, edgecolor=grid_color, alpha=1)
        )
    
    
    fig.set_size_inches(*opt.size_inch)
    #~ fig.subplots_adjust(left=0.05, right=.95, top=0.9, bottom=0.1)
    fig.tight_layout()
    
    create_folder(path(opt.o))
    fig.savefig(opt.o)
    
    pns.plot_option_to_xml(opt_save, sel = osel, mod="overwrite")
    print("{green}ploted {greenb}{} {green}to {greenb}{}{green} with selection {greenb}{}{green} (-> {}){none}".format(pns.file_, opt.o, isel, osel, **color))
    reset_lim()

def join_pns(all_pns, p):
    if len(all_pns) == 0:
        return None
        
    elif len(all_pns) == 1:
        return all_pns[0]
        
    else:
        for ns, ns_i in zipi(all_pns):
            if ns_i == 0:
                pns = ns
                param_compare = pns.param
                p.isel = p.get("isel", 1)
                pns.label = ["{:0>2}-{}".format(ns_i, l) for l in pns.label]
                pns.data = list(pns.data)
            else:
                if param_compare != ns.param:
                    ERROR("parameter not the same in {} and {}".format(pns.file_, ns.file_))
                else:
                    pns.data += list(ns.data)
                    pns.label += ["{:0>2}-{}".format(ns_i, l) for l in ns.label]
        return pns
    
def plot(p = parameter):
    p.flag = p.get("flag", []) #since a namespace may lack flag
    
    files = p.arg
    
    if "conv" in p.keys():
        for file_ in files:
            txt_to_xml(file_, p.conv, p)
        return
    
    if "update" in p.flag:
        for file_ in files:
            pns = xml_to_plot(file_)
            dir_ = path(file_)
            if pns.source != None:
                p.comment = p.get("comment", pns.source["comment"])
                txt_to_xml(pns.source["file_"], pns.file_, p)
        return
    
    if "cp_opt" in p.keys() or "cp_opt" in p.flag:
        if "cp_opt" in p.keys():
            isel, osel =  p.cp_opt
        else:
            isel, osel =  0, 0
        
        opt = xml_to_plot(files[0]).plot_option
        for file_ in files[1:]:
            xml_to_plot(file_).plot_option_to_xml(opt[isel], sel = osel, mod="overwrite")
            YELLOW("copied opt {yellowb}{} {yellow}from {yellowb}{} {yellow}to {yellowb}{} {yellow}opt {yellowb}{}".format(isel, files[0], file_, osel, **color))
        return
    
    
    if "plot" in p.flag:
        all_pns = []
        for file_ in files:
            all_pns.append(xml_to_plot(file_))
        
        if "parallel" in p.flag:
            for pns in all_pns:
                plot_handler(pns, p)
        else:
            pns = join_pns(all_pns, p)
            plot_handler(pns, p)
        
def plot2(args = parameter):
    if "parallel" in p.flag:
        if "split" in p.keys() and "a3data" in p.keys():
            #------------------- prepare join namespace -------------------
            join = namespace()
            join.label = nsp[0].label + [p.a3data[0]]
            join.data = [[] for i in range(len(nsp[0].data) + 1)]
            
            #------------------- join all data -------------------
            for ns, ns_i in zipi(nsp):
                for d, d_i in zipi(ns.data):
                    join.data[d_i] += list(d)
                join.data[-1] += [p.a3data[ns_i+1] for i in range(len(d))]
            
            join.data = transpose(join.data)
            join.data = sorted(join.data, key = lambda x: x[p.split])
            
            #------------------- write out .txt files -------------------
            join.data = split_list(join.data, key = lambda x: x[p.split])
            
            for data, data_i in zipi(join.data):
                #------------------- extract identical data to dict_ -------------------
                dict_ = {}
                for l, l_i in zipi(join.label):
                    compare = data[0][l_i]
                    for i in range(1, len(data)):
                        if compare != data[i][l_i]:
                            break
                    else:
                        dict_[l] = compare
                
                file_ = p.o.format(**dict_)
                create_folder(path(file_))
                
                if file_[-3:] == "txt":
                    ofs = open(file_, "w")
                    ofs.write(" ".join(join.label)+"\n")
                    for d in data:
                        ofs.write(" ".join([str(x) for x in d])+"\n")
                    GREEN("written {greenb}{}".format(file_, **color))
                    ofs.close()
                elif file_[-3:] == "xml":
                    temp = open("temp.txt", "w")
                    temp.write(" ".join(join.label)+"\n")
                    for d in data:
                        temp.write(" ".join([str(x) for x in d])+"\n")
                    temp.close()
                    
                    txt_to_xml("temp.txt", file_)
                
                bash("rm temp.txt", silent = True)
    
