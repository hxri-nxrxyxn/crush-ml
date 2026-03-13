# The Complete Machine Learning Kata Masterclass

An exhaustive, modular progression mapped directly to Aurélien Géron's *Hands-On Machine Learning (3rd Ed.)*. Each file is a self-contained Python script demonstrating a single concept.

## Part 1: Fundamentals & Data Wrangling (Ch. 2)
| File | Title | Description |
| :--- | :--- | :--- |
| `ex001.py` | Fetching Data | Downloading and extracting compressed datasets programmatically. |
| `ex002.py` | Pandas EDA | Exploring data structures with `head()`, `info()`, and `describe()`. |
| `ex003.py` | Histogram Analysis | Plotting numerical feature distributions. |
| `ex004.py` | Random Splitting | Creating a basic train/test split. |
| `ex005.py` | Stratified Splitting | Ensuring representative category ratios in splits. |
| `ex006.py` | Correlation Matrices | Computing Pearson's r to find linear correlations. |
| `ex007.py` | Scatter Matrices | Visualizing correlations between multiple attributes. |
| `ex008.py` | Handling NaN | Dropping missing data vs. filling with median. |
| `ex009.py` | Sklearn Imputer | Automating missing value replacement. |
| `ex010.py` | Ordinal Encoding | Mapping categorical text to integer ranges. |
| `ex011.py` | One-Hot Encoding | Creating dummy binary variables for nominal categories. |
| `ex012.py` | Min-Max Scaling | Normalizing data to a [0, 1] range. |
| `ex013.py` | Standardization | Scaling data to zero mean and unit variance. |
| `ex014.py` | Custom Transformers | Writing a class to automate custom feature engineering. |
| `ex015.py` | Sklearn Pipelines | Chaining preprocessing steps sequentially. |
| `ex016.py` | ColumnTransformer | Routing different pipelines to specific column types. |

## Part 2: Classification Metrics (Ch. 3)
| File | Title | Description |
| :--- | :--- | :--- |
| `ex017.py` | SGD Classifier | Training a binary classifier on a toy dataset. |
| `ex018.py` | K-Fold CV | Evaluating performance via cross-validation. |
| `ex019.py` | Confusion Matrix | Extracting true/false positives and negatives. |
| `ex020.py` | Precision & Recall | Calculating precision, recall, and F1-score. |
| `ex021.py` | Threshold Tuning | Using `decision_function` to shift the P/R tradeoff. |
| `ex022.py` | Precision-Recall Curve | Plotting P vs R for threshold selection. |
| `ex023.py` | The ROC Curve | Plotting TPR vs FPR and calculating AUC. |
| `ex024.py` | OvR vs OvO | Strategies for multiclass classification. |
| `ex025.py` | Error Visualization | Plotting confusion matrix heatmaps to find weaknesses. |
| `ex026.py` | Multilabel Target | Classifying instances into multiple binary categories. |
| `ex027.py` | Multioutput Target | Predicting multiple multiclass labels (e.g., image denoising). |

## Part 3: Under the Hood of Training (Ch. 4)
| File | Title | Description |
| :--- | :--- | :--- |
| `ex028.py` | The Normal Equation | Solving Linear Regression with raw NumPy matrix math. |
| `ex029.py` | Batch GD | Implementing Gradient Descent from scratch. |
| `ex030.py` | Stochastic GD | Implementing SGD with a decaying learning rate. |
| `ex031.py` | Mini-batch GD | Vectorizing gradient descent over small batches. |
| `ex032.py` | Polynomial Regression | Adding degree-N features to fit non-linear data. |
| `ex033.py` | Learning Curves | Visualizing training vs validation RMSE. |
| `ex034.py` | Ridge Regression | Applying L2 weight decay to reduce overfitting. |
| `ex035.py` | Lasso Regression | Applying L1 penalty for automatic feature selection. |
| `ex036.py` | Elastic Net | Combining L1 and L2 regularization. |
| `ex037.py` | Early Stopping | Halting gradient descent when validation error climbs. |
| `ex038.py` | Logistic Regression | Estimating probabilities with the sigmoid function. |
| `ex039.py` | Softmax Regression | Multinomial logistic regression for mutually exclusive classes. |

## Part 4: Support Vector Machines (Ch. 5)
| File | Title | Description |
| :--- | :--- | :--- |
| `ex040.py` | Linear SVM | Hard margin classification on linearly separable data. |
| `ex041.py` | Soft Margin SVM | Tuning the `C` hyperparameter for margin violations. |
| `ex042.py` | Polynomial SVM | Adding polynomial features for non-linear SVMs. |
| `ex043.py` | The Kernel Trick | Using `kernel='poly'` to avoid combinatorial explosion. |
| `ex044.py` | RBF Kernel | Using Gaussian Radial Basis Functions for complex boundaries. |
| `ex045.py` | SVM Regression | Fitting an SVM to a continuous target variable. |

