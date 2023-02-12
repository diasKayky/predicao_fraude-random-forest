# Predição de Fraude no Cartão de Crédito

> Uma empresa que oferece serviço de gateway de pagamentos precisa avaliar a qualidade das transações do seu volume. Para tal, é desenvolvido um fluxo de ML utilizando principios da engenharia de dados e Pyspark para obter dados de distintas fontes. O modelo de ML é construído utilizando o algoritmo de aprendizagem supervisionada Random Forest. O deploy é por meio de API Flask. 

# ML Workflow
<img src="https://github.com/diasKayky/predicao_fraude-random-forest/blob/main/project_structure.png" data-canonical-src="https://github.com/diasKayky/predicao_fraude-random-forest/blob/main/project_structure.png" width="600" />

1. Desenvolvimento da pipeline de dados (ETL) utilizando o Pyspark
2. Carregamento dos dados que serão utilizados pelo modelo
3. Treinamento e avaliação do modelo de Random Forest
4. Serialização do modelo
5. Deploy do modelo via API Flask

# Problemas e dificuldades

1. Treinar o modelo utilizando o `final_dataset` devido ao modesto computador utilizado | Solução: treinar em apenas um dos datasets.
2. Fazer upload dos datasets massivos para o Github | Solução: criar o arquivo `datasets_links`.


##  💻 Desenvolvedor


<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/75142111?v=4" width="100px;" alt="Foto do Mark Zuckerberg"/><br>
        <sub>
          <b>Kayky Santos</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
