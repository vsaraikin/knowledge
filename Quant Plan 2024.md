# Quant Plan 2024

## Вектора

- Трейдинг
	- Коннекторы CEX
	- Коннекторы DEX
	- MM Models
	- Statistical Arbitrage
- Алгосы
- [Blockchain](Blockchain.md)
- C++
- Архитектура

## Задачи


## Inbox

- GARCH, ARCH, ARIMA, Choletsky decomposition, LU decomposition, QR decomposition, Facebook Prophet, Stationarity, Fama-French model, investingating feature perfomance, Cointegration
- Mean-revert vs momentum strategies
- The Fama-French three-factor
- Statistical arbitrage
- Gradient boosting
- SVM
- Factor models: fundamental factors (e.g., value, momentum, volatility)
- Alternative data: satelite data, web traffic, social media sentiment
- [C++ Articles | QuantStart](https://www.quantstart.com/articles/topic/c/)
- [Python Articles | QuantStart](https://www.quantstart.com/articles/topic/python/)
- Отличие биткоин и эфир кошельков
- Написать обзоры [Review – Option Volatility & Pricing](Review%20–%20Option%20Volatility%20&%20Pricing.md) & [Review – Designing data-intensive applications](Review%20–%20Designing%20data-intensive%20applications.md)
- Прочитать книгу и законспектировать [GitHub - ethereumbook/ethereumbook: Mastering Ethereum, by Andreas M. Antonopoulos, Gavin Wood](https://github.com/ethereumbook/ethereumbook?tab=readme-ov-file)
- Прочитать книгу и законспектировать [GitHub - bitcoinbook/bitcoinbook: Mastering Bitcoin 3rd Edition - Programming the Open Blockchain](https://github.com/bitcoinbook/bitcoinbook)
- TCP/IP
- FIX
- OMS свою написать
- Оптимизация программ: [Перформанс Инженерия - Путь Программистов из Топ 10% - YouTube](https://www.youtube.com/watch?v=EjO89zgT8Hc)
- Оптимизация программ: [Bentley\_Rules.pdf](https://progforperf.github.io/Bentley_Rules.pdf)
- Brainteasers JS: [Jane Street Quant Trading Interview! - YouTube](https://www.youtube.com/watch?v=gQJTkuEVPrU)
- Repository Pattern
- [2024 Citadel Quant Trading Interview with Analysis from Real Quants - YouTube](https://www.youtube.com/watch?v=SCP7JptxPU0)
- [C++ Low Latency High Frequency Programming Course](https://hackwise.io/)


## Courses

### C++

- [Learn C++ – Skill up with our free tutorials](https://www.learncpp.com/)
### ML & DL

- [Курс Start ML - обучение Machine Learning в Python для начинающих | karpov.courses](https://karpov.courses/ml-start)
- [Dive into Deep Learning — Dive into Deep Learning 1.0.3 documentation](https://d2l.ai/)

### Computer Science

- [Teach Yourself Computer Science](https://teachyourselfcs.com/)

#### Algorithms

- [Algorithms Tutorial - GeeksforGeeks](https://www.geeksforgeeks.org/fundamentals-of-algorithms/)

### Math

- [Бесплатный курс Математика для Data Science - математический анализ с нуля для взрослых | karpov.courses](https://karpov.courses/mathsds)

## Misc Questions

How to reduce transaction costs?

- Avoid volatile times and trade during high-liquidity
- Use limit orders
- Scale trades based on liquidity?
- 

How to avoid slippage?

- Trade at high liquidity hours
- Use limit orders
- Avoid large orders on tiny markets

How to reduce market impact?

- Break into smaller pieces *(may cause slippage)*
- Dark pools – private exchanges that allow traders to place large orders without revealing their intentions to the broader market.
- Limit orders
- Smart order routing



> One common measure of liquidity is the average daily volume (it is your choice what lookback period you want to average over). As a rule of thumb, each order should not exceed 1 percent of the average daily volume.
> 
> Ernest P. Chan

Kelly criteria

[Formula determines optimal size of a series of bets or investments to maximize the long-term growth of capital, while managing risk.](https://en.wikipedia.org/wiki/Kelly_criterion)

$f^* = \frac{bp - q}{b}$

Where:
- $f^*$: The fraction of the current bankroll to wager/invest.
- $b$: The net odds received on the bet (for example, if you win $1 on a $1 bet, the net odds are 1).
- $p$: The probability of winning.
- $q$: The probability of losing (which is $(1 - p)$.

If you’re betting on an event with a 60% probability of winning (p = 0.6) and the odds are 1:1 (b = 1), then:

$f^* = \frac{(1 \times 0.6) - (1 \times 0.4)}{1} = 0.2$

This means you should wager 20% of your bankroll on this event.


What services may business sell?

- Smarter Order Routing
- Anti Sniping
- 