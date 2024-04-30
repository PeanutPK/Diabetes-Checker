import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import customtkinter as ctk


class DiabetesModel:
    @staticmethod
    def load_graph(name: str):
        file_csv = pd.read_csv('data/diabetes.csv')

        replace = {1: 'Diabetic', 0: 'Not Diabetic'}
        file_csv['Outcome'] = file_csv['Outcome'].replace(replace)

        ax = sns.histplot(file_csv, x=name, hue='Outcome')

        ax.set(xlabel='', ylabel='Frequency')

        plt.title('Diabetes Outcome for ' + name)
        plt.show()

    @staticmethod
    def describe(master: ctk.CTkFrame, name: str):
        for child in master.winfo_children():
            child.destroy()
        file_csv = pd.read_csv('data/diabetes.csv')

        label = ctk.CTkLabel(master, text=file_csv[name].describe())
        label.pack()


if __name__ == '__main__':
    DiabetesModel.load_graph('BMI')
