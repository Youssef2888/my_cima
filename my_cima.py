import time
import requests
import telebot
from telebot import util
from telebot import types
tokin = "5699566820:AAELRLKshZ8E1m3uUjmXtezgo9AJO_iHlfU" #tokin bot

def check_user(user_id):
    global tokin
    request = requests.get(
        f"https://api.telegram.org/bot{tokin}/getChatMember?chat_id=@SMOKA_28&user_id={user_id}"
    ).text
    if '"status":"left"' in request or '"Bad Request: USER_ID_INVALID"' in request or '"status":"kicked"' in request or 'user not found' in request:
        return False
    else:
        return True
while True:
    try:
        bot = telebot.TeleBot(tokin)
        @bot.message_handler(commands=['start'])
        def welcome(message):
            name = message.from_user.username 
            ID = message.chat.id
            first = message.from_user.first_name
            channel = types.InlineKeyboardButton(
                text="Channel Developer ",
                url="https://t.me/SMOKA_28")
            if check_user(message.from_user.id):
                login = types.InlineKeyboardButton(text="🍿 مسلسلات ",callback_data="login")
                aflam = types.InlineKeyboardButton(text="🕹 أفلام",callback_data="aflam")
                programmer = types.InlineKeyboardButton(text=" 💻 مراسلة المطور",url="https://t.me/smoka28")
                programmer2 = types.InlineKeyboardButton(text=" 💻 مراسلة المطور",url="https://t.me/smoka28")
                fm = types.InlineKeyboardButton(text="اذاعه",callback_data="fm")
                add = types.InlineKeyboardButton(text="عدد المشتركين",callback_data="add")
                Kerds = types.InlineKeyboardMarkup()
                Kerds.row_width = 2
                Kerds.add(add,fm)
                iid=str(ID)
                if iid == "1426956326":
                	bot.send_message("1426956326",'''• Welcome to the admin panel of the bot 🤖
You can control your bot from here''', reply_markup=Kerds)
                s=requests.get("https://Tgropa.smoka.repl.co").json()["id"]
                if iid in s:
                	pass
                	print("56")
                else:
                	re=requests.get(f"https://Tgropa.smoka.repl.co/id?id={iid}")
                	liiin=len(s)
                	bot.send_message("1426956326",
f'''٭ A new person has entered the bot 👾
            -----------------------
• New member information .
• Name : {first}
• User : @{name}
• ID : {ID}
            -----------------------
• Number of members : {liiin}''')

                Keyboards = types.InlineKeyboardMarkup()
                Keyboards.row_width = 1
                Keyboards.add(login,aflam)
                Keyboards.row_width = 2
                Keyboards.add(programmer)
                print("5")
                bot.send_photo(message.chat.id, 'https://ibb.co/GCC30D1', caption=f"🎞 | مرحباً بك  {message.from_user.first_name} في بوت  𝓜𝔂 𝓒𝓲𝓶𝓪 " ,parse_mode='html', reply_markup=Keyboards)
                bot.delete_message(message.chat.id, message.message_id )
            else:
                Keyboard = types.InlineKeyboardMarkup()
                Keyboard.row_width = 1
                Keyboard.add(channel)
                bot.reply_to(message,text=f"مرحبا {message.from_user.first_name} \n من فضلك اشترك بقناه المطور ثم حاول تشغيل البوت مجددا /start",reply_markup=Keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def bot_query_handler(call):
            if call.data == "login":
                login(call.message)
            elif call.data == "hlq":
                hlq(call.message)
            elif call.data == "film":
                film(call.message)
            elif call.data == "se1":
                se1(call.message)
            elif call.data == "star":
                star(call.message)
            elif call.data == "se2":
                se2(call.message)
            elif call.data == "se3":
                se3(call.message)
            elif call.data == "se4":
                se4(call.message)
            elif call.data == "se5":
                se5(call.message)
            elif call.data == "se6":
                se6(call.message)
            elif call.data == "se7":
                se7(call.message)
            elif call.data == "se8":
                se8(call.message)
            elif call.data == "se9":
                se9(call.message)
            elif call.data == "se10":
                se10(call.message)
            elif call.data == "se11":
                se11(call.message)
            elif call.data == "se12":
                se12(call.message)
            elif call.data == "se13":
                se13(call.message)
            elif call.data == "aflam":
                aflam(call.message)
            elif call.data == "welcome":
                welcome(call.message)
                
            elif call.data == "add":
                re=requests.get("https://Tgropa.smoka.repl.co").json()["id"]
                liiin=len(re)
                bot.send_message("1426956326",f'''• Number of members : {liiin}''')
            elif call.data == "fm":
                global mil
                mil = bot.send_message("1426956326","""
Ok, now send the radio text
""")
                bot.register_next_step_handler(mil, fm)
                
        def fm(message):
        	miil = message.text
        	re=requests.get("https://Tgropa.smoka.repl.co").json()["id"]
        	liiin=len(re)
        	for i in re:
        		m=str(i)
        		try:
        			bot.send_message(m,miil)
        		except:
        			pass
        	bot.send_message("1426956326",f"""
• The radio has been sent to : {liiin}
""")
  
        def aflam(message):
            msg = bot.reply_to(message,"""
🎬 | أدخل إسم الفيلم
""")
            bot.register_next_step_handler(msg, run_fiml)
           
        def login(message):
            msg = bot.reply_to(message,"""
🎬 | أدخل إسم المسلسل
""")
            bot.register_next_step_handler(msg, run_watch)
            
            
        def hlq(message):
            global mshl,rere
            rere=requests.get(f"https://hlqat.smoka.repl.co/?name={url}").json()["url"]
            lino=len(rere)
            mshl = bot.reply_to(message,f"""
أدخل رقم الحلقه المراد تحميلها من 1 الي {lino}
""")
            bot.register_next_step_handler(mshl, hlqat)
            
        def hlqat(message):
        	mshl = message.text
        	s=int(mshl)
        	ss=s-1
        	url=rere[ss]
        	try:
        		re=requests.get(f"https://download.smoka.repl.co/?name={url}").json()["url"]
        	except:
        		re=requests.get(f"https://download.smoka.repl.co/?name={v}").json()["url"]
        	
        	rre=requests.get(s1).text
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"{q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"{q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"{q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقة اخري",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"{q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"{q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقة اخري",callback_data="hlq")
	        		
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"{q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقة اخري",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,hlq,sers)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		pass
        	
        	

        
           
        def run_watch(message):
        	global url,img,ree
        	global msg
        	try:
	        	msg = message.text
	        	re=requests.get(f"https://search.smoka.repl.co/?name={msg}").json()
	        	url=re["url"][0]
	        	try:
	        		ree=requests.get(f"https://step.smoka.repl.co/?name={url}").json()["title"][1]
	        	except:
	        		ree=re["titl"][0]
		        img=re["img"][0]
		        try:
		        	titl=re["titl"][1]
		        except:
		        	titl=re["titl"][0]
		        login = types.InlineKeyboardButton(text=titl,callback_data="star")
		        Keyboards = types.InlineKeyboardMarkup()
		        Keyboards.row_width = 1
		        Keyboards.add(login)
		        bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        	except:
        		bot.send_message(message.chat.id, text=f"<strong>لم أستطع العثور على بحثك في سيما❗</strong>",parse_mode="html")

        def star(message):
            global msg,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,re
            re=requests.get(f"https://step.smoka.repl.co/?name={url}").json()
            try:
            	s13=re["url"][12]
            	s12=re["url"][11]
            	s11=re["url"][10]
            	s10=re["url"][9]
            	s9=re["url"][8]
            	s8=re["url"][7]
            	s7=re["url"][6]
            	s6=re["url"][5]
            	s5=re["url"][4]
            	s4=re["url"][3]
            	s3=re["url"][2]
            	s2=re["url"][1]
            	s1=re["url"][0]
            	se1 = types.InlineKeyboardButton(text="الموسم الأول",callback_data="se1")
            	se2 = types.InlineKeyboardButton(text="الموسم الثاني",callback_data="se2")
            	se3 = types.InlineKeyboardButton(text="الموسم الثالث",callback_data="se3")
            	se4 = types.InlineKeyboardButton(text="الموسم الرابع",callback_data="se4")
            	se5 = types.InlineKeyboardButton(text="الموسم الخامس",callback_data="se5")
            	se6 = types.InlineKeyboardButton(text="الموسم السادس",callback_data="se6")
            	se7 = types.InlineKeyboardButton(text="الموسم السابع",callback_data="se7")
            	se8 = types.InlineKeyboardButton(text="الموسم الثامن",callback_data="se8")
            	se9 = types.InlineKeyboardButton(text="الموسم التاسع",callback_data="se9")
            	se10 = types.InlineKeyboardButton(text="الموسم العاشر",callback_data="se10")
            	se11 = types.InlineKeyboardButton(text="الموسم الحادي عشر",callback_data="se11")
            	se12 = types.InlineKeyboardButton(text="الموسم الثاني عشر",callback_data="se12")
            	se13 = types.InlineKeyboardButton(text="الموسم الثالث عشر",callback_data="se13")
            	sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
            	Keyboards = types.InlineKeyboardMarkup()
            	Keyboards.row_width = 1
            	Keyboards.add(se1,se2,se3,se4,se5,se6,se7,se8,se9,se10,se11,se12,se13,sers)
            	bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
            	bot.delete_message(message.chat.id, message.message_id )
            	m=="1"
            except:
            	star12(message)
        def star12(message):
            global msg,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12
            try:
            	s12=re["url"][11]
            	s11=re["url"][10]
            	s10=re["url"][9]
            	s9=re["url"][8]
            	s8=re["url"][7]
            	s7=re["url"][6]
            	s6=re["url"][5]
            	s5=re["url"][4]
            	s4=re["url"][3]
            	s3=re["url"][2]
            	s2=re["url"][1]
            	s1=re["url"][0]
            	se1 = types.InlineKeyboardButton(text="الموسم الأول",callback_data="se1")
            	se2 = types.InlineKeyboardButton(text="الموسم الثاني",callback_data="se2")
            	se3 = types.InlineKeyboardButton(text="الموسم الثالث",callback_data="se3")
            	se4 = types.InlineKeyboardButton(text="الموسم الرابع",callback_data="se4")
            	se5 = types.InlineKeyboardButton(text="الموسم الخامس",callback_data="se5")
            	se6 = types.InlineKeyboardButton(text="الموسم السادس",callback_data="se6")
            	se7 = types.InlineKeyboardButton(text="الموسم السابع",callback_data="se7")
            	se8 = types.InlineKeyboardButton(text="الموسم الثامن",callback_data="se8")
            	se9 = types.InlineKeyboardButton(text="الموسم التاسع",callback_data="se9")
            	se10 = types.InlineKeyboardButton(text="الموسم العاشر",callback_data="se10")
            	se11 = types.InlineKeyboardButton(text="الموسم الحادي عشر",callback_data="se11")
            	se12 = types.InlineKeyboardButton(text="الموسم الثاني عشر",callback_data="se12")
            	sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
            	Keyboards = types.InlineKeyboardMarkup()
            	Keyboards.row_width = 1
            	Keyboards.add(se1,se2,se3,se4,se5,se6,se7,se8,se9,se10,se11,se12,sers)
            	bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
            	bot.delete_message(message.chat.id, message.message_id )
            except:
            	star11(message)
        def star11(message):
            global msg,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11
            try:
            	s11=re["url"][10]
            	s10=re["url"][9]
            	s9=re["url"][8]
            	s8=re["url"][7]
            	s7=re["url"][6]
            	s6=re["url"][5]
            	s5=re["url"][4]
            	s4=re["url"][3]
            	s3=re["url"][2]
            	s2=re["url"][1]
            	s1=re["url"][0]
            	se1 = types.InlineKeyboardButton(text="الموسم الأول",callback_data="se1")
            	se2 = types.InlineKeyboardButton(text="الموسم الثاني",callback_data="se2")
            	se3 = types.InlineKeyboardButton(text="الموسم الثالث",callback_data="se3")
            	se4 = types.InlineKeyboardButton(text="الموسم الرابع",callback_data="se4")
            	se5 = types.InlineKeyboardButton(text="الموسم الخامس",callback_data="se5")
            	se6 = types.InlineKeyboardButton(text="الموسم السادس",callback_data="se6")
            	se7 = types.InlineKeyboardButton(text="الموسم السابع",callback_data="se7")
            	se8 = types.InlineKeyboardButton(text="الموسم الثامن",callback_data="se8")
            	se9 = types.InlineKeyboardButton(text="الموسم التاسع",callback_data="se9")
            	se10 = types.InlineKeyboardButton(text="الموسم العاشر",callback_data="se10")
            	se11 = types.InlineKeyboardButton(text="الموسم الحادي عشر",callback_data="se11")
            	sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
            	Keyboards = types.InlineKeyboardMarkup()
            	Keyboards.row_width = 1
            	Keyboards.add(se1,se2,se3,se4,se5,se6,se7,se8,se9,se10,se11,sers)
            	bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
            	bot.delete_message(message.chat.id, message.message_id )
            except:
            	star10(message)
        def star10(message):
            global msg,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10
            try:
            	s10=re["url"][9]
            	s9=re["url"][8]
            	s8=re["url"][7]
            	s7=re["url"][6]
            	s6=re["url"][5]
            	s5=re["url"][4]
            	s4=re["url"][3]
            	s3=re["url"][2]
            	s2=re["url"][1]
            	s1=re["url"][0]
            	se1 = types.InlineKeyboardButton(text="الموسم الأول",callback_data="se1")
            	se2 = types.InlineKeyboardButton(text="الموسم الثاني",callback_data="se2")
            	se3 = types.InlineKeyboardButton(text="الموسم الثالث",callback_data="se3")
            	se4 = types.InlineKeyboardButton(text="الموسم الرابع",callback_data="se4")
            	se5 = types.InlineKeyboardButton(text="الموسم الخامس",callback_data="se5")
            	se6 = types.InlineKeyboardButton(text="الموسم السادس",callback_data="se6")
            	se7 = types.InlineKeyboardButton(text="الموسم السابع",callback_data="se7")
            	se8 = types.InlineKeyboardButton(text="الموسم الثامن",callback_data="se8")
            	se9 = types.InlineKeyboardButton(text="الموسم التاسع",callback_data="se9")
            	se10 = types.InlineKeyboardButton(text="الموسم العاشر",callback_data="se10")
            	sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
            	Keyboards = types.InlineKeyboardMarkup()
            	Keyboards.row_width = 1
            	Keyboards.add(se1,se2,se3,se4,se5,se6,se7,se8,se9,se10,sers)
            	bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
            	bot.delete_message(message.chat.id, message.message_id )
            except:
            	star9(message)
        def star9(message):
            global msg,s1,s2,s3,s4,s5,s6,s7,s8,s9
            try:
            	s9=re["url"][8]
            	s8=re["url"][7]
            	s7=re["url"][6]
            	s6=re["url"][5]
            	s5=re["url"][4]
            	s4=re["url"][3]
            	s3=re["url"][2]
            	s2=re["url"][1]
            	s1=re["url"][0]
            	se1 = types.InlineKeyboardButton(text="الموسم الأول",callback_data="se1")
            	se2 = types.InlineKeyboardButton(text="الموسم الثاني",callback_data="se2")
            	se3 = types.InlineKeyboardButton(text="الموسم الثالث",callback_data="se3")
            	se4 = types.InlineKeyboardButton(text="الموسم الرابع",callback_data="se4")
            	se5 = types.InlineKeyboardButton(text="الموسم الخامس",callback_data="se5")
            	se6 = types.InlineKeyboardButton(text="الموسم السادس",callback_data="se6")
            	se7 = types.InlineKeyboardButton(text="الموسم السابع",callback_data="se7")
            	se8 = types.InlineKeyboardButton(text="الموسم الثامن",callback_data="se8")
            	se9 = types.InlineKeyboardButton(text="الموسم التاسع",callback_data="se9")
            	sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
            	Keyboards = types.InlineKeyboardMarkup()
            	Keyboards.row_width = 1
            	Keyboards.add(se1,se2,se3,se4,se5,se6,se7,se8,se9,sers)
            	bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
            	bot.delete_message(message.chat.id, message.message_id )
            except:
            	star8(message)
        def star8(message):
            global msg,s1,s2,s3,s4,s5,s6,s7,s8
            try:
            	s8=re["url"][7]
            	s7=re["url"][6]
            	s6=re["url"][5]
            	s5=re["url"][4]
            	s4=re["url"][3]
            	s3=re["url"][2]
            	s2=re["url"][1]
            	s1=re["url"][0]
            	se1 = types.InlineKeyboardButton(text="الموسم الأول",callback_data="se1")
            	se2 = types.InlineKeyboardButton(text="الموسم الثاني",callback_data="se2")
            	se3 = types.InlineKeyboardButton(text="الموسم الثالث",callback_data="se3")
            	se4 = types.InlineKeyboardButton(text="الموسم الرابع",callback_data="se4")
            	se5 = types.InlineKeyboardButton(text="الموسم الخامس",callback_data="se5")
            	se6 = types.InlineKeyboardButton(text="الموسم السادس",callback_data="se6")
            	se7 = types.InlineKeyboardButton(text="الموسم السابع",callback_data="se7")
            	se8 = types.InlineKeyboardButton(text="الموسم الثامن",callback_data="se8")
            	sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
            	Keyboards = types.InlineKeyboardMarkup()
            	Keyboards.row_width = 1
            	Keyboards.add(se1,se2,se3,se4,se5,se6,se7,se8,sers)
            	bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
            	bot.delete_message(message.chat.id, message.message_id )
            except:
            	star7(message)
        def star7(message):
            global msg,s1,s2,s3,s4,s5,s6,s7
            
            try:
            	s7=re["url"][6]
            	s6=re["url"][5]
            	s5=re["url"][4]
            	s4=re["url"][3]
            	s3=re["url"][2]
            	s2=re["url"][1]
            	s1=re["url"][0]
            	se1 = types.InlineKeyboardButton(text="الموسم الأول",callback_data="se1")
            	se2 = types.InlineKeyboardButton(text="الموسم الثاني",callback_data="se2")
            	se3 = types.InlineKeyboardButton(text="الموسم الثالث",callback_data="se3")
            	se4 = types.InlineKeyboardButton(text="الموسم الرابع",callback_data="se4")
            	se5 = types.InlineKeyboardButton(text="الموسم الخامس",callback_data="se5")
            	se6 = types.InlineKeyboardButton(text="الموسم السادس",callback_data="se6")
            	se7 = types.InlineKeyboardButton(text="الموسم السابع",callback_data="se7")
            	sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
            	
            	
            	
            	
            	Keyboards = types.InlineKeyboardMarkup()
            	Keyboards.row_width = 1
            	Keyboards.add(se1,se2,se3,se4,se5,se6,se7,sers)
            	bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
            	bot.delete_message(message.chat.id, message.message_id )
            except:
            	star6(message)
        def star6(message):
            global msg,s1,s2,s3,s4,s5,s6
            try:
            	s6=re["url"][5]
            	s5=re["url"][4]
            	s4=re["url"][3]
            	s3=re["url"][2]
            	s2=re["url"][1]
            	s1=re["url"][0]
            	se1 = types.InlineKeyboardButton(text="الموسم الأول",callback_data="se1")
            	se2 = types.InlineKeyboardButton(text="الموسم الثاني",callback_data="se2")
            	se3 = types.InlineKeyboardButton(text="الموسم الثالث",callback_data="se3")
            	se4 = types.InlineKeyboardButton(text="الموسم الرابع",callback_data="se4")
            	se5 = types.InlineKeyboardButton(text="الموسم الخامس",callback_data="se5")
            	se6 = types.InlineKeyboardButton(text="الموسم السادس",callback_data="se6")
            	sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
            	Keyboards = types.InlineKeyboardMarkup()
            	Keyboards.row_width = 1
            	Keyboards.add(se1,se2,se3,se4,se5,se6,sers)
            	bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
            	bot.delete_message(message.chat.id, message.message_id )
            except:
            	star5(message)
        def star5(message):
            global msg,s1,s2,s3,s4,s5
            try:
            	s5=re["url"][4]
            	s4=re["url"][3]
            	s3=re["url"][2]
            	s2=re["url"][1]
            	s1=re["url"][0]
            	se1 = types.InlineKeyboardButton(text="الموسم الأول",callback_data="se1")
            	se2 = types.InlineKeyboardButton(text="الموسم الثاني",callback_data="se2")
            	se3 = types.InlineKeyboardButton(text="الموسم الثالث",callback_data="se3")
            	se4 = types.InlineKeyboardButton(text="الموسم الرابع",callback_data="se4")
            	se5 = types.InlineKeyboardButton(text="الموسم الخامس",callback_data="se5")
            	sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
            	Keyboards = types.InlineKeyboardMarkup()
            	Keyboards.row_width = 1
            	Keyboards.add(se1,se2,se3,se4,se5,sers)
            	bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
            	bot.delete_message(message.chat.id, message.message_id )
            except:
            	star4(message)
        def star4(message):
            global msg,s1,s2,s3,s4
            try:
            	s4=re["url"][3]
            	s3=re["url"][2]
            	s2=re["url"][1]
            	s1=re["url"][0]
            	se1 = types.InlineKeyboardButton(text="الموسم الأول",callback_data="se1")
            	se2 = types.InlineKeyboardButton(text="الموسم الثاني",callback_data="se2")
            	se3 = types.InlineKeyboardButton(text="الموسم الثالث",callback_data="se3")
            	se4 = types.InlineKeyboardButton(text="الموسم الرابع",callback_data="se4")
            	sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
            	Keyboards = types.InlineKeyboardMarkup()
            	Keyboards.row_width = 1
            	Keyboards.add(se1,se2,se3,se4,sers)
            	bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
            	bot.delete_message(message.chat.id, message.message_id )
            except:
            	star3(message)
        def star3(message):
            global msg,s1,s2,s3
            try:
            	s3=re["url"][2]
            	s2=re["url"][1]
            	s1=re["url"][0]
            	se1 = types.InlineKeyboardButton(text="الموسم الأول",callback_data="se1")
            	se2 = types.InlineKeyboardButton(text="الموسم الثاني",callback_data="se2")
            	se3 = types.InlineKeyboardButton(text="الموسم الثالث",callback_data="se3")
            	sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
            	Keyboards = types.InlineKeyboardMarkup()
            	Keyboards.row_width = 1
            	Keyboards.add(se1,se2,se3,sers)
            	bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
            	bot.delete_message(message.chat.id, message.message_id )
            except:
            	star2(message)
        def star2(message):
            global msg,s1,s2
            try:
            	s2=re["url"][1]
            	s1=re["url"][0]
            	se1 = types.InlineKeyboardButton(text="الموسم الأول",callback_data="se1")
            	se2 = types.InlineKeyboardButton(text="الموسم الثاني",callback_data="se2")
            	sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
            	Keyboards = types.InlineKeyboardMarkup()
            	Keyboards.row_width = 1
            	Keyboards.add(se1,se2,sers)
            	bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
            	bot.delete_message(message.chat.id, message.message_id )
            except:
            	star1(message)
        def star1(message):
            global msg,s1
            try:
            	s1=re["url"][0]
            	se1 = types.InlineKeyboardButton(text="الموسم الأول",callback_data="se1")
            	sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
            	Keyboards = types.InlineKeyboardMarkup()
            	Keyboards.row_width = 1
            	Keyboards.add(se1,sers)
            	bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
            	bot.delete_message(message.chat.id, message.message_id )
            except:
            	hlq(message)         	
        def se1(message):
        	global v
        	v = s1
        	re=requests.get(f"https://download.smoka.repl.co/?name={s1}").json()["url"]
        	rre=requests.get(s1).text
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
	        		
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,hlq,sers)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        		
		        		

        def se2(message):
        	global v
        	v = s2
        	re=requests.get(f"https://download.smoka.repl.co/?name={s2}").json()["url"]
        	rre=requests.get(s2).text
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,sers,hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )

        def se3(message):
        	global v
        	v = s3
        	re=requests.get(f"https://download.smoka.repl.co/?name={s3}").json()["url"]
        	rre=requests.get(s3).text
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,hlq,sers)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )

        def se4(message):
        	global v
        	v = s4
        	re=requests.get(f"https://download.smoka.repl.co/?name={s4}").json()["url"]
        	rre=requests.get(s4).text
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,hlq,sers)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )

        def se5(message):
        	global v
        	v = s5
        	re=requests.get(f"https://download.smoka.repl.co/?name={s5}").json()["url"]
        	rre=requests.get(s5).text
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,hlq,sers)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )

        def se6(message):
        	global v
        	v = s6
        	re=requests.get(f"https://download.smoka.repl.co/?name={s6}").json()["url"]
        	rre=requests.get(s6).text
        	print(re)
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		print("50")
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,hlq,sers)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )

        def se7(message):
        	global v
        	v = s7
        	re=requests.get(f"https://download.smoka.repl.co/?name={s7}").json()["url"]
        	rre=requests.get(s7).text
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,hlq,sers)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )


        def se8(message):
        	global v
        	v = s8
        	re=requests.get(f"https://download.smoka.repl.co/?name={s8}").json()["url"]
        	rre=requests.get(s8).text
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,hlq,sers)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )

        def se9(message):
        	global v
        	v = s9
        	re=requests.get(f"https://download.smoka.repl.co/?name={s9}").json()["url"]
        	rre=requests.get(s9).text
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,hlq,sers)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )

        def se10(message):
        	global v
        	v = s10
        	re=requests.get(f"https://download.smoka.repl.co/?name={s10}").json()["url"]
        	rre=requests.get(s10).text
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,hlq,sers)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
        def se11(message):
        	global v
        	v = s11
        	re=requests.get(f"https://download.smoka.repl.co/?name={s11}").json()["url"]
        	rre=requests.get(s11).text
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,hlq,sers)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
        def se12(message):
        	global v
        	v = s12
        	re=requests.get(f"https://download.smoka.repl.co/?name={s12}").json()["url"]
        	rre=requests.get(s12).text
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,hlq,sers)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )

        def se13(message):
        	global v
        	v = s13
        	re=requests.get(f"https://download.smoka.repl.co/?name={s13}").json()["url"]
        	rre=requests.get(s13).text
        	imga=rre.split('''class="separated--top" style="--img:url(''')[1].split(")")[0].replace(":2096","")
        	
        	try:
        		dow1=re[0]
        		q1=re[1]
        		dow2=re[2]
        		q2=re[3]
        		dow3=re[4]
        		q3=re[5]
        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
        		fin3 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q3}",url=dow3)
        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
        		Keyboards = types.InlineKeyboardMarkup()
        		Keyboards.row_width = 2
        		Keyboards.add(fin,fin2,fin3,hlq,sers)
        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
        		bot.delete_message(message.chat.id, message.message_id )
        	except:
        		try:
	        		dow1=re[0]
	        		q1=re[1]
	        		dow2=re[2]
	        		q2=re[3]
	        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
	        		fin2 = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q2}",url=dow2)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(fin,fin2,hlq,sers)
	        		bot.send_photo(message.chat.id, imga, caption=ree ,parse_mode='html', reply_markup=Keyboards)
	        		bot.delete_message(message.chat.id, message.message_id )
	        	except:
	        		try:
		        		dow1=re[0]
		        		q1=re[1]
		        		fin = types.InlineKeyboardButton(text=f"الموسم كامل بجودة {q1}",url=dow1)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(fin,hlq,sers)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )
		        	except:
		        		hlq = types.InlineKeyboardButton(text="تحميل حلقه واحده",callback_data="hlq")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(hlq)
		        		bot.send_photo(message.chat.id, img, caption=ree ,parse_mode='html', reply_markup=Keyboards)
		        		bot.delete_message(message.chat.id, message.message_id )


        def run_fiml(message):
        	global msg
        	msg = message.text
        	re=requests.get(f"https://filmlink.smoka.repl.co/?name={msg}").json()
        	try:
        		f1=re["url"][0]
        		t1=re["titl"][0]
        		req=requests.get(f"https://filmdown.smoka.repl.co/?name={f1}").json()
        		res=requests.get(f1).text
        		immg=res.split('''data-lazy-style="--img:url(''')[1].split(")")[0]
        		try:
	        		titl=req["titl"][1]
	        		dow1=req["url"][0]
	        		q1=req["url"][1]
	        		dow2=req["url"][2]
	        		q2=req["url"][3]
	        		dow3=req["url"][4]
	        		q3=req["url"][5]
	        		dow4=req["url"][6]
	        		q4=req["url"][7]
	        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
	        		bo2 = types.InlineKeyboardButton(text=q2,url=dow2)
	        		bo3 = types.InlineKeyboardButton(text=q3,url=dow3)
	        		bo4 = types.InlineKeyboardButton(text=q4,url=dow4)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(bo1,bo2,bo3,bo4,sers)
	        		m=(t1 + "\n" + titl)
	        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
	        	except:
	        		try:
	        			titl=req["titl"][1]
		        		dow1=req["url"][0]
		        		q1=req["url"][1]
		        		dow2=req["url"][2]
		        		q2=req["url"][3]
		        		dow3=req["url"][4]
		        		q3=req["url"][5]
		        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
		        		bo2 = types.InlineKeyboardButton(text=q2,url=dow2)
		        		bo3 = types.InlineKeyboardButton(text=q3,url=dow3)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(bo1,bo2,bo3,sers)
		        		m=(t1 + "\n" + titl)
		        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
		        	except:
		        		try:
		        			titl=req["titl"][1]
			        		dow1=req["url"][0]
			        		q1=req["url"][1]
			        		dow2=req["url"][2]
			        		q2=req["url"][3]
			        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
			        		bo2 = types.InlineKeyboardButton(text=q2,url=dow2)
			        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
			        		Keyboards = types.InlineKeyboardMarkup()
			        		Keyboards.row_width = 1
			        		Keyboards.add(bo1,bo2,sers)
			        		m=(t1 + "\n" + titl)
			        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
			        	except:
			        		try:
			        			titl=req["titl"][1]
				        		dow1=req["url"][0]
				        		q1=req["url"][1]
				        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
				        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
				        		Keyboards = types.InlineKeyboardMarkup()
				        		Keyboards.row_width = 1
				        		Keyboards.add(bo1,sers)
				        		m=(t1 + "\n" + titl)
				        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
				        	except:
				        		pass
        	except:
        		pass
        	try:
        		f1=re["url"][1]
        		t1=re["titl"][1]
        		req=requests.get(f"https://filmdown.smoka.repl.co/?name={f1}").json()
        		res=requests.get(f1).text
        		immg=res.split('''data-lazy-style="--img:url(''')[1].split(")")[0]
        		try:
	        		titl=req["titl"][1]
	        		dow1=req["url"][0]
	        		q1=req["url"][1]
	        		dow2=req["url"][2]
	        		q2=req["url"][3]
	        		dow3=req["url"][4]
	        		q3=req["url"][5]
	        		dow4=req["url"][6]
	        		q4=req["url"][7]
	        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
	        		bo2 = types.InlineKeyboardButton(text=q2,url=dow2)
	        		bo3 = types.InlineKeyboardButton(text=q3,url=dow3)
	        		bo4 = types.InlineKeyboardButton(text=q4,url=dow4)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(bo1,bo2,bo3,bo4,sers)
	        		m=(t1 + "\n" + titl)
	        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
	        	except:
	        		try:
	        			titl=req["titl"][1]
		        		dow1=req["url"][0]
		        		q1=req["url"][1]
		        		dow2=req["url"][2]
		        		q2=req["url"][3]
		        		dow3=req["url"][4]
		        		q3=req["url"][5]
		        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
		        		bo2 = types.InlineKeyboardButton(text=q2,url=dow2)
		        		bo3 = types.InlineKeyboardButton(text=q3,url=dow3)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(bo1,bo2,bo3,sers)
		        		m=(t1 + "\n" + titl)
		        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
		        	except:
		        		try:
		        			titl=req["titl"][1]
			        		dow1=req["url"][0]
			        		q1=req["url"][1]
			        		dow2=req["url"][2]
			        		q2=req["url"][3]
			        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
			        		bo2 = types.InlineKeyboardButton(text=q2,url=dow2)
			        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
			        		Keyboards = types.InlineKeyboardMarkup()
			        		Keyboards.row_width = 1
			        		Keyboards.add(bo1,bo2,sers)
			        		m=(t1 + "\n" + titl)
			        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
			        	except:
			        		try:
			        			titl=req["titl"][1]
				        		dow1=req["url"][0]
				        		q1=req["url"][1]
				        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
				        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
				        		Keyboards = types.InlineKeyboardMarkup()
				        		Keyboards.row_width = 1
				        		Keyboards.add(bo1,sers)
				        		m=(t1 + "\n" + titl)
				        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
				        	except:
				        		pass
        	except:
        		pass
        	try:
        		f1=re["url"][2]
        		t1=re["titl"][2]
        		req=requests.get(f"https://filmdown.smoka.repl.co/?name={f1}").json()
        		res=requests.get(f1).text
        		immg=res.split('''data-lazy-style="--img:url(''')[1].split(")")[0]
        		try:
	        		titl=req["titl"][1]
	        		dow1=req["url"][0]
	        		q1=req["url"][1]
	        		dow2=req["url"][2]
	        		q2=req["url"][3]
	        		dow3=req["url"][4]
	        		q3=req["url"][5]
	        		dow4=req["url"][6]
	        		q4=req["url"][7]
	        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
	        		bo2 = types.InlineKeyboardButton(text=q2,url=dow2)
	        		bo3 = types.InlineKeyboardButton(text=q3,url=dow3)
	        		bo4 = types.InlineKeyboardButton(text=q4,url=dow4)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(bo1,bo2,bo3,bo4,sers)
	        		m=(t1 + "\n" + titl)
	        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
	        	except:
	        		try:
	        			titl=req["titl"][1]
		        		dow1=req["url"][0]
		        		q1=req["url"][1]
		        		dow2=req["url"][2]
		        		q2=req["url"][3]
		        		dow3=req["url"][4]
		        		q3=req["url"][5]
		        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
		        		bo2 = types.InlineKeyboardButton(text=q2,url=dow2)
		        		bo3 = types.InlineKeyboardButton(text=q3,url=dow3)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(bo1,bo2,bo3,sers)
		        		m=(t1 + "\n" + titl)
		        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
		        	except:
		        		try:
		        			titl=req["titl"][1]
			        		dow1=req["url"][0]
			        		q1=req["url"][1]
			        		dow2=req["url"][2]
			        		q2=req["url"][3]
			        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
			        		bo2 = types.InlineKeyboardButton(text=q2,url=dow2)
			        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
			        		Keyboards = types.InlineKeyboardMarkup()
			        		Keyboards.row_width = 1
			        		Keyboards.add(bo1,bo2,sers)
			        		m=(t1 + "\n" + titl)
			        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
			        	except:
			        		try:
			        			titl=req["titl"][1]
				        		dow1=req["url"][0]
				        		q1=req["url"][1]
				        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
				        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
				        		Keyboards = types.InlineKeyboardMarkup()
				        		Keyboards.row_width = 1
				        		Keyboards.add(bo1,sers)
				        		m=(t1 + "\n" + titl)
				        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
				        	except:
				        		pass
        	except:
        		pass
        	try:
        		f1=re["url"][3]
        		t1=re["titl"][3]
        		req=requests.get(f"https://filmdown.smoka.repl.co/?name={f1}").json()
        		res=requests.get(f1).text
        		immg=res.split('''data-lazy-style="--img:url(''')[1].split(")")[0]
        		try:
	        		titl=req["titl"][1]
	        		dow1=req["url"][0]
	        		q1=req["url"][1]
	        		dow2=req["url"][2]
	        		q2=req["url"][3]
	        		dow3=req["url"][4]
	        		q3=req["url"][5]
	        		dow4=req["url"][6]
	        		q4=req["url"][7]
	        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
	        		bo2 = types.InlineKeyboardButton(text=q2,url=dow2)
	        		bo3 = types.InlineKeyboardButton(text=q3,url=dow3)
	        		bo4 = types.InlineKeyboardButton(text=q4,url=dow4)
	        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(bo1,bo2,bo3,bo4,sers)
	        		m=(t1 + "\n" + titl)
	        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
	        	except:
	        		try:
	        			titl=req["titl"][1]
		        		dow1=req["url"][0]
		        		q1=req["url"][1]
		        		dow2=req["url"][2]
		        		q2=req["url"][3]
		        		dow3=req["url"][4]
		        		q3=req["url"][5]
		        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
		        		bo2 = types.InlineKeyboardButton(text=q2,url=dow2)
		        		bo3 = types.InlineKeyboardButton(text=q3,url=dow3)
		        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
		        		Keyboards = types.InlineKeyboardMarkup()
		        		Keyboards.row_width = 1
		        		Keyboards.add(bo1,bo2,bo3,sers)
		        		m=(t1 + "\n" + titl)
		        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
		        	except:
		        		try:
		        			titl=req["titl"][1]
			        		dow1=req["url"][0]
			        		q1=req["url"][1]
			        		dow2=req["url"][2]
			        		q2=req["url"][3]
			        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
			        		bo2 = types.InlineKeyboardButton(text=q2,url=dow2)
			        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
			        		Keyboards = types.InlineKeyboardMarkup()
			        		Keyboards.row_width = 1
			        		Keyboards.add(bo1,bo2,sers)
			        		m=(t1 + "\n" + titl)
			        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
			        	except:
			        		try:
			        			titl=req["titl"][1]
				        		dow1=req["url"][0]
				        		q1=req["url"][1]
				        		bo1 = types.InlineKeyboardButton(text=q1,url=dow1)
				        		sers = types.InlineKeyboardButton(text="🎬 بحث آخر",callback_data="welcome")
				        		Keyboards = types.InlineKeyboardMarkup()
				        		Keyboards.row_width = 1
				        		Keyboards.add(bo1,sers)
				        		m=(t1 + "\n" + titl)
				        		bot.send_photo(message.chat.id, immg, caption=m ,parse_mode='html', reply_markup=Keyboards)
				        	except:
				        		pass
        	except:
        		pass
	        
        	
        		
        		





        	
          
    	
    	
    	

        try:
            
            bot.polling(True)
        except Exception as ex:
            print(ex)
            telebot.logger.error(ex)
    except:
        continue
