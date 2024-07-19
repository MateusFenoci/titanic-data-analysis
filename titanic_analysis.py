import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Função para carregar os dados
def load_data(file_path):
    return pd.read_csv(file_path)

# Função para preencher dados faltantes
def fill_missing_values(data):
    data['Cabin'].fillna('Unknown', inplace=True)
    data['Age'].fillna(data['Age'].median(), inplace=True)
    data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
    return data

# Função para adicionar coluna 'Deck'
def add_deck_column(data):
    data['Deck'] = data['Cabin'].str[0]
    data['Deck'].fillna('U', inplace=True)
    return data

# Função para mapear valores de sobrevivência
def map_survived(data):
    survived_map = {0: 'Não Sobreviveu', 1: 'Sobreviveu'}
    data['Survived'] = data['Survived'].map(survived_map)
    return data

# Função para gerar e salvar visualizações
def generate_and_save_plots(data):
    if not os.path.exists('images'):
        os.makedirs('images')

    # Distribuição da Sobrevivência
    sns.countplot(data=data, x='Survived')
    plt.title('Distribuição da Sobrevivência')
    plt.xlabel('Sobreviveu')
    plt.ylabel('Frequência')
    plt.savefig('images/survival_distribution.png')
    plt.clf()

    # Sobrevivência por Gênero
    sns.countplot(data=data, x='Sex', hue='Survived')
    plt.title('Sobrevivência por Gênero')
    plt.xlabel('Gênero')
    plt.ylabel('Frequência')
    plt.legend(title='Sobreviveu')
    plt.savefig('images/survival_by_gender.png')
    plt.clf()

    # Distribuição de Idades
    data['Age'].hist(bins=30, edgecolor='black')
    plt.title('Distribuição das Idades')
    plt.xlabel('Idade')
    plt.ylabel('Frequência')
    plt.savefig('images/age_distribution.png')
    plt.clf()

# Função principal
def main():
    # Carregar os dados
    data = load_data('data/titanic.csv')

    # Preencher dados faltantes
    data = fill_missing_values(data)

    # Adicionar coluna 'Deck'
    data = add_deck_column(data)

    # Mapear valores de sobrevivência
    data = map_survived(data)

    # Gerar e salvar visualizações
    generate_and_save_plots(data)

if __name__ == "__main__":
    main()
