#!/usr/bin/python3
# =============================================================================
# bowline_1.py — the glide path (target-date de-risking): edge, or just a schedule?
#
# A bowline is a fixed loop that won't slip. Target-date funds glide from equity-heavy (young) to
# bond-heavy (near the date). Does gliding ADD value vs a static mix — or is it a marketing schedule
# whose only real job is sequence-of-returns protection (shielding the LARGEST balance from a late crash)?
#   Q1  Glide (90%→40% equity) vs static 60/40 / static 90-10 / SPY — return & risk.
#   Q2  Does the TIMING of de-risking beat just holding the glide's AVERAGE static allocation?
#   Q3  Sequence-of-returns value — drawdown in the FINAL third (when the balance is largest).
# Alpaca SIP daily, total-return. The sample stands in for one investor's horizon.
# =============================================================================
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from _bowline_common import panel, rets

def metrics(r, months):
    r=np.asarray(r,float); c=np.cumprod(1+r); dd=(c/np.maximum.accumulate(c)-1).min()
    sh=r.mean()/r.std()*math.sqrt(252) if r.std()>0 else float("nan")
    cagr=c[-1]**(252/len(r))-1
    return dict(sh=sh,cagr=cagr,dd=float(dd))

def latedd(r, frac=0.33):
    r=np.asarray(r,float); k=int(len(r)*(1-frac)); seg=r[k:]
    c=np.cumprod(1+seg); return float((c/np.maximum.accumulate(c)-1).min())

def main():
    syms=["SPY","IEF","AGG","BIL"]; P,dates=panel(syms); R={s:rets(P[s]) for s in P}
    L=min(len(R[s]) for s in R); months=[d[:7] for d in dates[1:]][-L:]; r={s:R[s][-L:] for s in R}
    spy,bond=r["SPY"],r["AGG"]
    print("="*88); print("BOWLINE — the glide path (target-date de-risking): edge, or just a schedule?"); print("="*88)
    print(f"  window {dates[-L]}..{dates[-1]}  ({L/252:.1f}y) — stands in for one investor's horizon")

    eqw=np.linspace(0.90,0.40,L)                 # glide: 90% equity → 40% over the horizon
    glide=eqw*spy+(1-eqw)*bond
    avg_w=eqw.mean()
    books={
        "glide 90%→40% equity":   glide,
        f"static {avg_w*100:.0f}/{100-avg_w*100:.0f} (glide avg)": avg_w*spy+(1-avg_w)*bond,
        "static 60/40":           0.60*spy+0.40*bond,
        "static 90/10":           0.90*spy+0.10*bond,
        "SPY (all equity)":       spy,
    }
    print(f"\n  Q1/Q2  {'book':26}{'CAGR':>8}{'Sharpe':>8}{'maxDD':>8}{'late-⅓ DD':>11}")
    for k,v in books.items():
        m=metrics(v,months); print(f"         {k:26}{m['cagr']*100:>+7.1f}%{m['sh']:>+8.2f}{m['dd']*100:>+7.0f}%{latedd(v)*100:>+10.0f}%")

    print("\n  Q3  SEQUENCE-OF-RETURNS: the glide's job is a shallower drawdown LATE (biggest balance)")
    print(f"      glide late-⅓ maxDD {latedd(glide)*100:+.0f}%  vs  static-90/10 late-⅓ maxDD {latedd(books['static 90/10'])*100:+.0f}%")
    print(f"      (early, the glide is MORE aggressive to grow a small balance; late, it de-risks the large one)")

    print("\n  READ: if the glide ≈ its own average static allocation on return/Sharpe, the TIMING adds no")
    print("  edge — gliding is a schedule, not alpha. Its real value is sequence-of-returns protection: a")
    print("  shallower drawdown in the final third, when the dollar balance is largest and a crash hurts most.")
    print("  Horizon risk-management (like bide/barbell), not a return edge. bowline_2 = add contributions/")
    print("  withdrawals (the cashflow path where sequence risk actually bites) + a glide-slope sweep.")

if __name__ == "__main__":
    main()
