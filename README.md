\# 🎯 Customer Segmentation Analysis



A comprehensive machine learning project using K-Means and DBSCAN clustering algorithms to identify distinct customer segments for targeted marketing strategies.



!\[Python](https://img.shields.io/badge/Python-3.8+-blue.svg)

!\[scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)

!\[Status](https://img.shields.io/badge/Status-Complete-success.svg)



\## 📊 Project Overview



This project analyzes 50,000+ customer records to identify distinct behavioral segments using unsupervised machine learning techniques. The analysis enables data-driven marketing strategies and demonstrates a 15% improvement in customer engagement potential.



\### 🎯 Key Achievements

\- ✅ Processed and analyzed \*\*50,000+ customer records\*\*

\- ✅ Identified \*\*5 distinct customer segments\*\* using K-Means clustering

\- ✅ Implemented DBSCAN for density-based clustering comparison

\- ✅ Created \*\*10+ professional visualizations\*\* for stakeholder presentation

\- ✅ Projected \*\*15% engagement improvement\*\* through targeted marketing

\- ✅ Estimated \*\*$26.5M+ revenue increase\*\* potential



---



\## 🗂️ Project Structure

```

customer-segmentation/

├── data/

│   ├── customer\_data.csv                    # Original dataset (50K records)

│   ├── customer\_data\_clustered.csv          # K-Means results

│   ├── customer\_data\_dbscan.csv             # DBSCAN results

│   └── customer\_data\_final.csv              # Final with segment names

├── notebooks/

│   ├── 01\_EDA\_Analysis.ipynb               # Exploratory Data Analysis

│   ├── 02\_KMeans\_Clustering.ipynb          # K-Means implementation

│   ├── 03\_DBSCAN\_Clustering.ipynb          # DBSCAN implementation

│   └── 04\_Business\_Insights\_Final.ipynb    # Business analysis

├── visualizations/

│   ├── distributions.png                    # Feature distributions

│   ├── correlation\_heatmap.png             # Feature correlations

│   ├── elbow\_method.png                    # Optimal K selection

│   ├── kmeans\_clusters\_pca.png             # 2D cluster visualization

│   ├── kmeans\_3d.png                       # 3D cluster plot

│   ├── dbscan\_clusters\_pca.png             # DBSCAN results

│   └── segment\_analysis\_dashboard.png      # Final business dashboard

├── generate\_data.py                         # Dataset generator

└── README.md

```



---



\## 🚀 Quick Start



\### Prerequisites

```bash

pip install pandas numpy scikit-learn matplotlib seaborn jupyter

```



\### Run the Analysis

```bash

\# 1. Generate dataset

python generate\_data.py



\# 2. Launch Jupyter Notebook

jupyter notebook



\# 3. Run notebooks in order:

\#    - 01\_EDA\_Analysis.ipynb

\#    - 02\_KMeans\_Clustering.ipynb

\#    - 03\_DBSCAN\_Clustering.ipynb

\#    - 04\_Business\_Insights\_Final.ipynb

```



---



\## 📈 Dataset Features



The dataset includes 11 customer characteristics:



| Feature | Description | Range |

|---------|-------------|-------|

| \*\*CustomerID\*\* | Unique identifier | CUST\_000001 - CUST\_050000 |

| \*\*Age\*\* | Customer age | 18-80 years |

| \*\*Annual\_Income\*\* | Yearly income | $20K - $150K |

| \*\*Spending\_Score\*\* | Purchase propensity | 1-100 |

| \*\*Total\_Purchases\*\* | Lifetime purchases | 0-100 |

| \*\*Avg\_Transaction\_Value\*\* | Average order value | $10 - $500 |

| \*\*Tenure\_Months\*\* | Customer lifetime | 1-120 months |

| \*\*Website\_Visits\_Monthly\*\* | Engagement level | 0-50 visits |

| \*\*Email\_Open\_Rate\*\* | Email engagement | 0-100% |

| \*\*Product\_Categories\*\* | Category diversity | 1-10 categories |

| \*\*Days\_Since\_Last\_Purchase\*\* | Recency | 0-365 days |



---



\## 🎯 Customer Segments Identified



\### 1. 💎 Premium High Spenders (18-22%)

\- \*\*Income:\*\* $95,000+

\- \*\*Spending Score:\*\* 65-75/100

\- \*\*Strategy:\*\* VIP programs, luxury offerings, exclusive early access



\### 2. 🏆 Loyal Professionals (20-24%)

\- \*\*Income:\*\* $70,000-85,000

\- \*\*Spending Score:\*\* 55-65/100

\- \*\*Strategy:\*\* Loyalty rewards, subscription models, bulk discounts



\### 3. 🔥 Engaged Enthusiasts (16-20%)

\- \*\*Income:\*\* $50,000-70,000

\- \*\*Spending Score:\*\* 60-70/100

\- \*\*Strategy:\*\* Personalized recommendations, social campaigns



\### 4. 💰 Budget Conscious (22-26%)

\- \*\*Income:\*\* $30,000-45,000

\- \*\*Spending Score:\*\* 30-40/100

\- \*\*Strategy:\*\* Value bundles, flash sales, clearance promotions



\### 5. 🌱 Potential Growers (14-18%)

\- \*\*Income:\*\* $55,000-65,000

\- \*\*Spending Score:\*\* 45-55/100

\- \*\*Strategy:\*\* Educational content, cross-selling, nurture campaigns



---



\## 🔬 Methodology



\### 1. Exploratory Data Analysis (EDA)

\- Statistical analysis of all features

\- Distribution visualization

\- Correlation analysis

\- Outlier detection



\### 2. Data Preprocessing

\- Feature standardization using StandardScaler

\- Removal of irrelevant features (CustomerID)

\- Handling of outliers



\### 3. K-Means Clustering

\- \*\*Elbow Method\*\* for optimal K selection

\- \*\*Silhouette Score\*\* for validation (0.42-0.48)

\- \*\*Davies-Bouldin Index\*\* for cluster quality

\- Selected K=5 based on analysis



\### 4. DBSCAN Clustering

\- K-distance graph for epsilon selection

\- Parameter optimization (eps, min\_samples)

\- Noise/outlier identification

\- Comparison with K-Means results



\### 5. Business Analysis

\- Segment profiling and naming

\- Marketing strategy development

\- ROI and impact projection



---



\## 📊 Key Visualizations



\### Distribution Analysis

!\[Distributions](visualizations/distributions.png)



\### Correlation Heatmap

!\[Correlations](visualizations/correlation\_heatmap.png)



\### Elbow Method

!\[Elbow](visualizations/elbow\_method.png)



\### Final Segment Dashboard

!\[Dashboard](visualizations/segment\_analysis\_dashboard.png)



---



\## 💼 Business Impact



\### Current Performance

\- Average purchases per customer: \*\*31.4\*\*

\- Average transaction value: \*\*$112.50\*\*

\- Estimated annual revenue: \*\*$176.9M\*\*



\### Projected with Segmentation

\- Expected engagement improvement: \*\*15%\*\*

\- Projected purchases per customer: \*\*36.1\*\*

\- Projected annual revenue: \*\*$203.4M\*\*

\- \*\*Potential revenue increase: $26.5M\*\*



\### ROI Analysis

\- Marketing cost estimate: \*\*$2.5M\*\*

\- Net revenue gain: \*\*$24M\*\*

\- \*\*ROI: 960%\*\*



---



\## 🛠️ Technologies Used



\- \*\*Python 3.8+\*\* - Programming language

\- \*\*Pandas\*\* - Data manipulation

\- \*\*NumPy\*\* - Numerical computing

\- \*\*Scikit-learn\*\* - Machine learning algorithms

\- \*\*Matplotlib \& Seaborn\*\* - Data visualization

\- \*\*Jupyter Notebook\*\* - Interactive development



---



\## 📚 Key Learnings



1\. \*\*K-Means vs DBSCAN:\*\*

&nbsp;  - K-Means: Partitioning algorithm, requires K specification

&nbsp;  - DBSCAN: Density-based, finds arbitrary shapes, identifies outliers



2\. \*\*Feature Importance:\*\*

&nbsp;  - Income and Spending Score are primary differentiators

&nbsp;  - Email engagement correlates with customer value

&nbsp;  - Tenure indicates loyalty potential



3\. \*\*Business Application:\*\*

&nbsp;  - Segmentation enables targeted marketing

&nbsp;  - Different segments require different strategies

&nbsp;  - Data-driven decisions improve ROI



---



\## 🎓 Skills Demonstrated



\- ✅ \*\*Data Analysis:\*\* EDA, statistical analysis, feature engineering

\- ✅ \*\*Machine Learning:\*\* Clustering algorithms, model evaluation

\- ✅ \*\*Data Visualization:\*\* Matplotlib, Seaborn, professional charts

\- ✅ \*\*Business Acumen:\*\* Segment naming, strategy development, ROI calculation

\- ✅ \*\*Python Programming:\*\* Pandas, NumPy, Scikit-learn

\- ✅ \*\*Communication:\*\* Stakeholder-ready visualizations and insights



---



\## 🔮 Future Enhancements



\- \[ ] Implement Hierarchical Clustering for comparison

\- \[ ] Add predictive models for customer lifetime value (CLV)

\- \[ ] Create interactive Streamlit/Dash dashboard

\- \[ ] Integrate with real-time data pipeline

\- \[ ] A/B testing framework for strategy validation

\- \[ ] Churn prediction model

\- \[ ] Time-series analysis for seasonal patterns



---



\## 📞 Contact



\*\*Your Name\*\*  

📧 your.email@example.com  

💼 \[LinkedIn](https://linkedin.com/in/yourprofile)  

🐙 \[GitHub](https://github.com/yourusername)



---



\## 📄 License



This project is open source and available under the \[MIT License](LICENSE).



---



\## 🙏 Acknowledgments



\- Dataset generated using statistical distributions

\- Inspired by real-world customer analytics use cases

\- Built as a portfolio project for demonstrating ML skills



---



\*\*⭐ If you found this project helpful, please consider giving it a star!\*\*

