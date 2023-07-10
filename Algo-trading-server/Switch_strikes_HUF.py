# import xlwings as xw
import tradehull
import pandas as pd

# https://docs.google.com/spreadsheets/d/1CMAY4GmZBK1PeCKyYN_mwoieJrG7t9JYJ05jispXPzs/edit?usp=sharing
# sheet id : 1CMAY4GmZBK1PeCKyYN_mwoieJrG7t9JYJ05jispXPzs

gsheetid = "1CMAY4GmZBK1PeCKyYN_mwoieJrG7t9JYJ05jispXPzs"
sheet_name = "Sheet1" 

data=[]

gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

df = pd.read_csv(gsheet_url)
for index, row in df.iterrows():
    for column in df.columns:
        cell_value = row[column]
        if pd.isna(cell_value):  
            continue  
        data.append(cell_value)

print(data[-2])



TH = tradehull.Tradehull("ff883tlro25hje9c", "71qh5x9zbiqpa6fny4t86ubsd084ztng")
kite = TH.kite

#Opening an excel
wb = xw.Book('orders_new.xlsm')
sheet2 = wb.sheets['switch']



# Get get live pnl
# pnl = TH.get_live_pnl()

##Get order list in excel
# orders = kite.orders()
# df = pd.DataFrame(data=orders)
# df1 = df[['order_id', 'tradingsymbol', 'order_type', 'quantity', 'price']]
# df1.to_excel("orders.xlsx", sheet_name='Sheet1')
# print(df1.columns)

symbol1 = data[-2]
quantity = data[4]
transaction1 = data[5]
sl_q = data[7]
ord_type = data[-3]

symbol2 = data[-1]
transaction2 = data[6]

kite_variety = kite.VARIETY_REGULAR

if ord_type == "LIMIT":
    if quantity > sl_q:
        no_orders = quantity//sl_q
        rem = quantity - no_orders * sl_q


        for x in range(no_orders):
            bnf1 = kite.quote('NFO:' + symbol1)
            best_bid1 = bnf1['NFO:' + symbol1]['depth']['buy'][0]['price']
            best_offer1 = bnf1['NFO:' + symbol1]['depth']['sell'][0]['price']
            limit_price1 = (best_offer1 + best_bid1) / 2
            diff = round(((best_offer1 - best_bid1) * 100) % 2, 2)
            print(best_offer1, best_bid1)
            print(diff)
            if diff == 1 and transaction1 == 'BUY':
                limit_price1 = (best_offer1 + best_bid1 - 0.05) / 2
            if diff == 1 and transaction1 == 'SELL':
                limit_price1 = (best_offer1 + best_bid1 + 0.05) / 2

            order_id1 = kite.place_order(variety=kite_variety, exchange="NFO", tradingsymbol=symbol1, transaction_type=transaction1,
                             quantity=sl_q, product="NRML", order_type="LIMIT", price=limit_price1, validity="DAY",
                             disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None,
                             tag=None)
            order_status1 = kite.order_history(order_id1)
            count = 0
            try:
                while order_status1[0]['status'] != 'COMPLETE':
                    bnf1 = kite.quote('NFO:' + symbol1)
                    best_bid1 = bnf1['NFO:' + symbol1]['depth']['buy'][0]['price']
                    best_offer1 = bnf1['NFO:' + symbol1]['depth']['sell'][0]['price']
                    limit_price1 = (best_offer1 + best_bid1) / 2
                    diff = round(((best_offer1 - best_bid1) * 100) % 2, 2)
                    print(best_offer1, best_bid1)
                    if diff == 1 and transaction1 == 'BUY':
                        limit_price1 = (best_offer1 + best_bid1 - 0.05) / 2
                    if diff == 1 and transaction1 == 'SELL':
                        limit_price1 = (best_offer1 + best_bid1 + 0.05) / 2
                    order_id1 = kite.modify_order(variety=kite_variety, order_id=order_id1, parent_order_id=None, quantity=sl_q,
                                                    price=limit_price1, order_type="LIMIT", trigger_price=None, validity="DAY",
                                                    disclosed_quantity=None)
                    count = count + 1
                    print(count)
                    if count > 20 and transaction1 == "BUY":
                        order_id1 = kite.modify_order(variety=kite_variety, order_id=order_id1, parent_order_id=None, quantity=sl_q,
                                                    price=limit_price1 + .1, order_type="LIMIT", trigger_price=None, validity="DAY",
                                                    disclosed_quantity=None)
                    elif count > 20 and transaction1 == "SELL":
                        order_id1 = kite.modify_order(variety=kite_variety, order_id=order_id1, parent_order_id=None, quantity=sl_q,
                                                    price=limit_price1 - .1, order_type="LIMIT", trigger_price=None, validity="DAY",
                                                    disclosed_quantity=None)
                    order_status1 = kite.order_history(order_id1)
            except Exception as e:
                print(e)

            count = 0
            try:

                bnf2 = kite.quote('NFO:' + symbol2)
                best_bid2 = bnf2['NFO:' + symbol2]['depth']['buy'][0]['price']
                best_offer2 = bnf2['NFO:' + symbol2]['depth']['sell'][0]['price']
                limit_price2 = (best_offer2 + best_bid2) / 2
                diff = round(((best_offer2 - best_bid2) * 100) % 2, 2)
                print(best_offer2, best_bid2)
                if diff == 1 and transaction2 == 'BUY':
                    limit_price2 = (best_offer2 + best_bid2 - 0.05) / 2
                if diff == 1 and transaction2 == 'SELL':
                    limit_price2 = (best_offer2 + best_bid2 + 0.05) / 2
                order_id2 = kite.place_order(variety=kite_variety, exchange="NFO", tradingsymbol=symbol2,
                                            transaction_type=transaction2,
                                            quantity=sl_q, product="NRML", order_type="LIMIT", price=limit_price2,
                                            validity="DAY",
                                            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None,
                                            trailing_stoploss=None,
                                            tag=None)
                order_status2 = kite.order_history(order_id2)

                while order_status2[0]['status'] != 'COMPLETE':
                    bnf2 = kite.quote('NFO:' + symbol2)
                    best_bid2 = bnf2['NFO:' + symbol2]['depth']['buy'][0]['price']
                    best_offer2 = bnf2['NFO:' + symbol2]['depth']['sell'][0]['price']
                    limit_price2 = (best_offer2 + best_bid2) / 2
                    diff = round(((best_offer2 - best_bid2) * 100) % 2, 2)
                    print(best_offer2, best_bid2)
                    if diff == 1 and transaction2 == 'BUY':
                        limit_price2 = (best_offer2 + best_bid2 - 0.05) / 2
                    if diff == 1 and transaction2 == 'SELL':
                        limit_price2 = (best_offer2 + best_bid2 + 0.05) / 2
                    kite.modify_order(variety=kite_variety, order_id=order_id2, parent_order_id=None, quantity=sl_q,
                                      price=limit_price2, order_type="LIMIT", trigger_price=None, validity="DAY",
                                      disclosed_quantity=None)
                    count = count + 1
                    print(count)
                    if count > 20 and transaction2 == "BUY":
                        order_id2 = kite.modify_order(variety=kite_variety, order_id=order_id2, parent_order_id=None, quantity=sl_q,
                                                    price=limit_price2 + .1, order_type="LIMIT", trigger_price=None, validity="DAY",
                                                    disclosed_quantity=None)
                    elif count > 20 and transaction2 == "SELL":
                        order_id2 = kite.modify_order(variety=kite_variety, order_id=order_id2, parent_order_id=None, quantity=sl_q,
                                                    price=limit_price2 - .1, order_type="LIMIT", trigger_price=None, validity="DAY",
                                                    disclosed_quantity=None)
            except Exception as e:
                print(e)
                continue

                print()
        if rem > 0:
            kite.place_order(variety=kite_variety, exchange="NFO", tradingsymbol=symbol1, transaction_type=transaction1,
                             quantity=rem, product="NRML", order_type="MARKET", price=None, validity="DAY",
                             disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None,
                             trailing_stoploss=None,
                             tag=None)
            kite.place_order(variety=kite_variety, exchange="NFO", tradingsymbol=symbol2, transaction_type=transaction2,
                             quantity=rem, product="NRML", order_type="MARKET", price=None, validity="DAY",
                             disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None,
                             trailing_stoploss=None,
                             tag=None)

    else:
        kite.place_order(variety=kite_variety, exchange="NFO", tradingsymbol=symbol1, transaction_type=transaction1,
                         quantity=quantity, product="NRML", order_type="MARKET", price=None, validity="DAY",
                         disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None,
                         trailing_stoploss=None,
                         tag=None)
        kite.place_order(variety=kite_variety, exchange="NFO", tradingsymbol=symbol2, transaction_type=transaction2,
                         quantity=quantity, product="NRML", order_type="MARKET", price=None, validity="DAY",
                         disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None,
                         trailing_stoploss=None,
                         tag=None)


