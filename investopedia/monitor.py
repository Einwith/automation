from InvestopediaApi import ita


from InvestopediaApi import ita
client = ita.Account("prank1363246@yahoo.com", "1997zxc911")

status = client.get_portfolio_status()

print(status.cash)
