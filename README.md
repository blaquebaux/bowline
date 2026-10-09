# bowline

**The glide path (target-date de-risking) — an edge, or just a schedule?**

A bowline is a fixed loop that won't slip. Target-date funds glide from equity-heavy (young) to
bond-heavy (near the date). Does gliding *add value* over a static mix — or is it a marketing schedule
whose only real job is sequence-of-returns protection (shielding the largest balance from a late crash)?
Alpaca SIP daily, total-return; the sample stands in for one investor's horizon.

## Verdict

**CONDITIONAL — no return edge; its value is sequence-of-returns protection.** The glide is
indistinguishable from its own average static allocation on return and Sharpe (the *timing* of the
de-risk adds nothing), but it does the one thing it's designed for: a materially shallower drawdown late
in the horizon, when the dollar balance is largest and a crash does the most damage.

| book | CAGR | Sharpe | maxDD | late-⅓ DD |
|---|---|---|---|---|
| glide 90% → 40% equity | +10.2% | +0.88 | −25% | **−9%** |
| static 65/35 (the glide's average) | +10.6% | +0.91 | −23% | −12% |
| static 60/40 | +9.9% | +0.92 | −22% | −11% |
| static 90/10 | +13.8% | +0.89 | −31% | −17% |
| SPY (all equity) | +15.0% | +0.88 | −34% | −19% |

*2016-01 … 2026-07 (10.5y).*

- **The timing adds no edge.** The glide (+10.2%, Sharpe 0.88) ≈ a *static* 65/35 (+10.6%, 0.91) — the
  same average equity weight, held constant, does just as well. Gliding is not alpha; it's a schedule for
  *when* you hold what.
- **But the schedule has a real job.** The glide's **late-third drawdown is −9%**, versus −17% for a
  static 90/10 and −19% for all-equity. Because it de-risks as the horizon (and the balance) grows, a
  late crash hits a smaller equity share — exactly the sequence-of-returns risk a retiree can't afford.
  Early, it's *more* aggressive (grow a small balance); late, it's defensive (protect a large one).

So the glide isn't a free lunch and it isn't a fraud: it trades a little terminal wealth (vs staying
aggressive) for a much gentler drawdown precisely when drawdowns matter most in dollars. That's horizon
risk-management — the same family as [`bide`](https://github.com/blaquebaux/bide) and
[`barbell`](https://github.com/blaquebaux/barbell): managing *when* you're exposed, not finding an edge.

## `bowline_2`

The honest test of sequence risk needs **cashflows** — regular contributions (accumulation) and
withdrawals (decumulation) — because that's where the *order* of returns actually bites (a crash just
before retirement, with no time to recover, is the whole point). Add a contribution/withdrawal path and
sweep the glide slope (aggressive vs conservative vs the "rising equity glide" variant).

## Reproduce

```bash
export ALPACA_KEY_ID=... ALPACA_SECRET_KEY=...
python3 research/bowline_1.py
```

---

*Blaque Baux — a Carter Warrens research initiative. Research only; not investment advice. The verdict
falls where the data puts it — the glide doesn't beat the market, it just picks a better time to be scared.*
