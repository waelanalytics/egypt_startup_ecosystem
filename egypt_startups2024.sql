-- 1. إنشاء قاعدة بيانات جديدة للمشروع
CREATE DATABASE Egypt_Startups_DB;

-- 2. استخدام قاعدة البيانات
USE Egypt_Startups_DB;

-- 3. إنشاء الجدول
CREATE TABLE Startups (
    id INT AUTO_INCREMENT PRIMARY KEY, -- رقم تسلسلي للشركة
    Company VARCHAR(100),              -- اسم الشركة
    Sector VARCHAR(50),                -- القطاع (Fintech, HealthTech...)
    Founded_Year INT,                  -- سنة التأسيس
    Funding_USD_Millions DECIMAL(10,2),-- التمويل (يقبل كسور عشرية)
    City VARCHAR(50),                  -- المدينة
    Stage VARCHAR(50)                  -- المرحلة (Series A, Seed...)
);

SELECT * FROM Startups;

SELECT 
    Sector, 
    COUNT(*) as Company_Count, -- عدد الشركات في كل قطاع
    SUM(Funding_USD_Millions) as Total_Funding -- إجمالي التمويل
FROM Startups
GROUP BY Sector
ORDER BY Total_Funding DESC;

SELECT 
    Company, 
    Sector, 
    Funding_USD_Millions 
FROM Startups
ORDER BY Funding_USD_Millions DESC
LIMIT 5;

SELECT 
    Founded_Year, 
    COUNT(*) as New_Companies
FROM Startups
GROUP BY Founded_Year
ORDER BY Founded_Year DESC;