import penglang.modules.pengmoney as pm
import penglang.say as plsay
from decimal import Decimal

plsay.info_box(
    "Welcome to the money station."
)

coin_place = pm.PenguinSafeCoinPlace()
john_wallet = pm.PenguinCoinBag(
    balance=Decimal("50"),
    name="le wallet of john",
    owner="john"
)

@john_wallet.spend(amount=Decimal("10"), allow_debt=False)
def ice_cream(spend, name):
    plsay.penguin_speech_bubble(f"{name} buys ice cream for {spend}")

ice_cream()

john_wallet.spend(Decimal("20"), allow_debt=False)(coin_place.deposit)()


plsay.say(coin_place.storage)

for _ in range(3):
    ice_cream()

john_wallet.receive(Decimal("10"))(coin_place.withdraw)()

plsay.say(f"{', '.join(john_wallet.coin_history)}")

plsay.say(john_wallet.balance)