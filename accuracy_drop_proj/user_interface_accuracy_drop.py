from accuracy_drop_proj.utilities.save_dataset.save_pickle_obj import Save_Pickle_Obj
from accuracy_drop_proj.utilities.load_dataset.load_pickle_obj import Load_Pickle_Obj
from accuracy_drop_proj.utilities.load_dataset.iris_loader import Iris_Loader
from accuracy_drop_proj.utilities.load_dataset.abalone_loader import Abalone_loader
from accuracy_drop_proj.utilities.load_dataset.digits_loader import Digits_Loader
from accuracy_drop_proj.strategies.change_feature_one_by_one.change_feature_one_by_one import Change_Feature_One_By_One
from accuracy_drop_proj.strategies.change_feature_randomly.change_feature_randomly import Change_Feature_randomly
from accuracy_drop_proj.strategies.change_most_important_feature.change_most_important_feature import Change_Most_Important_Feature
from accuracy_drop_proj.strategies.change_combination.change_combination import Change_Combination
from accuracy_drop_proj.strategies.change_combination_min.change_combination_min import Change_Combination_Min
from accuracy_drop_proj.strategies.change_combination_feature_min.change_combination_feature_min import Change_Combination_Feature_Min
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import time


#---------------------- load data set -----------------------
# loader=Iris_Loader()
loader=Abalone_loader()
# loader=Digits_Loader()

x_train, x_test, y_train, y_test = loader.load()


#---------------------train model -----------------------------

#----------------------MNB-------------------------------------
# print("train MNB")
# mnb = MultinomialNB()
# mnb.fit(x_train,y_train)
# print('Accuracy of MNB classifier on test set: {:.2f}'.format(mnb.score(x_test, y_test)))
#----------------------SVM--------------------------------------
print("train SVM")
svm = SVC()
svm.fit(x_train, y_train)
print('Accuracy of SVM classifier on test set: {:.2f}'.format(svm.score(x_test, y_test)))

#--------------------choose your method--------------------------------------------

# mymethod = Change_Feature_One_By_One() #BUG
# mymethod= Change_Feature_randomly() #BUG
mymethod=Change_Most_Important_Feature()
# mymethod= Change_Combination()
# mymethod =Change_Combination_Min()
# mymethod=Change_Combination_Feature_Min()

start = time.time()

change_plan={"key":[[9,7],[8,7],[10,7]],"number":[140,40,28]}
# change_plan={"key":[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 0], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 0], [2, 1], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 0], [3, 1], [3, 2], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [4, 0], [4, 1], [4, 2], [4, 3], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 6], [5, 7], [5, 8], [5, 9], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 7], [6, 8], [6, 9], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 8], [7, 9], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 9], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8]],"number":[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]}
out=mymethod.change(x_test,y_test,10,svm,change_plan)

end = time.time()

#--------------------------- evaluation ---------------------------------------------

y_pred=svm.predict(out)

print("your execuation time is {} (s)".format(end - start))
print ("\n Accuracy is: {} ".format(accuracy_score(y_test, y_pred)))
print('\n Accuracy was: {:.2f}'.format(svm.score(x_test, y_test)))


#--------------------------------------------
# save the output
# saver=Save_Pickle_Obj()
# saver.save_object(out,'./outputs/results_output/output_{}_{}.pkl'.format(loader.name,start))
# # load the output
# obj_loader=Load_Pickle_Obj()
# newobj=obj_loader.load('./outputs/results_output/output_{}_{}.pkl'.format(loader.name,start))
