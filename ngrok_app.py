# Phase 1 — Upgraded Knowledge Base
# More plans + better accuracy + real numbers

savings_plans_v2 = {

    # ═══════════════════════════════════
    # EXISTING PLANS — IMPROVED ACCURACY
    # ═══════════════════════════════════

    "PPF": {
        "full_name": "Public Provident Fund",
        "category": "Government Scheme",
        "interest_rate": "7.1% per annum (compounded annually)",
        "lock_in": "15 years. Partial withdrawal allowed from year 7. Loan against PPF from year 3-6.",
        "min_investment": "Rs. 500 per year minimum",
        "max_investment": "Rs. 1,50,000 per year maximum",
        "tax_section": "Section 80C",
        "tax_benefit": "EEE status — Exempt Exempt Exempt. Investment tax free + Interest tax free + Maturity tax free. Maximum 80C benefit of Rs. 46,800 per year in 30% tax slab.",
        "who_can_invest": "Any Indian resident citizen. One account per person. Minors through parents.",
        "risk_level": "ZERO RISK — backed by Government of India",
        "returns_taxable": "Completely tax free — no tax at any stage",
        "best_for": "Long term retirement savings. Best for people in 30% tax slab who want zero risk.",
        "not_suitable_for": "People needing liquidity in less than 7 years. NRIs cannot open new PPF.",
        "target_audience": "Everyone — salaried, self-employed, students, government employees",
        "real_example": "Invest maximum Rs. 1,50,000 every year for 15 years. Total invested = Rs. 22,50,000. You receive approximately Rs. 40,68,209 completely tax free at maturity!",
        "pro_tip": "Invest on April 1st each year to earn interest for full year. Even investing Rs. 500/month builds significant corpus over 15 years."
    },

    "EPF": {
        "full_name": "Employee Provident Fund",
        "category": "Government Scheme",
        "interest_rate": "8.15% per annum (FY 2023-24). Highest among all zero-risk government schemes.",
        "lock_in": "Until retirement at age 58. Partial withdrawal allowed for medical emergency, home purchase, education, marriage.",
        "min_investment": "12% of basic salary + dearness allowance is mandatory for employees earning up to Rs. 15,000 basic. Voluntary above that.",
        "max_investment": "No upper limit. Can do Voluntary Provident Fund (VPF) at higher percentage.",
        "tax_section": "Section 80C for employee contribution",
        "tax_benefit": "Employee contribution qualifies for 80C. Employer contribution is tax free. Interest is tax free if withdrawn after 5 years of continuous service.",
        "who_can_invest": "Salaried employees only — both private and government organizations with 20+ employees.",
        "risk_level": "ZERO RISK — government backed EPFO",
        "returns_taxable": "Tax free if withdrawn after 5 years of continuous service. Taxable if withdrawn before 5 years.",
        "best_for": "Best passive retirement savings for salaried employees. Money grows automatically without effort.",
        "not_suitable_for": "Self-employed, freelancers, and business owners — they cannot contribute to EPF.",
        "target_audience": "Salaried employees in private and government organizations",
        "real_example": "Basic salary Rs. 50,000/month. Employee contributes Rs. 6,000 + Employer Rs. 6,000 = Rs. 12,000/month = Rs. 1,44,000/year. At 8.15% interest over 30 years this becomes approximately Rs. 1.82 crores!",
        "pro_tip": "Check your EPFO passbook regularly at epfindia.gov.in. Ensure employer is depositing your contribution every month."
    },

    "NPS": {
        "full_name": "National Pension System",
        "category": "Government Scheme — Pension",
        "interest_rate": "9% to 12% historically (market linked). Equity NPS funds have given 10-14% over 10 years.",
        "lock_in": "Until age 60. At 60 — withdraw 60% as lump sum and use 40% to buy annuity (monthly pension).",
        "min_investment": "Rs. 500 per month minimum. No maximum limit.",
        "max_investment": "No upper limit. For self-employed: up to 20% of gross income qualifies for deduction.",
        "tax_section": "Section 80C (Rs. 1.5 lakh) PLUS Section 80CCD(1B) — EXTRA Rs. 50,000 over and above 80C!",
        "tax_benefit": "MAXIMUM TAX SAVING POSSIBLE! Rs. 1,50,000 under 80C + Rs. 50,000 under 80CCD(1B) = Total Rs. 2,00,000 deduction. Saves Rs. 62,400 in 30% slab, Rs. 41,600 in 20% slab.",
        "who_can_invest": "Any Indian citizen aged 18 to 65 years. Both salaried and self-employed.",
        "risk_level": "Low to Medium — market linked but professionally managed by PFRDA approved fund managers",
        "returns_taxable": "60% of corpus at age 60 is completely tax free. 40% used for annuity purchase is tax free at withdrawal.",
        "best_for": "BEST plan for maximum tax saving. Unique extra Rs. 50,000 deduction under 80CCD(1B) available to everyone.",
        "not_suitable_for": "People who need money before age 60. Limited liquidity until retirement.",
        "target_audience": "Everyone — especially self-employed who have no EPF and IT employees wanting maximum tax saving",
        "real_example": "Invest Rs. 12,500/month (Rs. 1.5L/year) in NPS from age 30 to 60. At 10% returns you accumulate approximately Rs. 2.83 crores! Use 60% = Rs. 1.7 crore as lump sum. Buy annuity with 40% = Rs. 1.13 crore for monthly pension of approximately Rs. 75,000!",
        "pro_tip": "Open NPS Tier 1 account for tax benefits. Tier 2 is like a mutual fund with no tax benefit but full liquidity. For self-employed the 20% of income deduction under 80CCD(1) is extremely powerful."
    },

    "ELSS": {
        "full_name": "Equity Linked Savings Scheme",
        "category": "Mutual Fund — Tax Saving",
        "interest_rate": "12% to 18% historically (market linked equity fund). ELSS funds have beaten inflation consistently over 10+ year periods.",
        "lock_in": "3 years — SHORTEST lock-in among all 80C options! PPF is 15 years, FD is 5 years, ULIP is 5 years. ELSS wins on flexibility.",
        "min_investment": "Rs. 500 per month via SIP. No minimum for lump sum.",
        "max_investment": "No limit. But 80C benefit only on first Rs. 1,50,000.",
        "tax_section": "Section 80C",
        "tax_benefit": "Invest Rs. 1,50,000 → save up to Rs. 46,800 in 30% slab. Shortest lock-in for 80C benefit.",
        "who_can_invest": "Any Indian citizen including NRIs.",
        "risk_level": "Medium to High — pure equity mutual fund. Value can fall in short term. Best for 5+ year horizon.",
        "returns_taxable": "Long Term Capital Gains (LTCG) — gains above Rs. 1,00,000 per year taxed at 10%. Below Rs. 1 lakh completely tax free!",
        "best_for": "Young IT employees (25-35 years) with long investment horizon who want high returns with tax benefit.",
        "not_suitable_for": "Risk-averse investors, senior citizens, people who cannot handle short-term losses.",
        "target_audience": "Young private employees, self-employed professionals with high income and risk appetite",
        "real_example": "SIP of Rs. 12,500/month for 10 years = Rs. 15 lakhs invested. At 14% returns you get approximately Rs. 29 lakhs. Tax saving over 10 years = approximately Rs. 3,74,400 saved in taxes (30% slab)!",
        "pro_tip": "Start ELSS SIP on 1st of every month for discipline. Choose funds with 5+ year track record. Reinvest after 3-year lock-in for compounding."
    },

    "SSY": {
        "full_name": "Sukanya Samriddhi Yojana",
        "category": "Government Scheme — Girl Child",
        "interest_rate": "8.2% per annum — highest interest rate among all small savings schemes in India!",
        "lock_in": "Account matures when girl turns 21. Can withdraw 50% when she turns 18 for education or marriage.",
        "min_investment": "Rs. 250 per year minimum — most affordable savings scheme",
        "max_investment": "Rs. 1,50,000 per year",
        "tax_section": "Section 80C",
        "tax_benefit": "EEE status — Triple tax exemption. Investment + interest + maturity all completely tax free!",
        "who_can_invest": "Parents or legal guardians of girl child. Account must be opened before girl turns 10. Maximum 2 accounts per family (exception for twins).",
        "risk_level": "ZERO RISK — Government of India guaranteed",
        "returns_taxable": "Completely tax free at all stages",
        "best_for": "BEST PLAN for parents with daughters below 10 years. Highest interest + triple tax exemption + government guarantee.",
        "not_suitable_for": "Parents of boys. Girl child above 10 years cannot open new account.",
        "target_audience": "All parents — government employees, private employees, self-employed, farmers — anyone with a daughter below 10",
        "real_example": "Open account when daughter is born. Invest Rs. 1,50,000/year for 15 years (mandatory deposit period). Total invested Rs. 22,50,000. At 8.2% she receives approximately Rs. 63,87,664 when she turns 21 — completely tax free!",
        "pro_tip": "Open at post office or authorized bank. Best return on investment for girl child education. Start as early as possible — even Rs. 250/month makes a difference."
    },

    "SCSS": {
        "full_name": "Senior Citizens Savings Scheme",
        "category": "Government Scheme — Senior Citizens",
        "interest_rate": "8.2% per annum paid quarterly — highest guaranteed return for senior citizens!",
        "lock_in": "5 years. Extendable by 3 more years. Premature withdrawal allowed with penalty.",
        "min_investment": "Rs. 1,000 minimum deposit",
        "max_investment": "Rs. 30,00,000 maximum (Rs. 30 lakhs)",
        "tax_section": "Section 80C",
        "tax_benefit": "Investment up to Rs. 1,50,000 qualifies for 80C deduction",
        "who_can_invest": "Indian citizens aged 60 years and above. Age 55-60 allowed if retired on superannuation or VRS within last 1 month.",
        "risk_level": "ZERO RISK — Government of India guaranteed with quarterly interest payout",
        "returns_taxable": "Interest income is taxable as per income tax slab. TDS deducted if interest exceeds Rs. 50,000 per year. Senior citizens can claim 80TTB deduction of Rs. 50,000 on interest.",
        "best_for": "BEST PLAN for senior citizens wanting regular income. Quarterly interest credited directly to bank account.",
        "not_suitable_for": "People below 60 years. Those who don't need regular income.",
        "target_audience": "Retired government employees, retired private employees, senior citizens above 60",
        "real_example": "Invest Rs. 15,00,000 at 8.2% interest. Receive Rs. 30,750 every quarter = Rs. 1,23,000 per year as regular pension income! After 5 years get back original Rs. 15 lakhs.",
        "pro_tip": "Available at post offices and major banks. Combine with PM Vaya Vandana Yojana for maximum senior citizen income. Use 80TTB deduction to reduce tax on interest income."
    },

    # ═══════════════════════════════════
    # NEW PLANS ADDED
    # ═══════════════════════════════════

    "VPF": {
        "full_name": "Voluntary Provident Fund",
        "category": "Government Scheme",
        "interest_rate": "8.15% per annum — same as EPF, best guaranteed return for salaried employees",
        "lock_in": "Until retirement. Same rules as EPF.",
        "min_investment": "Any amount above mandatory 12% EPF contribution",
        "max_investment": "Up to 100% of basic salary",
        "tax_section": "Section 80C",
        "tax_benefit": "Additional contribution beyond EPF qualifies for 80C. Interest tax free.",
        "who_can_invest": "Only existing EPF members — salaried employees in EPF-covered organizations",
        "risk_level": "ZERO RISK — Government of India guaranteed",
        "returns_taxable": "Tax free if withdrawn after 5 years of service",
        "best_for": "Salaried employees who have already exhausted 80C limit and want higher guaranteed returns than FD",
        "not_suitable_for": "Self-employed, freelancers, students",
        "target_audience": "IT employees, private sector employees who want to increase retirement savings",
        "real_example": "Already investing Rs. 6,000 EPF. Increase VPF by Rs. 6,000 more. Extra Rs. 72,000/year grows at guaranteed 8.15% = approximately Rs. 3,60,000 extra in 5 years!",
        "pro_tip": "Request VPF through your HR or EPFO portal. Best when you have already used full 80C limit elsewhere. Far better returns than bank FD."
    },

    "PMJJBY": {
        "full_name": "Pradhan Mantri Jeevan Jyoti Bima Yojana",
        "category": "Government Insurance",
        "interest_rate": "Pure protection — no investment returns",
        "lock_in": "1 year renewable annual plan",
        "min_investment": "Only Rs. 436 per year — auto-debited from bank account!",
        "max_investment": "Rs. 436 per year (fixed)",
        "tax_section": "Section 80C",
        "tax_benefit": "Premium of Rs. 436 qualifies for 80C deduction",
        "who_can_invest": "Indian citizens aged 18 to 50 years with a savings bank account",
        "risk_level": "ZERO financial risk — pure life insurance",
        "returns_taxable": "Death benefit of Rs. 2,00,000 completely tax free under Section 10(10D)",
        "best_for": "MOST AFFORDABLE life insurance in India. Just Rs. 1.19 per day for Rs. 2 lakh life cover!",
        "not_suitable_for": "People above 55 years. Those wanting returns on investment.",
        "target_audience": "Students, daily wage workers, low income groups, young people starting career",
        "real_example": "Pay Rs. 436/year from your bank account. Your family gets Rs. 2,00,000 if you pass away. This is the cheapest life insurance available anywhere in India!",
        "pro_tip": "Enroll through your bank branch or net banking. Auto-renews every year. Combine with PMSBY accident cover for total protection at just Rs. 456/year!"
    },

    "PMSBY": {
        "full_name": "Pradhan Mantri Suraksha Bima Yojana",
        "category": "Government Insurance",
        "interest_rate": "Pure protection — no investment returns",
        "lock_in": "1 year renewable",
        "min_investment": "Only Rs. 20 per year — less than cost of a cup of tea!",
        "max_investment": "Rs. 20 per year (fixed)",
        "tax_section": "Section 80C",
        "tax_benefit": "Premium qualifies for 80C deduction",
        "who_can_invest": "Indian citizens aged 18 to 70 years with savings bank account",
        "risk_level": "ZERO financial risk — pure accident insurance",
        "returns_taxable": "Rs. 2,00,000 for accidental death or permanent disability — completely tax free",
        "best_for": "CHEAPEST accident insurance in India. Rs. 20/year for Rs. 2 lakh accident cover!",
        "not_suitable_for": "People wanting returns on investment.",
        "target_audience": "Everyone — students, workers, employees, self-employed — universal coverage",
        "real_example": "Rs. 20/year protects you with Rs. 2,00,000 accidental death cover. Rs. 1,00,000 for partial disability. Combined with PMJJBY = Rs. 4 lakh total protection at just Rs. 456/year!",
        "pro_tip": "Enroll through your bank. Auto-deducted from savings account. Every Indian should have this — less than a rupee per day for accident protection!"
    },

    "APY": {
        "full_name": "Atal Pension Yojana",
        "category": "Government Scheme — Pension",
        "interest_rate": "Government guaranteed minimum 8% return on contribution",
        "lock_in": "Until age 60. Early exit allowed only in special circumstances.",
        "min_investment": "Rs. 42/month if joining at age 18 for Rs. 1,000/month pension",
        "max_investment": "Rs. 1,454/month if joining at age 40 for Rs. 5,000/month pension",
        "tax_section": "Section 80C",
        "tax_benefit": "Contribution qualifies for 80C deduction",
        "who_can_invest": "Indian citizens aged 18 to 40 years. Especially for unorganized sector workers NOT covered under EPF.",
        "risk_level": "ZERO RISK — Government of India guarantees minimum pension",
        "returns_taxable": "Pension income is taxable as per income tax slab",
        "best_for": "BEST pension scheme for unorganized sector, self-employed, students, gig workers, domestic workers — anyone without EPF.",
        "not_suitable_for": "People above 40 years. Those already covered under any other statutory pension scheme.",
        "target_audience": "Students with income, gig workers, domestic workers, small business owners, farmers",
        "real_example": "Join APY at age 25. Pay Rs. 376/month. At 60 you get Rs. 5,000/month guaranteed pension for life. Your spouse gets same pension after you. After both pass away, nominee gets Rs. 8.5 lakhs back!",
        "pro_tip": "Open through bank account. Choose highest pension of Rs. 5,000/month for best value. The earlier you join the lower your monthly contribution!"
    },

    "TERM_INSURANCE": {
        "full_name": "Term Life Insurance",
        "category": "Life Insurance — Pure Protection",
        "interest_rate": "No investment returns — pure life protection at lowest cost",
        "lock_in": "Policy term chosen by you (10 to 40 years)",
        "min_investment": "Rs. 600-1,200/month for Rs. 1 crore cover (age 30, non-smoker)",
        "max_investment": "Premium depends on sum assured, age, health",
        "tax_section": "Section 80C",
        "tax_benefit": "Annual premium qualifies for 80C deduction",
        "who_can_invest": "Indian citizens aged 18 to 65 years",
        "risk_level": "ZERO financial risk — guaranteed payout to family on death",
        "returns_taxable": "Death benefit completely tax free under Section 10(10D)",
        "best_for": "MUST HAVE for everyone with family dependents. Cheapest way to give your family massive financial security.",
        "not_suitable_for": "Singles with no dependents. Those who want returns on insurance premium.",
        "target_audience": "Everyone with family dependents — salaried, self-employed, government employees",
        "real_example": "30-year-old non-smoker. Rs. 1 crore cover for 30 years = approximately Rs. 800/month premium. Your family gets Rs. 1,00,00,000 tax free if something happens to you. RULE: Insurance cover should be 10-15 times your annual income!",
        "pro_tip": "Buy term insurance EARLY — premiums are much lower at younger age. Never mix insurance with investment (avoid endowment/ULIP plans). Buy pure term plan from ICICI Pru, HDFC Life, LIC — compare on PolicyBazaar."
    },

    "HEALTH_INSURANCE": {
        "full_name": "Health Insurance",
        "category": "Health Insurance",
        "interest_rate": "No returns — financial protection against medical expenses",
        "lock_in": "1 year (renewable annually)",
        "min_investment": "Rs. 500-1500/month for Rs. 5-10 lakh cover",
        "max_investment": "Based on sum insured needed",
        "tax_section": "Section 80D — SEPARATE from 80C limit!",
        "tax_benefit": "Rs. 25,000 for self and family below 60 years + Rs. 25,000 for parents below 60 = Rs. 50,000 total. Rs. 50,000 if parents are senior citizens (60+) = Rs. 75,000 total deduction!",
        "who_can_invest": "Any Indian citizen. Available for individual, family floater, senior citizens.",
        "risk_level": "ZERO financial risk — pays hospital bills directly",
        "returns_taxable": "Claim amount completely tax free",
        "best_for": "ABSOLUTELY ESSENTIAL for everyone. Medical inflation is 15% per year. One hospitalization can wipe out years of savings without insurance.",
        "not_suitable_for": "Nobody — everyone needs health insurance!",
        "target_audience": "Everyone without exception — students, employees, self-employed, senior citizens",
        "real_example": "Family floater of Rs. 10 lakh for family of 4. Annual premium approximately Rs. 18,000. Premium saves Rs. 18,000 tax under 80D. One hospitalization avoided = savings of Rs. 2-5 lakhs. Best ROI of any financial product!",
        "pro_tip": "Buy early when young and healthy — premiums much lower. Take Rs. 10-25 lakh cover for urban families (medical costs are very high). Add top-up plan for extra cover at low cost. Company insurance alone is NEVER enough."
    },

    "SIP_EQUITY": {
        "full_name": "Equity Mutual Fund SIP",
        "category": "Mutual Fund — Wealth Creation",
        "interest_rate": "12% to 15% historical long-term average. Nifty 50 has given 13.5% CAGR over last 20 years.",
        "lock_in": "No lock-in period! Withdraw anytime. But recommended for 5+ years for good returns.",
        "min_investment": "Rs. 100/month minimum SIP — most accessible investment!",
        "max_investment": "No upper limit",
        "tax_section": "No direct tax benefit (except ELSS SIP)",
        "tax_benefit": "Long Term Capital Gains above Rs. 1,00,000 taxed at only 10%. Short term at 15%.",
        "who_can_invest": "Any Indian citizen including NRIs and students with PAN and bank account",
        "risk_level": "Medium to High in short term. Low in long term (5+ years) due to market growth",
        "returns_taxable": "LTCG above Rs. 1 lakh per year at 10%. Gains below Rs. 1 lakh per year — ZERO TAX!",
        "best_for": "Best wealth creation tool over long term. Beats inflation and fixed deposits consistently over 10+ years.",
        "not_suitable_for": "People needing money within 1-2 years. Risk-averse investors who cannot handle temporary losses.",
        "target_audience": "Everyone — students can start at Rs. 100/month, IT employees can invest surplus after tax saving",
        "real_example": "Rs. 10,000/month SIP in Nifty index fund for 20 years. Total invested = Rs. 24 lakhs. Expected value at 13% returns = approximately Rs. 1,06,94,000 — over 1 CRORE! Power of compounding is real!",
        "pro_tip": "Start SIP on 5th of every month (post salary credit). Choose low-cost index funds (Nifty 50, Nifty Next 50). Never stop SIP during market falls — that is when you buy cheap. Increase SIP by 10% every year."
    },

    "SGB": {
        "full_name": "Sovereign Gold Bond",
        "category": "Gold Investment",
        "interest_rate": "2.5% per annum interest PLUS gold price appreciation. Total returns historically 10-13% per year.",
        "lock_in": "8 years maturity. Early exit allowed after 5 years on interest payment dates.",
        "min_investment": "1 gram of gold minimum",
        "max_investment": "4 kilograms per individual per year. 20 kg for trusts.",
        "tax_section": "No specific section for capital gain benefit",
        "tax_benefit": "CAPITAL GAIN ON MATURITY IS COMPLETELY TAX FREE if held till 8-year maturity! 2.5% annual interest is taxable though.",
        "who_can_invest": "Indian residents, HUFs, trusts, universities, charitable institutions",
        "risk_level": "Low — price moves with gold. But RBI guarantees redemption at prevailing gold price.",
        "returns_taxable": "2.5% interest is taxable. Capital gain at maturity is TAX FREE!",
        "best_for": "Best way to invest in gold — no making charges, no storage risk, earn interest on gold, and capital gain is tax free!",
        "not_suitable_for": "People wanting physical gold for jewelry. Those needing full liquidity before 5 years.",
        "target_audience": "Everyone wanting gold as part of portfolio — government employees, IT professionals, self-employed",
        "real_example": "Buy 10 grams SGB at Rs. 6,000/gram = invest Rs. 60,000. Earn 2.5% interest = Rs. 1,500/year. After 8 years if gold price is Rs. 10,000/gram you get Rs. 1,00,000. Capital gain of Rs. 40,000 is completely TAX FREE!",
        "pro_tip": "Buy SGB when RBI announces new series — available in tranches. Alternatively buy on NSE/BSE in secondary market. Carry in demat account — no theft or purity risk unlike physical gold."
    },

    "HOME_LOAN": {
        "full_name": "Home Loan Tax Benefits",
        "category": "Real Estate — Tax Benefits",
        "interest_rate": "Home loan interest rate 8.5-9.5%. But tax benefits reduce effective cost significantly.",
        "lock_in": "Home loan tenure 10-30 years",
        "min_investment": "Based on property value and loan eligibility",
        "max_investment": "No limit on loan amount",
        "tax_section": "Section 80C (principal) + Section 24B (interest) + Section 80EEA (first home buyers)",
        "tax_benefit": "MAXIMUM HOME LOAN BENEFIT: Rs. 1,50,000 principal under 80C + Rs. 2,00,000 interest under 24B + Rs. 1,50,000 additional interest for first home under 80EEA = TOTAL Rs. 5,00,000 deduction per year! Saves Rs. 1,56,000 tax in 30% slab!",
        "who_can_invest": "Any Indian citizen taking home loan. 80EEA only for first home buyers with loan sanctioned between April 2019 and March 2022.",
        "risk_level": "Low — property appreciates over long term",
        "returns_taxable": "Rental income from property is taxable. Capital gain on sale taxable but with indexation benefit.",
        "best_for": "IT employees and government employees buying first home. Maximum tax benefit available under multiple sections simultaneously!",
        "not_suitable_for": "People in low income brackets where EMI is a burden. Those in metros where property prices are very high relative to income.",
        "target_audience": "Salaried employees planning to buy home — private IT, government, public sector",
        "real_example": "Home loan Rs. 50 lakhs at 8.8% for 20 years. Annual interest approximately Rs. 4,30,000 (first year). Deduction under 24B = Rs. 2,00,000. Principal deduction under 80C = Rs. 1,50,000. Total deduction = Rs. 3,50,000. Tax saving = Rs. 1,09,200 per year in 30% slab!",
        "pro_tip": "Joint home loan with spouse doubles tax benefit — both can claim Rs. 2,00,000 interest and Rs. 1,50,000 principal deduction each! Check pre-payment option to save on interest."
    },

    "FD_TAX_SAVING": {
        "full_name": "Tax Saving Fixed Deposit",
        "category": "Bank Deposit — Tax Saving",
        "interest_rate": "6.5% to 7.5% per annum (varies by bank). Senior citizens get 0.25-0.50% extra.",
        "lock_in": "Exactly 5 years — NO PREMATURE WITHDRAWAL allowed for tax saving FD",
        "min_investment": "Rs. 1,000 minimum",
        "max_investment": "Rs. 1,50,000 for 80C benefit. Can invest more but no additional tax benefit.",
        "tax_section": "Section 80C",
        "tax_benefit": "Investment amount up to Rs. 1,50,000 qualifies for 80C deduction",
        "who_can_invest": "Any Indian citizen. Available at all banks and post offices.",
        "risk_level": "ZERO RISK — insured up to Rs. 5 lakhs per bank by DICGC",
        "returns_taxable": "YES — interest is fully taxable as per your income tax slab. TDS deducted if interest exceeds Rs. 40,000 per year (Rs. 50,000 for senior citizens).",
        "best_for": "Conservative investors who want guaranteed returns with 80C benefit. Best for people in 10-20% tax slab.",
        "not_suitable_for": "People in 30% tax slab — interest is fully taxable so effective return after tax is only 4.5-5%. PPF or ELSS is better.",
        "target_audience": "Risk-averse investors, senior citizens, government employees nearing retirement",
        "real_example": "Invest Rs. 1,50,000 in SBI tax saving FD at 7%. You get Rs. 2,10,384 after 5 years. Tax saved under 80C = Rs. 46,800 in 30% slab. But interest of Rs. 60,384 is taxable — net return reduces. Compare with PPF which is 100% tax free!",
        "pro_tip": "Tax saving FD gives lower effective return than PPF for people in 30% slab. Choose FD only if you have already maxed PPF and want 100% guaranteed option. Post office time deposit also qualifies for 80C."
    },

    "RD": {
        "full_name": "Recurring Deposit",
        "category": "Bank Deposit — Regular Savings",
        "interest_rate": "5.5% to 7% per annum (varies by bank and tenure)",
        "lock_in": "6 months to 10 years (chosen at opening). Premature closure allowed with penalty.",
        "min_investment": "Rs. 100 per month minimum — most accessible savings tool!",
        "max_investment": "No limit",
        "tax_section": "No direct tax benefit",
        "tax_benefit": "No 80C benefit. Interest is taxable as per slab.",
        "who_can_invest": "Any Indian citizen including students and minors (through parents)",
        "risk_level": "ZERO RISK — bank deposit, DICGC insured",
        "returns_taxable": "Yes — interest is fully taxable as per income tax slab",
        "best_for": "BEST starting investment for students and beginners. Builds discipline of regular saving. No market risk.",
        "not_suitable_for": "Tax-saving purpose. High returns. Long-term wealth creation.",
        "target_audience": "Students, beginners starting savings journey, people wanting disciplined saving habit",
        "real_example": "Student saves Rs. 1,000/month in RD for 3 years at 6.5%. Total deposited = Rs. 36,000. Maturity value = Rs. 39,536. Small amount but builds habit and emergency fund!",
        "pro_tip": "Open RD in your bank or post office. Use it to build emergency fund (6 months expenses). Once you have emergency fund switch to ELSS or SIP for better returns."
    },

    "NPS_SELF_EMPLOYED": {
        "full_name": "NPS for Self-Employed and Freelancers",
        "category": "Government Scheme — Self-Employed Special",
        "interest_rate": "9-12% market linked historically. Same as regular NPS.",
        "lock_in": "Until age 60",
        "min_investment": "Rs. 500 per month",
        "max_investment": "Up to 20% of gross total income can be deducted under 80CCD(1)",
        "tax_section": "Section 80CCD(1) + Section 80CCD(1B)",
        "tax_benefit": "MAXIMUM TAX SAVING FOR SELF-EMPLOYED! 20% of income under 80CCD(1) — MUCH MORE than 10% allowed for salaried employees! PLUS Rs. 50,000 extra under 80CCD(1B). Doctor earning Rs. 20L can deduct Rs. 4L + Rs. 50K = Rs. 4.5L!",
        "who_can_invest": "Self-employed individuals — doctors, lawyers, chartered accountants, freelancers, consultants, small business owners",
        "risk_level": "Low to medium — same as NPS",
        "returns_taxable": "60% of corpus at 60 is tax free. 40% for annuity.",
        "best_for": "BEST pension and tax saving option for self-employed who have NO EPF. Unbeatable tax deduction of 20% of income!",
        "not_suitable_for": "People needing liquidity before 60. Very high risk tolerance investors.",
        "target_audience": "Freelancers, doctors, lawyers, CAs, architects, consultants, small business owners",
        "real_example": "Freelance developer earning Rs. 15,00,000/year. Can invest Rs. 3,00,000 (20% of income) under 80CCD(1) + Rs. 50,000 under 80CCD(1B) = Rs. 3,50,000 total NPS deduction. Saves Rs. 1,09,200 in taxes! Better than any other investment for self-employed!",
        "pro_tip": "Open NPS Tier 1 account online at enps.nsdl.com. Choose aggressive life cycle fund for higher equity allocation when young. Increase contribution every year as income grows."
    },

    "EDUCATION_LOAN": {
        "full_name": "Education Loan Interest Tax Benefit",
        "category": "Education — Tax Benefit",
        "interest_rate": "8.5% to 15% (varies by bank and institution)",
        "lock_in": "Loan repayment tenure — typically 5 to 15 years",
        "min_investment": "Based on loan availed",
        "max_investment": "NO UPPER LIMIT on deduction — full interest paid is deductible!",
        "tax_section": "Section 80E — COMPLETELY SEPARATE from 80C limit!",
        "tax_benefit": "ENTIRE INTEREST AMOUNT IS DEDUCTIBLE — NO UPPER LIMIT! This is the only deduction with zero ceiling. Deduction available for 8 years or until interest is fully paid whichever is earlier.",
        "who_can_invest": "Individual who took education loan for self, spouse, children or student for whom they are legal guardian",
        "risk_level": "No financial risk — this is tax deduction not investment",
        "returns_taxable": "Not applicable — this is a deduction not an investment",
        "best_for": "Students and fresh graduates repaying education loan. Reduces effective cost of education significantly.",
        "not_suitable_for": "People without education loans.",
        "target_audience": "Students repaying education loan, young IT professionals who took loan for engineering/MBA/professional courses",
        "real_example": "Education loan Rs. 10 lakhs at 10% interest. First year interest = Rs. 1,00,000. Deduct ENTIRE Rs. 1,00,000 under 80E. In 30% tax slab saves Rs. 31,200 just on interest! Effective loan cost reduces from 10% to 6.9%!",
        "pro_tip": "Section 80E is separate from 80C — you get BOTH deductions simultaneously! Claim every year during repayment. Loan must be from scheduled bank or approved institution. Private lender loans do not qualify."
    },

    "STUDENT_SIP": {
        "full_name": "Equity SIP for Students — Start Early",
        "category": "Mutual Fund — Student Special",
        "interest_rate": "12-15% long term historical returns",
        "lock_in": "No lock-in — withdraw anytime",
        "min_investment": "Rs. 100/month — lowest minimum investment in India!",
        "max_investment": "No limit",
        "tax_section": "No direct tax benefit",
        "tax_benefit": "LTCG above Rs. 1 lakh at 10%. Gains below Rs. 1 lakh completely tax free.",
        "who_can_invest": "Anyone with PAN card and bank account including students with part-time income",
        "risk_level": "Medium — equity market. But long time horizon (40+ years if started at 20) almost eliminates risk.",
        "returns_taxable": "Yes — LTCG above Rs. 1 lakh per year at 10%",
        "best_for": "MOST POWERFUL investment for students and young people. Starting at 20 vs 30 doubles your retirement corpus thanks to compounding!",
        "not_suitable_for": "People needing money within 1-2 years.",
        "target_audience": "Students with any income — part-time job, pocket money, tuition earnings",
        "real_example": "Start Rs. 500/month SIP at age 20. Total invested by age 60 = Rs. 2,40,000. Expected corpus at 13% = approximately Rs. 1,76,49,130 — Rs. 1.76 CRORES! Same Rs. 500/month started at 30 gives only Rs. 59,41,404. Starting 10 years early gives 3X more money!",
        "pro_tip": "Open SIP in Paytm Money, Zerodha Coin or Groww with zero commission. Start with Nifty 50 index fund for beginners. Even Rs. 100/month builds the habit. Increase every year as income grows. Never stop for market falls."
    },
}

