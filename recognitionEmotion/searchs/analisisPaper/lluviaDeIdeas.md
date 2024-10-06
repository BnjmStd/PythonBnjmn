
# Conceptos relacionados con deepLearning

::: mermaid

mindmap
  root((Deep Learning))
    Neural Networks
      Convolutional Neural Networks (CNN)
      Recurrent Neural Networks (RNN)
    Machine Learning
      Supervised Learning
      Unsupervised Learning
    Artificial Intelligence

:::

# Conceptos relacionados con Clasificación de emociones

::: mermaid
mindmap
  root((Emotion Classification))
    Emotion detection
    Emotion recognition
      Facial expression recognition
      Speech emotion recognition
    Affective computing
    Sentiment analysis
    Emotion AI

:::

# Relacionadas con  niños y adolescentes 


::: mermaid

mindmap
  root((Children and Adolescents))
    Children
    Adolescents
      Youth
    Pediatric
    Developmental psychology
      Emotional development
      Emotional regulation

:::


# Relacionadas con emociones y sentimientos

::: mermaid

mindmap
  root((Emotions and Feelings))
    Emotions
    Feelings
    Affect
    Emotional intelligence
    Emotional awareness
    Sentiment
    Affective states
    Emotional expression
    Mood

::: 


# Términos de exclusión

::: mermaid

mindmap
  root((Términos de Exclusión))
    Por tecnicismos
      Hardware
    Por léxico Médico
      Biomedical applications
      Drug therapy
      Disease classification
    Por edad y organismo
      Adults (si no te interesa literatura sobre adultos)
      Elderly
      Animals

:::


# Resultados por consulta

::: mermaid 

%%{init: {'themeVariables': { 'rootColor': '#09f', 'resultColor': '#4CAF50'}}}%%
graph TD;
    A[Base de datos: PubMed]:::root
    
    B1[Consulta 1: Deep Learning AND Emotion detection AND Neural Networks AND Children]:::query
    B2[Consulta 2: Emotional intelligence AND Machine Learning AND Emotional development AND Emotion AI AND Children]:::query
    B3[Consulta 3: Artificial Intelligence AND Neural Networks AND Emotion classification AND Children]:::query
    
    A -->|Resultados: 7| B1:::result
    A -->|Resultados: 3| B2:::result
    A -->|Resultados: 9| B3:::result

    classDef root fill:#09f,stroke:#09f,color:#fff;
    classDef query fill:#fff,stroke:#09f,color:#09f;
    classDef result fill:#4CAF50,stroke:#4CAF50,color:#fff;



:::