## Part 5: Decision Trees & Ensembles (Ch. 6 & 7)
| File | Title | Description |
| :--- | :--- | :--- |
| `ex046.py` | Tree Training | Fitting a DecisionTreeClassifier. |
| `ex047.py` | Tree Visualization | Exporting tree graphs via `export_graphviz`. |
| `ex048.py` | Gini vs Entropy | Calculating node impurity metrics. |
| `ex049.py` | Tree Regularization | Pruning via `max_depth` and `min_samples_leaf`. |
| `ex050.py` | Tree Regression | Predicting continuous values with leaf node averages. |
| `ex051.py` | Hard Voting | Aggregating discrete predictions from multiple models. |
| `ex052.py` | Soft Voting | Aggregating predicted class probabilities. |
| `ex053.py` | Bagging | Training ensembles on bootstrapped subsets of data. |
| `ex054.py` | Pasting | Training ensembles on random subsets without replacement. |
| `ex055.py` | Out-of-Bag Eval | Evaluating bagging models without a separate validation set. |
| `ex056.py` | Random Forests | Building an optimized ensemble of Decision Trees. |
| `ex057.py` | Feature Importance | Extracting feature importances from a Random Forest. |
| `ex058.py` | AdaBoost | Sequentially updating instance weights to correct errors. |
| `ex059.py` | Gradient Boosting | Sequentially fitting trees to residual errors. |
| `ex060.py` | XGBoost | High-performance gradient boosting. |

## Part 6: Dimensionality Reduction & Unsupervised (Ch. 8 & 9)
| File | Title | Description |
| :--- | :--- | :--- |
| `ex061.py` | SVD Math | Extracting principal components using Singular Value Decomposition. |
| `ex062.py` | Sklearn PCA | Projecting data down to lower dimensions. |
| `ex063.py` | Explained Variance | Choosing the right number of dimensions to keep. |
| `ex064.py` | Randomized PCA | Using stochastic algorithms for faster decomposition. |
| `ex065.py` | Kernel PCA | Unrolling twisted manifolds via the kernel trick. |
| `ex066.py` | K-Means | Grouping data into K clusters. |
| `ex067.py` | K-Means Init | Optimizing centroid initialization (K-Means++). |
| `ex068.py` | Silhouette Score | Finding the optimal number of clusters. |
| `ex069.py` | Image Segmentation | Using K-Means to reduce color palettes in images. |
| `ex070.py` | DBSCAN | Density-based spatial clustering for arbitrary shapes. |
| `ex071.py` | Gaussian Mixtures | Modeling data as a mixture of multiple Gaussian distributions. |

## Part 7: Intro to Artificial Neural Networks (Ch. 10)
| File | Title | Description |
| :--- | :--- | :--- |
| `ex072.py` | The Perceptron | Implementing a basic TLU (Threshold Logic Unit). |
| `ex073.py` | Keras Sequential | Building an MLP stack layer by layer. |
| `ex074.py` | Compiling Models | Setting loss functions, optimizers, and metrics. |
| `ex075.py` | Keras History | Plotting loss and accuracy over epochs. |
| `ex076.py` | Keras Functional API | Building networks with complex topologies (Multiple inputs/outputs). |
| `ex077.py` | Subclassing API | Writing custom model architectures using Python classes. |
| `ex078.py` | Model Checkpoints | Saving the best model during training. |
| `ex079.py` | Early Stopping Callback| Interrupting training when validation loss stalls. |
| `ex080.py` | TensorBoard | Logging metrics for visualization in the TensorBoard dashboard. |

## Part 8: Training Deep Neural Networks (Ch. 11)
| File | Title | Description |
| :--- | :--- | :--- |
| `ex081.py` | Glorot/He Init | Preventing vanishing/exploding gradients with proper weight initialization. |
| `ex082.py` | Non-Saturating Acts | Replacing Sigmoid with ReLU, LeakyReLU, and ELU. |
| `ex083.py` | Batch Normalization | Centering and scaling inputs to activation functions. |
| `ex084.py` | Gradient Clipping | Capping gradients to prevent exploding weights in RNNs. |
| `ex085.py` | Transfer Learning | Reusing lower layers of a pre-trained neural network. |
| `ex086.py` | Momentum Optimizer | Accelerating gradient descent using moving averages. |
| `ex087.py` | RMSProp | Adapting the learning rate to parameter gradients. |
| `ex088.py` | Adam Optimization | Combining Momentum and RMSProp. |
| `ex089.py` | Learning Rate Schedules| Implementing exponential scheduling. |
| `ex090.py` | L1/L2 in NNs | Adding regularization penalties to layer weights. |
| `ex091.py` | Dropout | Randomly deactivating neurons during training to enforce robustness. |

