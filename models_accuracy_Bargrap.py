"""
bar graph 
of Crop recommendation
code

Accuracies of the Models
Decision Tree --->		 90.00 %
Naive Bayes --->		 99.09 %
SVM --->		         97.95 %
Logistic Regression ---> 95.23 %
RF --->		             99.09 %
XGBoost --->		     99.32 %
"""

#acc = [0.9, 0.990909090909091, 0.9795454545454545, 0.9522727272727273, 0.990909090909091, 0.9931818181818182]
#model = ['Decision Tree', 'Naive Bayes', 'SVM', 'Logistic Regression', 'RF', 'XGBoost']
plt.figure(figsize=[10,5],dpi = 100)
plt.title('Accuracy Comparison')
plt.xlabel('Accuracy')
plt.ylabel('Algorithm')
sns.barplot(x = acc, y = model ,palette='dark')