# ═══════════════════════════════════
# IMPROVED TAX SECTIONS
# ═══════════════════════════════════

tax_sections_v2 = {
    "80C": {
        "limit": "Rs. 1,50,000 per year — most important tax section",
        "what_qualifies": "EPF employee contribution, PPF, NPS (partial), ELSS, 5-year FD, NSC, SSY, SCSS, LIC premium, ULIP, home loan principal, tuition fees for children, PMJJBY, PMSBY",
        "tax_saving_30_percent": "Rs. 46,800 (30% slab + 4% cess)",
        "tax_saving_20_percent": "Rs. 31,200 (20% slab + 4% cess)",
        "tax_saving_5_percent": "Rs. 7,800 (5% slab + 4% cess)",
        "available_to": "Everyone — salaried, self-employed, students with income",
        "best_plans": "EPF + NPS + ELSS = covers full Rs. 1.5 lakh with best returns"
    },
    "80CCD_1B": {
        "limit": "Rs. 50,000 per year — EXTRA above 80C limit!",
        "what_qualifies": "Only NPS Tier 1 contribution",
        "tax_saving_30_percent": "Rs. 15,600 additional saving",
        "tax_saving_20_percent": "Rs. 10,400 additional saving",
        "available_to": "Everyone — salaried and self-employed",
        "best_plans": "Invest Rs. 50,000 in NPS to get this extra deduction"
    },
    "80D": {
        "limit": "Rs. 25,000 self+family (below 60) + Rs. 25,000 parents (below 60) = Rs. 50,000. If parents senior citizens: Rs. 75,000 total!",
        "what_qualifies": "Health insurance premium for self, spouse, children, parents. Also preventive health checkup up to Rs. 5,000.",
        "tax_saving_30_percent": "Rs. 15,600 to Rs. 23,400",
        "tax_saving_20_percent": "Rs. 10,400 to Rs. 15,600",
        "available_to": "Everyone. SEPARATE from 80C limit — you get both benefits!",
        "best_plans": "Family floater health insurance + parents health insurance"
    },
    "24B": {
        "limit": "Rs. 2,00,000 per year for self-occupied property home loan interest",
        "what_qualifies": "Interest on home loan for self-occupied property. Let-out property: entire interest deductible.",
        "tax_saving_30_percent": "Rs. 62,400",
        "tax_saving_20_percent": "Rs. 41,600",
        "available_to": "Home loan borrowers",
        "best_plans": "Home loan on self-occupied property. Joint loan doubles benefit."
    },
    "80EEA": {
        "limit": "Rs. 1,50,000 per year ADDITIONAL — over and above 24B!",
        "what_qualifies": "First home buyers. Loan sanctioned between April 2019 to March 2022. Stamp duty value up to Rs. 45 lakhs. Buyer should not own any other residential property.",
        "tax_saving_30_percent": "Rs. 46,800 additional",
        "available_to": "First time home buyers with eligible loan",
        "best_plans": "First home purchase with home loan. Total benefit with 24B = Rs. 3.5 lakh deduction!"
    },
    "80E": {
        "limit": "NO UPPER LIMIT — entire interest amount is deductible!",
        "what_qualifies": "Interest on education loan for higher education of self, spouse, children or dependent. Loan from bank or approved institution.",
        "tax_saving_30_percent": "Unlimited — depends on interest paid",
        "tax_saving_20_percent": "Unlimited",
        "available_to": "Students and parents repaying education loan",
        "best_plans": "Claim every year during loan repayment for up to 8 years"
    },
    "HRA": {
        "limit": "Minimum of: actual HRA received, 50% of basic salary (metro cities Delhi Mumbai Chennai Kolkata) or 40% (non-metro), actual rent paid minus 10% of basic salary",
        "what_qualifies": "Only for salaried employees receiving HRA as part of salary. Must pay rent to landlord (not spouse). Rent above Rs. 1 lakh/year needs landlord PAN.",
        "tax_saving_30_percent": "Rs. 50,000 to Rs. 2,00,000+ depending on city and salary",
        "available_to": "Salaried employees paying rent and receiving HRA component in salary",
        "best_plans": "Keep rent receipts. File Form 12BB with employer to claim."
    },
    "80TTA": {
        "limit": "Rs. 10,000 per year",
        "what_qualifies": "Interest on savings bank account only (NOT FD or RD)",
        "tax_saving_30_percent": "Rs. 3,120",
        "available_to": "All individuals below 60 years",
        "best_plans": "Automatic — just file ITR and claim."
    },
    "80TTB": {
        "limit": "Rs. 50,000 per year — for senior citizens only",
        "what_qualifies": "Interest from ALL deposits — savings account, FD, RD, post office deposits",
        "tax_saving_30_percent": "Rs. 15,600",
        "available_to": "Senior citizens aged 60 and above ONLY. Much better than 80TTA!",
        "best_plans": "Claim on SCSS interest, bank FD interest, post office deposit interest."
    },
    "80G": {
        "limit": "50% to 100% of donation amount depending on organization",
        "what_qualifies": "Donations to approved charitable organizations, PM Relief Fund, temples, hospitals",
        "tax_saving_30_percent": "Rs. 31,200 for Rs. 1 lakh donation to 100% eligible fund",
        "available_to": "Everyone donating to approved organizations",
        "best_plans": "PM CARES Fund, PMNRF, National Defence Fund give 100% deduction."
    }
}

