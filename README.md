# Project Overview

This project evaluates how the marketing department allocates its advertising budget across social media platforms. The goal was to assess current spending efficiency, understand performance patterns across markets, and provide data-driven recommendations to improve marketing ROI and guide smarter budget allocation.

---

# Main Insights

### 1. Current marketing performance is acceptable but not optimized
- Most key metrics remain relatively flat over time, suggesting limited learning or improvement in campaign strategy.  
- Performance correlates directly with spend, indicating that results scale with budget rather than increased efficiency.
              
***Recommendations:***  
- Narrow the target audience to increase relevance, reduce costs, and support stronger organic growth.  
- Current campaigns are too general—create more targeted and differentiated content tailored to specific audiences.      
### 2. Very low acquisition costs
- **CAC ≈ $0.65** and CPI ≈ $0.357, which are extremely low for the dating mobile app industry. (Typical CPI: $10–15; premium markets: $30–60)  
- These results are strong; however, without LTV data, profitability and long-term marketing efficiency cannot be fully assessed.
                 
***Recommendations:***  
- Calculate **LTV vs CAC** to understand true unit economics.  
  - If **LTV/CAC > 3:1**, increase marketing investment.  
  - If below, determine a desirable CAC and ensure marketing spend does not exceed it
### 3. High conversion rate from install to sign-up
Most countries show high conversion from install to sign-up, indicating strong initial engagement.

***Recommendation:***
- Review and simplify the sign-up process, or consider offering a trial without sign-up to further reduce friction and improve early engagement.

### 4. Channel effectiveness varies by country
Different channels perform differently across markets, showing that a uniform strategy is not cost-effective.

***Recommendations:***
- Reallocate budget using a two-step approach:
  1. Define the total budget per country based on performance and growth potential.
  2. Allocate that budget across the best-performing social media channels in each country.  
     *Channel-level recommendations are included in the analysis.*

---

# Details

### KPI Summary
Most key metrics remain relatively flat over time, suggesting limited learning or optimization in campaign strategy (left chart).  
Performance correlates directly with spend, indicating that results scale with budget rather than increased efficiency (right chart).

<img width="2850" height="730" alt="image" src="https://github.com/user-attachments/assets/edbcde5d-4e1d-4e70-a1fe-4fe56b542df4" />

### **Statistical Overview (Last 4 Months)**
- **Total new users:** 107,203  
- **Total installs:** 195,392  
- **Total spend:** $70,010
  
<img width="784" height="484" alt="image" src="https://github.com/user-attachments/assets/4bbada56-023b-4600-8941-946157723dc5" />

**Averages:**  
- **CPI:** $0.357  
- **CAC:** $0.65  

### Country Breakdown
Each country demonstrates different performance metrics. France shows the greatest potential for improving overall KPIs, supporting the idea of reallocating budget across countries.
<img width="2754" height="660" alt="image" src="https://github.com/user-attachments/assets/cc3e8809-ec97-4fd3-ac5d-aad5213626d5" />

Another visualization indicates that the current allocation has some skew, but it is not proportional, and there is still room for improvement.

<img width="884" height="433" alt="Screenshot 2025-11-28 at 21 18 46" src="https://github.com/user-attachments/assets/e039a4ff-1b56-480e-a7a1-500cad285129" />

A subsequent chart supports the high conversion rate from install to sign-up across markets.

<img width="953" height="642" alt="Screenshot 2025-11-28 at 21 20 18" src="https://github.com/user-attachments/assets/12bf6c98-a147-4a84-a772-620bad717191" />


####  US CAC and CPI Across Channels
CAC in the US shows a brief anomaly. Although it corrected quickly and does not appear problematic overall, it would be useful to understand what caused the spike.

<img width="2778" height="720" alt="image" src="https://github.com/user-attachments/assets/c66a78e7-fdc6-4503-b6cc-7a02ee367bba" />

###  Social Media Channel Breakdown
Different countries show varying levels of efficiency across channels, indicating that a unified, one-size-fits-all strategy is not effective.

<img width="2400" height="1266" alt="image" src="https://github.com/user-attachments/assets/9cc5f857-0e51-4ea9-8711-c53b4eb0c9e2" />

###  Reallocation Methodology
For budget reallocation, a **deterministic model** was used instead of more complex approaches such as Linear Optimization or Response-Curve Modeling (MMM / Bayesian / ML).  
This decision was based on limited historical data (approximately **20 events per channel**), which is insufficient for stable modeling.

 ****Method Used****
1. Compute a weight for each channel:  
   weight = 1 / CAC
2. Normalize all weights so that their sum equals 1.
3. Allocate budget according to the normalized weights.

---

### Results

| Channel               | CAC       | CPI       | inv_CAC  | Weight   | % Budget |
|----------------------|-----------|-----------|----------|----------|----------|
| FR-Google-Android    | 0.518608  | 0.236509  | 1.928238 | 0.087331 | 8.733102 |
| FR-FB-Android        | 0.526500  | 0.368316  | 1.899337 | 0.086022 | 8.602208 |
| FR-FB-iOS            | 0.643788  | 0.482186  | 1.553306 | 0.070350 | 7.035013 |
| CA-Google-Android    | 0.765125  | 0.349415  | 1.306976 | 0.059194 | 5.919369 |
| UK-Google-Android    | 0.769141  | 0.276326  | 1.300151 | 0.058885 | 5.888461 |
| UK-Apple-Ads         | 0.823924  | 0.376518  | 1.213704 | 0.054969 | 5.496935 |
| US-Google-Android    | 0.845697  | 0.349596  | 1.182456 | 0.053554 | 5.355413 |
| CA-Apple-Ads         | 0.847742  | 0.457761  | 1.179604 | 0.053425 | 5.342498 |
| UK-FB-iOS            | 0.913458  | 0.600027  | 1.094742 | 0.049581 | 4.958149 |
| US-FB-iOS            | 0.914524  | 0.653068  | 1.093465 | 0.049524 | 4.952366 |
| CA-FB-iOS            | 0.947198  | 0.700938  | 1.055746 | 0.047815 | 4.781534 |
| CA-FB-Android        | 0.999357  | 0.636208  | 1.000643 | 0.045320 | 4.531973 |
| UK-FB-Android        | 1.008566  | 0.593778  | 0.991507 | 0.044906 | 4.490592 |
| US-FB-Android        | 1.018676  | 0.663662  | 0.981666 | 0.044460 | 4.446025 |
| FR-Apple-Ads         | 1.055745  | 0.393415  | 0.947199 | 0.042899 | 4.289919 |
| US-Apple-Ads         | 1.085990  | 0.573085  | 0.920819 | 0.041704 | 4.170444 |
| FR-Google-iOS        | 1.125846  | 0.493468  | 0.888221 | 0.040228 | 4.022806 |
| UK-Google-iOS        | 1.342759  | 0.661623  | 0.744735 | 0.033729 | 3.372949 |
| US-Google-iOS        | 1.882567  | 0.722986  | 0.531190 | 0.024058 | 2.405789 |
| CA-Google-iOS        | 3.760248  | 0.852314  | 0.265940 | 0.012045 | 1.204458 |

---