elif ord_type == "MARKET":
    if quantity > sl_q:
        no_orders = quantity // sl_q
        rem = quantity - no_orders * sl_q

        for x in range(no_orders):
            try:
                order_id1 = kite.place_order(variety=kite_variety, exchange="NFO", tradingsymbol=symbol1,
                                         transaction_type=transaction1,
                                         quantity=sl_q, product="NRML", order_type="MARKET", price=None,
                                         validity="DAY",
                                         disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None,
                                         trailing_stoploss=None,
                                         tag=None)
            except Exception as e:
                print(e)
                continue

            try:
                order_id2 = kite.place_order(variety=kite_variety, exchange="NFO", tradingsymbol=symbol2,
                                             transaction_type=transaction2,
                                             quantity=sl_q, product="NRML", order_type="MARKET", price=None,
                                             validity="DAY",
                                             disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None,
                                             trailing_stoploss=None,
                                             tag=None)
            except Exception as e:
                print(e)
                continue

        if rem > 0:
            kite.place_order(variety=kite_variety, exchange="NFO", tradingsymbol=symbol1, transaction_type=transaction1,
                             quantity=rem, product="NRML", order_type="MARKET", price=None, validity="DAY",
                             disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None,
                             trailing_stoploss=None,
                             tag=None)
            kite.place_order(variety=kite_variety, exchange="NFO", tradingsymbol=symbol2, transaction_type=transaction2,
                             quantity=rem, product="NRML", order_type="MARKET", price=None, validity="DAY",
                             disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None,
                             trailing_stoploss=None,
                             tag=None)

    else:
        kite.place_order(variety=kite_variety, exchange="NFO", tradingsymbol=symbol1, transaction_type=transaction1,
                         quantity=quantity, product="NRML", order_type="MARKET", price=None, validity="DAY",
                         disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None,
                         trailing_stoploss=None,
                         tag=None)
        kite.place_order(variety=kite_variety, exchange="NFO", tradingsymbol=symbol2, transaction_type=transaction2,
                         quantity=quantity, product="NRML", order_type="MARKET", price=None, validity="DAY",
                         disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None,
                         trailing_stoploss=None,
                         tag=None)