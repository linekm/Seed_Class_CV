import sklearn

from load_cifar10 import load_CIFAR_batch

X, Y = load_CIFAR_batch('./cifar-10-batches-py/data_batch_1')

pca = sklearn.decomposition.PCA(n_components=52)

newX = pca.fit_transform(X)

print(newX)