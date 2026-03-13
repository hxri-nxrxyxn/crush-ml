from sklearn.linear_model import ElasticNet
import numpy as np

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=42)
elastic_net.fit(X, y)
print("Elastic Net Intercept/Coef:", elastic_net.intercept_, elastic_net.coef_)
