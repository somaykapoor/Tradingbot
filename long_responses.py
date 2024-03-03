import random

R_EATING = "I am a Bot and I don't eat obviously!"
R_ADVICE = "If I were you, I would go to the internet and buy Tata Power Stocks Immediately!"
R_BUYING = "Paper Trading Begins: Purchased 10 Units of Agro Tech"
R_BALANCE = "The Balance is Rs. 15689.2156 Units: 516"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response