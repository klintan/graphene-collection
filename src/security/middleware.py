
class HideIntrospectMiddleware:
    """
    This middleware should only be used for production mode. This class hides the
    introspection.

    From @arfey https://github.com/graphql-python/graphene/issues/907#issuecomment-484014679
    """
    def resolve(self, next, root, info, **args):
        if info.field_name == '__schema':
            return None
        return next(root, info, **args)



class XSSValidationMiddleware:
    """
    This middleware validates fields for XSS injection
    """
    def resolve_fields(self, next, root, info, **args):
        return next(root, info, **args)