# ═══════════════════════════════════
# IMPROVED AUDIENCE GUIDE
# ═══════════════════════════════════

audience_guide_v2 = {
    "IT Employee (Private Sector)": {
        "recommended_plans": ["EPF", "NPS", "ELSS", "VPF", "TERM_INSURANCE", "HEALTH_INSURANCE", "SIP_EQUITY", "HOME_LOAN", "SGB"],
        "priority_action": "Max out 80C with EPF+ELSS, get extra NPS 80CCD(1B) benefit, buy term insurance",
        "monthly_plan": "EPF (auto) + Rs. 12,500 ELSS SIP + Rs. 4,167 NPS = full Rs. 2 lakh deduction",
        "tax_saving": "Up to Rs. 62,400 in 30% slab + health insurance 80D savings"
    },
    "Government Employee": {
        "recommended_plans": ["EPF", "NPS", "PPF", "SCSS", "HEALTH_INSURANCE", "HOME_LOAN", "SGB", "TERM_INSURANCE"],
        "priority_action": "Contribute to NPS Tier 1, maximize PPF, buy health insurance for family",
        "monthly_plan": "NPS (from salary) + Rs. 12,500 PPF + health insurance premium",
        "tax_saving": "Up to Rs. 78,000 in 30% slab with NPS + PPF + health insurance"
    },
    "Self Employed": {
        "recommended_plans": ["NPS_SELF_EMPLOYED", "ELSS", "PPF", "HEALTH_INSURANCE", "TERM_INSURANCE", "SIP_EQUITY", "SGB"],
        "priority_action": "Open NPS for 20% income deduction, buy health and term insurance, invest in PPF",
        "monthly_plan": "Rs. 12,500 NPS + Rs. 12,500 ELSS + health insurance + term insurance",
        "tax_saving": "Up to Rs. 1,09,200+ in 30% slab with NPS self-employed benefit"
    },
    "Student": {
        "recommended_plans": ["STUDENT_SIP", "RD", "APY", "PMJJBY", "PMSBY", "EDUCATION_LOAN"],
        "priority_action": "Start SIP immediately even Rs. 100/month, join APY for pension, get PMSBY accident cover",
        "monthly_plan": "Rs. 100-1000 SIP + Rs. 42-291 APY contribution",
        "tax_saving": "Education loan interest deduction under 80E if applicable"
    },
    "Senior Citizen (60+)": {
        "recommended_plans": ["SCSS", "FD_TAX_SAVING", "SGB", "HEALTH_INSURANCE", "APY"],
        "priority_action": "Invest in SCSS for highest guaranteed income, buy senior citizen health insurance",
        "monthly_plan": "SCSS for quarterly income + FD for safety + health insurance",
        "tax_saving": "80TTB Rs. 50,000 interest deduction + 80D Rs. 50,000 health insurance = Rs. 1 lakh deduction"
    },
    "Public Sector Employee": {
        "recommended_plans": ["EPF", "VPF", "NPS", "PPF", "HOME_LOAN", "SGB", "HEALTH_INSURANCE"],
        "priority_action": "Maximize VPF over EPF, invest in NPS for extra deduction, buy home for tax benefit",
        "monthly_plan": "EPF+VPF (auto) + Rs. 4,167 NPS + health insurance",
        "tax_saving": "Up to Rs. 78,000 in 30% slab with combined EPF+NPS+PPF"
    },
    "Freelancer or Consultant": {
        "recommended_plans": ["NPS_SELF_EMPLOYED", "ELSS", "PPF", "HEALTH_INSURANCE", "TERM_INSURANCE", "SIP_EQUITY"],
        "priority_action": "NPS 20% income deduction is your EPF substitute — open immediately!",
        "monthly_plan": "15-20% of monthly income in NPS + ELSS SIP + health insurance",
        "tax_saving": "20% of income + Rs. 50,000 extra NPS = massive deduction unique to self-employed"
    }
}

