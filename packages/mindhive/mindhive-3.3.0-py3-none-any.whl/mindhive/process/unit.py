class Unit:
    def __init__(self, customer: str, site: str, unit: str):
        def as_py(part: str) -> str:
            return part.replace("-", "_")

        self.customer = customer
        self.site = site
        self.unit = unit
        self.redis_prefix = unit
        self.path_segments = self.customer, self.site, self.unit
        self.name = "-".join(self.path_segments)
        self.site_name = "-".join([self.customer, self.site])
        self.path = "/".join(self.path_segments)
        self.python_module_name = ".".join(["customers", as_py(customer), f"{as_py(site)}_{as_py(unit)}"])

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, Unit) and other.name == self.name

    def __str__(self):
        return self.name
