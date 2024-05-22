def aboveline(x1,x2,x3):
    m = (x2[1] - x1[1])/(x2[0] - x1[0])
    b = x1[1] - m * x1[0]
    return(x3[1] > m * x3[0] + b)

def comfort(temp,rh):
# from https://www.azosensors.com/article.aspx?ArticleID=487
    return(
         aboveline([86.5,67.1],[29.3,69.0],[rh,temp]) and
         aboveline([29.3,69.0],[23.0,76.0],[rh,temp]) and
         not aboveline([23.0,76.0],[58.3,74.3],[rh,temp]) and
         not aboveline([58.3,74.3],[86.5,67.1],[rh,temp]))