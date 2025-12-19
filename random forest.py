from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,ConfusionMatrixDisplay,confusion_matrix
import mlflow.sklearn
import seaborn as sns
from seaborn.datasets import load_wine
import pandas as pd
import matplotlib.pyplot as plt
