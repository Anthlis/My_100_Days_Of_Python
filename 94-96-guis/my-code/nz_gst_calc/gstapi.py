

def add_gst(add_total):
    gst = (add_total*15)/100
    add_gst = (add_total*15)/100
    return gst, add_gst


def subt_gst(subt_total):
    gst = (subt_total*15)/100
    subt_gst = (1-0.15) * subt_total
    return gst, subt_gst
