import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def mlpred(temp,hum,wind,preci,cloud,atm,uv,sea,visi,loc):

    dataset = pd.read_csv('weather_classification_data.csv')
    x = dataset.iloc[:,:-1].values
    y = dataset.iloc[:,-1].values

    """# Encoding Columns of Matrix Feature

    Encoding Cloud cover
    """

    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    x[:,4] = le.fit_transform(x[:,4])


    """Encoding Season"""


    from sklearn.preprocessing import LabelEncoder
    le1 = LabelEncoder()
    x[:,7] = le1.fit_transform(x[:,7])


    """Encoding Location"""


    from sklearn.preprocessing import LabelEncoder
    le2 = LabelEncoder()
    x[:,9] = le2.fit_transform(x[:,9])


    """# Encoding Weather Type - Result"""


    from sklearn.preprocessing import LabelEncoder
    le3 = LabelEncoder()
    y = le3.fit_transform(y)


    """# Data After Encoding"""


    """# Splitting the Dataset to training and test sets"""

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=0)


    """# Feature Scaling"""

    from sklearn.preprocessing import StandardScaler
    ss = StandardScaler()
    x_train = ss.fit_transform(x_train)
    x_test = ss.transform(x_test)

    """# Training the Random Forest Classification Model"""

    from sklearn.ensemble import RandomForestClassifier
    rfc = RandomForestClassifier(n_estimators=10, criterion='entropy',random_state=0)
    rfc.fit(x_train,y_train)

    """# Confusion Matrix"""

    from sklearn.metrics import confusion_matrix, accuracy_score
    y_pred  = rfc.predict(x_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    accuracy_score(y_test, y_pred)

    """# Applying K_Fold_Cross_Validation"""

    from sklearn.model_selection import cross_val_score
    accuracies = cross_val_score(estimator=rfc, X=x_train,y=y_train,cv=10)
    print("Accuracy:",accuracies.mean()*100)
    print("Standard Deviation:",accuracies.std()*100)

    """# Predicting The Results of New Data"""

    pred = rfc.predict([[temp,hum,wind,preci,le.transform([[cloud]])[0],atm,uv,le1.transform([[sea]])[0],visi,le2.transform([[loc]])[0]]])
    print(le3.inverse_transform(pred))

    return le3.inverse_transform(pred)

    # from xgboost import XGBClassifier
    # xg = XGBClassifier()
    # xg.fit(x_train, y_train)

    # from sklearn.metrics import confusion_matrix, accuracy_score
    # y_pred  = xg.predict(x_test)
    # cm = confusion_matrix(y_test, y_pred)
    # print(cm)
    # accuracy_score(y_test, y_pred)

    # pred = xg.predict([[temp,hum,wind,preci,le.transform([[cloud]])[0],atm,uv,le1.transform([[sea]])[0],visi,le2.transform([[loc]])[0]]])
    # print(le3.inverse_transform(pred))

    # return le3.inverse_transform(pred)
