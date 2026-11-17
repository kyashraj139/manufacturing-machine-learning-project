"""Shared synthetic data and evaluation helpers for educational ML labs."""
import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, roc_auc_score, precision_score, recall_score, f1_score, accuracy_score

def make_domain_data(domain, n=2400, seed=42):
    rng=np.random.default_rng(seed)
    if domain=='healthcare':
        age=rng.integers(18,85,n); bmi=np.clip(rng.normal(27,5,n),16,48); systolic=np.clip(rng.normal(125,18,n),85,205); glucose=np.clip(rng.normal(105,30,n),60,260); visits=rng.poisson(2,n)
        z=-5.8+0.028*(age-40)+0.065*(bmi-25)+0.017*(systolic-120)+0.014*(glucose-100)+0.18*visits
        frame=pd.DataFrame({'age':age,'bmi':bmi.round(1),'systolic_bp':systolic.round(1),'glucose':glucose.round(1),'prior_visits':visits,'region':rng.choice(['North','South','West'],n)})
        target='risk_flag'; desc='Synthetic screening-risk classification (NOT a clinical diagnosis)'
    elif domain=='manufacturing':
        temp=rng.normal(72,13,n); vibration=np.clip(rng.normal(3.2,1.1,n),0.1,9); pressure=rng.normal(100,15,n); runtime=rng.integers(50,6000,n); maintenance=rng.integers(0,400,n)
        z=-5.5+0.075*(temp-70)+0.85*(vibration-3)+0.00024*(runtime-2500)+0.003*(maintenance-150)+0.012*np.abs(pressure-100)
        frame=pd.DataFrame({'temperature_c':temp.round(2),'vibration_mm_s':vibration.round(2),'pressure_bar':pressure.round(2),'runtime_hours':runtime,'days_since_maintenance':maintenance,'machine_type':rng.choice(['Pump','Motor','Compressor'],n)})
        target='failure_flag'; desc='Synthetic equipment-failure prediction'
    elif domain=='emobility':
        temp=rng.normal(39,11,n); voltage=rng.normal(400,25,n); current=np.clip(rng.normal(95,30,n),10,220); age=rng.integers(1,90,n); sessions=rng.integers(1,45,n)
        z=-5.2+0.085*(temp-38)+0.014*np.abs(voltage-400)+0.012*(current-90)+0.026*(age-36)+0.022*(sessions-20)
        frame=pd.DataFrame({'charger_temp_c':temp.round(2),'voltage_v':voltage.round(2),'current_a':current.round(2),'charger_age_months':age,'daily_sessions':sessions,'station_region':rng.choice(['Hyderabad','Chennai','Bengaluru'],n)})
        target='fault_flag'; desc='Synthetic EV-charger fault prediction'
    else: raise ValueError('unknown domain')
    prob=1/(1+np.exp(-np.clip(z,-25,25)))
    frame[target]=rng.binomial(1,prob)
    return frame,target,desc

def score_classifier(name, estimator, X_test, y_test):
    pred=estimator.predict(X_test)
    proba=estimator.predict_proba(X_test)[:,1] if hasattr(estimator,'predict_proba') else None
    return {'model':name,'accuracy':accuracy_score(y_test,pred),'precision':precision_score(y_test,pred,zero_division=0),'recall':recall_score(y_test,pred,zero_division=0),'f1':f1_score(y_test,pred,zero_division=0),'roc_auc':roc_auc_score(y_test,proba) if proba is not None else np.nan,'pr_auc':average_precision_score(y_test,proba) if proba is not None else np.nan}
