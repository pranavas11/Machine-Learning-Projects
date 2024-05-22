import matplotlib.pyplot as plt

def plot_aux(x, y, clf, poly, xs, labs, predictions, title):
  plt.plot(x, y, color='black', label='true function')
  
  if poly is None:
    plt.plot(x, clf.predict(x.reshape(-1,1)), color='green' , label='predicted function')
  else:  
    plt.plot(x, clf.predict(poly.fit_transform(x.reshape(-1,1))), color='green' , label='predicted function')

  plt.plot(xs,labs,'o',color="blue", markersize=2, label='labels')
  plt.plot(xs,predictions,'x', color='red', markersize=4, label='predictions')

  # plt.yscale("log")
  plt.title(title)
  plt.legend()
  plt.show()