#Copyright
print("\nWeb Maker v 0.50\nCopyright(c) 2018 Program Valley\n")

name = input("Web name >>>")

#<--------------------------------SCRIPT---------------------------->
WC = "<!--CREATED BY WEB MAKER Copyright(c) 2018 Program Valley-->\n"
slozka = name+".html"

#title size
num = ["1","2","3","4","5","6"]
# unsupported characters----------------------------
list= ["ě","š","č","ř","ž","ý","á","í","é","´","ˇ",]
# unsupported characters----------------------------
chyba = False
# "error checkers"----

radkovani = ">"

class displayTags:
    #paragraphs can not be next to each other
    pS = "<p>"
    pE = "</p>"
    #lines can bz store next to each other
    aS = "<a"
    aE = "</a>"
    #span =lines
    SS = "<span>"
    SE = "</span>\n"
    #div = blocks
    DS = "<div>"
    DE = "</div>\n"

#basic tags with funciton
class Tags:
    bacS= ' style="background-color:'
    bacE = ';"'
    colorS = ' style="color:'
    colorE = ';">'
    htmlS = "<html>\n"
    htmlEND = "\n</html>"
    hlavni = "<!DOCTYPE html>\n"
    charset = ' charset="UTF-8"'
    meta = "<meta"
    metaEnd = ">\n"
    hlavickaStart = " <head>\n"
    hlavickaEnd = " </head>\n"
    titleS = ("<title>")
    titleE = ("</title>\n")
    teloStart = "<body" + bacS
    teloEnd = "\n</body>\n"
    linkS ='<a href="'
    linkE ='">'
    linkN = "</a>\n"
    videoS = '<video src=" '
    videoSE = '" controls width="'
    videoEE = '"></video>'

class text:
    nadpisS = "<h"
    nadpisE = "</h"
    boldS = "<b>"
    boldE = "</b>"
    kuryS = "<i>"
    kurzE = "</i>"
    bigS="<big>"
    bigE="</big>"
    smallS ="<small>"
    smallE="</small>"

# message
def info():
    print("Your web is done :)")
    input("hold Ctrl + C for end")

# write to file </html>
def konec ():
    file = open(slozka , "a")
    file.write(Tags.teloEnd)
    file.write(Tags.htmlEND)
    file.close()

# write to file setup
def setup():
    file = open(slozka , "w")
    file.write(WC + Tags.htmlS + Tags.hlavickaStart+Tags.titleS+name+Tags.titleE + Tags.meta +
               Tags.charset+Tags.metaEnd+Tags.hlavickaEnd+Tags.teloStart)
    file.close()

setup()
e = input("background color ? >>>")
file = open(slozka,"a")
file.write(e + Tags.bacE + ">" + "\n")
file.close()

#<--------------------------------SCRIPT---------------------------->
index = 0

#cmd
while index <100:
    hlavka = input(">>>")

    if hlavka.lower()=="vid":
        print('check if video is in folder "videos" ')
        video = input("name of file (cats.mp4)>>>")
        videosize=input("video size px >>>")
        divnos = input(">,/ >>>")
        def Video():
            file = open(slozka,"a")

            if divnos == ">":
                file = open(slozka, "a")
                file.write(displayTags.SS+Tags.videoS+"videos/"+video+Tags.videoSE+videosize+Tags.videoEE+displayTags.SE)
                file.close()
            if divnos == "/":
                file = open(slozka, "a")
                file.write(displayTags.DS+Tags.videoS+"videos/"+video+Tags.videoSE+videosize+Tags.videoEE+displayTags.DE)
                file.close()


            file.close()
        Video()

    if hlavka.lower() =="tit":
        b = input("title >>>")
        c = input("title size >>>")
        if int(c) <10:
            c="1"
        if int(c) >10:
            print("WARNING THIS SIZE MAY BE TOO BIG")
            velko = input("title size >>>")
            c="1"
            if int(velko) >100:
                velko=50
            bigS = b * int(velko)
            bigE = b * int(velko)
        d = input("title color >>>")


        def nadpis():
            file = open(slozka, "a")
            file.write(bigS+text.nadpisS + c  +Tags.colorS + d + Tags.colorE + b +text.nadpisE+ c + ">"+bigE)
            file.close()
        nadpis()


        #index = index +3
    if hlavka.lower() == "img":
        print('check if image is in folder "images" ')
        i = input("Image name (cat.jpg) >>>")
        v = input("size of the image px >>>")
        radkovani = input(">,/ >>>")

        def Image():
            if i != "no64_error_64image":
                image = ' <img width ="' + v + '"' + ' src="images/' + i + '"' + ' alt="Image is not available" />'

                if radkovani == ">":
                    file = open(slozka, "a")
                    file.write(displayTags.SS + image + displayTags.SE)
                    file.close()
                if radkovani == "/":
                    file = open(slozka, "a")
                    file.write(displayTags.DS + image + displayTags.DE)
                    file.close()

        Image()




        #index = index + 1
    if hlavka.lower() == "txt":
        texto=input("text >>>")
        textsize = input("text size >>>")
        textbar =input("text color >>>")
        if int(textsize) >15:
            print("WARNING THIS SIZE MAY BE TOO BIG")
            textsize = input("new or old text size >>>")
            if int(textsize) >= 72:
                textsize = 30


        divs = input(">,/ >>>")

        def txtx():
            velakS =text.bigS
            velakE =text.bigE
            big = velakS*int(textsize)
            bigg = velakE*int(textsize)
            if divs == ">":
                file = open(slozka, "a")
                file.write("\n<div"+Tags.colorS + textbar+Tags.colorE +big+ texto +bigg +displayTags.SE)
                file.close()
            if divs == "/":
                file = open(slozka, "a")
                file.write("\n<div" +Tags.colorS + textbar+Tags.colorE +big+ texto +bigg + displayTags.DE)
                file.close()

        txtx()
    if hlavka.lower() == "test":
        a = "-TEST-"
        b = "-TEST-"
        c = "1"
        d = "white"
        i ="TEST.JPG"
        v = "900"
        e = "black"
        index = index + 100
    if hlavka.lower() == "help":
        file = open("WEB HELP5.txt","r")
        print(file.read())
        file.close()
    if hlavka.lower()=="link":
        file = open(slozka, "a")
        URL = input("URL >>>")
        WEB = input("Link name >>>")
        file.write(Tags.linkS+URL+Tags.linkE+WEB+Tags.linkN)
        file.close()
    if hlavka.lower() == "end":
        index = index + 100

#output
konec()
info()