print("=" * 55)
print("SmartSave AI v2 — Upgraded Knowledge Base")
print("=" * 55)

categories = {}
for key, plan in savings_plans_v2.items():
    cat = plan["category"].split(" — ")[0]
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(key)

for cat, plans in categories.items():
    print(f"\n{cat}:")
    for p in plans:
        print(f"  ✅ {p} — {savings_plans_v2[p]['full_name']}")

print(f"\nTax Sections ({len(tax_sections_v2)}):")
for s in tax_sections_v2:
    print(f"  ✅ Section {s} — {tax_sections_v2[s]['limit'][:40]}")

print(f"\nAudience Guides ({len(audience_guide_v2)}):")
for a, d in audience_guide_v2.items():
    print(f"  👥 {a}: {len(d['recommended_plans'])} plans")

print(f"\nTotal plans: {len(savings_plans_v2)}")
print(f"Total tax sections: {len(tax_sections_v2)}")
print(f"Total audiences: {len(audience_guide_v2)}")
print("\nSmartSave AI v2 knowledge base ready!")


# Phase 2 — Cell: 3 Professional AI Agent Tools

import json
from groq import Groq

client = Groq(api_key="your_groq_api")

# ════════════════════════════
# TOOL 1 — TAX CALCULATOR
# ════════════════════════════

def calculate_tax_savings(annual_income, tax_slab, investments):
    """
    Calculate exact tax savings from investments.
    investments = dict of {plan_name: amount}
    """
    slab_rates = {
        "5%":  0.05,
        "10%": 0.10,
        "20%": 0.20,
        "30%": 0.30
    }

    cess_rate = 0.04
    rate = slab_rates.get(tax_slab, 0.20)
    effective_rate = rate * (1 + cess_rate)

    results = {}
    total_deduction = 0
    total_tax_saved = 0

    # Section 80C limit
    sec_80c_limit = 150000
    sec_80c_used = 0
    sec_80c_plans = ["EPF", "PPF", "ELSS", "NPS",
                     "VPF", "SSY", "SCSS", "FD",
                     "NSC", "PMJJBY", "PMSBY",
                     "TERM_INSURANCE"]

    for plan, amount in investments.items():
        deduction = 0

        if plan in sec_80c_plans:
            remaining_80c = sec_80c_limit - sec_80c_used
            deduction = min(amount, remaining_80c)
            sec_80c_used += deduction

        elif plan == "NPS_EXTRA":
            deduction = min(amount, 50000)

        elif plan == "HEALTH_INSURANCE":
            deduction = min(amount, 75000)

        elif plan == "HOME_LOAN_INTEREST":
            deduction = min(amount, 200000)

        elif plan == "HOME_LOAN_FIRST":
            deduction = min(amount, 150000)

        elif plan == "EDUCATION_LOAN":
            deduction = amount  # No limit!

        tax_saved = deduction * effective_rate
        total_deduction += deduction
        total_tax_saved += tax_saved

        results[plan] = {
            "invested": amount,
            "deduction": deduction,
            "tax_saved": round(tax_saved)
        }

    return {
        "annual_income": annual_income,
        "tax_slab": tax_slab,
        "investments": results,
        "total_deduction": total_deduction,
        "total_tax_saved": round(total_tax_saved),
        "effective_savings_percent": round(
            (total_tax_saved / annual_income) * 100, 2
        )
    }

# ════════════════════════════
# TOOL 2 — INVESTMENT CALCULATOR
# ════════════════════════════

def calculate_investment_returns(
    monthly_amount, years, expected_return_percent, plan_name
):
    """
    Calculate investment maturity value using
    compound interest formula.
    """
    r = expected_return_percent / 100 / 12
    n = years * 12
    monthly = float(monthly_amount)

    if r == 0:
        future_value = monthly * n
    else:
        future_value = monthly * (
            ((1 + r) ** n - 1) / r
        ) * (1 + r)

    total_invested = monthly * n
    total_returns = future_value - total_invested
    returns_multiple = round(future_value / total_invested, 1)

    milestones = {}
    for yr in [5, 10, 15, 20, 25, 30]:
        if yr <= years:
            n_temp = yr * 12
            if r == 0:
                fv_temp = monthly * n_temp
            else:
                fv_temp = monthly * (
                    ((1 + r) ** n_temp - 1) / r
                ) * (1 + r)
            milestones[f"{yr} years"] = round(fv_temp)

    return {
        "plan": plan_name,
        "monthly_investment": monthly_amount,
        "years": years,
        "expected_return": expected_return_percent,
        "total_invested": round(total_invested),
        "maturity_value": round(future_value),
        "total_returns": round(total_returns),
        "returns_multiple": returns_multiple,
        "milestones": milestones
    }

# ════════════════════════════
# TOOL 3 — PLAN COMPARATOR
# ════════════════════════════

