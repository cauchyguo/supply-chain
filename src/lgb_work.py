#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Cauchy
@file: lgb_work.py
@e-mail: cauchyguo@gmail.com
@time: 2018/10/8 13:12
"""
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV

params = {
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'learning_rate': 0.03,
    'lambda_l1': 0.1,
    'lambda_l2': 0.2,
    'max_depth': 25,
    'num_leaves': 31,
    'min_child_weight': 25
}

if __name__ == '__main__':
    datas = list()
    target = pd.read_csv(r'E:\PycharmProjects\Task2Plus\dataset\submit_example.csv')
    relation = pd.read_csv(r'E:\PycharmProjects\Task2Plus\dataset\goods_sku_relation.csv')
    target = pd.merge(target[['sku_id']], relation, on='sku_id')
    goods_list = target.goods_id.unique()
    scaler = MinMaxScaler()

    for i in range(6):
        trainPath = r'E:\PycharmProjects\Task2Plus\TrainSets\trainWithLabel' + str(i + 1) + '.csv'
        traindata = pd.read_csv(trainPath)
        datas.append(traindata[traindata.goods_id.isin(goods_list)])

    dataset = pd.concat(datas, axis=0)
    test = pd.read_csv(r'E:\PycharmProjects\Task2Plus\TestSets\TestPlus.csv')
    # test = pd.merge(test,target,on='sku_id')

    # for week1
    X = dataset[dataset.columns[2:-5]]
    X = scaler.fit_transform(X)
    Y = dataset['week1']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    lgb_train = lgb.Dataset(X_train, label=y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)
    gbm = lgb.train(params, lgb_train, num_boost_round=5000, valid_sets=lgb_eval, early_stopping_rounds=100)
    gbm.save_model(r'E:\PycharmProjects\Task2Plus\models\model1.txt')
    y_pred = gbm.predict(test[test.columns[2:]], num_iteration=gbm.best_iteration)
    # y_pred = y_pred.astype('int')
    test['week1'] = pd.Series(y_pred)

    # for week2
    X = dataset[dataset.columns[2:-5]]
    X = scaler.fit_transform(X)
    Y = dataset['week2']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    lgb_train = lgb.Dataset(X_train, label=y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)
    gbm = lgb.train(params, lgb_train, num_boost_round=5000, valid_sets=lgb_eval, early_stopping_rounds=100)
    gbm.save_model(r'E:\PycharmProjects\Task2Plus\models\model2.txt')
    y_pred = gbm.predict(test[test.columns[2:]], num_iteration=gbm.best_iteration)
    # y_pred = y_pred.astype('int')
    test['week2'] = pd.Series(y_pred)

    # for week3
    X = dataset[dataset.columns[2:-5]]
    X = scaler.fit_transform(X)
    Y = dataset['week3']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    lgb_train = lgb.Dataset(X_train, label=y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)
    gbm = lgb.train(params, lgb_train, num_boost_round=5000, valid_sets=lgb_eval, early_stopping_rounds=100)
    gbm.save_model(r'E:\PycharmProjects\Task2Plus\models\model3.txt')
    y_pred = gbm.predict(test[test.columns[2:]], num_iteration=gbm.best_iteration)
    # y_pred = y_pred.astype('int')
    test['week3'] = pd.Series(y_pred)

    # for week4
    X = dataset[dataset.columns[2:-5]]
    X = scaler.fit_transform(X)
    Y = dataset['week4']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    lgb_train = lgb.Dataset(X_train, label=y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)
    gbm = lgb.train(params, lgb_train, num_boost_round=5000, valid_sets=lgb_eval, early_stopping_rounds=100)
    gbm.save_model(r'E:\PycharmProjects\Task2Plus\models\model4.txt')
    y_pred = gbm.predict(test[test.columns[2:]], num_iteration=gbm.best_iteration)
    # y_pred = y_pred.astype('int')
    test['week4'] = pd.Series(y_pred)

    # for week5
    X = dataset[dataset.columns[2:-5]]
    X = scaler.fit_transform(X)
    Y = dataset['week5']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    lgb_train = lgb.Dataset(X_train, label=y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)
    gbm = lgb.train(params, lgb_train, num_boost_round=5000, valid_sets=lgb_eval, early_stopping_rounds=100)
    gbm.save_model(r'E:\PycharmProjects\Task2Plus\models\model5.txt')
    y_pred = gbm.predict(test[test.columns[2:]], num_iteration=gbm.best_iteration)
    # y_pred = y_pred.astype('int')
    test['week5'] = pd.Series(y_pred)

    test = test[['sku_id', 'week1', 'week2', 'week3', 'week4', 'week5']]
    test.to_csv(r'E:\PycharmProjects\Task2Plus\output\lgb_reault.csv', index=False)
