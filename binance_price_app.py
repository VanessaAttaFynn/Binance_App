import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import pandas as pd
import webbrowser
import requests



st.set_page_config(page_title='BINANCE PRICE APP', layout='wide')

#------------------------------------------------------------------------------------------------------------------------
# Stylesheet link for bootstap icons
#------------------------------------------------------------------------------------------------------------------------

st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.3/font/bootstrap-icons.css">',
    unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu("Crypto App", ["Quick Start", "Dashboard","Price Prediction","Model Monitering","Support"],
                         icons=['journal-bookmark-fill','clipboard-data', 'boxes', 'speedometer','gear'],
                         menu_icon="currency-exchange", default_index=0,
                         styles={"nav-link": {"--hover-color": "#092701"}}
                        )


if selected == "Quick Start":
	head_img, head_title = st.columns([1,4])
	head_img.markdown("####")
	
	head_img.image("images/monic.png")
	
	head_title.markdown('''# **Binance Price App**
		Cryptocurrency price app pulling data from Binance API''')
	
	st.markdown("____")
	
	st.subheader("Quick Start")
	video_file = open('images/The Weeknd - Save Your Tears (Official Music Video).mp4', 'rb')
	video_bytes = video_file.read()
	
	st.video(video_bytes)

	read_paper =  st.button("Read full paper")
	if read_paper:
		url = "https://www.linkedin.com/in/vanessa-atta-fynn/"
		webbrowser.open_new_tab(url)

if selected == "Dashboard":
	head_img, head_title = st.columns([1,4])
	head_img.markdown("####")
	
	head_img.image("images/crypto.png")
	
	head_title.markdown('''# **Binance Price App**
		Cryptocurrency price app pulling data from Binance API''')
	
	st.markdown("____")
	
	#Load market data from Binance API
	data = pd.read_json("https://api.binance.com/api/v3/ticker/24hr")

	#Custom function for rounding values
	def round_value(input_value):
		if input_value.values > 1:
			a = float(round(input_value, 2))
		else:
			a = float(round(input_value, 8))
		return a

	# Select Cryptocurrency
	coins = st.multiselect("Crypto",options=data['symbol'].unique(),default=['ETHBTC','LTCBTC',
		'BNBBTC','NEOBTC','QTUMETH','EOSETH','SNTETH','BNTETH','BCCBTC','GASBTC'])
	
	st.markdown("#")
	col1, col2, col3 = st.columns(3)

	#Widget (Cryptocurrency selection box)
	
	col1_selection = coins[0]
	col2_selection = coins[1]
	col3_selection = coins[2]
	col4_selection = coins[3]
	col5_selection = coins[4]
	col6_selection = coins[5]
	col7_selection = coins[6]
	col8_selection = coins[7]
	col9_selection = coins[8]
	
	#Dataframe for respective cryptocurrency
	col1_df = data[data['symbol'] == col1_selection]
	col2_df = data[data['symbol'] == col2_selection]
	col3_df = data[data['symbol'] == col3_selection]
	col4_df = data[data['symbol'] == col4_selection]
	col5_df = data[data['symbol'] == col5_selection]
	col6_df = data[data['symbol'] == col6_selection]
	col7_df = data[data['symbol'] == col7_selection]
	col8_df = data[data['symbol'] == col8_selection]
	col9_df = data[data['symbol'] == col9_selection]
	
	#Applying a custom function to round prices
	col1_price = round_value(col1_df['weightedAvgPrice'])
	col2_price = round_value(col2_df['weightedAvgPrice'])
	col3_price = round_value(col3_df['weightedAvgPrice'])
	col4_price = round_value(col4_df['weightedAvgPrice'])
	col5_price = round_value(col5_df['weightedAvgPrice'])
	col6_price = round_value(col6_df['weightedAvgPrice'])
	col7_price = round_value(col7_df['weightedAvgPrice'])
	col8_price = round_value(col8_df['weightedAvgPrice'])
	col9_price = round_value(col9_df['weightedAvgPrice'])
	
	#Select the priceChangePercent column
	col1_percent = f'{float(col1_df["priceChangePercent"])}%'
	col2_percent = f'{float(col2_df["priceChangePercent"])}%'
	col3_percent = f'{float(col3_df["priceChangePercent"])}%'
	col4_percent = f'{float(col4_df["priceChangePercent"])}%'
	col5_percent = f'{float(col5_df["priceChangePercent"])}%'
	col6_percent = f'{float(col6_df["priceChangePercent"])}%'
	col7_percent = f'{float(col7_df["priceChangePercent"])}%'
	col8_percent = f'{float(col8_df["priceChangePercent"])}%'
	col9_percent = f'{float(col9_df["priceChangePercent"])}%'
	
	#Create a metrics price box
	col1.metric(col1_selection, col1_price,col1_percent)
	col2.metric(col2_selection, col2_price,col2_percent)
	col3.metric(col3_selection, col3_price,col3_percent)
	col1.metric(col4_selection, col4_price,col4_percent)
	col2.metric(col5_selection, col5_price,col5_percent)
	col3.metric(col6_selection, col6_price,col6_percent)
	col1.metric(col7_selection, col7_price,col7_percent)
	col2.metric(col8_selection, col8_price,col8_percent)
	col3.metric(col9_selection, col9_price,col9_percent)
	
	st.markdown("#")
	expander1 = st.expander("View All Data")
	expander1.write(data)



