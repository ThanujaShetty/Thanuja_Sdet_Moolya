class UrlGenerator():

    def __init__(self, instance_url):
        self.instance_url = instance_url
        self.Authentication_end_point = "/api-clients/"
        self.submit_order_endpoint = "/orders"
        self.get_all_order_ep = "/orders/"