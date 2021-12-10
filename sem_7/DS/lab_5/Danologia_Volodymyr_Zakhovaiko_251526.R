# Ładujemy potrzebne biblioteki
library(ggplot2)
library(lattice)
library(xtable)
library(caret)
library(rJava)
library(RWeka)
library(FSelector)
library(mlr)
library(mlr3)
library(mlr3verse)
library(kernlab)
library(magrittr)
library(knitr)
library(dplyr)

set.seed(1) # ustawiamy seed rowny 1, zeby miec jednakowe dane przy randomie

# Zapisuje lokalizacje  datasetów (plików)
trainCsv <-
  "http://madeyski.e-informatyka.pl/download/stud/CaseStudies/Lucene/lucene2.2train.csv"
testCsv <-
  "http://madeyski.e-informatyka.pl/download/stud/CaseStudies/Lucene/lucene2.4test.csv"

# Czytamy pliki CSV
trainOrig <- read.csv(trainCsv, header = TRUE, sep = ",")
testOrig <- read.csv(testCsv, header = TRUE, sep = ",")

train <- trainOrig %>% mutate(dataset="train")
test <- testOrig %>% mutate(dataset="test")

# kombinujemy train i test datasety, żeby nie powtarzać te same akcje dwa razy
combined <- dplyr::bind_rows(train, test)
# usuwamy niepotrzebne do analizy kolumny 
combined <- combined %>% dplyr::select(-c(X, Project, Version, Class))

imp <- mlr::impute(combined, classes=list(factor=mlr::imputeMode(), integer=mlr::imputeMean(), numeric=mlr::imputeMean()))
combined <- imp$data

# filtrujemy wierszy ktore zawierają train oraz test kolumny bez dataset
train <- combined %>% filter(dataset=="train") %>% dplyr::select(-dataset)
test <- combined %>% filter(dataset=="test") %>% dplyr::select(-dataset)

# teraz tworzymy klasyfikatory dla train i test datasetów
trainTask <- mlr::makeClassifTask(data=train, target="isBuggy", positive="TRUE")
testTask <- mlr::makeClassifTask(data=test, target="isBuggy", positive="TRUE")

print(trainTask)

# waznosc cech
featureImportance <- mlr::generateFilterValuesData(testTask, method="FSelector_information.gain")
# drukujemy wykres cech
mlr::plotFilterValues(featureImportance)

# tworzymy learnera z okreslonym aglorytmem logistycznej regresji
lr.learner <- mlr::makeLearner("classif.logreg", predict.type="response")
# tworzymy model na podstawie tego lerneru
lr.model <- mlr::train(lr.learner, task=trainTask)
# liczymy predykcje wartosci wedlug testTasku
pred = predict(lr.model, task=testTask)
# wykonujemy learnera wedlug roznych algorytmow obliczenia bledu
perfMeasures <- mlr::performance(pred, measures=list(mlr::mcc, mlr::mmce, mlr::acc, mlr::f1, mlr::kappa))
perfMeasures

confusionMatrix <-mlr::calculateConfusionMatrix(pred)
confusionMatrix

# teraz tworzymy SVM learnera
svm.learner <- makeLearner("classif.ksvm", predict.type = "response")
# dodajemy cross-walidacje
setCV <- makeResampleDesc("CV", iters=3L)
# dodajemy dwa hyperparametry
paramSet <- makeParamSet(
  # dodajemy swoje wartosci, tzw costs
  # glownie tutaj nie dojsc do overfittingu
  makeDiscreteParam("C", values=2^c(-10, -20, -8, -4, -2, 0, 1, 2, 4, -30, -40, -25)),
  makeDiscreteParam("sigma", values=2^c(-10, -20, -8, -6, -4, -2, 0, 2, 4, 6, 8, 1.5, -1.5, -30, -40, -25))
)
# zmieniamy parametry
tuneParams <- tuneParams(learner=svm.learner, resampling = setCV, task=trainTask, par.set=paramSet, control=makeTuneControlGrid(), measure=mlr::mcc)
# szukamy najlepsze parametry
tuneParams$x

# ustawiamy powyzsze hyperparametry modelu svm
svmT.learner <- setHyperPars(svm.learner, par.vals=tuneParams$x)
svmT.model <- mlr::train(svmT.learner, task=trainTask)
# robimy predykcje danych
pred = predict(svmT.model, task=trainTask)
# liczymy blad uczenia sie
perfM <- mlr::performance(pred, measures=list(mlr::mcc, mlr::mmce, mlr::acc, mlr::f1, mlr::kappa))
perfM

confusionMatrixTSVM <-mlr::calculateConfusionMatrix(pred)
confusionMatrixTSVM
# jak widac ksvm dziala lepiej niz regresja logistyczna

Danologia_Volodymyr_Zakhovaiko_251526