#------------------------------------------------------------------------------------------------------------------------------
# THIS IS THE SUPPORT PAGE
#------------------------------------------------------------------------------------------------------------------------------


if selected == "Support":
	choose = option_menu(None,["Ask A Question","Resources","Contact"], 
		icons=['question-circle', 'bookmarks','person-rolodex'],default_index=0,orientation="horizontal")
	if choose == "Ask A Question":
		st.subheader("Frequently Asked Questions")
		faq_expander = st.expander("FAQ")
		faq_expander.markdown("No questions posted")

		form1 = st.form("Ask A Question")
		form1.text_input("Ask A Question")
		form1.form_submit_button("Post")

	if choose == "Contact":
		col7, col8 = st.columns([2,1])
		col7.image("images/profile.png")
		with col8:
			st.markdown('#')
			st.markdown('#')
			st.markdown('#')
			st.markdown("<center><p style='font-size:30px; font-weight:bold'>Vanessa Atta-Fynn</p>\
				<p >Data Analyst | Machine Learning Engineer</p></center>",unsafe_allow_html=True)

			st.markdown("<center><p style='font-size:2em'>\
					<a><i class='bi bi-linkedin'></i></a>\
					<a><i class='bi bi-github'></i></a>\
					<a><i class='bi bi-twitter'></i></a>\
					<a><i class='bi bi-envelope'></i></a>\
					</p></center>",unsafe_allow_html=True)

		st.subheader("Other Apps")
		col3, col4, col5 = st.columns(3)		
		with col3:
			st.markdown("<div style='border-radius:15px;padding:3em; \
				height:12em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #3c9401;'>\
				<center><p style='font-weight:bold'>Finance App<p>\
				<a href='https://nessdat-financedemo-finance-l4zmjm.streamlitapp.com/'>\
				<button class='t1'style='background-color:#289605;color:white; border:None;border-radius:10px;\
				padding:10px;min-height:20px;min-width: 120px;' type='button'></a>\
				DEMO<i class='bi bi-chevron-double-right'></i></button>\
				</center></div>",
				unsafe_allow_html=True)

		with col4:
			st.markdown("<div style='border-radius:15px;padding:3em; \
				height:12em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #3c9401;'>\
				<center><p style='font-weight:bold'>Agriculture App<p>\
				<a href='https://nessdat-financedemo-finance-l4zmjm.streamlitapp.com/'>\
				<button class='t1'style='background-color:#289605;color:white; border:None;border-radius:10px;\
				padding:10px;min-height:20px;min-width: 120px;' type='button'></a>\
				DEMO<i class='bi bi-chevron-double-right'></i></button>\
				</center></div>",
				unsafe_allow_html=True)

		with col5:
			st.markdown("<div style='border-radius:15px;padding:3em; \
				height:12em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #3c9401;'>\
				<center><p style='font-weight:bold'>Marketing & Retail App<p>\
				<a href='https://nessdat-financedemo-finance-l4zmjm.streamlitapp.com/'>\
				<button class='t1'style='background-color:#289605;color:white; border:None;border-radius:10px;\
				padding:10px;min-height:20px;min-width: 120px;' type='button'></a>\
				DEMO<i class='bi bi-chevron-double-right'></i></button>\
				</center></div>",
				unsafe_allow_html=True)

		st.markdown("#")
		st.markdown("#")
		st.markdown("<center><p style='font-weight:bold;font-size:40px'>Big news!! I'm starting a brand🥳</p></center>",unsafe_allow_html=True)
		col1,col2,col10 = st.columns([1,2,1])
		with col2:
			st.image("images/monic.png")