def compare_plans(plan1_key, plan2_key):
    """
    Compare two savings plans side by side.
    """
    comparison_data = {
        "PPF": {
            "returns": "7.1%", "risk": "Zero",
            "lock_in": "15 years", "tax_benefit": "80C + EEE",
            "liquidity": "Low", "best_for": "Long term safe",
            "min": "Rs. 500/yr", "max": "Rs. 1.5L/yr"
        },
        "EPF": {
            "returns": "8.15%", "risk": "Zero",
            "lock_in": "Till retirement", "tax_benefit": "80C",
            "liquidity": "Low", "best_for": "Salaried retirement",
            "min": "12% basic", "max": "Unlimited VPF"
        },
        "NPS": {
            "returns": "9-12%", "risk": "Low-Medium",
            "lock_in": "Till age 60", "tax_benefit": "80C + 80CCD(1B)",
            "liquidity": "Very Low", "best_for": "Max tax saving",
            "min": "Rs. 500/mo", "max": "Unlimited"
        },
        "ELSS": {
            "returns": "12-15%", "risk": "Medium-High",
            "lock_in": "3 years", "tax_benefit": "80C",
            "liquidity": "Medium", "best_for": "High returns + tax",
            "min": "Rs. 500/mo", "max": "Unlimited"
        },
        "SSY": {
            "returns": "8.2%", "risk": "Zero",
            "lock_in": "21 years (girl child)",
            "tax_benefit": "80C + EEE",
            "liquidity": "Very Low",
            "best_for": "Girl child future",
            "min": "Rs. 250/yr", "max": "Rs. 1.5L/yr"
        },
        "SCSS": {
            "returns": "8.2%", "risk": "Zero",
            "lock_in": "5 years", "tax_benefit": "80C",
            "liquidity": "Medium", "best_for": "Senior income",
            "min": "Rs. 1,000", "max": "Rs. 30L"
        },
        "FD_TAX_SAVING": {
            "returns": "6.5-7.5%", "risk": "Zero",
            "lock_in": "5 years", "tax_benefit": "80C",
            "liquidity": "None", "best_for": "Safe guaranteed",
            "min": "Rs. 1,000", "max": "Rs. 1.5L (80C)"
        },
        "SIP_EQUITY": {
            "returns": "12-15%", "risk": "Medium-High",
            "lock_in": "None", "tax_benefit": "None",
            "liquidity": "High", "best_for": "Wealth creation",
            "min": "Rs. 100/mo", "max": "Unlimited"
        },
        "SGB": {
            "returns": "2.5% + gold price",
            "risk": "Low",
            "lock_in": "8 years (exit at 5)",
            "tax_benefit": "Tax free at maturity",
            "liquidity": "Low", "best_for": "Gold investment",
            "min": "1 gram", "max": "4 kg/yr"
        },
        "HEALTH_INSURANCE": {
            "returns": "Protection only",
            "risk": "Zero financial",
            "lock_in": "1 year", "tax_benefit": "80D",
            "liquidity": "N/A", "best_for": "Medical protection",
            "min": "Rs. 500/mo", "max": "Based on cover"
        },
        "TERM_INSURANCE": {
            "returns": "Protection only",
            "risk": "Zero financial",
            "lock_in": "Policy term",
            "tax_benefit": "80C",
            "liquidity": "N/A",
            "best_for": "Family protection",
            "min": "Rs. 600/mo", "max": "Based on cover"
        },
        "APY": {
            "returns": "Guaranteed pension",
            "risk": "Zero",
            "lock_in": "Till age 60",
            "tax_benefit": "80C",
            "liquidity": "None",
            "best_for": "Unorganized sector pension",
            "min": "Rs. 42/mo", "max": "Rs. 1,454/mo"
        }
    }

    p1 = comparison_data.get(plan1_key, {})
    p2 = comparison_data.get(plan2_key, {})

    if not p1 or not p2:
        return {
            "error": f"Plan data not found for {plan1_key} or {plan2_key}"
        }

    winner = {}
    if p1.get("returns", "0") > p2.get("returns", "0"):
        winner["returns"] = plan1_key
    else:
        winner["returns"] = plan2_key

    if p1.get("risk") == "Zero" and p2.get("risk") != "Zero":
        winner["safety"] = plan1_key
    elif p2.get("risk") == "Zero":
        winner["safety"] = plan2_key
    else:
        winner["safety"] = "Both similar"

    return {
        "plan1": {"key": plan1_key, "details": p1},
        "plan2": {"key": plan2_key, "details": p2},
        "winners": winner,
        "recommendation": f"Choose {plan1_key} for: {p1.get('best_for')}. Choose {plan2_key} for: {p2.get('best_for')}"
    }

# ════════════════════════════
# TEST ALL 3 TOOLS
# ════════════════════════════

print("=" * 55)
print("PHASE 2 — TOOL TESTING")
print("=" * 55)

# Test 1 — Tax Calculator
print("\nTEST 1 — Tax Calculator")
print("-" * 40)
result = calculate_tax_savings(
    annual_income=1200000,
    tax_slab="30%",
    investments={
        "EPF": 72000,
        "ELSS": 78000,
        "NPS_EXTRA": 50000,
        "HEALTH_INSURANCE": 25000,
        "HOME_LOAN_INTEREST": 180000
    }
)
print(f"Income: Rs. {result['annual_income']:,}")
print(f"Total deduction: Rs. {result['total_deduction']:,}")
print(f"Total tax saved: Rs. {result['total_tax_saved']:,}")
print(f"Savings as % of income: {result['effective_savings_percent']}%")
for plan, data in result["investments"].items():
    if data["deduction"] > 0:
        print(f"  {plan}: Rs. {data['deduction']:,} deduction → Rs. {data['tax_saved']:,} saved")

# Test 2 — Investment Calculator
print("\nTEST 2 — Investment Calculator")
print("-" * 40)
result2 = calculate_investment_returns(
    monthly_amount=10000,
    years=20,
    expected_return_percent=13,
    plan_name="Equity SIP"
)
print(f"Monthly SIP: Rs. {result2['monthly_investment']:,}")
print(f"Duration: {result2['years']} years")
print(f"Expected return: {result2['expected_return']}%")
print(f"Total invested: Rs. {result2['total_invested']:,}")
print(f"Maturity value: Rs. {result2['maturity_value']:,}")
print(f"Your money grows: {result2['returns_multiple']}x!")
print("Milestones:")
for yr, val in result2["milestones"].items():
    print(f"  After {yr}: Rs. {val:,}")

# Test 3 — Plan Comparator
print("\nTEST 3 — Plan Comparator")
print("-" * 40)
result3 = compare_plans("PPF", "ELSS")
print(f"Comparing: {result3['plan1']['key']} vs {result3['plan2']['key']}")
for field, val in result3["plan1"]["details"].items():
    val2 = result3["plan2"]["details"].get(field, "N/A")
    print(f"  {field:12} | {str(val):25} | {val2}")
print(f"Recommendation: {result3['recommendation']}")


# Cell 5 — Write app using separate file writing
# This avoids ALL escape issues!

part1 = """import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from groq import Groq
import os

st.set_page_config(
    page_title="SmartSave AI",
    page_icon="$",
    layout="wide"
)

st.markdown("""

part2 = """<style>
    .stApp {
        background: linear-gradient(
            135deg, #0A2010 0%, #0F3A1A 25%,
            #1A4A0D 50%, #0F3A1A 75%, #061208 100%
        );
        background-size: 400% 400%;
        animation: emeraldShift 10s ease infinite;
    }
    @keyframes emeraldShift {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg, #061208 0%, #0A2010 100%
        ) !important;
        border-right: 1px solid #22C55E !important;
    }

    /* ALL INPUT LABELS VISIBLE */
    label {
        color: #4ADE80 !important;
        font-weight: 600 !important;
        font-size: 13px !important;
    }
    div[data-testid="stNumberInput"] label,
    div[data-testid="stSelectbox"] label,
    div[data-testid="stTextInput"] label {
        color: #4ADE80 !important;
        font-weight: 600 !important;
        visibility: visible !important;
        opacity: 1 !important;
    }

    /* INPUT FIELDS */
    .stTextInput > div > div > input {
        background-color: rgba(10,32,16,0.9) !important;
        color: #86EFAC !important;
        border: 1px solid #22C55E !important;
        border-radius: 10px !important;
    }
    .stTextInput > div > div > input::placeholder {
        color: #4ADE80 !important;
        opacity: 0.6 !important;
    }
    div[data-testid="stNumberInput"] input {
        background-color: rgba(10,32,16,0.9) !important;
        color: #86EFAC !important;
        border: 1px solid #22C55E !important;
        border-radius: 8px !important;
    }
    div[data-testid="stNumberInput"] button {
        background-color: rgba(10,32,16,0.9) !important;
        color: #4ADE80 !important;
        border: 1px solid #22C55E !important;
    }

    /* SELECTBOX */
    .stSelectbox > div > div {
        background-color: rgba(10,32,16,0.9) !important;
        color: #86EFAC !important;
        border: 1px solid #22C55E !important;
        border-radius: 8px !important;
    }
    div[data-testid="stSelectbox"] * {
        color: #86EFAC !important;
    }

    /* BUTTONS */
    .stButton > button {
        background-color: #16A34A !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        font-weight: bold !important;
        width: 100% !important;
        height: 45px !important;
    }
    .stButton > button:hover {
        background-color: #15803D !important;
    }

    /* TABS */
    .stTabs [data-baseweb="tab-list"] {
        background-color: rgba(10,32,16,0.8) !important;
        border-radius: 10px !important;
    }
    .stTabs [data-baseweb="tab"] {
        color: #86EFAC !important;
    }
    .stTabs [data-baseweb="tab"] p {
        color: #86EFAC !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #16A34A !important;
        border-radius: 8px !important;
    }
    .stTabs [aria-selected="true"] p {
        color: white !important;
    }

    /* GENERAL TEXT */
    p { color: #86EFAC !important; }
    h1, h2, h3, h4 { color: #4ADE80 !important; }
    span { color: #86EFAC !important; }

    /* MARKDOWN */
    .stMarkdown p { color: #86EFAC !important; }
    .stMarkdown h3 { color: #4ADE80 !important; }

    /* SCROLLBAR */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #061208; }
    ::-webkit-scrollbar-thumb {
        background: #16A34A;
        border-radius: 3px;
    }

    /* SPINNER */
    .stSpinner > div {
        border-top-color: #4ADE80 !important;
    }
</style>
"""