## Part 9: Custom Models & TensorFlow Data (Ch. 12 & 13)
| File | Title | Description |
| :--- | :--- | :--- |
| `ex092.py` | Custom Loss | Writing a custom Huber loss function. |
| `ex093.py` | Custom Layers | Building a stateless custom layer (e.g., custom activation). |
| `ex094.py` | Stateful Layers | Building a custom layer with trainable weights. |
| `ex095.py` | Custom Training Loop | Writing the forward and backward pass explicitly via `tf.GradientTape`. |
| `ex096.py` | tf.data.Dataset | Creating and iterating over data streams. |
| `ex097.py` | Chaining Data Ops | Applying `.map()`, `.shuffle()`, `.batch()`, and `.prefetch()`. |
| `ex098.py` | TFRecords | Saving data to TensorFlow's optimized binary format. |
| `ex099.py` | Keras TextVectorization | Preprocessing text inputs directly inside the model graph. |

## Part 10: Deep Computer Vision (Ch. 14)
| File | Title | Description |
| :--- | :--- | :--- |
| `ex100.py` | Convolution 2D | Implementing local receptive fields via filters. |
| `ex101.py` | Max Pooling | Downsampling feature maps to reduce spatial dimensions. |
| `ex102.py` | Basic CNN Arch | Stacking Conv2D, MaxPooling, and Dense layers for classification. |
| `ex103.py` | ResNet Skip Connections| Implementing residual blocks to bypass layers. |
| `ex104.py` | Pretrained Models | Loading ResNet50 with ImageNet weights. |
| `ex105.py` | Object Localization | Adding bounding box regression to a classifier. |
| `ex106.py` | Semantic Segmentation | Assigning a class to every pixel using Fully Convolutional Networks. |

## Part 11: Sequences, NLP & Attention (Ch. 15 & 16)
| File | Title | Description |
| :--- | :--- | :--- |
| `ex107.py` | Basic RNN | Predicting the next value in a time series. |
| `ex108.py` | Deep RNNs | Stacking recurrent layers for complex temporal patterns. |
| `ex109.py` | LSTM Cell | Solving long-term memory loss in sequences. |
| `ex110.py` | GRU Cell | A streamlined version of the LSTM. |
| `ex111.py` | 1D Convolutions | Using CNNs for sequence processing. |
| `ex112.py` | Char-RNN | Generating text character-by-character. |
| `ex113.py` | Word Embeddings | Learning dense vector representations of words. |
| `ex114.py` | Seq2Seq Basics | Encoder-Decoder architecture for translation. |
| `ex115.py` | Attention Mechanism | Allowing decoders to focus on specific input tokens. |
| `ex116.py` | Transformers | Multi-Head Attention blocks replacing recurrence entirely. |
| `ex117.py` | Hugging Face Basics | Loading a pre-trained transformer model from HF. |

## Part 12: Generative Models (Ch. 17)
| File | Title | Description |
| :--- | :--- | :--- |
| `ex118.py` | Basic Autoencoder | Reconstructing inputs to learn a compressed representation. |
| `ex119.py` | Denoising Autoencoders | Forcing the network to remove noise from corrupted inputs. |
| `ex120.py` | Variational Autoencoders| Generating new instances by sampling from a latent space. |
| `ex121.py` | Basic GAN | Pitting a Generator against a Discriminator. |
| `ex122.py` | Deep Conv GAN (DCGAN) | Using CNN architectures within the GAN framework. |

## Part 13: Local Deployment & Edge Inference (Applied)
*Goal: Optimize trained models to run efficiently on local, headless Linux environments (Debian/CPU).*
| File | Title | Description |
| :--- | :--- | :--- |
| `ex123.py` | SavedModel Format | Exporting architectures and weights to disk. |
| `ex124.py` | TF Lite Conversion | Stripping models down for edge devices. |
| `ex125.py` | Post-Training Quantization | Reducing FP32 weights to INT8 to massively cut memory usage. |
| `ex126.py` | ONNX Export | Converting models to the Open Neural Network Exchange format. |
| `ex127.py` | Headless CPU Threads | Restricting NumPy/TF thread limits for stable local server execution. |
| `ex128.py` | Local STT Inference | Passing audio through a lightweight Whisper/Piper model natively. |
| `ex129.py` | GGUF Loading | Loading quantized LLM formats (like Qwen) using `llama-cpp-python`. |
| `ex130.py` | The API Wrapper | Serving your optimized, quantized local model via a minimalist FastAPI script. |
