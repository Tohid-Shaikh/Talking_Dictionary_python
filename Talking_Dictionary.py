import pyttsx3

ball="chendu"
red="laal"
Beside="बाजुला"
Allow="परवानगी देणे"
Voice="आवाज"


Upset= "निराश चिंतीत"
Visible= "दिसुन येणा"
Invisible= "अदृश्य न दिसुन येणा"
Loan= "कर्ज,त्रण"

Interfere= "हस्तक्षेप करणे"
Insult= "अपमान"
Problem= "समस्या"
Sollution= "समस्येचे समाधान"
Still =  "ajun hee"
Real = "खरे"
Proper ="योग्य,उचित,व्यवस्थित"
Sure = "खात्री"
Dry = "कोरडा"
Full= "संपुर्ण"
Whole = "सर्व"
More = "अधिक"
Easy = "सहज"
Difficult= "कठिन"
Will = "ईच्छा"
Willing = "इच्छुक असणे"



engine = pyttsx3.init()


dict={"chendu":ball,"laal":red,"बाजुला":Beside,"परवानगी देणे":Allow,"चेंडू":ball,"लाल":red,"बाजुला":Beside,"परवानगी देणे":Allow,"आवाज":Voice,"निराश चिंतीत":Upset,"दिसुन येणा":Visible,"अदृश्य न दिसुन येणा":Invisible,"कर्ज,त्रण":Loan, "हस्तक्षेप करणे":Interfere,"अपमान":Insult,"समस्या":Problem,"समस्येचे समाधान":Sollution,"ajun hee":Still,"खरे":Real,"योग्य,उचित,व्यवस्थित":Proper,"खात्री":Sure,"कोरडा":Dry,"संपुर्ण":Full,"सर्व":Whole,"अधिक":More,"सहज":Easy,"कठिन":Difficult,"ईच्छा":Will,"इच्छुक असणे":Willing}



user_input=str(input("ENTER A WORD: "))

#++++++=+++=+++ words +++++++=+++=+++#
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.8)

if(user_input=="ball"):
    print(dict[ball])
    engine.say(dict[ball])
    
elif(user_input=="red"):
    print(dict[red])
    engine.say(dict[red])   
    
elif(user_input=="still"):
    print(dict[Still])
    engine.say(dict[Still])     
engine.runAndWait()