part3 = """, unsafe_allow_html=True)

# ── KNOWLEDGE BASE ──
@st.cache_resource
def load_everything():
    savings_plans = {
        "PPF": {"full_name":"Public Provident Fund","category":"Government Scheme","interest_rate":"7.1%","lock_in":"15 years","min_investment":"Rs. 500/yr","max_investment":"Rs. 1,50,000/yr","tax_section":"Section 80C","tax_benefit":"EEE triple tax free","who_can_invest":"Any Indian citizen","risk":"Zero risk","returns_taxable":"No","best_for":"Long term retirement savings","target_audience":"Everyone","example":"Rs. 1.5L/yr for 15 years gives Rs. 40 lakhs tax free!","pro_tip":"Invest on April 1st for maximum interest."},
        "EPF": {"full_name":"Employee Provident Fund","category":"Government Scheme","interest_rate":"8.15%","lock_in":"Until retirement","min_investment":"12% of basic","max_investment":"Unlimited VPF","tax_section":"Section 80C","tax_benefit":"Both contributions tax free","who_can_invest":"Salaried employees only","risk":"Zero risk","returns_taxable":"No after 5 years","best_for":"Automatic retirement savings","target_audience":"Private and Government employees","example":"Basic Rs. 50K gives Rs. 1.44L saved per year!","pro_tip":"Check EPFO passbook at epfindia.gov.in regularly."},
        "NPS": {"full_name":"National Pension System","category":"Government Scheme","interest_rate":"9-12% market linked","lock_in":"Until age 60","min_investment":"Rs. 500/month","max_investment":"Unlimited","tax_section":"80C plus 80CCD(1B)","tax_benefit":"MAXIMUM Rs. 2 lakh total deduction","who_can_invest":"18-65 years all citizens","risk":"Low to medium","returns_taxable":"40% tax free","best_for":"Maximum tax saving plus pension","target_audience":"Everyone especially self-employed","example":"Rs. 2L deduction saves Rs. 62,400 in 30% slab!","pro_tip":"Extra 80CCD Rs. 50K is unique to NPS."},
        "ELSS": {"full_name":"Equity Linked Savings Scheme","category":"Mutual Fund","interest_rate":"12-15% historical","lock_in":"3 years only","min_investment":"Rs. 500/month SIP","max_investment":"Unlimited","tax_section":"Section 80C","tax_benefit":"Rs. 1.5L deduction","who_can_invest":"Any Indian citizen","risk":"Medium to high","returns_taxable":"LTCG above Rs. 1L at 10%","best_for":"Young earners high returns plus tax","target_audience":"Private employees self-employed","example":"Rs. 12,500/month for 10 years gives Rs. 29 lakhs!","pro_tip":"Start SIP on 1st of month. Choose 5 year track record funds."},
        "SSY": {"full_name":"Sukanya Samriddhi Yojana","category":"Government Scheme","interest_rate":"8.2%","lock_in":"Until daughter turns 21","min_investment":"Rs. 250/yr","max_investment":"Rs. 1,50,000/yr","tax_section":"Section 80C","tax_benefit":"EEE triple tax free","who_can_invest":"Parents of girl child below 10","risk":"Zero risk","returns_taxable":"No","best_for":"Girl child education and marriage","target_audience":"All parents with daughter","example":"Rs. 1.5L/yr gives Rs. 63 lakhs for daughter!","pro_tip":"Open at post office. Highest rate small savings."},
        "SCSS": {"full_name":"Senior Citizens Savings Scheme","category":"Government Scheme","interest_rate":"8.2% quarterly","lock_in":"5 years","min_investment":"Rs. 1,000","max_investment":"Rs. 30,00,000","tax_section":"Section 80C","tax_benefit":"Investment qualifies for 80C","who_can_invest":"Age 60 and above only","risk":"Zero risk","returns_taxable":"Yes above Rs. 50,000","best_for":"BEST for senior citizens guaranteed income","target_audience":"Senior citizens aged 60 and above","example":"Rs. 15L gives Rs. 1,23,000 per year quarterly income!","pro_tip":"Combine with 80TTB deduction."},
        "VPF": {"full_name":"Voluntary Provident Fund","category":"Government Scheme","interest_rate":"8.15% same as EPF","lock_in":"Until retirement","min_investment":"Any above EPF","max_investment":"100% of basic salary","tax_section":"Section 80C","tax_benefit":"Additional 80C benefit","who_can_invest":"Existing EPF members only","risk":"Zero risk","returns_taxable":"Tax free after 5 years","best_for":"Salaried wanting more than EPF","target_audience":"IT and private sector employees","example":"Extra Rs. 72,000/yr grows to Rs. 3.6L in 5 years!","pro_tip":"Request VPF through HR. Better than bank FD."},
        "APY": {"full_name":"Atal Pension Yojana","category":"Government Scheme","interest_rate":"Guaranteed pension","lock_in":"Until age 60","min_investment":"Rs. 42/month","max_investment":"Rs. 1,454/month","tax_section":"Section 80C","tax_benefit":"Qualifies for 80C","who_can_invest":"18-40 years unorganized sector","risk":"Zero risk","returns_taxable":"Pension taxable","best_for":"Pension for unorganized sector","target_audience":"Students workers self-employed","example":"Join at 25 pay Rs. 376/month get Rs. 5,000/month pension!","pro_tip":"Join early for lowest contribution."},
        "PMJJBY": {"full_name":"PM Jeevan Jyoti Bima Yojana","category":"Government Insurance","interest_rate":"Protection only","lock_in":"1 year renewable","min_investment":"Rs. 436/year","max_investment":"Rs. 436/year","tax_section":"Section 80C","tax_benefit":"Premium qualifies for 80C","who_can_invest":"18-50 years with bank account","risk":"Zero financial risk","returns_taxable":"Rs. 2L death benefit tax free","best_for":"Cheapest life insurance India","target_audience":"Students workers low income groups","example":"Rs. 436/year gives Rs. 2 lakh life cover!","pro_tip":"Enroll through bank. Auto-renews annually."},
        "PMSBY": {"full_name":"PM Suraksha Bima Yojana","category":"Government Insurance","interest_rate":"Protection only","lock_in":"1 year renewable","min_investment":"Rs. 20/year","max_investment":"Rs. 20/year","tax_section":"Section 80C","tax_benefit":"Premium qualifies for 80C","who_can_invest":"18-70 years with bank account","risk":"Zero financial risk","returns_taxable":"Rs. 2L accident cover tax free","best_for":"Cheapest accident insurance India","target_audience":"Everyone universal coverage","example":"Rs. 20/year gives Rs. 2 lakh accident cover!","pro_tip":"Combine with PMJJBY for Rs. 4L protection at Rs. 456/yr!"},
        "TERM_INSURANCE": {"full_name":"Term Life Insurance","category":"Life Insurance","interest_rate":"Pure protection","lock_in":"Policy term","min_investment":"Rs. 600-1200/month","max_investment":"Based on cover","tax_section":"Section 80C","tax_benefit":"Premium qualifies for 80C","who_can_invest":"18-65 years","risk":"Zero financial risk","returns_taxable":"Death benefit tax free","best_for":"MUST HAVE family protection","target_audience":"Everyone with family dependents","example":"Rs. 1 crore cover for Rs. 800/month at age 30!","pro_tip":"Buy term early. 10-15x annual income as cover."},
        "HEALTH_INSURANCE": {"full_name":"Health Insurance","category":"Health Insurance","interest_rate":"Protection plan","lock_in":"1 year renewable","min_investment":"Rs. 500-1500/month","max_investment":"Based on cover","tax_section":"Section 80D","tax_benefit":"Rs. 25K self plus Rs. 50K with parents","who_can_invest":"Any Indian citizen","risk":"Zero financial risk","returns_taxable":"Claims tax free","best_for":"ESSENTIAL medical protection","target_audience":"Everyone without exception","example":"Rs. 15K premium saves Rs. 15K tax plus Rs. 10L cover!","pro_tip":"Take Rs. 10-25L cover. Company insurance alone never enough."},
        "SIP_EQUITY": {"full_name":"Equity Mutual Fund SIP","category":"Mutual Fund","interest_rate":"12-15% long term","lock_in":"No lock-in","min_investment":"Rs. 100/month","max_investment":"Unlimited","tax_section":"No direct benefit","tax_benefit":"LTCG above Rs. 1L at 10%","who_can_invest":"Any Indian citizen","risk":"Medium to high","returns_taxable":"Yes LTCG STCG","best_for":"Long term wealth creation","target_audience":"Everyone start at Rs. 100!","example":"Rs. 10,000/month for 20 years gives Rs. 1.14 crore!","pro_tip":"Start SIP on 5th of month. Never stop during market falls."},
        "SGB": {"full_name":"Sovereign Gold Bond","category":"Gold Investment","interest_rate":"2.5% plus gold price","lock_in":"8 years exit at 5","min_investment":"1 gram gold","max_investment":"4 kg per year","tax_section":"No specific section","tax_benefit":"Capital gain tax FREE at maturity","who_can_invest":"Any Indian citizen","risk":"Low government backed","returns_taxable":"No capital gain if held to maturity","best_for":"Best digital gold investment","target_audience":"Everyone wanting gold","example":"10g at Rs. 6K/g earns Rs. 1,500/year plus gold price!","pro_tip":"Buy when RBI announces new series."},
        "HOME_LOAN": {"full_name":"Home Loan Tax Benefits","category":"Real Estate","interest_rate":"8.5-9.5% loan rate","lock_in":"10-30 years","min_investment":"Based on property","max_investment":"Unlimited","tax_section":"80C plus 24B plus 80EEA","tax_benefit":"Rs. 5L total deduction first home!","who_can_invest":"Home loan borrowers","risk":"Low long term","returns_taxable":"Rental income taxable","best_for":"First home buyers maximum tax","target_audience":"All employees buying home","example":"First home loan gives Rs. 5L tax deductions per year!","pro_tip":"Joint loan doubles benefit."},
        "FD_TAX_SAVING": {"full_name":"Tax Saving Fixed Deposit","category":"Bank Deposit","interest_rate":"6.5-7.5%","lock_in":"5 years no premature","min_investment":"Rs. 1,000","max_investment":"Rs. 1.5L for 80C","tax_section":"Section 80C","tax_benefit":"Investment qualifies for 80C","who_can_invest":"Any Indian citizen","risk":"Zero risk DICGC insured","returns_taxable":"Yes interest fully taxable","best_for":"Safe guaranteed returns","target_audience":"Risk averse conservative investors","example":"Rs. 1L at 7% for 5 years gives Rs. 1,40,255!","pro_tip":"Better for low tax slabs. PPF better in 30% slab."},
        "RD": {"full_name":"Recurring Deposit","category":"Bank Deposit","interest_rate":"5.5-7%","lock_in":"6 months to 10 years","min_investment":"Rs. 100/month","max_investment":"Unlimited","tax_section":"No direct benefit","tax_benefit":"No 80C benefit","who_can_invest":"Any Indian including students","risk":"Zero risk","returns_taxable":"Yes fully taxable","best_for":"Building savings discipline","target_audience":"Students beginners","example":"Rs. 1,000/month for 3 years gives Rs. 39,536!","pro_tip":"Use for emergency fund then switch to ELSS."},
        "EDUCATION_LOAN": {"full_name":"Education Loan Tax Benefit","category":"Education","interest_rate":"Interest deductible","lock_in":"Repayment tenure","min_investment":"Based on loan","max_investment":"NO LIMIT","tax_section":"Section 80E","tax_benefit":"ENTIRE interest deductible NO LIMIT","who_can_invest":"Students repaying education loan","risk":"No risk deduction","returns_taxable":"Not applicable","best_for":"Students repaying education loan","target_audience":"Students fresh graduates","example":"Paying Rs. 50K interest? Deduct entire amount no limit!","pro_tip":"Claim every year during repayment for 8 years."},
        "STUDENT_SIP": {"full_name":"Student SIP Start Early","category":"Student Plan","interest_rate":"12-15% long term","lock_in":"No lock-in","min_investment":"Rs. 100/month","max_investment":"Unlimited","tax_section":"No direct benefit","tax_benefit":"LTCG at 10% only","who_can_invest":"Students with any income","risk":"Medium","returns_taxable":"Yes LTCG","best_for":"Building wealth from student age","target_audience":"Students start NOW!","example":"Rs. 500/month from age 20 gives Rs. 1.76 crore by 60!","pro_tip":"Start today even Rs. 100. Increase every year."},
        "NPS_SELF_EMPLOYED": {"full_name":"NPS for Self-Employed","category":"Self-Employed Plan","interest_rate":"9-12% market linked","lock_in":"Until age 60","min_investment":"Rs. 500/month","max_investment":"20% of gross income","tax_section":"80CCD(1) plus 80CCD(1B)","tax_benefit":"20% of income PLUS Rs. 50K extra MAXIMUM!","who_can_invest":"Self-employed freelancers doctors lawyers","risk":"Low to medium","returns_taxable":"40% tax free","best_for":"Maximum tax for self-employed","target_audience":"Freelancers consultants doctors lawyers","example":"Income Rs. 20L gives Rs. 4.5L NPS deduction!","pro_tip":"Best pension option for self-employed who have no EPF."}
    }

    tax_sections = {
        "80C": "Rs. 1.5 lakh limit. EPF PPF NPS ELSS FD SSY SCSS LIC term insurance home loan principal. Saves Rs. 46,800 in 30% slab.",
        "80CCD_1B": "Extra Rs. 50,000 for NPS above 80C limit. Saves Rs. 15,600 in 30% slab.",
        "80D": "Health insurance Rs. 25,000 self plus Rs. 25,000 parents equals Rs. 50,000. Rs. 75,000 if parents senior citizens.",
        "24B": "Home loan interest Rs. 2 lakh deduction.",
        "80EEA": "First home buyers Rs. 1.5 lakh additional on home loan interest.",
        "80E": "Education loan entire interest deductible NO UPPER LIMIT.",
        "HRA": "House Rent Allowance saves Rs. 50,000 to Rs. 2 lakhs.",
        "80TTA": "Savings account interest Rs. 10,000 deduction for everyone.",
        "80TTB": "Senior citizens Rs. 50,000 on all deposit interest.",
        "80G": "Donations 50% to 100% deductible based on organization."
    }

    audience_guide = {
        "IT Employee": ["EPF","NPS","ELSS","VPF","TERM_INSURANCE","HEALTH_INSURANCE","SIP_EQUITY","HOME_LOAN"],
        "Government Employee": ["EPF","NPS","PPF","SCSS","HEALTH_INSURANCE","HOME_LOAN","SGB","TERM_INSURANCE"],
        "Self Employed": ["NPS_SELF_EMPLOYED","ELSS","PPF","HEALTH_INSURANCE","TERM_INSURANCE","SIP_EQUITY","SGB"],
        "Student": ["STUDENT_SIP","APY","PMJJBY","PMSBY","EDUCATION_LOAN","RD"],
        "Senior Citizen": ["SCSS","FD_TAX_SAVING","SGB","HEALTH_INSURANCE"],
        "Public Sector": ["EPF","VPF","NPS","PPF","HOME_LOAN","SGB","HEALTH_INSURANCE"],
        "Freelancer": ["NPS_SELF_EMPLOYED","ELSS","PPF","HEALTH_INSURANCE","TERM_INSURANCE","SIP_EQUITY"]
    }

    comparison_data = {
        "PPF": {"returns":"7.1%","risk":"Zero","lock_in":"15 years","tax_benefit":"80C + EEE","liquidity":"Low","best_for":"Long term safe","min":"Rs. 500/yr","max":"Rs. 1.5L/yr"},
        "EPF": {"returns":"8.15%","risk":"Zero","lock_in":"Till retirement","tax_benefit":"80C","liquidity":"Low","best_for":"Salaried retirement","min":"12% basic","max":"Unlimited VPF"},
        "NPS": {"returns":"9-12%","risk":"Low-Medium","lock_in":"Till age 60","tax_benefit":"80C + 80CCD(1B)","liquidity":"Very Low","best_for":"Max tax saving","min":"Rs. 500/mo","max":"Unlimited"},
        "ELSS": {"returns":"12-15%","risk":"Medium-High","lock_in":"3 years","tax_benefit":"80C","liquidity":"Medium","best_for":"High returns + tax","min":"Rs. 500/mo","max":"Unlimited"},
        "SSY": {"returns":"8.2%","risk":"Zero","lock_in":"21 years","tax_benefit":"80C + EEE","liquidity":"Very Low","best_for":"Girl child future","min":"Rs. 250/yr","max":"Rs. 1.5L/yr"},
        "SCSS": {"returns":"8.2% quarterly","risk":"Zero","lock_in":"5 years","tax_benefit":"80C","liquidity":"Medium","best_for":"Senior income","min":"Rs. 1,000","max":"Rs. 30L"},
        "FD_TAX_SAVING": {"returns":"6.5-7.5%","risk":"Zero","lock_in":"5 years","tax_benefit":"80C","liquidity":"None","best_for":"Safe guaranteed","min":"Rs. 1,000","max":"Rs. 1.5L"},
        "SIP_EQUITY": {"returns":"12-15%","risk":"Medium-High","lock_in":"None","tax_benefit":"None","liquidity":"High","best_for":"Wealth creation","min":"Rs. 100/mo","max":"Unlimited"},
        "SGB": {"returns":"2.5% + gold","risk":"Low","lock_in":"8 years","tax_benefit":"Tax free maturity","liquidity":"Low","best_for":"Gold investment","min":"1 gram","max":"4 kg/yr"},
        "HEALTH_INSURANCE": {"returns":"Protection","risk":"Zero","lock_in":"1 year","tax_benefit":"80D","liquidity":"N/A","best_for":"Medical protection","min":"Rs. 500/mo","max":"Based on cover"},
        "TERM_INSURANCE": {"returns":"Protection","risk":"Zero","lock_in":"Policy term","tax_benefit":"80C","liquidity":"N/A","best_for":"Family protection","min":"Rs. 600/mo","max":"Based on cover"},
        "APY": {"returns":"Guaranteed pension","risk":"Zero","lock_in":"Till age 60","tax_benefit":"80C","liquidity":"None","best_for":"Unorganized sector","min":"Rs. 42/mo","max":"Rs. 1,454/mo"}
    }

    docs = []
    for key, plan in savings_plans.items():
        content = (
            "PLAN: " + plan["full_name"] + " (" + key + ")\\n"
            "CATEGORY: " + plan["category"] + "\\n"
            "INTEREST: " + plan["interest_rate"] + "\\n"
            "LOCK-IN: " + plan["lock_in"] + "\\n"
            "TAX SECTION: " + plan["tax_section"] + "\\n"
            "TAX BENEFIT: " + plan["tax_benefit"] + "\\n"
            "WHO: " + plan["who_can_invest"] + "\\n"
            "RISK: " + plan["risk"] + "\\n"
            "BEST FOR: " + plan["best_for"] + "\\n"
            "TARGET: " + plan["target_audience"] + "\\n"
            "EXAMPLE: " + plan["example"] + "\\n"
            "PRO TIP: " + plan["pro_tip"]
        )
        docs.append(Document(page_content=content,
            metadata={"plan_key":key,"plan_name":plan["full_name"],
                      "category":plan["category"],"target":plan["target_audience"]}))

    for section, detail in tax_sections.items():
        docs.append(Document(page_content="TAX SECTION " + section + ": " + detail,
            metadata={"plan_key":"TAX_"+section,"plan_name":"Section "+section,"category":"Tax Section","target":"Everyone"}))

    for audience, plans in audience_guide.items():
        docs.append(Document(page_content="AUDIENCE GUIDE for " + audience + ": Best plans are " + ", ".join(plans),
            metadata={"plan_key":"GUIDE_"+audience,"plan_name":"Guide for "+audience,"category":"Audience Guide","target":audience}))

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = FAISS.from_documents(docs, embeddings)
    return vectordb, savings_plans, audience_guide, comparison_data


with st.spinner("Loading SmartSave AI v2..."):
    vectordb, savings_plans, audience_guide, comparison_data = load_everything()

client = Groq(api_key=os.environ.get("GROQ_API_KEY", "your_groq_api_key"))


def calculate_tax_savings(annual_income, tax_slab, investments):
    slab_rates = {"5%":0.05,"10%":0.10,"20%":0.20,"30%":0.30}
    rate = slab_rates.get(tax_slab, 0.20) * 1.04
    results = {}
    total_deduction = 0
    total_tax_saved = 0
    sec_80c_limit = 150000
    sec_80c_used = 0
    sec_80c_plans = ["EPF","PPF","ELSS","NPS","VPF","SSY","SCSS","FD","NSC","PMJJBY","PMSBY","TERM_INSURANCE"]
    for plan, amount in investments.items():
        deduction = 0
        if plan in sec_80c_plans:
            remaining = sec_80c_limit - sec_80c_used
            deduction = min(amount, remaining)
            sec_80c_used += deduction
        elif plan == "NPS_EXTRA":
            deduction = min(amount, 50000)
        elif plan == "HEALTH_INSURANCE":
            deduction = min(amount, 75000)
        elif plan == "HOME_LOAN_INTEREST":
            deduction = min(amount, 200000)
        elif plan == "HOME_LOAN_FIRST":
            deduction = min(amount, 150000)
        elif plan == "EDUCATION_LOAN":
            deduction = amount
        tax_saved = deduction * rate
        total_deduction += deduction
        total_tax_saved += tax_saved
        if deduction > 0:
            results[plan] = {"invested":amount,"deduction":deduction,"tax_saved":round(tax_saved)}
    return {"total_deduction":total_deduction,"total_tax_saved":round(total_tax_saved),"breakdown":results}


def calculate_investment_returns(monthly_amount, years, return_percent, plan_name):
    r = return_percent / 100 / 12
    n = years * 12
    if r == 0:
        fv = monthly_amount * n
    else:
        fv = monthly_amount * (((1+r)**n - 1)/r) * (1+r)
    total_invested = monthly_amount * n
    milestones = {}
    for yr in [5,10,15,20,25,30]:
        if yr <= years:
            n_t = yr * 12
            fv_t = monthly_amount * (((1+r)**n_t - 1)/r) * (1+r) if r > 0 else monthly_amount * n_t
            milestones[yr] = round(fv_t)
    return {"plan":plan_name,"monthly":monthly_amount,"years":years,
            "total_invested":round(total_invested),"maturity":round(fv),
            "returns":round(fv-total_invested),"multiple":round(fv/total_invested,1),
            "milestones":milestones}


def compare_two_plans(plan1, plan2):
    p1 = comparison_data.get(plan1, {})
    p2 = comparison_data.get(plan2, {})
    if not p1 or not p2:
        return None
    return {"plan1_key":plan1,"plan2_key":plan2,"plan1":p1,"plan2":p2}


def smartsave_answer(question, user_type="General"):
    docs = vectordb.similarity_search(question, k=3)
    context = "\\n\\n".join([d.page_content for d in docs])
    system_prompt = (
        "You are SmartSave AI — a friendly expert financial advisor for ALL Indians. "
        "Help " + user_type + " with savings plans, tax benefits and investment strategies. "
        "Use ONLY the knowledge base context. Give specific rupee amounts. "
        "Mention exact tax savings. Keep language simple and friendly. "
        "End with: Would you like to know more about any specific plan?"
    )
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"system","content":system_prompt},
            {"role":"user","content":"Context:\\n" + context + "\\n\\nQuestion: " + question}
        ]
    )
    return response.choices[0].message.content


def green_card(value, label):
    return (
        "<div style='background:rgba(10,32,16,0.8);border:1px solid #22C55E;"
        "border-radius:10px;padding:12px 16px;text-align:center;margin:4px 0;'>"
        "<div style='color:#4ADE80;font-size:20px;font-weight:bold;'>" + str(value) + "</div>"
        "<div style='color:#86EFAC;font-size:11px;'>" + label + "</div>"
        "</div>"
    )


# ── SIDEBAR ──
with st.sidebar:
    st.markdown(
        "<div style='text-align:center;padding:16px;'>"
        "<h2 style='color:#4ADE80;margin:0;'>SmartSave AI</h2>"
        "<p style='color:#86EFAC;font-size:13px;'>Your Investment Advisor</p>"
        "</div>",
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown("<p style='color:#4ADE80;font-weight:bold;font-size:14px;'>I am a...</p>", unsafe_allow_html=True)
    user_type = st.selectbox("Profile",
        ["Select profile...","IT Employee","Government Employee",
         "Self Employed","Student","Senior Citizen","Public Sector","Freelancer"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    if user_type != "Select profile...":
        matched = None
        for audience in audience_guide:
            if audience.lower() in user_type.lower() or user_type.lower() in audience.lower():
                matched = audience
                break
        if matched:
            st.markdown("<p style='color:#4ADE80;font-weight:bold;font-size:13px;'>Recommended plans:</p>", unsafe_allow_html=True)
            for plan_key in audience_guide[matched]:
                if plan_key in savings_plans:
                    plan = savings_plans[plan_key]
                    st.markdown(
                        "<div style='background:rgba(10,32,16,0.8);padding:8px;border-radius:6px;"
                        "margin:4px 0;border-left:3px solid #22C55E;'>"
                        "<span style='color:#4ADE80;font-size:12px;font-weight:bold;'>" + plan_key + "</span><br>"
                        "<span style='color:#86EFAC;font-size:11px;'>" + plan["full_name"] + "</span><br>"
                        "<span style='color:#22C55E;font-size:11px;'>" + plan["tax_section"] + "</span>"
                        "</div>",
                        unsafe_allow_html=True
                    )
    st.markdown("---")
    st.markdown(
        "<p style='color:#166534;font-size:11px;text-align:center;'>"
        "Built by Charan Sai N<br>AI Career Accelerator 2026</p>",
        unsafe_allow_html=True
    )


# ── HEADER ──
st.markdown(
    "<div style='background:linear-gradient(135deg,#052E16,#14532D);"
    "padding:24px;border-radius:12px;text-align:center;"
    "margin-bottom:20px;border:1px solid #22C55E;'>"
    "<h1 style='color:white;margin:0;font-size:32px;'>SmartSave AI</h1>"
    "<p style='color:#4ADE80;margin:4px 0;'>Personalized Investment Advisor for ALL Indians</p>"
    "<p style='color:#86EFAC;font-size:12px;margin:0;'>"
    "Government · Private · Self-Employed · Students · Senior Citizens</p>"
    "</div>",
    unsafe_allow_html=True
)


# ── TABS ──
tab1, tab2, tab3, tab4 = st.tabs([
    "Chat Advisor", "Tax Calculator",
    "Investment Calculator", "Compare Plans"
])


# ── TAB 1: CHAT ──
with tab1:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role":"assistant","content":"Hello! I am SmartSave AI — your personal investment advisor for ALL Indians! Tell me about yourself — age, employment type, monthly income and your goal. I will give you a personalized investment plan with exact rupee amounts!"}]
    if "input_key" not in st.session_state:
        st.session_state.input_key = 0
    if "last_processed" not in st.session_state:
        st.session_state.last_processed = ""
    if "saved_input" not in st.session_state:
        st.session_state.saved_input = ""

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                "<div style='display:flex;justify-content:flex-end;margin:8px 0;'>"
                "<div style='background:#14532D;color:#DCFCE7;padding:10px 16px;"
                "border-radius:18px 18px 4px 18px;max-width:80%;font-size:14px;"
                "border:1px solid #22C55E;'>" + msg["content"] + "</div></div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div style='display:flex;justify-content:flex-start;margin:8px 0;align-items:flex-start;'>"
                "<div style='background:#16A34A;color:white;border-radius:50%;width:36px;height:36px;"
                "display:flex;align-items:center;justify-content:center;margin-right:10px;"
                "font-size:16px;flex-shrink:0;'>$</div>"
                "<div style='background:rgba(10,32,16,0.9);color:#86EFAC;padding:12px 16px;"
                "border-radius:4px 18px 18px 18px;max-width:80%;font-size:14px;"
                "border:1px solid #22C55E;'>" + msg["content"] + "</div></div>",
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_input(
            "Ask",
            placeholder="Ask about savings plans, tax benefits...",
            label_visibility="collapsed",
            key="chat_input_" + str(st.session_state.input_key)
        )
    with col2:
        send = st.button("Ask")

   # Get current input value
    current_input = st.session_state.get(
        "chat_input_" + str(st.session_state.input_key), ""
    )

    msg_to_process = ""

    # Enter key pressed — user_input has value
    if current_input and current_input != st.session_state.last_processed:
        msg_to_process = current_input

    # Send button clicked — use current_input
    elif send and current_input and current_input != st.session_state.last_processed:
        msg_to_process = current_input

    if msg_to_process:
        # Mark as processed FIRST to prevent duplicate
        st.session_state.last_processed = msg_to_process

        # Clear input box
        st.session_state.input_key += 1

        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": msg_to_process
        })

        # Get AI response
        with st.spinner("SmartSave AI is thinking..."):
            reply = smartsave_answer(
                msg_to_process, user_type
            )

        # Add AI response
        st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })

        st.rerun()


# ── TAB 2: TAX CALCULATOR ──
with tab2:
    st.markdown("<h3 style='color:#4ADE80;'>Tax Savings Calculator</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#86EFAC;'>Enter your investments to calculate exact tax savings</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        income = st.number_input("Annual Income (Rs.)", min_value=100000, max_value=10000000, value=1200000, step=100000)
    with col2:
        slab = st.selectbox("Tax Slab", ["5%","10%","20%","30%"])

    st.markdown("<p style='color:#4ADE80;font-weight:bold;margin-top:16px;'>Enter your investments:</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        epf_amt = st.number_input("EPF (Rs.)", min_value=0, max_value=150000, value=72000, step=1000)
        elss_amt = st.number_input("ELSS (Rs.)", min_value=0, max_value=150000, value=78000, step=1000)
        ppf_amt = st.number_input("PPF (Rs.)", min_value=0, max_value=150000, value=0, step=1000)
    with col2:
        nps_amt = st.number_input("NPS Extra 80CCD (Rs.)", min_value=0, max_value=50000, value=50000, step=1000)
        health_amt = st.number_input("Health Insurance (Rs.)", min_value=0, max_value=75000, value=25000, step=1000)
        term_amt = st.number_input("Term Insurance (Rs.)", min_value=0, max_value=150000, value=0, step=1000)
    with col3:
        home_int = st.number_input("Home Loan Interest (Rs.)", min_value=0, max_value=350000, value=0, step=10000)
        edu_loan = st.number_input("Education Loan Interest (Rs.)", min_value=0, max_value=500000, value=0, step=5000)

    if st.button("Calculate Tax Savings"):
        investments = {}
        if epf_amt > 0: investments["EPF"] = epf_amt
        if elss_amt > 0: investments["ELSS"] = elss_amt
        if ppf_amt > 0: investments["PPF"] = ppf_amt
        if nps_amt > 0: investments["NPS_EXTRA"] = nps_amt
        if health_amt > 0: investments["HEALTH_INSURANCE"] = health_amt
        if term_amt > 0: investments["TERM_INSURANCE"] = term_amt
        if home_int > 0: investments["HOME_LOAN_INTEREST"] = home_int
        if edu_loan > 0: investments["EDUCATION_LOAN"] = edu_loan

        result = calculate_tax_savings(income, slab, investments)

        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(green_card("Rs. " + "{:,}".format(result["total_deduction"]), "Total Deduction"), unsafe_allow_html=True)
        with col2:
            st.markdown(green_card("Rs. " + "{:,}".format(result["total_tax_saved"]), "Tax Saved"), unsafe_allow_html=True)
        with col3:
            pct = str(round((result["total_tax_saved"] / income) * 100, 1)) + "%"
            st.markdown(green_card(pct, "of Income Saved"), unsafe_allow_html=True)

        st.markdown("<p style='color:#4ADE80;font-weight:bold;margin-top:16px;'>Breakdown:</p>", unsafe_allow_html=True)
        for plan, data in result["breakdown"].items():
            st.markdown(
                "<div style='background:rgba(10,32,16,0.8);padding:8px 12px;border-radius:6px;"
                "margin:4px 0;border-left:3px solid #22C55E;display:flex;justify-content:space-between;'>"
                "<span style='color:#86EFAC;'>" + plan + "</span>"
                "<span style='color:#4ADE80;font-weight:bold;'>Rs. " + "{:,}".format(data["tax_saved"]) + " saved</span>"
                "</div>",
                unsafe_allow_html=True
            )


# ── TAB 3: INVESTMENT CALCULATOR ──
with tab3:
    st.markdown("<h3 style='color:#4ADE80;'>Investment Return Calculator</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#86EFAC;'>See how your money grows over time</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        monthly = st.number_input("Monthly Amount (Rs.)", min_value=100, max_value=500000, value=10000, step=500)
    with col2:
        years = st.number_input("Years", min_value=1, max_value=40, value=20, step=1)
    with col3:
        plan_choice = st.selectbox("Plan", ["SIP Equity (13%)","ELSS (12%)","PPF (7.1%)","EPF (8.15%)","NPS (10%)","SSY (8.2%)","SCSS (8.2%)","FD (7%)","RD (6.5%)"])

    rate_map = {"SIP Equity (13%)":13,"ELSS (12%)":12,"PPF (7.1%)":7.1,"EPF (8.15%)":8.15,"NPS (10%)":10,"SSY (8.2%)":8.2,"SCSS (8.2%)":8.2,"FD (7%)":7,"RD (6.5%)":6.5}
    rate = rate_map[plan_choice]

    if st.button("Calculate Returns"):
        result = calculate_investment_returns(monthly, years, rate, plan_choice)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(green_card("Rs. " + "{:,}".format(result["total_invested"]), "Total Invested"), unsafe_allow_html=True)
        with col2:
            st.markdown(green_card("Rs. " + "{:,}".format(result["maturity"]), "Maturity Value"), unsafe_allow_html=True)
        with col3:
            st.markdown(green_card("Rs. " + "{:,}".format(result["returns"]), "Total Returns"), unsafe_allow_html=True)
        with col4:
            st.markdown(green_card(str(result["multiple"]) + "x", "Money Multiplied"), unsafe_allow_html=True)

        if result["milestones"]:
            st.markdown("<p style='color:#4ADE80;font-weight:bold;margin-top:16px;'>Growth milestones:</p>", unsafe_allow_html=True)
            cols = st.columns(len(result["milestones"]))
            for i, (yr, val) in enumerate(result["milestones"].items()):
                with cols[i]:
                    st.markdown(green_card("Rs. " + "{:,}".format(val), "After " + str(yr) + " years"), unsafe_allow_html=True)


# ── TAB 4: COMPARE PLANS ──
with tab4:
    st.markdown("<h3 style='color:#4ADE80;'>Compare Two Plans</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#86EFAC;'>Compare any two savings plans side by side</p>", unsafe_allow_html=True)

    plan_list = list(comparison_data.keys())
    col1, col2 = st.columns(2)
    with col1:
        plan1 = st.selectbox("Plan 1", plan_list, index=0)
    with col2:
        plan2 = st.selectbox("Plan 2", plan_list, index=3)

    if st.button("Compare Now"):
        result = compare_two_plans(plan1, plan2)
        if result:
            p1 = result["plan1"]
            p2 = result["plan2"]
            fields = ["returns","risk","lock_in","tax_benefit","liquidity","best_for","min","max"]
            labels = ["Returns","Risk Level","Lock-in Period","Tax Benefit","Liquidity","Best For","Min Investment","Max Investment"]
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(
                    "<div style='background:rgba(10,32,16,0.8);padding:16px;border-radius:10px;border:2px solid #22C55E;'>"
                    "<h4 style='color:#4ADE80;text-align:center;'>" + plan1 + "</h4>",
                    unsafe_allow_html=True
                )
                for field, label in zip(fields, labels):
                    st.markdown(
                        "<div style='padding:6px 0;border-bottom:1px solid rgba(34,197,94,0.2);'>"
                        "<span style='color:#86EFAC;font-size:12px;'>" + label + "</span><br>"
                        "<span style='color:#DCFCE7;font-size:13px;font-weight:bold;'>" + str(p1.get(field,"N/A")) + "</span>"
                        "</div>",
                        unsafe_allow_html=True
                    )
                st.markdown("</div>", unsafe_allow_html=True)
            with col2:
                st.markdown(
                    "<div style='background:rgba(10,32,16,0.8);padding:16px;border-radius:10px;border:2px solid #4ADE80;'>"
                    "<h4 style='color:#4ADE80;text-align:center;'>" + plan2 + "</h4>",
                    unsafe_allow_html=True
                )
                for field, label in zip(fields, labels):
                    st.markdown(
                        "<div style='padding:6px 0;border-bottom:1px solid rgba(34,197,94,0.2);'>"
                        "<span style='color:#86EFAC;font-size:12px;'>" + label + "</span><br>"
                        "<span style='color:#DCFCE7;font-size:13px;font-weight:bold;'>" + str(p2.get(field,"N/A")) + "</span>"
                        "</div>",
                        unsafe_allow_html=True
                    )
                st.markdown("</div>", unsafe_allow_html=True)


# ── FOOTER ──
st.markdown(
    "<div style='text-align:center;margin-top:30px;color:#166534;font-size:11px;'>"
    "SmartSave AI · Built by Charan Sai N · AI Career Accelerator 2026 · "
    "Not financial advice — consult a SEBI registered advisor for personal decisions"
    "</div>",
    unsafe_allow_html=True
)
"""

# Write all parts to file
with open("smartsave_app.py", "w", encoding="utf-8") as f:
    f.write(part1)
    f.write('"""')
    f.write(part2)
    f.write('"""')
    f.write(part3)

print("smartsave_app.py created successfully!")
print("Now run launch cell!")

# Cell 6 — Launch SmartSave AI Web App
from pyngrok import ngrok
import subprocess
import time

ngrok.set_auth_token("your_ngrok_key")
ngrok.kill()
time.sleep(2)

subprocess.Popen([
    "streamlit", "run", "smartsave_app.py",
    "--server.port=8502",
    "--server.headless=true"
])
time.sleep(5)

url = ngrok.connect(8502)
print("="*55)
print("SmartSave AI is LIVE!")
print(f"Open: {url}")
print("="*55)
