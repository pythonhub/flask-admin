DEFAULT_PAGE_SIZE = 10


class AjaxModelLoader(object):
    """
        Ajax related model loader. Override this to implement custom loading behavior.
    """
    def __init__(self, name):
        """
            Constructor.

            :param name:
                Field name
        """
        self.name = name

    def format(self, model):
        """
            Return (id, name) tuple from the model.
        """
        raise NotImplemented()

    def get_one(self, pk):
        """
            Find model by its primary key.

            :param pk:
                Primary key value
        """
        raise NotImplemented()

    def get_list(self, query, offset=0, limit=DEFAULT_PAGE_SIZE):
        """
            Return models that match `query`.

            :param view:
                Administrative view.
            :param query:
                Query string
            :param offset:
                Offset
            :param limit:
                Limit
        """
        raise NotImplemented()
