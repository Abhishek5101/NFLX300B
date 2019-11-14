from stocker import Stocker

amazon = Stocker('AMZN')
amazon.plot_stock()
# predict days into the future
model, model_data = amazon.create_prophet_model(days=90)
amazon.evaluate_prediction()
