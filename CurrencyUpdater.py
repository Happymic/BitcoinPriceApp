import tkinter as tk
import requests

def get_bitcoin_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd,cny,gbp,eur,jpy"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def update_bitcoin_data():
    bitcoin_data = get_bitcoin_data()
    if "bitcoin" in bitcoin_data:
        bitcoin_prices = bitcoin_data["bitcoin"]
        usd_price.set(f"Current Bitcoin Price (USD): ${'{:,.2f}'.format(bitcoin_prices.get('usd', 0))}")
        cny_price.set(f"1 Bitcoin to CNY: ¥{'{:,.2f}'.format(bitcoin_prices.get('cny', 0))}")
        gbp_price.set(f"1 Bitcoin to GBP: £{'{:,.2f}'.format(bitcoin_prices.get('gbp', 0))}")
        eur_price.set(f"1 Bitcoin to EUR: €{'{:,.2f}'.format(bitcoin_prices.get('eur', 0))}")
        jpy_price.set(f"1 Bitcoin to JPY: ¥{'{:,.2f}'.format(bitcoin_prices.get('jpy', 0))}")
    else:
        usd_price.set("Failed to retrieve Bitcoin data")
        cny_price.set("")
        gbp_price.set("")
        eur_price.set("")
        jpy_price.set("")


window = tk.Tk()
window.title("比特币价格和汇率")

update_button = tk.Button(window, text="更新数据", command=update_bitcoin_data)
update_button.pack()

usd_price = tk.StringVar()
cny_price = tk.StringVar()
gbp_price = tk.StringVar()
eur_price = tk.StringVar()
jpy_price = tk.StringVar()

update_bitcoin_data()  # 初始化数据

usd_label = tk.Label(window, textvariable=usd_price)
cny_label = tk.Label(window, textvariable=cny_price)
gbp_label = tk.Label(window, textvariable=gbp_price)
eur_label = tk.Label(window, textvariable=eur_price)
jpy_label = tk.Label(window, textvariable=jpy_price)

usd_label.pack()
cny_label.pack()
gbp_label.pack()
eur_label.pack()
jpy_label.pack()

window.mainloop()
