import pandas as pd

# بيانات حقيقية لأهم الشركات الناشئة المصرية (تم تجميعها للمشروع)
data = {
    'Company': [
        'MNT-Halan', 'Fawry', 'Swvl', 'Paymob', 'MaxAB', 'Valu', 'Thndr', 
        'Breadfast', 'MoneyFellows', 'Trella', 'Khazna', 'Yodawy', 'Mozare3', 
        'Nawy', 'Lucky', 'InstaDiet', 'Elmenus', 'Homzmart', 'Bosta', 'Rabbit',
        'Sympl', 'Telda', 'Kashat', 'Raqamyat', 'Vezeeta', 'BasharSoft (Wuzzuf)',
        'Eventtus', 'InstaPay', 'Robosta', 'WideBot'
    ],
    'Sector': [
        'Fintech', 'Fintech', 'Transport', 'Fintech', 'E-commerce', 'Fintech', 'Fintech',
        'E-commerce', 'Fintech', 'Logistics', 'Fintech', 'HealthTech', 'AgriTech',
        'PropTech', 'Fintech', 'HealthTech', 'FoodTech', 'E-commerce', 'Logistics', 'E-commerce',
        'Fintech', 'Fintech', 'Fintech', 'SaaS', 'HealthTech', 'SaaS',
        'EventTech', 'Fintech', 'AI & Tech', 'AI & Chatbots'
    ],
    'Founded_Year': [
        2018, 2008, 2017, 2015, 2018, 2017, 2019,
        2017, 2019, 2019, 2019, 2018, 2020,
        2016, 2018, 2020, 2011, 2019, 2017, 2021,
        2021, 2020, 2019, 2018, 2012, 2009,
        2012, 2021, 2016, 2016
    ],
    'Funding_USD_Millions': [
        400.0, 100.0, 150.0, 68.5, 60.0, 25.0, 22.0,
        30.0, 35.0, 42.0, 38.0, 16.0, 2.0,
        5.0, 20.0, 1.5, 10.0, 40.0, 15.0, 11.0,
        6.0, 20.0, 4.5, 2.0, 63.0, 8.0,
        3.0, 0.0, 1.0, 0.5 
        # ملاحظة: InstaPay مملوك للبنوك ولا يعتمد على تمويل استثماري كلاسيكي، وضعنا 0 أو يمكن اعتباره Corporate
    ],
    'City': [
        'Cairo', 'Cairo', 'Cairo', 'Cairo', 'Cairo', 'Giza', 'Cairo',
        'Cairo', 'Giza', 'Cairo', 'Giza', 'Cairo', 'Giza',
        'Cairo', 'Giza', 'Cairo', 'Cairo', 'Cairo', 'Cairo', 'Cairo',
        'Cairo', 'Cairo', 'Cairo', 'Cairo', 'Cairo', 'Cairo',
        'Cairo', 'Cairo', 'Alexandria', 'Cairo'
    ],
    'Stage': [
        'Unicorn', 'IPO', 'IPO', 'Series B', 'Series B', 'Series A', 'Series A',
        'Series B', 'Series B', 'Series A', 'Series A', 'Series B', 'Seed',
        'Seed', 'Series A', 'Seed', 'Series C', 'Series B', 'Series A', 'Pre-Seed',
        'Seed', 'Seed', 'Seed', 'Seed', 'Series D', 'Series B',
        'Series A', 'Corporate', 'Bootstrapped', 'Seed'
    ]
}

# تحويل البيانات إلى جدول DataFrame
df = pd.DataFrame(data)

# حفظ البيانات في ملف CSV لنستخدمه في التحليل
file_name = 'egypt_startups_2024.csv'
df.to_csv(file_name, index=False)

print("✅ تم إنشاء ملف البيانات بنجاح!")
print(f"📄 اسم الملف: {file_name}")
print(f"📊 عدد الشركات: {len(df)}")