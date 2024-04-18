# Mobile Price Classification


<div style="width: 95%; border-radius:10px; border: #04942b solid; padding: 12px; background-color: #d9fce3; font-size:110%; color: black; text-align:justify">

Deployment: <a href='https://mobilepriceclassification-w8clyq2btydf4ikyplspq3.streamlit.app/'>Run here...</a>

<h3 align="left"><font color= #04942b>Introduction</font></h3>
    
In todays market, mobile phones come in a wide range of prices, each offering different features and specifications. For consumers, selecting a mobile phone that aligns with their budget and requirements can be challenging. To assist consumers in making informed decisions, this project aims to develop a machine learning model that can classify mobile phones into different price ranges based on their features.

<h3 align="left"><font color= #04942b>Problem Statement</font></h3>
The task is to build a predictive model that can accurately classify mobile phones into predefined price ranges based on various attributes such as battery power, camera features, memory, connectivity options, and more. The dataset provided contains information about several mobile phones, including their specifications and corresponding price ranges.

<h3 align="left"><font color= #04942b>Dataset</font></h3>

Dataset columns are as follows:
- **battery_power** - Total energy a battery can store in one time measured in mAh.
- **blue** - Bluetooth enabled:
    - 0 (no)
    - 1 (yes)
- **clock_speed** - Speed at which microprocessor executes instructions.
- **dual_sim** - Has dual sim support or not
- **fc** - Front Camera mega pixels.
- **four_g** - 4G network support:
    - 0 (no)
    - 1 (yes)
- **int_memory** - Internal Memory (in gigabytes).
- **m_dep** - Mobile Depth in cm.
- **mobile_wt** - Weight of mobile phone.
- **n_cores** - Number of cores of processor.
- **pc** - Primary Camera mega pixels.
- **px_height** - Pixel Resolution Height.
- **px_width** - Pixel Resolution Width.
- **ram** - Random Access Memory in megabytes.
- **sc_h** - Screen Height of mobile in cm.
- **sc_w** - Screen Width of mobile in cm.
- **talk_time** - Longest time that a single battery charge will last when you are talking.
- **three_g** - 3G network support:
    - 0 (no)
    - 1 (yes)
- **touch_screen** - Touch screen support:
    - 0 (no)
    - 1 (yes)
- **wifi** - Wifi connectivity:
    - 0 (no)
    - 1 (yes)    
- **price_range** - Price range of the mobile phone:
    - 0 (low cost)
    - 1 (medium cost)
    - 2 (high cost)
    - 3 (very high cost)
    
    
<h3 align="left"><font color= #04942b>Objectives</font></h3>

- Explore and preprocess the dataset to handle missing values, outliers, and any other data inconsistencies.
- Perform exploratory data analysis (EDA) to gain insights into the relationships between different features and the target variable (price range).
- Select appropriate machine learning algorithms for classification and evaluate their performance using suitable metrics.
- Fine-tune the chosen model to improve its predictive accuracy.
- Validate the final model using cross-validation techniques to ensure its robustness.
- Deploy the model for real-time predictions if applicable.
    
<h3 align="left"><font color= #04942b>Applied Models:</font></h3>

- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree (DT)
- Random Forest (RF)
- Gradient Boosting

Among the examined classifiers, __Logistic Regression__ got the best accuracy:
    
🏆 Accuracy = 98%

</div>


