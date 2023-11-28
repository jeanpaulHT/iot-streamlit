from .dht11 import view as dht11_view
from .rules import view as rules_view


views_dict = {
    "DHT11": dht11_view,
    "Rules": rules_view
}
